#!/usr/bin/env
# encoding: utf-8
"""
Author:     Daniel Boeckenhoff
Mail:       daniel.boeckenhoff@ipp.mpg.de

core of tfields library
contains numpy ndarray derived bases of the tfields package

Notes:
    It could be worthwhile concidering `np.li.mixins.NDArrayOperatorsMixin ...
    <https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/...
    ... numpy.lib.mixins.NDArrayOperatorsMixin.html>`_
"""
import warnings
import pathlib
from six import string_types
from contextlib import contextmanager
from collections import Counter

import numpy as np
import sympy
import scipy as sp
import rna
import tfields.bases

np.seterr(all="warn", over="raise")


def rank(tensor):
    """
    Tensor rank
    """
    return len(tensor.shape) - 1


def dim(tensor):
    """
    Manifold dimension
    """
    if rank(tensor) == 0:
        return 1
    return tensor.shape[1]


class AbstractNdarray(np.ndarray):
    """
    All tensors and subclasses should derive from AbstractNdarray.
    AbstractNdarray implements all the inheritance specifics for np.ndarray
    Whene inheriting, three attributes are of interest:

    Attributes:
        __slots__ (list of str): If you want to add attributes to
            your AbstractNdarray subclass, add the attribute name to __slots__
        __slot_defaults__ (list): if __slot_defaults__ is None, the
            defaults for the attributes in __slots__ will be None
            other values will be treaded as defaults to the corresponding
            arg at the same position in the __slots__ list.
        __slotDtype__ (list of types): for the conversion of the
            args in __slots__ to numpy arrays. None values mean no
            conversion.

    Args:
        array (array-like): input array
        **kwargs: arguments corresponding to __slots__

    TODO:
        equality check

    """

    __slots__ = []
    __slot_defaults__ = []
    __slotDtypes__ = []
    __slot_setters__ = []

    def __new__(cls, array, **kwargs):  # pragma: no cover
        raise NotImplementedError(
            "{clsType} type must implement '__new__'".format(clsType=type(cls))
        )

    def __array_finalize__(self, obj):
        if obj is None:
            return
        for attr in self._iter_slots():
            setattr(self, attr, getattr(obj, attr, None))

    def __array_wrap__(self, out_arr, context=None):
        return np.ndarray.__array_wrap__(self, out_arr, context)

    @classmethod
    def _iter_slots(cls):
        return [att for att in cls.__slots__ if att != "_cache"]

    @classmethod
    def _update_slot_kwargs(cls, kwargs):
        """
        set the defaults in kwargs according to __slot_defaults__
        and convert the kwargs according to __slotDtypes__
        """
        slotDefaults = cls.__slot_defaults__ + [None] * (
            len(cls.__slots__) - len(cls.__slot_defaults__)
        )
        slotDtypes = cls.__slotDtypes__ + [None] * (
            len(cls.__slots__) - len(cls.__slotDtypes__)
        )
        for attr, default, dtype in zip(
            cls.__slots__, slotDefaults, slotDtypes
        ):
            if attr == "_cache":
                continue
            if attr not in kwargs:
                kwargs[attr] = default
            if dtype is not None:
                try:
                    kwargs[attr] = np.array(kwargs[attr], dtype=dtype)
                except Exception as err:
                    raise ValueError(
                        str(attr) + str(dtype) + str(kwargs[attr]) + str(err)
                    )

    def __setattr__(self, name, value):
        if name in self.__slots__:
            index = self.__slots__.index(name)
            try:
                setter = self.__slot_setters__[index]
            except IndexError:
                setter = None
            if setter is not None:
                value = setter(value)
        super(AbstractNdarray, self).__setattr__(name, value)

    def __reduce__(self):
        """
        important for pickling (see `here <https://stackoverflow.com/questions/26598109/preserve-custom-attributes-when-pickling-subclass-of-numpy-array>`_)

        Examples:
            >>> from tempfile import NamedTemporaryFile
            >>> import pickle
            >>> import tfields

            Build a dummy scalar field

            >>> from tfields import Tensors, TensorFields
            >>> scalars = Tensors([0, 1, 2])
            >>> vectors = Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
            >>> scalar_field = TensorFields(vectors,
            ...                             scalars,
            ...                             coord_sys='cylinder')

            Save it and restore it

            >>> out_file = NamedTemporaryFile(suffix='.pickle')

            >>> pickle.dump(scalar_field,
            ...             out_file)
            >>> _ = out_file.seek(0)

            >>> sf = pickle.load(out_file)
            >>> sf.coord_sys == 'cylinder'
            True
            >>> sf.fields[0][2] == 2.
            True

        """
        # Get the parent's __reduce__ tuple
        pickled_state = super(AbstractNdarray, self).__reduce__()

        # Create our own tuple to pass to __setstate__
        new_state = pickled_state[2] + tuple(
            [getattr(self, slot) for slot in self._iter_slots()]
        )

        # Return a tuple that replaces the parent's __setstate__
        # tuple with our own
        return (pickled_state[0], pickled_state[1], new_state)

    def __setstate__(self, state):
        """
        Counterpart to __reduce__. Important for unpickling.
        """
        # Call the parent's __setstate__ with the other tuple elements.
        super(AbstractNdarray, self).__setstate__(
            state[0 : -len(self._iter_slots())]
        )

        # set the __slot__ attributes
        valid_slot_attrs = list(self._iter_slots())
        added_slot_attrs = ['name']  # attributes that have been added later
                                     # have not been pickled with the full
                                     # information and thus need to be
                                     # excluded from the __setstate__
                                     # need to be in the same order as they have
                                     # been added to __slots__
        n_old = len(valid_slot_attrs) - len(state[5:])
        if n_old > 0:
            for latest_index in range(n_old):
                new_slot = added_slot_attrs[-latest_index]
                warnings.warn("Slots with names '{new_slot}' appears to have been "
                              "added after the creation of the reduced state. "
                              "No corresponding state found in __setstate__."
                              .format(**locals()))
                valid_slot_attrs.pop(valid_slot_attrs.index(new_slot))
                setattr(self, new_slot, None)

        for slot_index, slot in enumerate(valid_slot_attrs):
            state_index = 5 + slot_index
            setattr(self, slot, state[state_index])

    @property
    def bulk(self):
        """
        The pure ndarray version of the actual state
            -> nothing attached
        """
        return np.array(self)

    @classmethod
    @contextmanager
    def _bypass_setter(cls, slot, demand_existence=False):
        """
        Temporarily remove the setter in __slot_setters__ corresponding to slot
        position in __slot__. You should know what you do, when using this.
        """
        slot_index = cls.__slots__.index(slot) if slot in cls.__slots__ else None
        if slot_index is None:
            if demand_existence:
                raise ValueError("Slot {slot} not existing".format(**locals()))
            else:
                yield
                return
        setter = cls.__slot_setters__[slot_index]
        cls.__slot_setters__[slot_index] = None
        yield
        cls.__slot_setters__[slot_index] = setter

    def copy(self, *args, **kwargs):
        """
        The standard ndarray copy does not copy slots. Correct for this.

        Examples:
            >>> import tfields
            >>> m = tfields.TensorMaps(
            ...     [[1,2,3], [3,3,3], [0,0,0], [5,6,7]],
            ...     maps=[tfields.TensorFields([[0, 1, 2], [1, 2, 3]],
            ...                                 [1, 2])])
            >>> mc = m.copy()
            >>> mc is m
            False
            >>> mc.maps[0].fields[0] is m.maps[0].fields[0]
            False

        TODO:
            This function implementation could be more general or maybe
            redirect to deepcopy?
        """
        inst = super(AbstractNdarray, self).copy(*args, **kwargs)
        for attr in self._iter_slots():
            value = getattr(self, attr)
            if hasattr(value, "copy") and not isinstance(value, list):
                setattr(inst, attr, value.copy(*args, **kwargs))
            elif isinstance(value, list):
                list_copy = []
                for item in value:
                    if hasattr(item, "copy"):
                        list_copy.append(item.copy(*args, **kwargs))
                    else:
                        list_copy.append(item)
                setattr(inst, attr, list_copy)

        return inst

    def save(self, path, *args, **kwargs):
        """
        Saving a tensors object by redirecting to the correct save method depending on path

        Args:
            path (str or buffer)
            *args:
                forwarded to extension specific method
            **kwargs:
                extension (str): only needed if path is buffer
                ... remaining:forwarded to extension specific method
        """
        # get the extension
        if isinstance(path, (string_types, pathlib.Path)):
            extension = pathlib.Path(path).suffix.lstrip(".")
        else:
            raise ValueError("Wrong path type {0}".format(type(path)))
        path = str(path)

        # get the save method
        try:
            save_method = getattr(self, "_save_{extension}".format(**locals()))
        except:
            raise NotImplementedError(
                "Can not find save method for extension: "
                "{extension}.".format(**locals())
            )

        path = rna.path.resolve(path)
        return save_method(path, **kwargs)

    @classmethod
    def load(cls, path, *args, **kwargs):
        """
        load a file as a tensors object.

        Args:
            path (str or buffer)
            *args:
                forwarded to extension specific method
            **kwargs:
                extension (str): only needed if path is buffer
                ... remaining:forwarded to extension specific method
        """
        if isinstance(path, (string_types, pathlib.Path)):
            extension = pathlib.Path(path).suffix.lstrip(".")
            path = str(path)
            path = rna.path.resolve(path)
        else:
            extension = kwargs.pop("extension", "npz")

        try:
            load_method = getattr(cls, "_load_{e}".format(e=extension))
        except:
            raise NotImplementedError(
                "Can not find load method for extension: "
                "{extension}.".format(**locals())
            )
        return load_method(path, *args, **kwargs)

    def _save_npz(self, path, **kwargs):
        """
        Args:
            path (open file or str/unicode): destination to save file to.

        Examples:
            Build some dummies:
            >>> import tfields
            >>> from tempfile import NamedTemporaryFile
            >>> out_file = NamedTemporaryFile(suffix='.npz')
            >>> p = tfields.Points3D([[1., 2., 3.], [4., 5., 6.], [1, 2, -6]],
            ...                      name='my_points')
            >>> scalars = tfields.Tensors([0, 1, 2], name=42)
            >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
            >>> maps = [tfields.TensorFields([[0, 1, 2], [0, 1, 2]], [42, 21]),
            ...         tfields.TensorFields([[1], [2]], [-42, -21])]
            >>> m = tfields.TensorMaps(vectors, scalars,
            ...                        maps=maps)

            Simply give the file name to save
            >>> p.save(out_file.name)
            >>> _ = out_file.seek(0)  # this is only necessary in the test
            >>> p1 = tfields.Points3D.load(out_file.name)
            >>> assert p.equal(p1)
            >>> assert p.coord_sys == p1.coord_sys

            The fully nested structure of a TensorMaps object is reconstructed
            >>> out_file_maps = NamedTemporaryFile(suffix='.npz')
            >>> m.save(out_file_maps.name)
            >>> _ = out_file_maps.seek(0)
            >>> m1 = tfields.TensorMaps.load(out_file_maps.name,
            ...                              allow_pickle=True)
            >>> assert m.equal(m1)
            >>> assert m.maps[0].dtype == m1.maps[0].dtype

            Names are preserved
            >>> assert p.name == 'my_points'
            >>> m.names
            [42]

        """
        content_dict = self._as_dict()
        np.savez(path, **content_dict)

    @classmethod
    def _load_npz(cls, path, **load_kwargs):
        """
        Factory method
        Given a path to a npz file, construct the object
        """
        np_file = np.load(path, **load_kwargs)
        return cls._from_dict(**np_file)

    def _as_dict(self):
        """
        Recursively walk trough all __slots__ and describe all elements
        """
        d = {}
        d["bulk"] = self.bulk
        d["bulk_type"] = self.__class__.__name__
        for attr in self._iter_slots():
            value = getattr(self, attr)
            if isinstance(value, list):
                if len(value) == 0:
                    d[attr] = None
                if all([isinstance(part, AbstractNdarray) for part in value]):
                    for i, part in enumerate(value):
                        part_dict = part._as_dict()
                        for part_attr, part_value in part_dict.items():
                            d[
                                "{attr}::{i}::{part_attr}".format(**locals())
                            ] = part_value
                    continue
            if isinstance(value, AbstractNdarray):
                value = value._as_dict()
            d[attr] = value
        return d

    @classmethod
    def _from_dict(cls, **d):
        """
        Opposite of _as_dict
        """
        list_dict = {}
        kwargs = {}
        """
        De-Flatten the first layer of lists
        """
        for key in sorted(list(d)):
            if "::" in key:
                splits = key.split("::")
                attr, _, end = key.partition("::")
                if attr not in list_dict:
                    list_dict[attr] = {}

                index, _, end = end.partition("::")
                if not index.isdigit():
                    raise ValueError("None digit index given")
                index = int(index)
                if index not in list_dict[attr]:
                    list_dict[attr][index] = {}
                list_dict[attr][index][end] = d[key]
            else:
                kwargs[key] = d[key]

        """
        Build the lists (recursively)
        """
        for key in list(list_dict):
            sub_dict = list_dict[key]
            list_dict[key] = []
            for index in sorted(list(sub_dict)):
                bulk_type = sub_dict[index].get("bulk_type").tolist()
                if isinstance(bulk_type, bytes):
                    # asthonishingly, this is not necessary under linux. Found under nt. ???
                    bulk_type = bulk_type.decode("UTF-8")
                bulk_type = getattr(tfields, bulk_type)
                list_dict[key].append(bulk_type._from_dict(**sub_dict[index]))

        with cls._bypass_setter('fields'):
            '''
            Build the normal way
            '''
            bulk = kwargs.pop('bulk')
            bulk_type = kwargs.pop('bulk_type')
            obj = cls.__new__(cls, bulk, **kwargs)

            '''
            Set list attributes
            '''
            for attr, list_value in list_dict.items():
                setattr(obj, attr, list_value)
        return obj


