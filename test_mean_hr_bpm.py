
def test_mean_bpm():
    """This function unit tests the mean_hr_bpm function.

    This function requires the numpy package, as well as the mean_hr_bpm
    function being testing. The first line in the function is the input
    data being given into the test function. This is then tested in
    response to the result from the mean_hr_bpm function.
    """

    import numpy as np
    from mean_hr_bpm import mean_beats

    response = mean_beats(voltage_array=np.array([2, 10, 2, 1, 1]),
                          time_array=np.array([0, 2, 4, 6, 8])
                          )
    assert response == float(60/8)