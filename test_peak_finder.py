def test_peak():
    import numpy as np
    from peak_finder import peak
    response = peak(threshold=0.7, voltage=np.array([1, 2, 3, 2, 1]))
    assert response == 2