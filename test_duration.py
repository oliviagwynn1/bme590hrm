
def test_duration():
    """This function unit tests the duration function.

    This function requires the numpy package, as well as the duration
    function being testing. The first line in the function is the input
    data being given into the test function. This is then tested in
    response to the result from the duration function.
    """

    import numpy as np
    from duration import duration

    response = duration(time_array=np.array([0, 9, 30, 40]))
    assert response == 40