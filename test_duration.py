def test_duration():
    from duration import duration
    import numpy as np
    response = duration(time_array=np.array([0, 9, 30, 40]))
    assert response == 40