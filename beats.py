
def beats_test(threshold=0.7, voltage_array=None, time_array=None):
    """returns time_of_beats

    This function determines the time that each beat occurs.

    This function uses the peakutils package to detect for peaks above the set
    threshold, and returns their indexes. The second line in the
    function finds the corresponding time of these indexes from the
    time_array. The final line in the code converts the array of the
    time of each beats into a list, to allow conversion of the
    dictionary into a JSON file.

    :param threshold: sets threshold value for peaks
    :param voltage_array: array of voltage values
    :param time_array: array of time values
    :type threshold: float
    :type voltage_array: ndarray
    :type time_array: ndarray
    :returns: time_of_beats
    :rtype: list
    """

    import peakutils

    indexes = peakutils.indexes((voltage_array), thres=threshold)
    time_of_beats = time_array[indexes]
    time_of_beats = time_of_beats.tolist()

    return time_of_beats







