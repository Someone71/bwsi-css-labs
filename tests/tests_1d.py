"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test():
    assert two_sum([2, 7, 11, 15], 18) == [1, 2]
    assert two_sum([2, 7, 11, 15], 26) == [2, 3]
    assert two_sum([2, 7, 11, 15], 22) == [1, 3]


if __name__ == "__main__":
    pytest.main()