class Tensors(AbstractNdarray):
    """
    Set of tensors with the same basis.

    TODO:
        all slot args should be protected -> _base

    Args:
        tensors: np.ndarray or AbstractNdarray subclass
        **kwargs:
            name: optional - custom name, can be anything

    Examples:
        >>> import numpy as np
        >>> import tfields

        Initialize a scalar range

        >>> scalars = tfields.Tensors([0, 1, 2])
        >>> scalars.rank == 0
        True

        Initialize vectors

        >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
        >>> vectors.rank == 1
        True
        >>> vectors.dim == 3
        True
        >>> assert vectors.coord_sys == 'cartesian'

        Initialize the Levi-Zivita Tensor

        >>> matrices = tfields.Tensors(
        ...                     [[[0, 0, 0], [0, 0, 1], [0, -1, 0]],
        ...                      [[0, 0, -1], [0, 0, 0], [1, 0, 0]],
        ...                      [[0, 1, 0], [-1, 0, 0], [0, 0, 0]]])
        >>> matrices.shape == (3, 3, 3)
        True
        >>> matrices.rank == 2
        True
        >>> matrices.dim == 3
        True

        Initializing in different start coordinate system

        >>> cyl = tfields.Tensors([[5, np.arctan(4. / 3.), 42]], coord_sys='cylinder')
        >>> assert cyl.coord_sys == 'cylinder'
        >>> cyl.transform('cartesian')
        >>> assert cyl.coord_sys == 'cartesian'
        >>> cart = cyl
        >>> assert round(cart[0, 0], 10) == 3.
        >>> assert round(cart[0, 1], 10) == 4.
        >>> assert cart[0, 2] == 42

        Initialize with copy constructor keeps the coordinate system

        >>> with vectors.tmp_transform('cylinder'):
        ...     vect_cyl = tfields.Tensors(vectors)
        ...     assert vect_cyl.coord_sys == vectors.coord_sys
        >>> assert vect_cyl.coord_sys == 'cylinder'

        You can demand a special dimension.

        >>> _ = tfields.Tensors([[1, 2, 3]], dim=3)
        >>> _ = tfields.Tensors([[1, 2, 3]], dim=2)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        ValueError: Incorrect dimension: 3 given, 2 demanded.

        The dimension argument (dim) becomes necessary if you want to initialize
        an empty array

        >>> _ = tfields.Tensors([])  # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        ValueError: Empty tensors need dimension parameter 'dim'.
        >>> tfields.Tensors([], dim=7)
        Tensors([], shape=(0, 7), dtype=float64)

    """
    __slots__ = ['coord_sys', 'name']
    __slot_defaults__ = ['cartesian']
    __slot_setters__ = [tfields.bases.get_coord_system_name]

    def __new__(cls, tensors, **kwargs):
        dtype = kwargs.pop("dtype", None)
        order = kwargs.pop("order", None)
        dim = kwargs.pop("dim", None)

        """ copy constructor extracts the kwargs from tensors"""
        if issubclass(type(tensors), Tensors):
            if dim is not None:
                dim = tensors.dim
            coord_sys = kwargs.pop("coord_sys", tensors.coord_sys)
            tensors = tensors.copy()
            tensors.transform(coord_sys)
            kwargs['coord_sys'] = coord_sys
            kwargs['name'] = kwargs.pop('name', tensors.name)
            if dtype is None:
                dtype = tensors.dtype
        else:
            if dtype is None:
                if hasattr(tensors, "dtype"):
                    dtype = tensors.dtype
                else:
                    dtype = np.float64

        """ demand iterable structure """
        try:
            len(tensors)
        except TypeError as err:
            raise TypeError(
                "Iterable structure necessary."
                " Got {tensors}".format(**locals())
            )

        """ process empty inputs """
        if len(tensors) == 0:
            if issubclass(type(tensors), tfields.Tensors):
                tensors = np.empty(tensors.shape, dtype=tensors.dtype)
            elif dim is not None:
                tensors = np.empty((0, dim))
            if issubclass(type(tensors), np.ndarray):
                # np.empty
                pass
            else:
                raise ValueError(
                    "Empty tensors need dimension " "parameter 'dim'."
                )

        tensors = np.asarray(tensors, dtype=dtype, order=order)
        obj = tensors.view(cls)

        """ check dimension(s) """
        for d in obj.shape[1:]:
            if not d == obj.dim:
                raise ValueError(
                    "Dimensions are inconstistent. "
                    "Manifold dimension is {obj.dim}. "
                    "Found dimensions {found} in {obj}.".format(
                        found=obj.shape[1:], **locals()
                    )
                )
        if dim is not None:
            if dim != obj.dim:
                raise ValueError(
                    "Incorrect dimension: {obj.dim} given,"
                    " {dim} demanded.".format(**locals())
                )

        """ update kwargs with defaults from slots """
        cls._update_slot_kwargs(kwargs)

        """ set kwargs to slots attributes """
        for attr in kwargs:
            if attr not in cls._iter_slots():
                raise AttributeError(
                    "Keyword argument {attr} not accepted "
                    "for class {cls}".format(**locals())
                )
            setattr(obj, attr, kwargs[attr])

        return obj

    def __iter__(self):
        """
        Forwarding iterations to the bulk array. Otherwise __getitem__ would
        kick in and slow down imensely.

        Examples:
            >>> import tfields
            >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
            >>> scalar_field = tfields.TensorFields(vectors, [42, 21, 10.5], [1, 2, 3])
            >>> [(point.rank, point.dim) for point in scalar_field]
            [(0, 1), (0, 1), (0, 1)]

        """
        for index in range(len(self)):
            yield super(Tensors, self).__getitem__(index).view(Tensors)

    @classmethod
    def merged(cls, *objects, **kwargs):
        """
        Factory method
        Merges all tensor inputs to one tensor

        Examples:
            >>> import numpy as np
            >>> import tfields
            >>> import tfields.bases

            Use of most frequent coordinate system

            >>> vec_a = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
            >>> vec_b = tfields.Tensors([[5, 4, 1]], coord_sys=tfields.bases.cylinder)
            >>> vec_c = tfields.Tensors([[4, 2, 3]], coord_sys=tfields.bases.cylinder)
            >>> merge = tfields.Tensors.merged(vec_a, vec_b, vec_c, [[2, 0, 1]])
            >>> assert merge.coord_sys == 'cylinder'
            >>> assert merge.equal([[0, 0, 0],
            ...                     [0, 0, 1],
            ...                     [1, -np.pi / 2, 0],
            ...                     [5, 4, 1],
            ...                     [4, 2, 3],
            ...                     [2, 0, 1]])

            Merge also shifts the maps to still refer to the same tensors

            >>> tm_a = tfields.TensorMaps(merge, maps=[[[0, 1, 2]]])
            >>> tm_b = tm_a.copy()
            >>> assert tm_a.coord_sys == 'cylinder'
            >>> tm_merge = tfields.TensorMaps.merged(tm_a, tm_b)
            >>> assert tm_merge.coord_sys == 'cylinder'
            >>> assert tm_merge.maps[0].equal([[0, 1, 2],
            ...                               list(range(len(merge),
            ...                                          len(merge) + 3,
            ...                                          1))])

            >>> obj_list = [tfields.Tensors([[1, 2, 3]], coord_sys=tfields.bases.CYLINDER),
            ...             tfields.Tensors([[3] * 3]),
            ...             tfields.Tensors([[5, 1, 3]])]
            >>> merge2 = tfields.Tensors.merged(*obj_list, coord_sys=tfields.bases.CARTESIAN)
            >>> assert merge2.equal([[-0.41614684, 0.90929743, 3.],
            ...                      [3, 3, 3], [5, 1, 3]], atol=1e-8)

        """

        """ get most frequent coord_sys or predefined coord_sys """
        coord_sys = kwargs.get("coord_sys", None)
        dimension = kwargs.get("dim", None)
        if coord_sys is None:
            bases = []
            for t in objects:
                try:
                    bases.append(t.coord_sys)
                except AttributeError:
                    pass
            if bases:
                # get most frequent coord_sys
                coord_sys = sorted(bases, key=Counter(bases).get, reverse=True)[
                    0
                ]
                kwargs["coord_sys"] = coord_sys
            else:
                default = cls.__slot_defaults__[
                    cls.__slots__.index("coord_sys")
                ]
                kwargs["coord_sys"] = default

        """ transform all raw inputs to cls type with correct coord_sys. Also
        automatically make a copy of those instances that are of the correct
        type already."""
        objects = [cls.__new__(cls, t, **kwargs) for t in objects]

        """ check rank and dimension equality """
        if not len(set([t.rank for t in objects])) == 1:
            raise TypeError("Tensors must have the same rank for merging.")
        if not len(set([t.dim for t in objects])) == 1:
            raise TypeError("Tensors must have the same dimension for merging.")

        """ merge all objects """
        remainingObjects = objects[1:] or []
        tensors = objects[0]

        for i, obj in enumerate(remainingObjects):
            tensors = np.append(tensors, obj, axis=0)

        if len(tensors) == 0 and dimension is None:
            for obj in objects:
                kwargs["dim"] = dim(obj)

        return cls.__new__(cls, tensors, **kwargs)

    @classmethod
    def grid(cls, *base_vectors, **kwargs):
        """
        Args:
            *base_vectors (Iterable): base coordinates. The amount of base
                vectors defines the dimension

            **kwargs:
                iter_order (list): order in which the iteration will be done.
                    Frequency rises with position in list. default is [0, 1, 2]
                    iteration will be done like::

                    for v0 in base_vectors[iter_order[0]]:
                        for v1 in base_vectors[iter_order[1]]:
                            for v2 in base_vectors[iter_order[2]]:
                                coords0.append(locals()['v%i' % iter_order[0]])
                                coords1.append(locals()['v%i' % iter_order[1]])
                                coords2.append(locals()['v%i' % iter_order[2]])

        Examples:
            Initilaize using the mgrid notation

            >>> import tfields
            >>> mgrid = tfields.Tensors.grid((0, 1, 2j), (3, 4, 2j), (6, 7, 2j))
            >>> mgrid.equal([[0, 3, 6],
            ...              [0, 3, 7],
            ...              [0, 4, 6],
            ...              [0, 4, 7],
            ...              [1, 3, 6],
            ...              [1, 3, 7],
            ...              [1, 4, 6],
            ...              [1, 4, 7]])
            True

            Lists or arrays are accepted also.
            Furthermore, the iteration order can be changed

            >>> lins = tfields.Tensors.grid(np.linspace(3, 4, 2), np.linspace(0, 1, 2),
            ...                             np.linspace(6, 7, 2), iter_order=[1, 0, 2])
            >>> lins.equal([[3, 0, 6],
            ...             [3, 0, 7],
            ...             [4, 0, 6],
            ...             [4, 0, 7],
            ...             [3, 1, 6],
            ...             [3, 1, 7],
            ...             [4, 1, 6],
            ...             [4, 1, 7]])
            True
            >>> lins2 = tfields.Tensors.grid(np.linspace(0, 1, 2),
            ...                              np.linspace(3, 4, 2),
            ...                              np.linspace(6, 7, 2),
            ...                              iter_order=[2, 0, 1])
            >>> lins2.equal([[0, 3, 6],
            ...              [0, 4, 6],
            ...              [1, 3, 6],
            ...              [1, 4, 6],
            ...              [0, 3, 7],
            ...              [0, 4, 7],
            ...              [1, 3, 7],
            ...              [1, 4, 7]])
            True

            When given the coord_sys argument, the grid is performed in the
            given coorinate system:

            >>> lins3 = tfields.Tensors.grid(np.linspace(4, 9, 2),
            ...                              np.linspace(np.pi/2, np.pi/2, 1),
            ...                              np.linspace(4, 4, 1),
            ...                              iter_order=[2, 0, 1],
            ...                              coord_sys=tfields.bases.CYLINDER)
            >>> assert lins3.coord_sys == 'cylinder'
            >>> lins3.transform('cartesian')
            >>> assert np.array_equal(lins3[:, 1], [4, 9])

        """
        cls_kwargs = {
            attr: kwargs.pop(attr)
            for attr in list(kwargs)
            if attr in cls.__slots__
        }
        inst = cls.__new__(
            cls, tfields.lib.grid.igrid(*base_vectors, **kwargs), **cls_kwargs
        )
        return inst

    @property
    def rank(self):
        """
        Tensor rank
        """
        return rank(self)

    @property
    def dim(self):
        """
        Manifold dimension
        """
        return dim(self)

    def transform(self, coord_sys):
        """
        Args:
            coord_sys (str)

        Examples:
            >>> import numpy as np
            >>> import tfields

            CARTESIAN to SPHERICAL
            >>> t = tfields.Tensors([[1, 2, 2], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, 0, 0]])
            >>> t.transform('spherical')

            r

            >>> assert t[0, 0] == 3

            phi

            >>> assert t[1, 1] == 0.
            >>> assert t[2, 1] == 0.

            theta is 0 at (0, 0, 1) and pi / 2 at (0, 0, -1)

            >>> assert round(t[1, 2], 10) == round(0, 10)
            >>> assert t[2, 2] == -np.pi / 2
            >>> assert t[3, 2] == np.pi / 2

            theta is defined 0 for R == 0

            >>> assert t[4, 0] == 0.
            >>> assert t[4, 2] == 0.


            CARTESIAN to CYLINDER

            >>> tCart = tfields.Tensors([[3, 4, 42], [1, 0, 0], [0, 1, -1], [-1, 0, 1], [0, 0, 0]])
            >>> t_cyl = tCart.copy()
            >>> t_cyl.transform('cylinder')
            >>> assert t_cyl.coord_sys == 'cylinder'

            R

            >>> assert t_cyl[0, 0] == 5
            >>> assert t_cyl[1, 0] == 1
            >>> assert t_cyl[2, 0] == 1
            >>> assert t_cyl[4, 0] == 0

            Phi

            >>> assert round(t_cyl[0, 1], 10) == round(np.arctan(4. / 3), 10)
            >>> assert t_cyl[1, 1] == 0
            >>> assert round(t_cyl[2, 1], 10) == round(np.pi / 2, 10)
            >>> assert t_cyl[1, 1] == 0

            Z

            >>> assert t_cyl[0, 2] == 42
            >>> assert t_cyl[2, 2] == -1

            >>> t_cyl.transform('cartesian')
            >>> assert t_cyl.coord_sys == 'cartesian'
            >>> assert t_cyl[0, 0] == 3

        """
        #           scalars                 empty             already there
        if self.rank == 0 or self.shape[0] == 0 or self.coord_sys == coord_sys:
            self.coord_sys = coord_sys
            return

        tfields.bases.transform(self, self.coord_sys, coord_sys)
        # self[:] = tfields.bases.transform(self, self.coord_sys, coord_sys)
        self.coord_sys = coord_sys

    @contextmanager
    def tmp_transform(self, coord_sys):
        """
        Temporarily change the coord_sys to another coord_sys and change it back at exit
        This method is for cleaner code only.
        No speed improvements go with this.

        Args:
            see transform

        Examples:
            >>> import tfields
            >>> p = tfields.Tensors([[1,2,3]], coord_sys=tfields.bases.SPHERICAL)
            >>> with p.tmp_transform(tfields.bases.CYLINDER):
            ...     assert p.coord_sys == tfields.bases.CYLINDER
            >>> assert p.coord_sys == tfields.bases.SPHERICAL

        """
        baseBefore = self.coord_sys
        if baseBefore == coord_sys:
            yield
        else:
            self.transform(coord_sys)

            yield

            self.transform(baseBefore)

    def mirror(self, coordinate, condition=None):
        """
        Reflect/Mirror the entries meeting <condition> at <coordinate> = 0

        Args:
            coordinate (int): coordinate index

        Examples:
            >>> import tfields
            >>> p = tfields.Tensors([[1., 2., 3.], [4., 5., 6.], [1, 2, -6]])
            >>> p.mirror(1)
            >>> assert p.equal([[1, -2, 3], [4, -5,  6], [1, -2, -6]])

            multiple coordinates can be mirrored at the same time
            i.e. a point mirrorion would be

            >>> p = tfields.Tensors([[1., 2., 3.], [4., 5., 6.], [1, 2, -6]])
            >>> p.mirror([0,2])
            >>> assert p.equal([[-1, 2, -3], [-4, 5, -6], [-1, 2., 6.]])

            You can give a condition as mask or as str.
            The mirroring will only be applied to the points meeting the condition.

            >>> import sympy
            >>> x, y, z = sympy.symbols('x y z')
            >>> p.mirror([0, 2], y > 3)
            >>> p.equal([[-1, 2, -3], [4, 5, 6], [-1, 2, 6]])
            True

        """
        if condition is None:
            condition = np.array([True for i in range(len(self))])
        elif isinstance(condition, sympy.Basic):
            condition = self.evalf(condition)
        if isinstance(coordinate, list) or isinstance(coordinate, tuple):
            for c in coordinate:
                self.mirror(c, condition=condition)
        elif isinstance(coordinate, int):
            self[:, coordinate][condition] *= -1
        else:
            raise TypeError()

    def to_segment(
        self,
        segment,
        num_segments,
        coordinate,
        periodicity=2 * np.pi,
        offset=0.0,
        coord_sys=None,
    ):
        """
        For circular (close into themself after
        <periodicity>) coordinates at index <coordinate> assume
        <num_segments> segments and transform all values to
        segment number <segment>

        Args:
            segment (int): segment index (starting at 0)
            num_segments (int): number of segments
            coordinate (int): coordinate index
            periodicity (float): after what lenght, the coordiante repeats
            offset (float): offset in the mapping
            coord_sys (str or sympy.CoordinateSystem): in which coord sys the
                transformation should be done

        Examples:
            >>> import tfields
            >>> import numpy as np
            >>> pStart = tfields.Points3D([[6, 2 * np.pi, 1],
            ...                            [6, 2 * np.pi / 5 * 3, 1]],
            ...                           coord_sys='cylinder')
            >>> p = tfields.Points3D(pStart)
            >>> p.to_segment(0, 5, 1, offset=-2 * np.pi / 10)
            >>> assert np.array_equal(p[:, 1], [0, 0])

            >>> p2 = tfields.Points3D(pStart)
            >>> p2.to_segment(1, 5, 1, offset=-2 * np.pi / 10)
            >>> assert np.array_equal(np.round(p2[:, 1], 4), [1.2566] * 2)

        """
        if segment > num_segments - 1:
            raise ValueError("Segment {0} not existent.".format(segment))

        if coord_sys is None:
            coord_sys = self.coord_sys
        with self.tmp_transform(coord_sys):
            # map all values to first segment
            self[:, coordinate] = (
                (self[:, coordinate] - offset) % (periodicity / num_segments)
                + offset
                + segment * periodicity / num_segments
            )

    def equal(
        self, other, rtol=None, atol=None, equal_nan=False, return_bool=True
    ):
        """
        Evaluate, whether the instance has the same content as other.

        Args:
            optional:
                rtol (float)
                atol (float)
                equal_nan (bool)
            see numpy.isclose
        """
        if (
            issubclass(type(other), Tensors)
            and self.coord_sys != other.coord_sys
        ):
            other = other.copy()
            other.transform(self.coord_sys)
        x, y = np.asarray(self), np.asarray(other)
        if rtol is None and atol is None:
            mask = x == y
            if equal_nan:
                both_nan = np.isnan(x) & np.isnan(y)
                mask[both_nan] = both_nan[both_nan]
        else:
            if rtol is None:
                rtol = 0.0
            if atol is None:
                atol = 0.0
            mask = np.isclose(x, y, rtol=rtol, atol=atol, equal_nan=equal_nan)
        if return_bool:
            return bool(np.all(mask))
        return mask

    def contains(self, other, **kwargs):
        """
        Inspired by a speed argument @
        stackoverflow.com/questions/14766194/testing-whether-a-numpy-array-contains-a-given-row

        Examples:
            >>> import tfields
            >>> p = tfields.Tensors([[1,2,3], [4,5,6], [6,7,8]])
            >>> p.contains([4,5,6])
            True

        """
        return any(self.equal(other, return_bool=False).all(1))

    def indices(self, tensor, rtol=None, atol=None):
        """
        Returns:
            list of int: indices of tensor occuring

        Examples:
            Rank 1 Tensors

            >>> import tfields
            >>> p = tfields.Tensors([[1,2,3], [4,5,6], [6,7,8], [4,5,6],
            ...                      [4.1, 5, 6]])
            >>> p.indices([4,5,6])
            array([1, 3])
            >>> p.indices([4,5,6.1], rtol=1e-5, atol=1e-1)
            array([1, 3, 4])

            Rank 0 Tensors

            >>> p = tfields.Tensors([2, 3, 6, 3.01])
            >>> p.indices(3)
            array([1])
            >>> p.indices(3, rtol=1e-5, atol=1e-1)
            array([1, 3])

        """
        x, y = np.asarray(self), np.asarray(tensor)
        if rtol is None and atol is None:
            equal_method = np.equal
        else:
            equal_method = lambda a, b: np.isclose(a, b, rtol=rtol, atol=atol)

        # inspired by https://stackoverflow.com/questions/19228295/find-ordered-vector-in-numpy-array
        if self.rank == 0:
            indices = np.where(equal_method((x - y), 0))[0]
        elif self.rank == 1:
            indices = np.where(np.all(equal_method((x - y), 0), axis=1))[0]
        else:
            raise NotImplementedError()
        return indices

    def index(self, tensor, **kwargs):
        """
        Args:
            tensor

        Returns:
            int: index of tensor occuring
        """
        indices = self.indices(tensor, **kwargs)
        if not indices:
            return None
        if len(indices) == 1:
            return indices[0]
        raise ValueError("Multiple occurences of value {}".format(tensor))

    def moment(self, moment, weights=None):
        """
        Returns:
            Moments of the distribution.

        Args:
            moment (int): n-th moment

        Examples:
            >>> import tfields
            >>> import numpy as np

            Skalars

            >>> t = tfields.Tensors(range(1, 6))
            >>> assert t.moment(1) == 0
            >>> assert t.moment(1, weights=[-2, -1, 20, 1, 2]) == 0.5
            >>> assert t.moment(2, weights=[0.25, 1, 17.5, 1, 0.25]) == 0.2

            Vectors

            >>> t = tfields.Tensors(list(zip(range(1, 6), range(1, 6))))
            >>> assert Tensors([0.5, 0.5]).equal(t.moment(1, weights=[-2, -1, 20, 1, 2]))
            >>> assert Tensors([1. , 0.5]).equal(
            ...     t.moment(1, weights=list(zip([-2, -1, 10, 1, 2],
            ...                                  [-2, -1, 20, 1, 2]))))

        """
        array = tfields.lib.stats.moment(self, moment, weights=weights)
        if self.rank == 0:  # scalar
            array = [array]
        return Tensors(array, coord_sys=self.coord_sys)

    def closest(self, other, **kwargs):
        """
        Args:
            other (Tensors): closest points to what? -> other
            **kwargs: forwarded to scipy.spatial.cKDTree.query

        Returns:
            array shape(len(self)): Indices of other points that are closest to own points

        Examples:
            >>> import tfields
            >>> m = tfields.Tensors([[1,0,0], [0,1,0], [1,1,0], [0,0,1],
            ...                      [1,0,1]])
            >>> p = tfields.Tensors([[1.1,1,0], [0,0.1,1], [1,0,1.1]])
            >>> p.closest(m)
            array([2, 3, 4])

        """
        with other.tmp_transform(self.coord_sys):
            # balanced_tree option gives huge speedup!
            kd_tree = sp.spatial.cKDTree(other, 1000, balanced_tree=False)
            res = kd_tree.query(self, **kwargs)
            array = res[1]

        return array

    def evalf(self, expression=None, coord_sys=None):
        """
        Args:
            expression (sympy logical expression)
            coord_sys (str): coord_sys to evalfuate the expression in.

        Returns:
            np.ndarray: mask of dtype bool with lenght of number of points in self.
                 This array is True, where expression evalfuates True.

        Examples:
            >>> import tfields
            >>> import numpy
            >>> import sympy
            >>> x, y, z = sympy.symbols('x y z')
            >>> p = tfields.Tensors([[1., 2., 3.], [4., 5., 6.], [1, 2, -6],
            ...                      [-5, -5, -5], [1,0,-1], [0,1,-1]])
            >>> np.array_equal(p.evalf(x > 0),
            ...                [True, True, True, False, True, False])
            True
            >>> np.array_equal(p.evalf(x >= 0),
            ...                [True, True, True, False, True, True])
            True

            And combination

            >>> np.array_equal(p.evalf((x > 0) & (y < 3)),
            ...                [True, False, True, False, True, False])
            True

            Or combination

            >>> np.array_equal(p.evalf((x > 0) | (y > 3)),
            ...                [True, True, True, False, True, False])
            True

        """
        coords = sympy.symbols("x y z")
        with self.tmp_transform(coord_sys or self.coord_sys):
            mask = tfields.evalf(np.array(self), expression, coords=coords)
        return mask

    def cut(self, expression, coord_sys=None):
        """
        Default cut method for Points3D. Works on a copy.

        Args:
            expression (sympy logical expression): logical expression which will be evalfuated.
                             use symbols x, y and z
            coord_sys (str): coord_sys to evalfuate the expression in.

        Examples:
            >>> import tfields
            >>> import sympy
            >>> x, y, z = sympy.symbols('x y z')
            >>> p = tfields.Tensors([[1., 2., 3.], [4., 5., 6.], [1, 2, -6],
            ...                      [-5, -5, -5], [1,0,-1], [0,1,-1]])
            >>> p.cut(x > 0).equal([[1, 2, 3],
            ...                     [4, 5, 6],
            ...                     [1, 2, -6],
            ...                     [1, 0, -1]])
            True

            combinations of cuts

            >>> p.cut((x > 0) & (z < 0)).equal([[1, 2, -6], [1, 0, -1]])
            True

        Returns:
            copy of self with cut applied

        """
        if len(self) == 0:
            return self.copy()
        mask = self.evalf(expression, coord_sys=coord_sys or self.coord_sys)
        mask.astype(bool)
        inst = self[mask].copy()
        return inst

    def distances(self, other, **kwargs):
        """
        Args:
            other(Iterable)
            **kwargs:
                ... is forwarded to sp.spatial.distance.cdist

        Examples:
            >>> import tfields
            >>> p = tfields.Tensors.grid((0, 2, 3j),
            ...                          (0, 2, 3j),
            ...                          (0, 0, 1j))
            >>> p[4,2] = 1
            >>> p.distances(p)[0,0]
            0.0
            >>> p.distances(p)[5,1]
            1.4142135623730951
            >>> p.distances([[0,1,2]])[-1][0] == 3
            True

        """
        if (
            issubclass(type(other), Tensors)
            and self.coord_sys != other.coord_sys
        ):
            other = other.copy()
            other.transform(self.coord_sys)
        return sp.spatial.distance.cdist(self, other, **kwargs)

    def min_dists(self, other=None, **kwargs):
        """
        Args:
            other(array | None): if None: closest distance to self
            **kwargs:
                memory_saving (bool): for very large array comparisons
                    default False
                ... rest is forwarded to sp.spatial.distance.cdist

        Returns:
            np.array: minimal distances of self to other

        Examples:
            >>> import tfields
            >>> import numpy as np
            >>> p = tfields.Tensors.grid((0, 2, 3),
            ...                          (0, 2, 3),
            ...                          (0, 0, 1))
            >>> p[4,2] = 1
            >>> dMin = p.min_dists()
            >>> expected = [1] * 9
            >>> expected[4] = np.sqrt(2)
            >>> np.array_equal(dMin, expected)
            True

            >>> dMin2 = p.min_dists(memory_saving=True)
            >>> bool((dMin2 == dMin).all())
            True

        """
        memory_saving = kwargs.pop("memory_saving", False)

        if other is None:
            other = self
        else:
            raise NotImplementedError(
                "Should be easy but make shure not to remove diagonal"
            )

        try:
            if memory_saving:
                raise MemoryError()
            d = self.distances(other, **kwargs)
            return d[d > 0].reshape(d.shape[0], -1).min(axis=1)
        except MemoryError:
            min_dists = np.empty(self.shape[0])
            for i, point in enumerate(np.array(other)):
                d = self.distances([point], **kwargs)
                min_dists[i] = d[d > 0].reshape(-1).min()
            return min_dists

    def epsilon_neighbourhood(self, epsilon):
        """
        Returns:
            indices for those sets of points that lie within epsilon around the other

        Examples:
            Create mesh grid with one extra point that will have 8 neighbours
            within epsilon
            >>> import tfields
            >>> p = tfields.Tensors.grid((0, 1, 2j),
            ...                          (0, 1, 2j),
            ...                          (0, 1, 2j))
            >>> p = tfields.Tensors.merged(p, [[0.5, 0.5, 0.5]])
            >>> [len(en) for en in p.epsilon_neighbourhood(0.9)]
            [2, 2, 2, 2, 2, 2, 2, 2, 9]

        """
        indices = np.arange(self.shape[0])
        dists = self.distances(self)  # this takes long
        distsInEpsilon = dists <= epsilon
        indices = [indices[die] for die in distsInEpsilon]  # this takes long
        return indices

    def _weights(self, weights, rigid=True):
        """
        transformer method for weights inputs.

        Args:
            weights (np.ndarray | None):
                If weights is None, use np.ones
                Otherwise just pass the weights.
            rigid (bool): demand equal weights and tensor length

        Returns:
            weight array
        """
        # set weights to 1.0 if weights is None
        if weights is None:
            weights = np.ones(len(self))
        if rigid:
            if not len(weights) == len(self):
                raise ValueError("Equal number of weights as tensors demanded.")
        return weights

    def cov_eig(self, weights=None):
        """
        Calculate the covariance eigenvectors with lenghts of eigenvalues

        Args:
            weights (np.array | int | None): index to scalars to weight with
        """
        # weights = self.getNormedWeightedAreas(weights=weights)
        weights = self._weights(weights)
        cov = np.cov(self.T, ddof=0, aweights=weights)
        # calculate eigenvalues and eigenvectors of covariance
        evalfs, evecs = np.linalg.eigh(cov)
        idx = evalfs.argsort()[::-1]
        evalfs = evalfs[idx]
        evecs = evecs[:, idx]
        e = np.concatenate((evecs, evalfs.reshape(1, 3)))
        return e.T.reshape(12,)

    def main_axes(self, weights=None):
        """
        Returns:
            Main Axes eigen-vectors
        """
        # weights = self.getNormedWeightedAreas(weights=weights)
        weights = self._weights(weights)
        mean = np.array(self).mean(axis=0)
        relative_coords = self - mean
        cov = np.cov(relative_coords.T, ddof=0, aweights=weights)
        # calculate eigenvalues and eigenvectors of covariance
        evalfs, evecs = np.linalg.eigh(cov)
        return (evecs * evalfs.T).T

    def plot(self, **kwargs):
        """
        Forwarding to rna.plotting.plot_array
        """
        artist = rna.plotting.plot_array(self, **kwargs)
        return artist


