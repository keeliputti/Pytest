import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform != "darwin", reason="will run only on darwin")

const = 9/8

def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

#print(cent_to_fah())

@pytest.mark.skip(reason="Skipping for no reason specified")
def test_case01():
    assert type(const) == float


#@pytest.mark.skipif(sys.version_info < (3,8), reason="doesnt work on py version above 3.6")
@pytest.mark.skipif(cent_to_fah() == 32, reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32

@pytest.mark.skipif(pytest.__version__ < '5.4.0', reason="pytest version is less")
def test_case03():
    assert cent_to_fah(38) == 1004