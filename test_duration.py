from duration import duration
import pytest
import numpy as np



@pytest.mark.parametrize("time_array, expected",[
    ("[0, 4, 20]", 20),
    ("[9, 10, 100]", 100),
    ("[10]", 10)
])

def test_duration(time_array, expected):
    response = duration(time_array)
    assert response == expected