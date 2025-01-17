import numpy as np
from numpy import isclose
from pyroll.core import FlatGroove


def test_flat():
    g = FlatGroove(width=100)

    assert isclose(g.usable_width, 100)

    assert not np.any(np.isclose(np.diff(g.contour_points[:, 0]), 0))  # test for duplicated points