def as_tensors_list(tensors_list):
    """
    Setter for TensorFields.fields
    Copies input
    Examples:
        >>> import tfields
        >>> import numpy as np
        >>> scalars = tfields.Tensors([0, 1, 2])
        >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
        >>> maps = [tfields.TensorFields([[0, 1, 2], [0, 1, 2]]),
        ...         tfields.TensorFields([[1], [2]], [-42, -21])]
        >>> mesh = tfields.TensorMaps(vectors, scalars,
        ...                           maps=maps)
        >>> mesh.maps[0].fields = [[42, 21]]
        >>> assert len(mesh.maps[0].fields) == 1
        >>> assert mesh.maps[0].fields[0].equal([42, 21])

    """
    if tensors_list is not None:
        new_list = []
        for tensors in tensors_list:
            tensors_list = Tensors(tensors)
            new_list.append(tensors_list)
        tensors_list = new_list
    return tensors_list


class TensorFields(Tensors):
    """
    Discrete Tensor Field

    Args:
        tensors (array): base tensors
        *fields (array): multiple fields assigned to one base tensor. Fields
            themself are also of type tensor
        **kwargs:
            rigid (bool): demand equal field and tensor lenght
            ... : see tfields.Tensors

    Examples:
        >>> from tfields import Tensors, TensorFields
        >>> scalars = Tensors([0, 1, 2])
        >>> vectors = Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
        >>> scalar_field = TensorFields(vectors, scalars)
        >>> scalar_field.rank
        1
        >>> scalar_field.fields[0].rank
        0
        >>> vectorField = TensorFields(vectors, vectors)
        >>> vectorField.fields[0].rank
        1
        >>> vectorField.fields[0].dim
        3
        >>> multiField = TensorFields(vectors, scalars, vectors)
        >>> multiField.fields[0].dim
        1
        >>> multiField.fields[1].dim
        3

        Empty initialization

        >>> empty_field = TensorFields([], dim=3)
        >>> assert empty_field.shape == (0, 3)
        >>> assert empty_field.fields == []

        Directly initializing with lists or arrays

        >>> vec_field_raw = tfields.TensorFields([[0, 1, 2], [3, 4, 5]],
        ...                                       [1, 6], [2, 7])
        >>> assert len(vec_field_raw.fields) == 2

        Copying

        >>> cp = TensorFields(vectorField)
        >>> assert vectorField.equal(cp)

        Copying takes care of coord_sys

        >>> cp.transform(tfields.bases.CYLINDER)
        >>> cp_cyl = TensorFields(cp)
        >>> assert cp_cyl.coord_sys == tfields.bases.CYLINDER

        Copying with changing type

        >>> tcp = TensorFields(vectorField, dtype=int)
        >>> assert vectorField.equal(tcp)
        >>> assert tcp.dtype == int

    Raises:
        TypeError:

        >>> import tfields
        >>> tfields.TensorFields([1, 2, 3], [3])  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        ValueError: Length of base (3) should be the same as the length of all fields ([1]).

        This error can be suppressed by setting rigid=False

        >>> loose = tfields.TensorFields([1, 2, 3], [3], rigid=False)
        >>> assert len(loose) != 1

    """

    __slots__ = ['coord_sys', 'name', 'fields']
    __slot_setters__ = [tfields.bases.get_coord_system_name,
                        None,
                        as_tensors_list]

    def __new__(cls, tensors, *fields, **kwargs):
        rigid = kwargs.pop("rigid", True)

        obj = super(TensorFields, cls).__new__(cls, tensors, **kwargs)
        if issubclass(type(tensors), TensorFields):
            if tensors.fields is None:
                raise ValueError("Tensor fields were None")
            obj.fields = tensors.fields
        elif not fields:
            obj.fields = []
        if fields:
            # (over)write fields
            obj.fields = fields

        if rigid:
            olen = len(obj)
            field_lengths = [len(f) for f in obj.fields]
            if not all([flen == olen for flen in field_lengths]):
                raise ValueError(
                    "Length of base ({olen}) should be the same as"
                    " the length of all fields ({field_lengths}).".format(
                        **locals()
                    )
                )
        return obj

    def __getitem__(self, index):
        """
        In addition to the usual, also slice fields
        Examples:
            >>> import tfields
            >>> import numpy as np
            >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
            >>> scalar_field = tfields.TensorFields(vectors,
            ...                                     [42, 21, 10.5],
            ...                                     [1, 2, 3],
            ...                                     [[0, 0], [-1, -1], [-2, -2]])

            Slicing

            >>> sliced = scalar_field[2:]
            >>> assert isinstance(sliced, tfields.TensorFields)
            >>> assert isinstance(sliced.fields[0], tfields.Tensors)
            >>> assert sliced.fields[0].equal([10.5])

            Picking

            >>> picked = scalar_field[1]
            >>> assert np.array_equal(picked, [0, 0, 1])
            >>> assert np.array_equal(picked.fields[0], 21)

            Masking

            >>> masked = scalar_field[np.array([True, False, True])]
            >>> assert masked.equal([[0, 0, 0], [0, -1, 0]])
            >>> assert masked.fields[0].equal([42, 10.5])
            >>> assert masked.fields[1].equal([1, 3])

            Iteration

            >>> _ = [point for point in scalar_field]

        """
        item = super(TensorFields, self).__getitem__(index)
        try:
            if issubclass(type(item), TensorFields):
                if isinstance(index, tuple):
                    index = index[0]
                if item.fields:
                    # circumvent the setter here.
                    with self._bypass_setter('fields'):
                        item.fields = [
                            field.__getitem__(index) for field in item.fields
                        ]
        except IndexError as err:
            warnings.warn(
                "Index error occured for field.__getitem__. Error "
                "message: {err}".format(**locals())
            )

        return item

    def __setitem__(self, index, item):
        """
        In addition to the usual, also slice fields

        Examples:
            >>> import tfields
            >>> import numpy as np
            >>> original = tfields.TensorFields([[0, 0, 0], [0, 0, 1], [0, -1, 0]],
            ...                                  [42, 21, 10.5], [1, 2, 3])
            >>> obj = tfields.TensorFields([[0, 0, 0], [0, 0, np.nan], [0, -1, 0]],
            ...                             [42, 22, 10.5], [1, -1, 3])
            >>> slice_obj = obj.copy()
            >>> assert not obj.equal(original)
            >>> obj[1] = original[1]
            >>> assert obj[:2].equal(original[:2])

            >>> assert not slice_obj.equal(original)
            >>> slice_obj[:] = original[:]
            >>> assert slice_obj.equal(original)

        """
        super(TensorFields, self).__setitem__(index, item)
        if issubclass(type(item), TensorFields):
            if isinstance(index, slice):
                for i, field in enumerate(item.fields):
                    self.fields[i].__setitem__(index, field)
            elif isinstance(index, tuple):
                for i, field in enumerate(item.fields):
                    self.fields[i].__setitem__(index[0], field)
            else:
                for i, field in enumerate(item.fields):
                    self.fields[i].__setitem__(index, field)

    @classmethod
    def merged(cls, *objects, **kwargs):
        if not all([isinstance(o, cls) for o in objects]):
            types = [type(o) for o in objects]
            # TODO: could allow if all faceScalars are none
            raise TypeError(
                "Merge constructor only accepts {cls} instances."
                "Got objects of types {types} instead.".format(**locals())
            )

        inst = super(TensorFields, cls).merged(*objects, **kwargs)

        fields = []
        if all([len(obj.fields) == len(objects[0].fields) for obj in objects]):
            for fld_idx in range(len(objects[0].fields)):
                field = tfields.Tensors.merged(
                    *[obj.fields[fld_idx] for obj in objects]
                )
                fields.append(field)
        inst = cls.__new__(cls, inst, *fields)
        return inst

    @property
    def names(self):
        """
        Retrive the names of the fields as a list

        Examples:
            >>> import numpy as np
            >>> import tfields
            >>> s = tfields.Tensors([1,2,3], name=1.)
            >>> tf = tfields.TensorFields(s, *[s]*10)
            >>> assert len(tf.names) == 10
            >>> assert set(tf.names) == {1.}
            >>> tf.names = range(10)
            >>> tf.names
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        """
        return [f.name for f in self.fields]

    @names.setter
    def names(self, names):
        if not len(names) == len(self.fields):
            raise ValueError("len(names) ({0}) != len(fields) ({1})"
                             .format(len(names), len(self.fields)))
        for i, name in enumerate(names):
            self.fields[i].name = name

    # def transform(self, coord_sys):
    #     super(TensorFields, self).transform(coord_sys)
    #     # for field in self.fields:
    #     #     field.transform(coord_sys)

    def equal(self, other, **kwargs):
        """
        Test, whether the instance has the same content as other.

        Args:
            other (iterable)
            optional:
                see Tensors.equal
        """
        if not issubclass(type(other), Tensors):
            return super(TensorFields, self).equal(other, **kwargs)
        else:
            with other.tmp_transform(self.coord_sys):
                mask = super(TensorFields, self).equal(other, **kwargs)
                if issubclass(type(other), TensorFields):
                    if len(self.fields) != len(other.fields):
                        mask &= False
                    else:
                        for i, field in enumerate(self.fields):
                            mask &= field.equal(other.fields[i], **kwargs)
                return mask

    def _weights(self, weights, rigid=True):
        """
        Expansion of Tensors._weights with integer inputs

        Args:
            weights (np.ndarray | int | None):
                if weights is int: use field at index <weights>
                else: see Tensors._weights
        """
        if isinstance(weights, int):
            weights = self.fields[weights]
        return super(TensorFields, self)._weights(weights, rigid=rigid)

    def plot(self, **kwargs):
        """
        Override Tensors plot method:
            By default, vector fields are plotted with the quiver method
        """
        field_index = kwargs.pop("field_index", None)
        if field_index is None:
            artist = super(TensorFields, self).plot(**kwargs)
        else:
            field = self.fields[field_index].copy()
            if self.dim == field.dim:
                field.transform(self.coord_sys)
            else:
                import logging

                log = logging.getLogger()
                log.debug(
                    "Careful: Plotting tensors with field of"
                    "different dimension. No coord_sys check performed."
                )
            if field.dim <= 3:
                artist = rna.plotting.plot_tensor_field(self, field, **kwargs)
            else:
                raise NotImplementedError(
                    "Field of dimension {field.dim}".format(**locals())
                )
        return artist


