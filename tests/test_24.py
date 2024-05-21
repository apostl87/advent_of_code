import pytest

from f2022 import sday24

def test_l2s():
    grid = [['a', 'l', 'a'], ['b', 'a', 's']]
    assert list2string(grid) == "ala\nbas\n"