# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
=====================
sbpy.data core module
=====================

created on June 22, 2017
"""

from copy import deepcopy
from numpy import ndarray, array, hstack, iterable
from astropy.table import QTable, Column
from astropy.time import Time
import astropy.units as u

from . import conf
from ..exceptions import SbpyException, SbpyWarning

__all__ = ['DataClass', 'DataClassError', 'QueryError', 'TimeScaleWarning']


class DataClassError(SbpyException):
    """Will be raised in case of exceptions dealing with
    `~sbpy.data.DataClass`."""
    pass


class QueryError(SbpyException):
    """Will be raised in case of query errors."""
    pass


class TimeScaleWarning(SbpyWarning):
    """Will be raised in case time scales on `~astropy.time.Time` objects
    have to be converted to comply with query requirements."""
    pass


class DataClass():
    """`~sbpy.data.DataClass` serves as the base class for all data
    container classes in `sbpy` in order to provide consistent
    functionality. Classes derived from `~sbpy.data.DataClass` have
    the following properties:

    The core of `~sbpy.data.DataClass` is an `~astropy.table.QTable`
    object(referred to as the `data table` below) - a type of
    `~astropy.table.Table` object that supports the `~astropy.units`
    formalism on a per-column base - which already provides most of
    the required functionality. `~sbpy.data.DataClass` objects can be
    manually generated from dictionaries
    (`~sbpy.data.DataClass.from_dict`), list-like objects on a
    per-column basis(`~sbpy.data.DataClass.from_columns`) or a
    per-row basis(`~sbpy.data.DataClass.from_rows`), or directly from
    another `~astropy.table.QTable` object. It is possible to write
    `~sbpy.data.DataClass` objects to a file and from a file.

    `~sbpy.data.DataClass` objects can hold meta data that are stored
    as `~astropy.table.QTable` meta data and can be accessed as a
    `~sbpy.data.DataClass` property. Furthermore,
    `~sbpy.data.DataClass` objects have the ability to recognize
    alternative names for properties stored in the data table and even
    do transformations.

    A few high-level functions for table data access or modification
    are provided; other, more complex modifications can be applied to
    the underlying table object(`~sbpy.data.DataClass.table`) directly.
    """

    def __init__(self):
        self._table = QTable()

    @staticmethod
    def _unit_apply(val, unit):
        """Convenience function that applies a unit to a value, or converts
        a `~astropy.units.Quantity` to this unit if possible.

        Parameters
        ----------
        val: `~astropy.units.Quantity` or unit-less type
            Input value.
        unit: str or None
            Unit into which ``val`` will be converted. If None, ``val`` is
            considered not to be a `~astropy.units.Quantity`.

        Returns
        -------
        `~astropy.units.Quantity` or other

        """
        if isinstance(val, u.Quantity):
            if unit is None:
                return val.value
            else:
                return val.to(unit)
        else:
            if unit is not None:
                return val * u.Unit(unit)
            else:
                return val

    @staticmethod
    def _unit_convert_strip(val, unit):
        """Convenience function that transforms `~astropy.units.Quantities`
        and then strips the unit, but leaves non-Quantities untouched.

        Parameters
        ----------
        val: `~astropy.units.Quantity` or unit-less type
            Input value.
        unit: str or None
            Unit into which ``val`` will be converted. If None, ``val`` is
            considered not to be a `~astropy.units.Quantity`.

        Returns
        -------
        unit-less type
        """
        if unit is None:
            return val
        else:
            return DataClass._unit_apply(val, unit).value

    @classmethod
    def from_dict(cls, data, meta={}, **kwargs):
        """Create `~sbpy.data.DataClass` object from dictionary.

        Parameters
        ----------
        data: `~collections.OrderedDict` or dictionary
            Data that will be ingested in `~sbpy.data.DataClass`
            object. Each item in the dictionary will form a column in
            the data table. The item key will be used as column name,
            the item value, which must be list-like or a
            `~astropy.units.Quantity` vector, will be used as data. All
            columns, i.e., all item values, must have the same length.
            Please note that in order to make use of :ref:`fieldnames`
            and to ensure compatibility with sbpy functionality, the
            field names chosen must be in the list of :ref:`field name list`.
        meta: dictionary, optional
            Meta data that will be stored in the data table. Default:
            empty dictionary
        kwargs: additional keyword arguments, optional
            Additional keyword arguments that will be passed on to
            `~astropy.table.QTable` in the creation of the underlying
            data table.

        Returns
        -------
        `DataClass` object

        Examples
        --------
        The following example creates a single-row `~sbpy.data.Orbit`
        object (the other `~DataClass` objects work the exact same way).

        >>> import astropy.units as u
        >>> from sbpy.data import Orbit
        >>> orb = Orbit.from_dict({'a': 2.7674*u.au,
        ...                        'e': 0.0756,
        ...                        'i': 10.59321*u.deg})
        >>> orb  # doctest: +SKIP
        <QTable length=1>
           a       e       i
           AU             deg
        float64 float64 float64
        ------- ------- --------
         2.7674  0.0756 10.59321

        A double-row
        `~sbpy.data.Orbit` example would look like this:

        >>> orb = Orbit.from_dict({'a': [2.7674, 3.123]*u.au,
        ...                        'e': [0.0756, 0.021],
        ...                        'i': [10.59321, 3.21]*u.deg})
        >>> orb  # doctest: +SKIP
        <QTable length=2>
           a       e       i
           AU             deg
        float64 float64 float64
        ------- ------- --------
         2.7674  0.0756 10.59321
          3.123   0.021     3.21

        Note how in this case a list is passed
        to each key of the dictionary; if a unit is
        provided for either element in the dictionary, the
        corresponding `~astropy.units.Unit` has to be multiplied to
        this list, forming a `~astropy.units.Quantity` vector.

        Since dictionaries have no specific order, the ordering of the
        column in the example above is not defined. If your data table
        requires a specific order, use ``OrderedDict``. This example
        also shows the use of meta data.

        >>> from collections import OrderedDict
        >>> orb = Orbit.from_dict(OrderedDict([('a', [2.7674, 3.123]*u.au),
        ...                                    ('e', [0.0756, 0.021]),
        ...                                    ('i', [10.59, 3.21]*u.deg)]),
        ...                                   meta={'targetname': 'asteroid'})
        >>> orb  # doctest: +SKIP
        <QTable length=2>
           a       e       i
           AU             deg
        float64 float64 float64
        ------- ------- -------
         2.7674  0.0756   10.59
          3.123   0.021    3.21
        >> > orb.meta
        {'targetname': 'asteroid'}
        >> > orb.meta['targetname']
        'asteroid'
        """

        for key, val in data.items():
            if isinstance(val, (str, bytes)):
                data[key] = [val]
            elif not iterable(val):
                if isinstance(val, u.Quantity):
                    data[key] = [val.value]*val.unit
                elif isinstance(val, Time):
                    # workaround for scalar Time objects
                    data[key] = Time([val.value],
                                     format=val.format,
                                     scale=val.scale)
                else:
                    data[key] = [val]

        self = cls()
        self._table = QTable(data, meta=meta, **kwargs)
        return self

    @classmethod
    def from_columns(cls, columns, names, units=None, meta={}, **kwargs):
        """Create `~sbpy.data.DataClass` object from a sequence. If that
        sequence is one-dimensional, it is interpreted as
        a single column; if the sequence is two-dimensional, it is
        interpreted as a sequence of columns.

        Parameters
        ----------
        columns: list, `~numpy.ndarray`, tuple, or `~astropy.units.Quantity`
            Data that will be ingested in `DataClass` object. A
            one-dimensional sequence is interpreted as a single column.
            A two-dimensional sequence is interpreted as a sequence of
            columns, each of which must have the same length.
        names: str or list-like
            Field names, must have the same number of names as data columns.
            Please note that in order to make use of :ref:`fieldnames`
            and to ensure compatibility with sbpy functionality, the
            field names chosen must be in the list of :ref:`field name list`.
        units: str or list-like, optional
            Unit labels (as provided by `~astropy.units.Unit`) in which
            the data provided in ``columns`` will be stored in the underlying
            table. If None, the units as provided by ``columns``
            are used. If the units provided in ``units`` differ from those
            used in ``columns``, ``columns`` will be transformed to the units
            provided in ``units``. Must have the same length as ``names``
            and the individual data columns in ``columns``. Default: None
        meta: dictionary, optional
            Meta data that will be stored in the data table. Default:
            empty dictionary
        kwargs: additional keyword arguments, optional
            Additional keyword arguments that will be passed on to
            `~astropy.table.QTable` in the creation of the underlying
            data table.

        Returns
        -------
        `DataClass` object

        Examples
        --------
        The following example creates a single-column `~sbpy.data.Ephem`
        object.

        >>> from sbpy.data import Ephem
        >>> import astropy.units as u
        >>> eph = Ephem.from_columns([1, 2, 3, 4]*u.au,
        ...                          names='a')
        >>> eph
        <QTable length=4>
           a
           AU
        float64
        -------
            1.0
            2.0
            3.0
            4.0

        This example creates a two-column `~sbpy.data.Ephem` object in which
        units are assigned using the optional ``units`` keyword argument.

        >>> eph = Ephem.from_columns([[1, 2, 3, 4],
        ...                           [90, 50, 30, 10]],
        ...                          names=['r', 'alpha'],
        ...                          units=['au', 'deg'])
        >>> eph
        <QTable length=4>
           r     alpha
           AU     deg
        float64 float64
        ------- -------
            1.0    90.0
            2.0    50.0
            3.0    30.0
            4.0    10.0

        If units are provided in ``columns`` and ``units``, those units in
        ``columns`` will be transformed into those units in ``units`` on a
        per-column basis.

        >>> eph = Ephem.from_columns([[1, 2, 3, 4]*u.au,
        ...                           [90, 50, 30, 10]*u.deg],
        ...                           names=['r', 'alpha'],
        ...                           units=['km', 'rad'])
        >>> eph
        <QTable length=4>
                r                 alpha
                km                 rad
             float64             float64
        ------------------ -------------------
               149597870.7  1.5707963267948966
               299195741.4  0.8726646259971648
        448793612.09999996  0.5235987755982988
               598391482.8 0.17453292519943295
        """

        # turn single column name to a list
        if isinstance(names, str):
            names = [names]

        # turn single column to a list
        if not iterable(columns[0]):
            columns = [columns]
        elif isinstance(columns[0], (str, bytes)):
            columns = [columns]

        if units is not None:
            if all([isinstance(col, u.Quantity) for col in columns]):
                # if all columns have units, transform to `units`
                columns = [val.to(unit) for val, unit in
                           list(zip(columns, units))]
            else:
                # if columns has no units, apply `units`
                columns = [val*u.Unit(unit) if unit is not None else val
                           for val, unit in
                           list(zip(columns, units))]

        self = cls()
        self._table = QTable(columns, names=names, meta=meta, **kwargs)
        return self

    @classmethod
    def from_rows(cls, rows, names, units=None, meta={}, **kwargs):
        """Create `~sbpy.data.DataClass` object from a sequence. If that
        sequence is one-dimensional, it is interpreted as
        a single row; if the sequence is two-dimensional, it is
        interpreted as a sequence of rows.

        Parameters
        ----------
        rows : list, `~numpy.ndarray`, or tuple
            Data that will be ingested in `~DataClass` object. A
            one-dimensional sequence is interpreted as a single row.
            A two-dimensional sequence is interpreted as a sequence of
            rows, each of which must have the same length.
        names : str or list
            Column names, must have the same number of names as data columns
            in each row.
            Please note that in order to make use of :ref:`fieldnames`
            and to ensure compatibility with sbpy functionality, the
            field names chosen must be in the list of :ref:`field name list`.
        units : str or list-like, optional
            Unit labels (as provided by `~astropy.units.Unit`) in which
            the data provided in ``rows`` will be stored in the underlying
            table. If None, the units as provided by ``rows``
            are used. If the units provided in ``units`` differ from those
            used in ``rows``, ``rows`` will be transformed to the units
            provided in ``units``. Must have the same length as ``names``
            and the individual data rows in ``rows``. Default: None
        meta : dictionary, optional
            Meta data that will be stored in the data table. Default:
            empty dictionary
        kwargs : additional keyword arguments, optional
            Additional keyword arguments that will be passed on to
            `~astropy.table.QTable` in the creation of the underlying
            data table.

        Returns
        -------
        `DataClass` object

        Examples
        --------
        The following example creates a single-row `~sbpy.data.Phys` object.

        >>> from sbpy.data import Phys
        >>> import astropy.units as u
        >>> phys = Phys.from_rows([1*u.km, 0.05, 17*u.mag],
        ...                       names=['diam', 'pv', 'absmag'])
        >>> phys
        <QTable length=1>
          diam     pv    absmag
           km             mag
        float64 float64 float64
        ------- ------- -------
            1.0    0.05    17.0

        Providing ``units`` allows providing unit-less data in ``rows``:

        >>> phys = Phys.from_rows([[1, 0.05, 17],
        ...                        [2, 0.05, 16]],
        ...                       names=['diam', 'pv', 'absmag'],
        ...                       units=['km', None, 'mag'])
        >>> phys
        <QTable length=2>
          diam     pv    absmag
           km             mag
        float64 float64 float64
        ------- ------- -------
            1.0    0.05    17.0
            2.0    0.05    16.0
        """

        if isinstance(names, str):
            names = [names]
        if isinstance(units, (str, u.Unit)):
            units = [units]
        if units is not None and len(names) != len(units):
            raise DataClassError('Must provide the same number of names '
                                 'and units.')

        # reorganize rows, if necessary
        if not iterable(rows[0]):
            rows = [rows]
        elif isinstance(rows[0], (str, bytes)):
            rows = [rows]

        if units is None:
            # extract units
            units = []
            for col in rows[0]:
                if isinstance(col, u.Quantity):
                    units.append(col.unit)
                else:
                    units.append(None)

        # build unit-less list of columns from rows
        stripped_rows = [[cls._unit_convert_strip(vj, units[j])
                          for j, vj in enumerate(vi)]
                         for vi in rows]
        stripped_cols = list(map(list, zip(*stripped_rows)))

        return cls.from_columns(columns=stripped_cols,
                                units=units,
                                names=names,
                                meta=meta,
                                **kwargs)

    @classmethod
    def from_table(cls, table, meta={}, **kwargs):
        """Create `DataClass` object from `~astropy.table.Table` or
        `~astropy.table.QTable` object.

        Parameters
        ----------
        table : `~astropy.table.Table` object
            Data that will be ingested in `DataClass` object. Must be a
            `~astropy.table.Table` or `~astropy.table.QTable` object.
            Please note that in order to make use of :ref:`fieldnames`
            and to ensure compatibility with sbpy functionality, the
            field names chosen must be in the list of :ref:`field name
            list`.
        meta : dictionary, optional
            Meta data that will be stored in the data table. If ``table``
            already holds meta data, ``meta`` will be added. Default:
            empty dictionary
        kwargs : additional keyword arguments, optional
            Additional keyword arguments that will be passed on to
            `~astropy.table.QTable` in the creation of the underlying
            data table.

        Returns
        -------
        `DataClass` object

        Examples
        --------
        >>> from astropy.table import QTable
        >>> import astropy.units as u
        >>> from sbpy.data import DataClass
        >>> tab = QTable([[1,2,3]*u.kg,
        ...               [4,5,6]*u.m/u.s,],
        ...              names=['mass', 'velocity'])
        >>> dat = DataClass.from_table(tab)
        >>> dat
        <QTable length=3>
          mass  velocity
           kg    m / s
        float64 float64
        ------- --------
            1.0      4.0
            2.0      5.0
            3.0      6.0
        """
        self = cls()
        self._table = QTable(table, meta={**table.meta, **meta}, **kwargs)
        return self

    @classmethod
    def from_file(cls, filename, meta={}, **kwargs):
        """Create `DataClass` object from a file using
        `~astropy.table.Table.read`.

        Parameters
        ----------
        filename : str
             Name of the file that will be read and parsed.
        meta : dictionary, optional
             Meta data that will be stored in the data table. If the data
             to be read
             already holds meta data, ``meta`` will be added. Default:
             empty dictionary
        kwargs : additional parameters
             Optional parameters that will be passed on to
             `~astropy.table.Table.read`.

        Returns
        -------
        `DataClass` object

        Notes
        -----
        This function is merely a wrapper around
        `~astropy.table.Table.read`. Please note that the file formats
        available (see `here
        <https://docs.astropy.org/en/stable/io/unified.html#built-in-readers-writers>`_
        for a list of available formats) provide varying support for
        units and meta data. For instance, ``basic``, ``csv``,
        ``html``, and ``latex`` do not provide unit or meta data
        information. However, ``fits``, ``cds``, ``daophot``,
        ``ecsv``, and ``ipac`` do support units and meta data.

        Examples
        --------
        >>> from sbpy.data import DataClass

        >>> dat = DataClass.from_file('data.txt',
        ...                           format='ascii') # doctest: +SKIP

        """

        data = QTable.read(filename, **kwargs)

        self = cls()
        self._table = data
        self._table.meta = {**self._table.meta, **meta}

        return self

    def to_file(self, filename, format='ascii', **kwargs):
        """Write object to a file using
        `~astropy.table.Table.write`.

        Parameters
        ----------
        filename : str
             Name of the file that will be written.
        format : str, optional
             Data format in which the file should be written. Default:
             ``ASCII``
        kwargs : additional parameters
             Optional parameters that will be passed on to
             `~astropy.table.Table.write`.

        Returns
        -------
        None

        Notes
        -----
        This function is merely a wrapper around
        `~astropy.table.Table.write`. Please note that the file formats
        available (see `here
        <https://docs.astropy.org/en/stable/io/unified.html#built-in-readers-writers>`_
        for a list of available formats) provide varying support for
        units and meta data. For instance, ``basic``, ``csv``,
        ``html``, and ``latex`` do not provide unit or meta data
        information. However, ``fits``, ``cds``, ``daophot``,
        ``ecsv``, and ``ipac`` do support units and meta data.

        Examples
        --------
        >>> from sbpy.data import DataClass
        >>> import astropy.units as u
        >>> dat = DataClass.from_columns([[1, 2, 3]*u.deg,
        ...                               [4, 5, 6]*u.km,
        ...                               ['a', 'b', 'c']],
        ...                              names=('a', 'b', 'c'))
        >>> dat.to_file('test.txt')  # doctest: +SKIP
        """

        self._table.write(filename, format=format, **kwargs)

    def __len__(self):
        """Get number of data elements in _table"""
        return len(self._table)

    def __repr__(self):
        """Return representation of the underlying data table
        (``self._table.__repr__()``)"""
        return self._table.__repr__()

    def __getitem__(self, ident):
        """Return columns or rows from data table(``self._table``); checks
        for and may use alternative field names. This method will always return
        an instance of __class__, except in the case when a field name is
        requested (then return an `astropy.table.Column` if no units are
        provided or a `astropy.units.Quantity` if units are provided)."""

        # slices, iterables consisting of booleans and integers, and integer
        # indices are all treated in the same way and are required to return
        # a new __class__ object; only have to treat string identifiers
        # separately in that those have to be checked for conversions
        # and translations

        # list of field names
        if (isinstance(ident, (list, tuple, ndarray)) and
            all([isinstance(i, str) for i in ident])):
                self = self._convert_columns(ident)
                newkeylist = [self._translate_columns(i)[0] for i in ident]
                ident = newkeylist
        # individual field names
        elif isinstance(ident, str):
            self = self._convert_columns(ident)
            ident = self._translate_columns(ident)[0]
            return self._table[ident]

        # return as new instance of this class for all other identifiers
        return self.from_table(self._table[ident])

    def __setitem__(self, *args):
        """Refer cls.__setitem__ to self._table"""
        self._table.__setitem__(*args)

    def _translate_columns(self, target_colnames):
        """Translate target_colnames to the corresponding column names
        present in this object's table. Returns a list of actual column
        names present in this object that corresponds to target_colnames
        (order is preserved). Raises KeyError if not all columns are
        present or one or more columns could not be translated.
        """

        if not isinstance(target_colnames, (list, ndarray, tuple)):
            target_colnames = [target_colnames]

        translated_colnames = deepcopy(target_colnames)
        for idx, colname in enumerate(target_colnames):
            # colname is already a column name in self.table
            if colname in self.field_names:
                continue
            # colname is an alternative column name
            elif colname in sum(conf.fieldnames, []):
                for alt in conf.fieldnames[conf.fieldname_idx[colname]]:
                    # translation available for colname
                    if alt in self.field_names:
                        translated_colnames[idx] = alt
                        break
            # colname is unknown, raise a KeyError
            else:
                raise KeyError('field {:s} not available.'.format(
                    colname))

        return translated_colnames

    def _convert_columns(self, target_colnames):
        """Convert target_colnames, if necessary. Converted columns will be
        added as columns to ``self`` using the field names provided in
        target_colnames. No error is returned by this function if a
        field could not be converted.
        """

        if not isinstance(target_colnames, (list, ndarray, tuple)):
            target_colnames = [target_colnames]

        for colname in target_colnames:
            # ignore, if colname is unknown (KeyError)
            try:
                # ignore if colname has already been converted
                if any([alt in self.field_names for alt
                        in conf.fieldnames[conf.fieldname_idx[colname]]]):
                    continue
                # consider alternative names for colname -> alt
                for alt in conf.fieldnames[conf.fieldname_idx[colname]]:
                    if alt in list(conf.field_eq.keys()):
                        # conversion identified
                        convname = self._translate_columns(
                            list(conf.field_eq[alt].keys())[0])[0]
                        convfunc = list(conf.field_eq[alt].values())[0]
                        if convname in self.field_names:
                            # create new column for the converted field
                            self[colname] = convfunc(self.table[convname])
                            break
            except KeyError:
                continue

        return self

    @property
    def table(self):
        """Return `~astropy.table.QTable` object containing all data."""
        return self._table

    @property
    def field_names(self):
        """Return a list of all field names in the data table."""
        return self._table.columns

    @property
    def meta(self):
        """Enables access to the meta data of the underlying data table.

        Examples
        --------
        >>> from sbpy.data import DataClass
        >>> import astropy.units as u
        >>> data = DataClass.from_columns([[1, 2, 3, 4]*u.kg,
        ...                                [5, 6, 7, 8]*u.m],
        ...                               names=['a', 'b'],
        ...                               meta={'origin': 'measured'})
        >>> data.meta  # meta data access
        {'origin': 'measured'}
        >>> data.meta['date'] = '2019-06-27'  # meta data modification
        >>> data.meta['date']
        '2019-06-27'
        """
        return self._table.meta

    def apply(self, data, name, unit=None):
        """Apply an arbitrarily shaped sequence as additional column to a
        `~sbpy.data.DataClass` object and reshape it accordingly.

        Parameters
        ----------
        data : list or iterable `~astropy.units.Quantity` object
            Data to be added in a new column in form of a one-dimensional
            list or a two-dimensional nested sequence. Each element in
            ``data``
            corresponds to one of the rows in the existing data table. If
            an element
            of ``data`` is a list, the corresponding data table row is
            repeated the same the number of times as there are elements in
            this sublist. If ``data`` is
            provided as a flat list and has the same length as the current
            data table, ``data`` will be simply added as a column to the data
            table and the length of the data table will not change. If
            ``data`` is provided as a `~astropy.units.Quantity` object (only
            possible for flat lists), its
            unit is adopted, unless ``unit`` is specified (not None).
        name : str
            Name of the new data column.
        unit : `~astropy.units` object or str, optional
            Unit to be applied to the new column. Default:
            `None`

        Returns
        -------
        None

        Notes
        -----
        As a result of this method, the length of the underlying data table
        will be the same as the length of the flattened `data` parameter.

        Examples
        --------
        Imagine the following scenario: you obtain photometric measurements
        of the same asteroid over a number of nights. The following
        `~sbpy.data.Ephem` object summarizes the observations:

        >>> from sbpy.data import Ephem
        >>> import astropy.units as u
        >>> obs = Ephem.from_columns([[2451223, 2451224, 2451226]*u.d,
        ...                           [120.1, 121.3, 124.9]*u.deg,
        ...                           [12.4, 12.2, 10.8]*u.deg],
        ...                          names=('JD', 'RA', 'DEC'))
        >>> obs
        <QTable length=3>
            JD       RA     DEC
            d       deg     deg
         float64  float64 float64
        --------- ------- -------
        2451223.0   120.1    12.4
        2451224.0   121.3    12.2
        2451226.0   124.9    10.8

        After analyzing the observations, you would like to add the
        measured apparent V-band magnitudes to this object. You have
        one observation from the first night, two from the second night,
        and three from the third night. Instead of re-creating ``obs``,
        `~sbpy.data.DataClass.apply` offers a convenient way to
        supplement ``obs``:

        >>> obs.apply([[12.1], [12.5, 12.6], [13.5, 13.4, 13.5]],
        ...           name='V', unit='mag')
        >>> obs
        <QTable length=6>
            JD       RA     DEC      V
            d       deg     deg     mag
         float64  float64 float64 float64
        --------- ------- ------- -------
        2451223.0   120.1    12.4    12.1
        2451224.0   121.3    12.2    12.5
        2451224.0   121.3    12.2    12.6
        2451226.0   124.9    10.8    13.5
        2451226.0   124.9    10.8    13.4
        2451226.0   124.9    10.8    13.5

        Note how the data table has been re-arranged and rows have been
        duplicated in order to provide the expected shape.
        """
        _newtable = None

        # strip units off Quantity objects
        if isinstance(data, u.Quantity):
            unit = data.unit
            data = data.value

        if len(data) != len(self.table):
            raise DataClassError(
                'Data parameter must have '
                'same length as self._table')

        _newcolumn = array([])
        for i, val in enumerate(data):
            if not isinstance(val, (list, tuple, ndarray)):
                val = [val]
            _newcolumn = hstack([_newcolumn, val])
            # add corresponding row from _table for each element in val
            for j in range(len(val)):
                # initialize new QTable object
                if _newtable is None:
                    _newtable = QTable(self.table[0])
                    continue
                _newtable.add_row(self.table[i])

        # add new column
        _newtable.add_column(Column(_newcolumn, name=name, unit=unit))

        # restore meta data
        _newtable.meta = self.meta

        self._table = _newtable
