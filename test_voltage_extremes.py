
def test_voltage_extremes():
    """This function unit tests the voltage_extremes function.

    This function requires the numpy package, as well as the
    voltage_extremes function being testing. The first line in the
    function is the input data being given into the test function. This
    is then tested in response to the result from the voltage_extremes
    function.
    """

    import numpy as np
    from voltage_extremes import voltage_extremes

    response = voltage_extremes(voltage_array=np.array([5, -10, 100, 81]))
    assert response == (-10, 100)