class TensorMaps(TensorFields):
    """
    Args:
        tensors: see Tensors class
        *fields (Tensors): see TensorFields class
        **kwargs:
            coord_sys ('str'): see Tensors class
            maps (array-like): indices indicating a connection between the
                tensors at the respective index positions

    Examples:
        >>> import tfields
        >>> import numpy as np
        >>> scalars = tfields.Tensors([0, 1, 2])
        >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
        >>> maps = [tfields.TensorFields([[0, 1, 2], [0, 1, 2]], [42, 21]),
        ...         tfields.TensorFields([[1], [2]], [-42, -21])]
        >>> mesh = tfields.TensorMaps(vectors, scalars,
        ...                           maps=maps)
        >>> assert isinstance(mesh.maps, list)
        >>> assert len(mesh.maps) == 2

        >>> assert mesh.equal(tfields.TensorFields(vectors, scalars))
        >>> assert mesh.maps[0].fields[0].equal(maps[0].fields[0])

        Copy constructor

        >>> mesh_copy = tfields.TensorMaps(mesh)

        Copying takes care of coord_sys

        >>> mesh_copy.transform(tfields.bases.CYLINDER)
        >>> mesh_cp_cyl = tfields.TensorMaps(mesh_copy)
        >>> assert mesh_cp_cyl.coord_sys == tfields.bases.CYLINDER

    Raises:
        >>> import tfields
        >>> tfields.TensorMaps([1] * 4, dim=3, maps=[[1, 2, 3]])  # +doctest: ELLIPSIS
        Traceback (most recent call last):
        ...
        ValueError: Incorrect map rank 0

    """
    __slots__ = ['coord_sys', 'name', 'fields', 'maps']

    def __new__(cls, tensors, *fields, **kwargs):
        maps = kwargs.pop("maps", [])
        maps_cp = []
        for mp in maps:
            mp = TensorFields(mp, dtype=int)
            if not mp.rank == 1:
                raise ValueError(
                    "Incorrect map rank {mp.rank}".format(**locals())
                )
            maps_cp.append(mp)
        maps = maps_cp
        obj = super(TensorMaps, cls).__new__(cls, tensors, *fields, **kwargs)
        obj.maps = maps
        return obj

    def __getitem__(self, index):
        """
        In addition to the usual, also slice fields

        Examples:
            >>> import tfields
            >>> import numpy as np
            >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0],
            ...                            [1, 1, 1], [-1, -1, -1]])
            >>> maps=[tfields.TensorFields([[0, 1, 2], [0, 1, 3], [2, 3, 4]],
            ...                            [[1, 2], [3, 4], [5, 6]]),
            ...       tfields.TensorFields([[0], [1], [2], [3], [4]])]
            >>> mesh = tfields.TensorMaps(vectors,
            ...                           [42, 21, 10.5, 1, 1],
            ...                           [1, 2, 3, 3, 3],
            ...                           maps=maps)

            Slicing

            >>> sliced = mesh[2:]
            >>> assert isinstance(sliced, tfields.TensorMaps)
            >>> assert isinstance(sliced.fields[0], tfields.Tensors)
            >>> assert isinstance(sliced.maps[0], tfields.TensorFields)
            >>> assert sliced.fields[0].equal([10.5, 1, 1])
            >>> assert sliced.maps[0].equal([[0, 1, 2]])
            >>> assert sliced.maps[0].fields[0].equal([[5, 6]])

            Picking

            >>> picked = mesh[1]
            >>> assert np.array_equal(picked, [0, 0, 1])
            >>> assert np.array_equal(picked.maps[0], np.empty((0, 3)))
            >>> assert np.array_equal(picked.maps[1], [[0]])

            Masking

            >>> masked = mesh[np.array([True, False, True, True, True])]
            >>> assert masked.equal([[0, 0, 0], [0, -1, 0], [1, 1, 1], [-1, -1, -1]])
            >>> assert masked.fields[0].equal([42, 10.5, 1, 1])
            >>> assert masked.fields[1].equal([1, 3, 3, 3])
            >>> assert masked.maps[0].equal([[1, 2, 3]])
            >>> assert masked.maps[1].equal([[0], [1], [2], [3]])

            Iteration

            >>> _ = [vertex for vertex in mesh]

        """
        item = super(TensorMaps, self).__getitem__(index)
        try:
            if issubclass(type(item), TensorMaps):
                if isinstance(index, tuple):
                    index = index[0]
                if item.maps:
                    item.maps = [mp.copy() for mp in item.maps]
                    indices = np.array(range(len(self)))
                    keep_indices = indices[index]
                    if isinstance(keep_indices, (int, np.int64, np.int32)):
                        keep_indices = [keep_indices]
                    delete_indices = set(indices).difference(set(keep_indices))

                    # correct all maps that contain deleted indices
                    for mp_idx in range(len(self.maps)):
                        # build mask, where the map should be deleted
                        map_delete_mask = np.full(
                            (len(self.maps[mp_idx]),), False, dtype=bool
                        )
                        for i, mp in enumerate(self.maps[mp_idx]):
                            for index in mp:
                                if index in delete_indices:
                                    map_delete_mask[i] = True
                                    break
                        map_mask = ~map_delete_mask

                        # build the correction counters
                        move_up_counter = np.zeros(
                            self.maps[mp_idx].shape, dtype=int
                        )
                        for p in delete_indices:
                            move_up_counter[self.maps[mp_idx] > p] -= 1

                        item.maps[mp_idx] = (
                            self.maps[mp_idx] + move_up_counter
                        )[map_mask]
        except IndexError as err:
            warnings.warn(
                "Index error occured for field.__getitem__. Error "
                "message: {err}".format(**locals())
            )

        return item

    @classmethod
    def merged(cls, *objects, **kwargs):
        if not all([isinstance(o, cls) for o in objects]):
            # TODO: could allow if all faceScalars are none
            raise TypeError(
                "Merge constructor only accepts {cls} instances.".format(
                    **locals()
                )
            )
        tensor_lengths = [len(o) for o in objects]
        cum_tensor_lengths = [
            sum(tensor_lengths[:i]) for i in range(len(objects))
        ]

        maps = []
        dims = []
        for i, o in enumerate(objects):
            for map_field in o.maps:
                map_field = map_field + cum_tensor_lengths[i]
                try:
                    mp_idx = dims.index(map_field.dim)
                except ValueError:
                    maps.append(map_field)
                    dims.append(map_field.dim)
                else:
                    maps[mp_idx] = TensorFields.merged(maps[mp_idx], map_field)
        # kwargs['maps'] = maps

        inst = super(TensorMaps, cls).merged(*objects, **kwargs)
        inst = cls.__new__(cls, inst, maps=maps)
        return inst

    def equal(self, other, **kwargs):
        """
        Test, whether the instance has the same content as other.

        Args:
            other (iterable)
            optional:
                see TensorFields.equal

        Examples:
            >>> import tfields
            >>> maps = [tfields.TensorFields([[1]], [42])]
            >>> tm = tfields.TensorMaps(maps[0], maps=maps)

            # >>> assert tm.equal(tm)

            >>> cp = tm.copy()

            # >>> assert tm.equal(cp)

            >>> cp.maps[0].fields[0] = -42
            >>> assert tm.maps[0].fields[0] == 42
            >>> assert not tm.equal(cp)

        """
        if not issubclass(type(other), Tensors):
            return super(TensorMaps, self).equal(other, **kwargs)
        else:
            with other.tmp_transform(self.coord_sys):
                mask = super(TensorMaps, self).equal(other, **kwargs)
                if issubclass(type(other), TensorMaps):
                    if len(self.maps) != len(other.maps):
                        mask &= False
                    else:
                        for i, mp in enumerate(self.maps):
                            mask &= mp.equal(other.maps[i], **kwargs)
                return mask

    def stale(self):
        """
        Returns:
            Mask for all vertices that are stale i.e. are not refered by maps

        Examples:
            >>> import tfields
            >>> vectors = tfields.Tensors([[0, 0, 0], [0, 0, 1], [0, -1, 0], [4, 4, 4]])
            >>> tm = tfields.TensorMaps(vectors, maps=[[[0, 1, 2], [0, 1, 2]],
            ...                                       [[1, 1], [2, 2]]])
            >>> assert np.array_equal(tm.stale(), [False, False, False, True])

        """
        staleMask = np.full(self.shape[0], False, dtype=bool)
        used = set([ind for mp in self.maps for ind in mp.flatten()])
        for i in range(self.shape[0]):
            if i not in used:
                staleMask[i] = True
        return staleMask

    def cleaned(self, stale=True, duplicates=True):
        """
        Args:
            stale (bool): remove stale vertices
            duplicates (bool): replace duplicate vertices by originals

        Examples:
            >>> import tfields
            >>> mp1 = tfields.TensorFields([[0, 1, 2], [3, 4, 5]],
            ...                            *zip([1,2,3,4,5], [6,7,8,9,0]))
            >>> mp2 = tfields.TensorFields([[0], [3]])

            >>> tm = tfields.TensorMaps([[0,0,0], [1,1,1], [2,2,2], [0,0,0],
            ...                          [3,3,3], [4,4,4], [5,6,7]],
            ...                         maps=[mp1, mp2])

            >>> c = tm.cleaned()
            >>> assert c.equal([[0., 0., 0.],
            ...                 [1., 1., 1.],
            ...                 [2., 2., 2.],
            ...                 [3., 3., 3.],
            ...                 [4., 4., 4.]])
            >>> assert np.array_equal(c.maps[0], [[0, 1, 2], [0, 3, 4]])
            >>> assert np.array_equal(c.maps[1], [[0], [0]])


        Returns:
            copy of self without stale vertices and duplicat points (depending on arguments)
        """
        # remove stale vertices
        if stale:
            stale_mask = self.stale()
        else:
            stale_mask = np.full(self.shape[0], False, dtype=bool)
        # remove duplicates in order to not have any artificial separations
        inst = self
        if duplicates:
            inst = self.copy()
            duplicates = tfields.duplicates(self, axis=0)
            for tensor_index, duplicate_index in zip(
                range(self.shape[0]), duplicates
            ):
                if duplicate_index != tensor_index:
                    stale_mask[tensor_index] = True
                    # redirect maps
                    for mp_idx in range(len(self.maps)):
                        for f in range(len(self.maps[mp_idx])):
                            mp = np.array(self.maps[mp_idx], dtype=int)
                            if tensor_index in mp[f]:
                                index = tfields.index(mp[f], tensor_index)
                                inst.maps[mp_idx][f][index] = duplicate_index

        return inst.removed(stale_mask)

    def removed(self, remove_condition):
        """
        Return copy of self without vertices where remove_condition is True
        Copy because self is immutable

        Examples:
            >>> import tfields
            >>> m = tfields.TensorMaps([[0,0,0], [1,1,1], [2,2,2], [0,0,0],
            ...                         [3,3,3], [4,4,4], [5,5,5]],
            ...                        maps=[tfields.TensorFields([[0, 1, 2], [0, 1, 3],
            ...                                                    [3, 4, 5], [3, 4, 1],
            ...                                                    [3, 4, 6]],
            ...                                                   [1, 3, 5, 7, 9],
            ...                                                   [2, 4, 6, 8, 0])])
            >>> c = m.keep([False, False, False, True, True, True, True])
            >>> c.equal([[0, 0, 0],
            ...          [3, 3, 3],
            ...          [4, 4, 4],
            ...          [5, 5, 5]])
            True
            >>> assert c.maps[0].equal([[0, 1, 2], [0, 1, 3]])
            >>> assert c.maps[0].fields[0].equal([5, 9])
            >>> assert c.maps[0].fields[1].equal([6, 0])

        """
        remove_condition = np.array(remove_condition)
        # # built instance that only contains the vaild points
        # inst = self[~remove_condition].copy()
        # delete_indices = np.arange(self.shape[0])[remove_condition]
        # face_keep_masks = self.to_maps_masks(~remove_condition)

        # for mp_idx, face_keep_mask in enumerate(face_keep_masks):
        #     move_up_counter = np.zeros(self.maps[mp_idx].shape, dtype=int)

        #     # correct map:
        #     for p in delete_indices:
        #         move_up_counter[self.maps[mp_idx] > p] -= 1

        #     inst.maps[mp_idx] = (self.maps[mp_idx] + move_up_counter)[face_keep_mask]
        # return inst
        return self[~remove_condition]

    def keep(self, keep_condition):
        """
        Return copy of self with vertices where keep_condition is True
        Copy because self is immutable

        Examples:
            >>> import tfields
            >>> m = tfields.TensorMaps([[0,0,0], [1,1,1], [2,2,2], [0,0,0],
            ...                         [3,3,3], [4,4,4], [5,5,5]],
            ...                        maps=[tfields.TensorFields([[0, 1, 2], [0, 1, 3],
            ...                                                    [3, 4, 5], [3, 4, 1],
            ...                                                    [3, 4, 6]],
            ...                                                   [1, 3, 5, 7, 9],
            ...                                                   [2, 4, 6, 8, 0])])
            >>> c = m.removed([True, True, True, False, False, False, False])
            >>> c.equal([[0, 0, 0],
            ...          [3, 3, 3],
            ...          [4, 4, 4],
            ...          [5, 5, 5]])
            True
            >>> assert c.maps[0].equal(np.array([[0, 1, 2], [0, 1, 3]]))
            >>> assert c.maps[0].fields[0].equal([5, 9])
            >>> assert c.maps[0].fields[1].equal([6, 0])

        """
        keep_condition = np.array(keep_condition)
        return self[keep_condition]

    def to_maps_masks(self, mask):
        """
        Examples:
            >>> from tfields import TensorMaps
            >>> import numpy as np
            >>> m = TensorMaps([[1,2,3], [3,3,3], [0,0,0], [5,6,7]],
            ...                maps=[[[0, 1, 2], [1, 2, 3]],
            ...                      [[0], [3]]])
            >>> from sympy.abc import x,y,z
            >>> vertexMask = m.evalf(z < 6)
            >>> faceMask = m.to_maps_masks(vertexMask)
            >>> assert np.array_equal(faceMask, [[True, False], [True, False]])
            >>> index_face_mask = m.to_maps_masks(0)
            >>> assert np.array_equal(index_face_mask, [[False, False], [True, False]])

        Returns:
            masks of maps with all vertices in mask
        """
        indices = np.array(range(len(self)))
        keep_indices = indices[mask]
        if isinstance(keep_indices, int):
            keep_indices = np.array([keep_indices])
        delete_indices = set(indices.flat).difference(set(keep_indices.flat))

        masks = []
        for mp_idx in range(len(self.maps)):
            map_delete_mask = np.full(
                (len(self.maps[mp_idx]),), False, dtype=bool
            )
            for i, mp in enumerate(self.maps[mp_idx]):
                for index in mp:
                    if index in delete_indices:
                        map_delete_mask[i] = True
                        break
            masks.append(~map_delete_mask)
        return masks

    def parts(self, *map_descriptions):
        """
        Args:
            *map_descriptions (Tuple(int, List(List(int)))): tuples of
                map_pos_idx (int): reference to map position
                    used like: self.maps[map_pos_idx]
                map_indices_list (List(List(int))): each int refers
                    to index in a map.

        Returns:
            List(cls): One TensorMaps or TensorMaps subclass per
                map_description
        """
        # raise ValueError(map_descriptions)
        parts = []
        for map_description in map_descriptions:
            map_pos_idx, map_indices_list = map_description
            for map_indices in map_indices_list:
                obj = self.copy()
                map_indices = set(map_indices)  # for speed up
                map_delete_mask = np.array(
                    [
                        True if i not in map_indices else False
                        for i in range(len(self.maps[map_pos_idx]))
                    ]
                )
                obj.maps[map_pos_idx] = obj.maps[map_pos_idx][~map_delete_mask]
                obj = obj.cleaned(duplicates=False)
                parts.append(obj)
        return parts

    def disjoint_map(self, mp_idx):
        """
        Find the disjoint sets of map = self.maps[mp_idx]
        As an example, this method is interesting for splitting a mesh
        consisting of seperate parts

        Args:
            mp_idx (int): reference to map position
                used like: self.maps[mp_idx]
        Returns:
            Tuple(int, List(List(int))): map description(tuple): see self.parts

        Examples:
            >>> import tfields
            >>> a = tfields.TensorMaps(
            ...     [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]],
            ...     maps=[[[0, 1, 2], [0, 2, 3]]])
            >>> b = a.copy()

            >>> b[:, 0] += 2
            >>> m = tfields.TensorMaps.merged(a, b)
            >>> mp_description = m.disjoint_map(0)
            >>> parts = m.parts(mp_description)
            >>> aa, ba = parts
            >>> assert aa.maps[0].equal(ba.maps[0])
            >>> assert aa.equal(a)
            >>> assert ba.equal(b)

        """
        maps_list = tfields.lib.sets.disjoint_group_indices(self.maps[mp_idx])
        return (mp_idx, maps_list)

    def paths(self, mp_idx):
        """
        Find the minimal amount of graphs building the original graph with
        maximum of two links per node i.e.

            o-----o                       o-----o
             \   /                         \   /
              \ /                           \ /
            o--o--o            o--o          8--o
               |                  |
               |        =         |    +          +
               o                  o                    o
              / \                /                      \
             /   \              /                        \
            o     o            o                          o

        where 8 is a duplicated node (one has two links and one has only one.)
        Examples:
            >>> import tfields
            >>> import numpy as np

            Ascii figure above:
            >>> a = tfields.TensorMaps([[1, 0], [3, 0], [2, 2], [0, 4], [2, 4],
            ...                         [4, 4], [1, 6], [3, 6], [2, 2]],
            ...                        maps=[[[0, 2], [2, 4], [3, 4], [5, 4],
            ...                               [1, 8], [6, 4], [6, 7], [7, 4]]])

            >>> paths = a.paths(0)
            >>> assert paths[0].equal([[ 1.,  0.],
            ...                        [ 2.,  2.],
            ...                        [ 2.,  4.],
            ...                        [ 0.,  4.]])
            >>> assert paths[0].maps[0].equal([[ 0.,  1.,  2.,  3.]])
            >>> assert paths[1].equal([[ 4.,  4.],
            ...                        [ 2.,  4.],
            ...                        [ 1.,  6.],
            ...                        [ 3.,  6.],
            ...                        [ 2.,  4.]])
            >>> assert paths[2].equal([[ 3.,  0.],
            ...                        [ 2.,  2.]])

        Note:
            The Longest path problem is a NP-hard problem.

        """
        obj = self.cleaned()

        flat_map = np.array(obj.maps[mp_idx].flat)
        values, counts = np.unique(flat_map, return_counts=True)
        counts = {v: n for v, n in zip(values, counts)}

        # last is a helper
        last = np.full(max(flat_map) + 1, -3, dtype=int)
        duplicat_indices = []
        d_index = len(obj)
        for i, val in enumerate(flat_map.copy()):
            if counts[val] > 2:
                # The first two occurences are uncritical
                if last[val] < -1:
                    last[val] += 1
                    continue

                # Now we talk about nodes with more than two edges
                if last[val] == -1:
                    # append a point and re-link
                    duplicat_indices.append(val)
                    flat_map[i] = d_index
                    last[val] = d_index
                    d_index += 1
                else:
                    # last occurence of val was a duplicate, so we use the same
                    # value again.
                    flat_map[i] = last[val]
                    last[val] = -1

        if duplicat_indices:
            duplicates = obj[duplicat_indices]
            obj = type(obj).merged(obj, duplicates)
        obj.maps = [tfields.Tensors(flat_map.reshape(-1, *obj.maps[mp_idx].shape[1:]))]
        paths = obj.parts(obj.disjoint_map(0))
        # paths = [paths[2]]  # this path did not work previously - debugging # with vessel

        # remove duplicate map entries and sort
        sorted_paths = []
        for path in paths:
            # find start index
            values, counts = np.unique(path.maps[0].flat, return_counts=True)

            first_node = None
            for v, c in zip(values, counts):
                if c == 1:
                    first_node = v
                    break
            edges = [list(edge) for edge in path.maps[0]]
            if first_node is None:
                first_node = 0 # edges[0][0]
                path = path[list(range(len(path))) + [0]]
                found_first_node = False
                for edge in edges:
                    if first_node in edge:
                        if found_first_node:
                            edge[edge.index(first_node)] = len(path) - 1
                            break
                        else:
                            found_first_node = True

            # follow the edges until you hit the end
            chain = [first_node]
            visited = set()
            n_edges = len(edges)
            node = first_node
            while len(visited) < n_edges:
                for i, edge in enumerate(edges):
                    if i in visited:
                        continue
                    if node not in edge:
                        continue

                    # found edge
                    visited.add(i)
                    if edge.index(node) != 0:
                        edge = list(reversed(edge))
                    chain.extend(edge[1:])
                    node = edge[-1]
            path = path[chain]
            path.maps[0] = tfields.TensorFields([sorted(chain)])
            sorted_paths.append(path)

        paths = sorted_paths
        return paths


