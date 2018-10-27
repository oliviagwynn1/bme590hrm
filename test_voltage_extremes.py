def test_voltage_extremes():
    from voltage_extremes import voltage_extremes
    import numpy as np
    response = voltage_extremes(voltage_array=np.array([5,-10,100,81]))
    assert response == (-10, 100)
