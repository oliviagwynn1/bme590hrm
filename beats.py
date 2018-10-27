
def beats_test(threshold=0.7, voltage_array=None, time_array=None):
    """This function determines the time that each beat occurs.

    It requires 3 input parameters; threshold, which can be set in the
    function line; voltage_array, given from the read csv file;
    time_array, given from the read csv file.

    It uses the peakutils package to detect for peaks above the set
    threshold, and returns their indexes. The second line in the
    function finds the corresponding time of these indexes from the
    time_array.
    """

    import peakutils

    indexes = peakutils.indexes((voltage_array), thres=threshold)
    time_of_beats = time_array[indexes]

    return time_of_beats







