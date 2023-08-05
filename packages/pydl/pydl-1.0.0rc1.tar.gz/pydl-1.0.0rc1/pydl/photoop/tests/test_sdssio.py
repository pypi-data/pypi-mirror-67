# Licensed under a 3-clause BSD style license - see LICENSE.rst
# -*- coding: utf-8 -*-
"""Test the functions in pydl.photoop.sdssio.
"""
import os
import pytest
import numpy as np
from astropy.tests.helper import raises
from ..sdssio import (filtername, filternum, sdss_calib, sdss_name, sdss_path,
                      sdssflux2ab)


path_data = {
    'apObj': "/PHOTO_REDUX/301/137/objcs/4",
    'calibMatch': "/PHOTO_REDUX/301/137/nfcalib",
    'calibPhotom': "/PHOTO_REDUX/301/137/nfcalib",
    'calibPhotomGlobal': "/PHOTO_CALIB/301/137/nfcalib",
    'fakeIdR': "/PHOTO_DATA/137/fake_fields/4",
    'fpAtlas': "/PHOTO_REDUX/301/137/objcs/4",
    'fpBIN': "/PHOTO_REDUX/301/137/objcs/4",
    'fpC': "/PHOTO_REDUX/301/137/objcs/4",
    'fpFieldStat': "/PHOTO_REDUX/301/137/objcs/4",
    'fpM': "/PHOTO_REDUX/301/137/objcs/4",
    'fpObjc': "/PHOTO_REDUX/301/137/objcs/4",
    'hoggObj': "/PHOTO_REDUX/301/137/objcs/4",
    'idFF': "/PHOTO_REDUX/301/137/objcs/4",
    'idR': "/PHOTO_DATA/137/fields/4",
    'idRR': "/PHOTO_DATA/137/fields/4",
    'psBB': "/PHOTO_REDUX/301/137/objcs/4",
    'psFF': "/PHOTO_REDUX/301/137/objcs/4",
    'psField': "/PHOTO_REDUX/301/137/objcs/4",
    'reObjGlobal': "/PHOTO_RESOLVE/301/137/resolve/4",
    'reObjRun': "/PHOTO_REDUX/301/137/resolve/4",
    'reObjTmp': "/PHOTO_RESOLVE/301/137/resolve/4",
    'tsField': "/PHOTO_REDUX/301/137/calibChunks/4",
    }


name_data = {
    'apObj': "apObj-000137-r4-0042.fit",
    'calibMatch': "calibMatch-000137-4.fits",
    'calibPhotom': "calibPhotom-000137-4.fits",
    'calibPhotomGlobal': "calibPhotomGlobal-000137-4.fits",
    'fakeIdR': "idR-000137-r4-0042.fit",
    'fpAtlas': "fpAtlas-000137-4-0042.fit",
    'fpBIN': "fpBIN-000137-r4-0042.fit",
    'fpC': "fpC-000137-r4-0042.fit",
    'fpFieldStat': "fpFieldStat-000137-4-0042.fit",
    'fpM': "fpM-000137-r4-0042.fit",
    'fpObjc': "fpObjc-000137-4-0042.fit",
    'hoggObj': "hoggObj-000137-4-0042.fits",
    'idFF': "idFF-000137-r4.fit",
    'idR': "idR-000137-r4-0042.fit",
    'idRR': "idRR-000137-r4-0042.fit",
    'psBB': "psBB-000137-r4-0042.fit",
    'psFF': "psFF-000137-r4.fit",
    'psField': "psField-000137-4-0042.fit",
    'reObjGlobal': "reObjGlobal-000137-4-0042.fits",
    'reObjRun': "reObjRun-000137-4-0042.fits",
    'reObjTmp': "reObjTmp-000137-4-0042.fits",
    'tsField': "tsField-000137-4-301-0042.fit",
    }


@pytest.fixture
def sdss_env(request):
    """Set up environment variables for testing sdss_path and sdss_name.
    """
    m = request.getfixturevalue("monkeypatch")
    for p in ('PHOTO_CALIB', 'PHOTO_DATA', 'BOSS_PHOTOOBJ', 'PHOTO_REDUX',
              'PHOTO_RESOLVE', 'PHOTO_SKY', 'PHOTO_SWEEP'):
        m.setenv(p, '/' + p)
    return m


def test_filtername():
    assert filtername(0) == 'u'
    assert filtername(1) == 'g'
    assert filtername(2) == 'r'
    assert filtername(3) == 'i'
    assert filtername(4) == 'z'
    #
    # filtername should return its argument if it's not
    # integer-like
    #
    assert filtername('r') == 'r'


def test_filternum():
    assert filternum('u') == 0
    assert filternum('g') == 1
    assert filternum('r') == 2
    assert filternum('i') == 3
    assert filternum('z') == 4
    #
    # Test default return value
    #
    fn = filternum()
    for k in range(5):
        assert fn[k] == k


def test_sdss_calib():
    foo = sdss_calib(94, 6, 101)
    assert foo['NMGYPERCOUNT'] == 1.0


def test_sdss_name(sdss_env):
    #
    # Bad ftype
    #
    with raises(KeyError):
        p = sdss_name('fooBar', 137, 4, 42)
    for ftype in name_data:
        assert sdss_name(ftype, 137, 4, 42, '301', 'r',
                         no_path=True) == name_data[ftype]


def test_sdss_name_with_path(sdss_env):
    for ftype in name_data:
        assert (sdss_name(ftype, 137, 4, 42, '301', 'r') ==
                os.path.join(path_data[ftype], name_data[ftype]))


def test_sdss_name_reObj(sdss_env):
    assert sdss_name('reObj', 137, 4, 42, '301', 'r',
                     no_path=True) == name_data['reObjGlobal']
    sdss_env.delenv('PHOTO_RESOLVE')
    assert sdss_name('reObj', 137, 4, 42, '301', 'r',
                     no_path=True) == name_data['reObjRun']


def test_sdss_path(sdss_env):
    with raises(KeyError):
        p = sdss_path('fooBar', 137)
    for ftype in path_data:
        assert sdss_path(ftype, 137, 4, '301') == path_data[ftype]


def test_sdssflux2ab():
    correction = np.array([-0.042, 0.036, 0.015, 0.013, -0.002])
    mags = np.zeros((2, 5), dtype='d')
    mags[0, :] = 18.0
    mags[1, :] = 19.0
    ab = sdssflux2ab(mags, magnitude=True)
    assert (ab == (mags + correction)).all()
    flux = 10**((22.5 - mags)/2.5)  # nanomaggies
    ab = sdssflux2ab(flux)
    assert np.allclose(ab, 10**((22.5 - (mags + correction))/2.5))
    ivar = 1.0/flux
    ab = sdssflux2ab(ivar, ivar=True)
    assert np.allclose(ab, ivar/(10**(-2.0*correction/2.5)))
