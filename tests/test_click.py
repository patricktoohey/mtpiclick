import pytest
from mtpiclick.click import moveClick
from mtpiclick.point import point

def test_moveclick():
    with pytest.raises(Exception):
        origin = point(0, 0)
        moveClick(origin)