class Container(AbstractNdarray):
    """
    Store lists of tfields objects. Save mechanisms are provided

    Examples:
        >>> import numpy as np
        >>> import tfields
        >>> sphere = tfields.Mesh3D.grid(
        ...     (1, 1, 1),
        ...     (-np.pi, np.pi, 3),
        ...     (-np.pi / 2, np.pi / 2, 3),
        ...     coord_sys='spherical')
        >>> sphere2 = sphere.copy() * 3
        >>> c = tfields.Container([sphere, sphere2])

        # >>> c.save("~/tmp/spheres.npz")
        # >>> c1 = tfields.Container.load("~/tmp/spheres.npz")
    """

    __slots__ = ["items", "labels"]

    def __new__(cls, items, **kwargs):
        kwargs["items"] = items
        cls._update_slot_kwargs(kwargs)

        empty = np.empty(0, int)
        obj = empty.view(cls)

        """ set kwargs to slots attributes """
        for attr in kwargs:
            if attr not in cls._iter_slots():
                raise AttributeError(
                    "Keyword argument {attr} not accepted "
                    "for class {cls}".format(**locals())
                )
            setattr(obj, attr, kwargs[attr])
        return obj


if __name__ == "__main__":  # pragma: no cover
    import doctest
    doctest.testmod()
    # doctest.run_docstring_examples(TensorFields.__getitem__, globals())
    # doctest.run_docstring_examples(Tensors._save_npz, globals())
    # doctest.run_docstring_examples(TensorMaps.cut, globals())
    # doctest.run_docstring_examples(AbstractNdarray._save_npz, globals())
