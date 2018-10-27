def test_mean_bpm():
    from mean_hr_bpm import mean_beats
    import numpy as np
    response = mean_beats(voltage_array=np.array([2,10,2,1,1]),
                          time_array=np.array([0,2,4,6,8]))
    assert response == float(60/8)