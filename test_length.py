
def test_length():
    """This function unit tests the length function.

    This function requires the numpy and pytest packages, as well as the
    length function being testing. The with statement checks if an
    exception is raised if the input time and voltage arrays have
    unequal lengths.
    """

    import numpy as np
    import pytest
    from length import length

    with pytest.raises(Exception):
        length(time_array=np.array([0, 1, 2]),
               voltage_array=np.array([-1, 3, 4, 9])
               )

