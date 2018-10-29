
def test_negative():
    """This function unit tests the neg function in the negative file.

    The function requires the numpy and pytest packages, and also calls
    in the neg function that is subject to testing. The with statement
    utilises the pytest to check if an 'Exception' is raised when a
    value in the input time array is below zero.
    """

    import numpy as np
    import pytest
    from negative import neg

    with pytest.raises(Exception):
        neg(time_array=np.array([-1, 0, 1, 2]))