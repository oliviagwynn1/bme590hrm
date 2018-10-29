
def num_beats_test(threshold=0.7, voltage_array=None):
    """returns number_beats

    This function calculates the number of beats in each strip.

    The function requires the peakutils package to determine the indexes
    of every peak/beat in the voltage array. The second line in the function
    calculates the number of beats in the strip.

    :param threshold: threshold value for peak voltage
    :param voltage_array: array of voltage values
    :type threshold: float
    :type voltage_array: ndarray, none
    :return: number_beats
    :rtype: float
    """

    import peakutils

    indexes = peakutils.indexes(voltage_array, thres=threshold)
    number_beats = len(indexes)

    return number_beats