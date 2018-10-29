
def exceed(voltage_array, value=300):
    """This function checks if the voltage exceeds a given value.

    The for loop runs through the voltage_array, to
    determine if any number in the voltage array does exceed the given
    value. If so, an exception is raised.

    :param voltage_array: array of voltage values
    :param value: sets threshold value of voltage
    :type voltage_array: ndarray
    :type value: integer
    """

    for val in voltage_array:
        if val > value:
            raise Exception



