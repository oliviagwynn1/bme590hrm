def test_beats():
    from beats import beats_test
    import numpy as np
    response = beats_test(threshold = 0.7,
                          voltage_array = np.array([3,2,10,3,10,2]),
                          time_array=np.array([0,2,4,6,8,10]))
    np.testing.assert_array_almost_equal(response, np.array([4, 8]))
