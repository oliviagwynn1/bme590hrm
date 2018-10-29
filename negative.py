
def neg(time_array):
    """This functions checks if any value in the time array is
    negative.

    The for loop runs through the time array to see if any input is
    below zero. If so, an exception is raise.

    :param time_array: array of time values
    :type time_array: ndarray
    """

    for num in time_array:
        if num < 0:
            raise Exception

