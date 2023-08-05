# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position, wrong-import-order, import-outside-toplevel


"""
Class `I3ToNumpyConverter` and simple icetray wrapper function
`run_icetray_converter` to extract information from i3 files to Numpy arrays
"""


from __future__ import absolute_import, division, print_function

__author__ = "Justin L. Lanfranchi"

__license__ = """Copyright 2020 Justin L. Lanfranchi

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

__all__ = ["run_icetray_converter", "I3ToNumpyConverter"]


from collections import OrderedDict

try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence
from functools import partial

import numpy as np
from six import string_types

from i3cols import cols, utils
from i3cols import dtypes as dt


def run_icetray_converter(paths, outdir, sub_event_stream, keys, exclude_keys):
    """Simple function callable, e.g., by subprocesses (i.e., to run in
    parallel)

    Parameters
    ----------
    paths
    outdir
    sub_event_stream
    keys, exclude_keys

    Returns
    -------
    arrays : list of dict

    """
    # TODO: have subprocesses import I3Tray and instantiate converter
    # separately, then reuse these things for each subsequent "task" that is
    # placed in the queue. This would speed up, e.g., reading separately
    # (`i3cols.extract.extract_files_separately`) lots of small files.

    from I3Tray import I3Tray

    converter = I3ToNumpyConverter()

    is_key_valid = cols.get_valid_key_func(keys=keys, exclude_keys=exclude_keys)

    tray = I3Tray()
    tray.AddModule(_type="I3Reader", _name="reader", FilenameList=paths)
    tray.Add(
        _type=converter,
        _name="I3ToNumpyConverter",
        sub_event_stream=sub_event_stream,
        is_key_valid=is_key_valid,
    )
    tray.Execute()
    tray.Finish()

    arrays = converter.finalize_icetray(outdir=outdir)

    del tray, I3Tray

    return arrays


class I3ToNumpyConverter(object):  # pylint: disable=useless-object-inheritance
    """
    Converters to extract icecube objects to Numpy struct-dtype arrays
    """

    __slots__ = [
        "icetray",
        "dataio",
        "dataclasses",
        "key_converters",
        "i3type_converters",
        "unhandled_keys",
        "unhandled_types",
        "frame",
        "frame_data",
    ]

    def __init__(self):
        # pylint: disable=unused-variable, unused-import
        from icecube import icetray, dataio, dataclasses, recclasses, simclasses

        try:
            from icecube import millipede
        except ImportError:
            millipede = None

        try:
            from icecube import santa
        except ImportError:
            santa = None

        try:
            from icecube import genie_icetray
        except ImportError:
            genie_icetray = None

        try:
            from icecube import tpx
        except ImportError:
            tpx = None

        # icetray/public/icetray/I3Logging.h:
        # typedef enum {
        #   I3LOG_TRACE,
        #   I3LOG_DEBUG,
        #   I3LOG_INFO,
        #   I3LOG_NOTICE,
        #   I3LOG_WARN,
        #   I3LOG_ERROR,
        #   I3LOG_FATAL
        # } I3LogLevel;
        icetray.logging.set_level(icetray.I3LogLevel.LOG_INFO)

        self.icetray = icetray
        self.dataio = dataio
        self.dataclasses = dataclasses

        # Define a dict where keys are the names (keys) of items in a frame and
        # values are functions able to extract the obj. Note `key_converters`
        # takes precedence over `i3type_converters`.

        self.key_converters = {}

        self.key_converters["I3MCWeightDict"] = partial(
            self.extract_mapscalarattrs, obj_dtype=dt.MIN_OSCNEXT_GENIE_I3MCWEIGHTDICT_T
        )

        # Define a dict where keys are i3 types and values are functions
        # able to extract the obj; each must take just 2 args: (obj, to_numpy)
        # and either return a numpy array or scalar (if to_numpy=True) or a
        # 2-tuple where the first element is the tuple or list of tuples and
        # the second element is a numpy dtype (possibly structured) where
        # calling np.array(tup[0], dtype=tup[1]) would "work".

        self.i3type_converters = {}

        # I3 scalars
        for i3_dt, np_dt in {
            icetray.I3Bool: np.bool8,
            icetray.I3Int: np.int32,
            dataclasses.I3Double: np.float64,
            dataclasses.I3String: np.string0,
        }.items():
            self.i3type_converters[i3_dt] = partial(self.extract_scalar, dtype=np_dt)

        # Must extract values using "getters" (functions like GetX(), GetY(), etc.)
        for i3_dt, extract_getters_kw in {
            recclasses.I3PortiaEvent: dict(dtype=dt.I3PORTIAEVENT_T, fmt="Get{}")
        }.items():
            self.i3type_converters[i3_dt] = partial(
                self.extract_getters, **extract_getters_kw
            )

        # {<str>: <simple scalar>}
        for i3_dt, np_dt in {
            dataclasses.I3MapStringDouble: np.float64,
            dataclasses.I3MapStringInt: np.int32,
            dataclasses.I3MapStringBool: np.bool8,
        }.items():
            self.i3type_converters[i3_dt] = partial(
                utils.dict2struct, set_explicit_dtype_func=np_dt
            )

        # {<str>: <struct scalar>}
        mapping_str_structured_scalar = {}
        if genie_icetray:
            mapping_str_structured_scalar[
                genie_icetray.I3GENIEResultDict
            ] = dt.I3GENIERESULTDICT_SCALARS_T
        for i3_dt, np_dt in mapping_str_structured_scalar.items():
            self.i3type_converters[i3_dt] = partial(utils.maptype2np, dtype=np_dt)

        # Following make use of `self.extract_mapscalarattrs`; one of
        #
        #   obj_dtype({<str>: <scalar>, ...})
        #   {<str>: value_dtype(<scalar>), ...}
        #   {<str>: <inferred type scalar>, ...}
        #
        for i3_dt, extract_mapscalarattrs_kwargs in {
            dataclasses.I3FilterResultMap: dict(value_dtype=dt.I3FILTERRESULT_T)
        }.items():
            if extract_mapscalarattrs_kwargs is None:
                func = self.extract_mapscalarattrs
            else:
                func = partial(
                    self.extract_mapscalarattrs, **extract_mapscalarattrs_kwargs
                )
            self.i3type_converters[i3_dt] = func

        # tuple(obj.{name} for name in np_dt.names)
        attrs = {
            icetray.I3RUsage: dt.I3RUSAGE_T,
            icetray.OMKey: dt.OMKEY_T,
            dataclasses.TauParam: dt.TAUPARAM_T,
            dataclasses.LinearFit: dt.LINEARFIT_T,
            dataclasses.SPEChargeDistribution: dt.SPECHARGEDISTRIBUTION_T,
            dataclasses.I3Direction: dt.I3DIRECTION_T,
            dataclasses.I3EventHeader: dt.I3EVENTHEADER_T,
            dataclasses.I3FilterResult: dt.I3FILTERRESULT_T,
            dataclasses.I3Position: dt.I3POSITION_T,
            dataclasses.I3Particle: dt.I3PARTICLE_T,
            dataclasses.I3ParticleID: dt.I3PARTICLEID_T,
            dataclasses.I3VEMCalibration: dt.I3VEMCALIBRATION_T,
            dataclasses.SPEChargeDistribution: dt.SPECHARGEDISTRIBUTION_T,
            dataclasses.I3SuperDSTTrigger: dt.I3SUPERDSTTRIGGER_T,
            dataclasses.I3Time: dt.I3TIME_T,
            dataclasses.I3TimeWindow: dt.I3TIMEWINDOW_T,
            recclasses.I3DipoleFitParams: dt.I3DIPOLEFITPARAMS_T,
            recclasses.I3LineFitParams: dt.I3LINEFITPARAMS_T,
            recclasses.I3FillRatioInfo: dt.I3FILLRATIOINFO_T,
            recclasses.I3FiniteCuts: dt.I3FINITECUTS_T,
            recclasses.I3DirectHitsValues: dt.I3DIRECTHITSVALUES_T,
            recclasses.I3HitStatisticsValues: dt.I3HITSTATISTICSVALUES_T,
            recclasses.I3HitMultiplicityValues: dt.I3HITMULTIPLICITYVALUES_T,
            recclasses.I3TensorOfInertiaFitParams: dt.I3TENSOROFINERTIAFITPARAMS_T,
            recclasses.I3Veto: dt.I3VETO_T,
            recclasses.I3CLastFitParams: dt.I3CLASTFITPARAMS_T,
            recclasses.I3CscdLlhFitParams: dt.I3CSCDLLHFITPARAMS_T,
            recclasses.I3DST16: dt.I3DST16_T,
            recclasses.DSTPosition: dt.DSTPOSITION_T,
            recclasses.I3StartStopParams: dt.I3STARTSTOPPARAMS_T,
            recclasses.I3TrackCharacteristicsValues: dt.I3TRACKCHARACTERISTICSVALUES_T,
            recclasses.I3TimeCharacteristicsValues: dt.I3TIMECHARACTERISTICSVALUES_T,
            recclasses.CramerRaoParams: dt.CRAMERRAOPARAMS_T,
        }
        if millipede:
            attrs[
                millipede.gulliver.I3LogLikelihoodFitParams
            ] = dt.I3LOGLIKELIHOODFITPARAMS_T
        if santa:
            attrs[santa.I3SantaFitParams] = dt.I3SANTAFITPARAMS_T
        for i3_dt, np_dt in attrs.items():
            self.i3type_converters[i3_dt] = partial(
                self.extract_attrs, dtype=np_dt, dtype_descr=np_dt.descr
            )

        # Custom functions for types that don't fit into other categories
        self.i3type_converters.update(
            {
                dataclasses.I3MCTree: self.extract_flat_mctree,
                dataclasses.I3RecoPulseSeries: self.extract_flat_pulse_series,
                dataclasses.I3RecoPulseSeriesMap: self.extract_flat_pulse_series,
                dataclasses.I3RecoPulseSeriesMapMask: self.extract_flat_pulse_series,
                dataclasses.I3RecoPulseSeriesMapUnion: self.extract_flat_pulse_series,
                dataclasses.I3SuperDSTTriggerSeries: self.extract_seq_of_same_type,
                dataclasses.I3TriggerHierarchy: self.extract_flat_trigger_hierarchy,
                dataclasses.I3VectorI3Particle: self.extract_singleton_seq_to_scalar,
                dataclasses.I3DOMCalibration: self.extract_i3domcalibration,
            }
        )

        # Define types we know we don't handle; these will be expanded as new
        # types are encountered to avoid repeatedly failing on the same types

        self.unhandled_keys = set(
            [
                "I3Geometry",
                "I3Calibration",
                "I3DetectorStatus",
                "CalibrationErrata",
                "InIceRawData",
                "IceTopRawData",
                "I3DSTHeader",
            ]
        )
        self.unhandled_types = set(
            [
                dataclasses.I3Geometry,
                dataclasses.I3Calibration,
                dataclasses.I3DetectorStatus,
                dataclasses.I3DOMLaunchSeriesMap,
                dataclasses.I3MapKeyVectorDouble,
                dataclasses.I3RecoPulseSeriesMapApplySPECorrection,
                dataclasses.I3SuperDST,
                dataclasses.I3TimeWindowSeriesMap,
                dataclasses.I3VectorDouble,
                dataclasses.I3VectorOMKey,
                dataclasses.I3VectorTankKey,
                dataclasses.I3MapKeyDouble,
                recclasses.I3DSTHeader16,
            ]
        )
        if tpx:
            self.unhandled_types.add(tpx.I3TopPulseInfoSeriesMap)

        self.frame = None
        self.frame_data = []

    def __call__(self, frame, sub_event_stream=None, is_key_valid=None):
        """Allows calling the instantiated class directly, which is the
        mechanism IceTray uses (including requiring `frame` as the first
        argument)

        Parameters
        ----------
        frame : icetray.I3Frame
        sub_event_stream : str, iterable thereof, or None; optional
            Only process frames from these sub event streams. If None, process
            all sub event streams.
        is_key_valid : callable or None, optional

        Returns
        -------
        False
            This disallows frames from being pushed to subsequent modules. I
            don't know why I picked this value. Probably not the "correct"
            value, so modify if this is an issue or there is a better way.

        """
        if frame.Stop != self.icetray.I3Frame.Physics:
            return False

        if sub_event_stream is not None:
            if isinstance(sub_event_stream, string_types):
                if frame["I3EventHeader"].sub_event_stream != sub_event_stream:
                    return False
            elif frame["I3EventHeader"].sub_event_stream not in set(sub_event_stream):
                return False

        frame_data = self.extract_frame(frame, is_key_valid=is_key_valid)
        self.frame_data.append(frame_data)

        return False

    def finalize_icetray(self, outdir=None):
        """Construct arrays and cleanup data saved when running via icetray
        (i.e., the __call__ method)

        Parameters
        ----------
        outdir : str or None, optional
            If string, interpret as path to a directory in which to save the
            arrays (they are written to memory-mapped files to avoid excess
            memory usage). If None, exclusively construct the arrays in memory
            (do not save to disk).

        Returns
        -------
        arrays
            See `construct_arrays` for format of `arrays`

        """
        arrays = cols.construct_arrays(self.frame_data, outdir=outdir)
        del self.frame_data[:]
        return arrays

    def extract_frame(self, frame, is_key_valid=None):
        """Extract icetray frame objects to numpy typed objects

        Parameters
        ----------
        frame : icetray.I3Frame
        is_key_valid : callable or None, optional

        """
        self.frame = frame

        extracted_data = {}

        # NOTE: can't iterate over items because there might be an unhandled
        #   key where accessing its value requires a library be loaded that we
        #   haven't loaded (or it is impossible to do so)
        for key in frame.keys():
            if not is_key_valid(key) or key in self.unhandled_keys:
                continue

            try:
                value = frame[key]
            except Exception as err:
                print(
                    "ERROR: Failed to get value at key '{}', will skip same"
                    " key from here on. Error message:\n{}".format(key, err)
                )
                self.unhandled_keys.add(key)
                continue

            try:
                np_value = self.extract_object(value, key=key, to_numpy=True)
            except Exception:
                print("failed on key {}".format(key))
                raise

            # if auto_mode and np_value is None:
            if np_value is None:
                continue

            extracted_data[key] = np_value

        return extracted_data

    def extract_object(self, obj, key=None, to_numpy=True):
        """Convert an object from a frame to a Numpy typed object.

        Note that e.g. extracting I3RecoPulseSeriesMap{Mask,Union} requires
        that `self.frame` be assigned the current frame to work.

        Parameters
        ----------
        obj : frame object
            Frame object to have data extracted from

        key : str or None, optional
            key of the frame object. Only necessary for very specific cases
            (for now, just I3MCWeightDict)

        to_numpy : bool, optional
            Convert resulting tuple to a Numpy array or scalar (as appropriate
            for the frame item; see individual extraction methods for which is
            returned for a given key or object type)

        Returns
        -------
        np_obj : numpy-typed object or None

        """
        # Extract by key if key is provided and its extraction method is
        # defined

        if key in self.unhandled_keys:
            return None

        func = self.key_converters.get(key, None)
        if func is not None:
            return func(obj, to_numpy=to_numpy)

        # Otherwise, get extraction function based on obj's type

        obj_t = type(obj)

        if obj_t in self.unhandled_types:
            return None

        func = self.i3type_converters.get(obj_t, None)
        if func is not None:
            return func(obj, to_numpy=to_numpy)

        # New unhandled type found

        key_txt = " (key='{}')".format(key) if key else ""
        print("WARNING: found new unhandled type: {}{}".format(obj_t, key_txt))
        self.unhandled_types.add(obj_t)
        if key is not None:
            self.unhandled_keys.add(key)
        return None

    @staticmethod
    def extract_flat_trigger_hierarchy(obj, to_numpy=True):
        """Flatten a trigger hierarchy into a linear sequence of triggers,
        labeled such that the original hiercarchy can be recreated

        Parameters
        ----------
        obj : I3TriggerHierarchy
        to_numpy : bool, optional

        Returns
        -------
        flat_triggers : shape-(N-trigers,) numpy.ndarray of dtype FLAT_TRIGGER_T

        """
        iterattr = obj.items if hasattr(obj, "items") else obj.iteritems

        level_tups = []
        flat_triggers = []

        for level_tup, trigger in iterattr():
            level_tups.append(level_tup)
            level = len(level_tup) - 1
            if level == 0:
                parent_idx = -1
            else:
                parent_idx = level_tups.index(level_tup[:-1])
            # info_tup, _ = self.extract_attrs(trigger, TRIGGER_T, to_numpy=False)
            key = trigger.key
            flat_triggers.append(
                (
                    level,
                    parent_idx,
                    (
                        trigger.time,
                        trigger.length,
                        trigger.fired,
                        (key.source, key.type, key.subtype, key.config_id or 0),
                    ),
                )
            )

        if to_numpy:
            return np.array(flat_triggers, dtype=dt.FLAT_TRIGGER_T)

        return flat_triggers, dt.FLAT_TRIGGER_T

    def extract_flat_mctree(
        self,
        mctree,
        parent=None,
        parent_idx=-1,
        level=0,
        max_level=-1,
        flat_particles=None,
        to_numpy=True,
    ):
        """Flatten an I3MCTree into a sequence of particles with additional
        metadata "level" and "parent" for easily reconstructing / navigating the
        tree structure if need be.

        Parameters
        ----------
        mctree : icecube.dataclasses.I3MCTree
            Tree to flatten into a numpy array

        parent : icecube.dataclasses.I3Particle, optional

        parent_idx : int, optional

        level : int, optional

        max_level : int, optional
            Recurse to but not beyond `max_level` depth within the tree. Primaries
            are level 0, secondaries level 1, tertiaries level 2, etc. Set to
            negative value to capture all levels.

        flat_particles : appendable sequence or None, optional

        to_numpy : bool, optional


        Returns
        -------
        flat_particles : list of tuples or ndarray of dtype `FLAT_PARTICLE_T`

        Examples
        --------
        This is a recursive function, with defaults defined for calling simply for
        the typical use case of flattening an entire I3MCTree and producing a
        numpy.ndarray with the results. .. ::

            flat_particles = extract_flat_mctree(frame["I3MCTree"])

        """
        if flat_particles is None:
            flat_particles = []

        if max_level < 0 or level <= max_level:
            if parent:
                daughters = mctree.get_daughters(parent)
            else:
                level = 0
                parent_idx = -1
                daughters = mctree.get_primaries()

            if daughters:
                # Record index before we started appending
                idx0 = len(flat_particles)

                # First append all daughters found
                for daughter in daughters:
                    info_tup, _ = self.extract_attrs(
                        daughter,
                        dtype=dt.I3PARTICLE_T,
                        dtype_descr=dt.I3PARTICLE_T_DESCR,
                        to_numpy=False,
                    )
                    flat_particles.append((level, parent_idx, info_tup))

                # Now recurse, appending any granddaughters (daughters to these
                # daughters) at the end
                for daughter_idx, daughter in enumerate(daughters, start=idx0):
                    self.extract_flat_mctree(
                        mctree=mctree,
                        parent=daughter,
                        parent_idx=daughter_idx,
                        level=level + 1,
                        max_level=max_level,
                        flat_particles=flat_particles,
                        to_numpy=False,
                    )

        if to_numpy:
            return np.array(flat_particles, dtype=dt.FLAT_PARTICLE_T)

        return flat_particles, dt.FLAT_PARTICLE_T

    def extract_flat_pulse_series(self, obj, frame=None, to_numpy=True):
        """Flatten a pulse series into a 1D array of ((<OMKEY_T>), <PULSE_T>)

        Parameters
        ----------
        obj : dataclasses.I3RecoPUlseSeries{,Map,MapMask,MapUnion}
        frame : iectray.I3Frame, required if obj is {...Mask, ...Union}
        to_numpy : bool, optional

        Returns
        -------
        flat_pulses : shape-(N-pulses) numpy.ndarray of dtype FLAT_PULSE_T

        """
        if isinstance(
            obj,
            (
                self.dataclasses.I3RecoPulseSeriesMapMask,
                self.dataclasses.I3RecoPulseSeriesMapUnion,
            ),
        ):
            if frame is None:
                frame = self.frame
            obj = obj.apply(frame)

        flat_pulses = []
        for omkey, pulses in obj.items():
            omkey = (omkey.string, omkey.om, omkey.pmt)
            for pulse in pulses:
                info_tup, _ = self.extract_attrs(
                    pulse,
                    dtype=dt.PULSE_T,
                    dtype_descr=dt.PULSE_T_DESCR,
                    to_numpy=False,
                )
                flat_pulses.append((omkey, info_tup))

        if to_numpy:
            return np.array(flat_pulses, dtype=dt.FLAT_PULSE_T)

        return flat_pulses, dt.FLAT_PULSE_T

    def extract_singleton_seq_to_scalar(self, seq, to_numpy=True):
        """Extract a sole object from a sequence and treat it as a scalar.
        E.g., I3VectorI3Particle that, by construction, contains just one
        particle

        Parameters
        ----------
        seq : sequence
        to_numpy : bool, optional

        Returns
        -------
        obj

        """
        assert len(seq) == 1
        return self.extract_object(seq[0], to_numpy=to_numpy)

    def extract_attrs(self, obj, dtype, dtype_descr=None, to_numpy=True):
        """Extract attributes of an object (and optionally, recursively, attributes
        of those attributes, etc.) into a numpy.ndarray based on the specification
        provided by `dtype`.

        Parameters
        ----------
        obj
        dtype : numpy.dtype
        dtype_descr : optional
        to_numpy : bool, optional

        Returns
        -------
        vals : tuple or shape-(1,) numpy.ndarray of dtype `dtype`

        """
        vals = []
        if dtype_descr is None:
            if isinstance(dtype, np.dtype):
                dtype_descr = dtype.descr
            elif isinstance(dtype, Sequence):
                dtype_descr = dtype
            else:
                raise TypeError("{}".format(dtype))

        for name, subdtype in dtype_descr:
            val = getattr(obj, name)
            if isinstance(subdtype, (str, np.dtype)):
                vals.append(val)
            elif isinstance(subdtype, Sequence):
                out = self.extract_object(val, to_numpy=False)
                if out is None:
                    out = self.extract_attrs(val, subdtype, to_numpy=False)
                info_tup, _ = out
                vals.append(info_tup)
            else:
                raise TypeError("{}".format(subdtype))

        # Numpy converts tuples correctly; lists are interpreted differently
        vals = tuple(vals)

        if to_numpy:
            return np.array([vals], dtype=dtype)[0]

        return vals, dtype

    def extract_mapscalarattrs(
        self, mapping, obj_dtype=None, value_dtype=None, to_numpy=True
    ):
        """Convert a mapping (containing string keys and scalar-typed values)
        to a single-element Numpy array from the values of `mapping`, using
        keys defined by `value_dtype.names`.

        Use this function if you already know the `value_dtype` you want to end up
        with. Use `i3cols.utils.dict2struct` directly if you do not know
        the dtype(s) of the mapping's values ahead of time.

        Parameters
        ----------
        mapping : mapping from strings to scalars

        obj_dtype : numpy.dtype or None, optional
            Type that describes entire object. If both `obj_dtype` and
            `value_dtype` are provided as numpy.dtypes, `obj_dtype` takes
            precedence.

        value_dtype : numpy.dtype or None, optional
            Convert all values via this dtype; ignored if `obj_dtype` is
            specified (since that should contain all type information for
            values of the dict)

        Returns
        -------
        array : shape-(1,) numpy.ndarray of dtype `dtype`

        See Also
        --------
        i3cols.utils.dict2struct
            Convert from a mapping to a numpy.ndarray, dynamically building `dtype`
            as you go (i.e., this is not known a priori)

        """
        # TODO: sort by descending order of dtype # bits, _then_ by alphabetical order

        if obj_dtype is not None:
            out_vals = tuple(mapping[key] for key in obj_dtype.names)

        else:
            keys = mapping.keys()
            if not isinstance(mapping, OrderedDict):
                keys.sort()

            out_vals = []
            obj_dtype = []

            if value_dtype is not None:
                for key in keys:
                    out_vals.append(mapping[key])
                    obj_dtype.append((key, value_dtype))

            else:  # infer types from values
                for key in keys:
                    val = mapping[key]
                    info_tup, value_dtype = self.extract_object(val, to_numpy=False)
                    out_vals.append(info_tup)
                    obj_dtype.append((key, value_dtype))

            out_vals = tuple(out_vals)

        if to_numpy:
            return np.array([out_vals], dtype=obj_dtype)[0]

        return out_vals, obj_dtype

    def extract_getters(self, obj, dtype, fmt="Get{}", to_numpy=True):
        """Convert an object whose data has to be extracted via methods that
        behave like getters (e.g., .`xyz = get_xyz()`).

        Parameters
        ----------
        obj
        dtype
        fmt : str
        to_numpy : bool, optional

        Examples
        --------
        To get all of the values of an I3PortiaEvent: .. ::

            extract_getters(
                frame["PoleEHESummaryPulseInfo"], dtype=dt.I3PORTIAEVENT_T, fmt="Get{}"
            )

        """
        vals = []
        for name, subdtype in dtype.descr:
            getter_attr_name = fmt.format(name)
            getter_func = getattr(obj, getter_attr_name)
            val = getter_func()
            if not isinstance(subdtype, str) and isinstance(subdtype, Sequence):
                out = self.extract_object(val, to_numpy=False)
                if out is None:
                    raise ValueError(
                        "Failed to convert name {} val {} type {}".format(
                            name, val, type(val)
                        )
                    )
                val, _ = out
            # if isinstance(val, self.icetray.OMKey):
            #    val = self.extract_attrs(val, dtype=dt.OMKEY_T, to_numpy=False)
            vals.append(val)

        vals = tuple(vals)

        if to_numpy:
            return np.array([vals], dtype=dtype)[0]

        return vals, dtype

    def extract_seq_of_same_type(self, seq, to_numpy=True):
        """Convert a sequence of objects, all of the same type, to a numpy array of
        that type.

        Parameters
        ----------
        seq : seq of N objects all of same type
        to_numpy : bool, optional

        Returns
        -------
        out_seq : list of N tuples or shape-(N,) numpy.ndarray of `dtype`

        """
        assert len(seq) > 0

        # Convert first object in sequence to get dtype
        val0 = seq[0]
        val0_tup, val0_dtype = self.extract_object(val0, to_numpy=False)
        data_tups = [val0_tup]

        # Convert any remaining objects
        for obj in seq[1:]:
            data_tups.append(self.extract_object(obj, to_numpy=False)[0])

        if to_numpy:
            return np.array(data_tups, dtype=val0_dtype)

        return data_tups, val0_dtype

    @staticmethod
    def extract_scalar(obj, dtype, to_numpy=True):
        """Convert a scalar object."""
        val = dtype(obj.value)
        return val if to_numpy else (val, dtype)

    def extract_i3domcalibration(self, obj, to_numpy=True):
        """Extract the information from an I3DOMCalibration frame object"""
        vals = []
        for name, subdtype in dt.I3DOMCALIBRATION_T.descr:
            val = getattr(obj, name)
            if name == "dom_cal_version":
                if val == "unknown":
                    val = (-1, -1, -1)
                else:
                    val = tuple(int(x) for x in val.split("."))
            elif isinstance(subdtype, (str, np.dtype)):
                pass
            elif isinstance(subdtype, Sequence):
                out = self.extract_object(val, to_numpy=False)
                if out is None:
                    raise ValueError(
                        "{} {} {} {}".format(name, subdtype, val, type(val))
                    )
                val, _ = out
            else:
                raise TypeError(str(subdtype))
            vals.append(val)

        vals = tuple(vals)

        if to_numpy:
            return np.array([vals], dtype=dt.I3DOMCALIBRATION_T)[0]

        return vals, dt.I3DOMCALIBRATION_T
