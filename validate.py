
def validate(time_array, voltage_array):
    """This function validates the input data.

    This function also requires the length, neg and exceed
    functions from the length, negative and exceed files, respectively.
    The first line sets the variable final equal to an empty string. The
    next three lines create three different strings.

    The try and except functions each call in one of the imported
    functions (length, neg, exceed). If an exception is raised in either
    function, it adds a specific string to the variable final.

    The if statement checks to see if the final variable is not equal to
    an empty string, if so, a TypeError is raised and the final variable
    is printed.

    :param time_array: array of time values
    :param voltage_array: array of voltage values
    :type time_array: ndarray
    :type voltage_array: ndarray
    """

    from length import length
    from negative import neg
    from exceed import exceed

    final = ""
    s1 = "Time and Voltage arrays have different lengths."
    s2 = "Time has negative values."
    s3 = "Voltage exceeds 300mV."

    try:
        length(time_array, voltage_array)
    except:
        final += s1

    try:
        neg(time_array)
    except:
        final += s2

    try:
        exceed(voltage_array)
    except:
        final += s3

    if final != "":
        raise TypeError(final)


if __name__ == "__main__":

    import numpy as np

    validate(time_array = np.array([0, -1, 2, 3, 4, 5]),
             voltage_array=np.array([-5, 3, 9, 10, 305, -3, 2])
             )