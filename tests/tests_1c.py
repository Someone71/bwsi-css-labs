"""
tests_1b.py

This module contains unit tests for the max_subarray_sum function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([-2,1,-3,4,-1,2,3,-5,4]) == 8
    assert max_subarray_sum([-2,1,-3,1,-1,2,1,-5,4]) == 4


if __name__ == "__main__":
    pytest.main()