
def test_beats():
    """This function unit tests the beats function.

    This function requires the numpy package, as well as the beats
    function being testing. The first line in the function is the input
    data being given into the test_beats function. This is then tested
    in response to the result from the beats function.
    """

    import numpy as np
    from beats import beats_test

    response = beats_test(threshold=0.7,
                          voltage_array=np.array([3, 2, 10, 3, 10, 2]),
                          time_array=np.array([0, 2, 4, 6, 8, 10])
                          )
    np.testing.assert_array_almost_equal(response, np.array([4, 8]))
