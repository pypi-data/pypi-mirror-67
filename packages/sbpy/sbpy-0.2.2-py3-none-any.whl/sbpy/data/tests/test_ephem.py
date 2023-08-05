# Licensed under a 3-clause BSD style license - see LICENSE.rst

import pytest
from copy import deepcopy
from numpy import abs
import warnings

from numpy.testing import assert_allclose
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation
from astropy.tests.helper import assert_quantity_allclose

from ... import exceptions as sbe
from ... import bib
from ..core import conf
from .. import ephem
from .. import Ephem, Orbit, QueryError

try:
    import pyoorb
    HAS_PYOORB = True
except ImportError:
    HAS_PYOORB = False

# retreived from Horizons on 23 Apr 2020
CERES = {
    'targetname': '1 Ceres',
    'H': u.Quantity(3.4, 'mag'),
    'G': 0.12,
    'e': 0.07741102040801928,
    'q': u.Quantity(2.55375156, 'au'),
    'incl': u.Quantity(10.58910839, 'deg'),
    'Omega': u.Quantity(80.29081558, 'deg'),
    'w': u.Quantity(73.7435117, 'deg'),
    'n': u.Quantity(0.21401711, 'deg / d'),
    'M': u.Quantity(154.70418799, 'deg'),
    'nu': u.Quantity(158.18663933, 'deg'),
    'a': u.Quantity(2.76802739, 'AU'),
    'Q': u.Quantity(2.98230321, 'AU'),
    'P': u.Quantity(1682.10848349, 'd'),
    'epoch': Time(2458963.26397076, scale='tdb', format='jd'),
    'Tp': Time(2458240.40500675, scale='tdb', format='jd')
}


@pytest.mark.skipif('not HAS_PYOORB')
class TestEphemFromOorb:
    def test_missing_pyoorb(self, monkeypatch):
        monkeypatch.setattr(ephem, 'pyoorb', None)
        with pytest.raises(sbe.RequiredPackageUnavailable):
            Ephem.from_oo(CERES)

    def test_units(self):
        orbit1 = Orbit.from_dict(CERES)
        eph1 = Ephem.from_oo(orbit1)

        orbit2 = Orbit.from_dict({
            'targetname': orbit1['targetname'][0],
            'a': orbit1['a'].value[0],
            'e': orbit1['e'][0],
            'i': orbit1['i'].value[0],
            'w': orbit1['w'].value[0],
            'Omega': orbit1['Omega'].value[0],
            'epoch': orbit1['epoch'][0],
            'M': orbit1['M'].value[0],
            'H': orbit1['H'].value[0],
            'G': orbit1['G'][0]
        })
        eph2 = Ephem.from_oo(orbit2)

        for k in ['ra', 'dec', 'RA*cos(Dec)_rate', 'dec_rate', 'alpha', 'r',
                  'delta', 'V', 'hlon', 'hlat', 'EL']:
            assert u.isclose(eph1[k], eph2[k])

    def test_basic(self):
        orbit = Orbit.from_dict(CERES)
        oo_ephem = Ephem.from_oo(orbit, scope='basic')
        assert 'dec_rate' not in oo_ephem.field_names

    def test_timescale(self):
        orbit = Orbit.from_dict(CERES)
        epoch = Time.now()
        oo_ephem = Ephem.from_oo(orbit, epochs=epoch, scope='basic')
        assert oo_ephem['epoch'].scale == epoch.scale

    def test_bib(self):
        with bib.Tracking():
            orbit = Orbit.from_dict(CERES)
            oo_ephem = Ephem.from_oo(orbit, scope='basic')
            assert 'sbpy.data.ephem.Ephem.from_oo' in bib.show()
        bib.reset()
