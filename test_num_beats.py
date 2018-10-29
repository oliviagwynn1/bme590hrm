
def test_num_beats():
    """This function unit tests the num_beats function.

    This function requires the numpy package, as well as the num_beats
    function being testing. The first line in the function is the input
    data being given into the test function. This is then tested in
    response to the result from the num_beats function.
    """

    import numpy as np
    from num_beats import num_beats_test

    response = num_beats_test(threshold=0.7,
                              voltage_array=np.array([1, 3, 2, 3, 1])
                              )
    assert response == 2