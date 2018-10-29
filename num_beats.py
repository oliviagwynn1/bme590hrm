
def num_beats_test(threshold=0.7, voltage_array=None):
    """This function calculates the number of beats in each strip.

    This function requires 2 input parameters; threshold, which can be
    set in the function line; voltage_array, given from the read csv
    file.

    The function requires the peakutils package to determine the indexes
    of every peak/beat in the voltage array. The second line in the function
    calculates the number of beats in the strip.
    """

    import peakutils

    indexes = peakutils.indexes(voltage_array, thres=threshold)
    number_beats = len(indexes)

    return number_beats