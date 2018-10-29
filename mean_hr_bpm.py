
def mean_beats(threshold=0.7, voltage_array=None, time_array=None):
    """returns avg_beats

    This function calculates the average heart rate.

    The function requires the peakutils package to determine the indexes
    of every peak in the voltage array. The second line in the function
    calculates the number of peaks in the strip. The third line
    determines the total duration of the strip. The fourth line
    calculates the average heart rate.

    :param threshold: value for peak voltage threshold
    :param voltage_array: array of voltage values
    :param time_array: array of time values
    :type threshold: float
    :type voltage_array: ndarray, none
    :type time_array: ndarray, none
    :return: avg_beats
    :rtype: float
    """

    import peakutils

    indexes = peakutils.indexes((voltage_array), thres=threshold)
    number_beats = len(indexes)
    duration_beats = time_array[len(time_array) - 1]
    avg_beats = (number_beats/duration_beats)*60

    return avg_beats




