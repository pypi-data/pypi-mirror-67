#  PyMODAlib, a Python implementation of the algorithms from MODA (Multiscale Oscillatory Dynamics Analysis).
#  Copyright (C) 2020 Lancaster University
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
from typing import List

import numpy as np
from numpy import ndarray


def matlab_to_numpy(arr) -> ndarray:
    """
    Converts a matlab array to a numpy array. Can be much faster than simply calling "np.asarray()",
    for real arrays.

    Parameters
    ----------
    arr : array_like
        The MATLAB array to convert.

    Returns
    -------
    ndarray:
        The array, converted to a Numpy array.
    """
    try:
        # Should work for real arrays, maybe not for complex arrays.
        result = np.array(arr._data).reshape(arr.size, order="F")
    except:
        result = np.array(arr)
    return result


def multi_matlab_to_numpy(*args) -> List[ndarray]:
    """
    Converts multiple matlab arrays to numpy arrays using `matlab_to_numpy()`.

    This allows code like the following:

    `x, y = multi_matlab_to_numpy(x, y)`

    Parameters
    ----------
    args : array_like
        The arrays to convert.

    Returns
    -------
    List[ndarray]
        Ordered list containing the Numpy equivalent of each MATLAB array.
    """
    out = []
    for arr in args:
        out.append(matlab_to_numpy(arr))

    return out
