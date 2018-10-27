
def test_exceed():
    """This function unit tests the exceed function in the exceed file.

    The function requires the numpy and pytest packages, and also calls
    in the exceed function that is subject to testing. The with
    statement utilises the pytest to check if an 'Exception' is raised
    when a voltage_array that has bad data is input into the function.
    """

    import numpy as np
    import pytest
    from exceed import exceed

    with pytest.raises(Exception):
        exceed(voltage_array=np.array([0, 1, 301]))