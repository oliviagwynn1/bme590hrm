def test_num_beats():
    from num_beats import num_beats_test
    import numpy as np
    response = num_beats_test(threshold = 0.7, voltage_array = np.array([1, 2, 3, 2, 0, 2, 3, 2, 1]))
    assert response == 2