import numpy as np
from numpy import pi, isclose

from pyroll.core import CircularOvalGroove


def test_circular_oval():
    g = CircularOvalGroove(depth=5.05, r1=7, r2=33)

    assert isclose(g.usable_width, 17.63799973 * 2)
    assert isclose(g.alpha1, 29.102618 / 180 * pi)
    assert isclose(g.alpha2, 29.102618 / 180 * pi)
    assert isclose(g.z1, 19.45501221)

    assert not np.any(np.isclose(np.diff(g.contour_points[:, 0]), 0))  # test for duplicated points
