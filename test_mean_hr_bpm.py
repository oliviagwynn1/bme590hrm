def test_mean_beats():
    from mean_hr_beats import mean_beats
    import numpy as np

    response = num_beats_test(threshold = 0.7, voltage = [1, 2, 3, 2, 1, 2, 3, 2, 1])
    #    np.testing.assert_array_almost_equal(response, np.array([2, 6]))
    assert response == 2