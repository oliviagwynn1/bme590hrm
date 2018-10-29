def length(time_array, voltage_array):
    """This function checks if the time and voltage arrays are of equal
    lengths.

    The first two lines in the function determine the length of the time
    and voltage arrays, respectively. The if statement checks to see if
    they are unequal, if so, it raises and exception.

    :param time_array: array of time values
    :param voltage_array: array of voltage values
    :type time_array: ndarray
    :type voltage_array: ndarray
    """

    time_length = len(time_array)
    voltage_length = len(voltage_array)

    if time_length != voltage_length:
        raise Exception
