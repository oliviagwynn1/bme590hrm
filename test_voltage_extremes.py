from voltage_extremes import voltage_extremes
import pytest

@pytest.mark.parametrize("voltage_array, expected",[
    ([-14, 103, -3], (-14, 103)),
    ([6, 9, 10], (6, 10))
    ])

def test_voltage_extremes(voltage_array, expected):
    response = voltage_extremes(voltage_array)
    assert response == expected