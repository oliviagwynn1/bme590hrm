
def mean_beats(threshold=0.7, voltage_array, time_array):
    """This function calculates the average heart rate.

    This function requires 3 input parameters; threshold, which can be
    set in the function line; voltage_array, given from the read csv
    file; time_array, given from the read csv file.

    The function requires the peakutils package to determine the indexes
    of every peak in the voltage array. The second line in the function
    calculates the number of peaks in the strip. The third line
    determines the total duration of the strip. The fourth line
    calculates the average heart rate.
    """

    import peakutils

    indexes = peakutils.indexes((voltage_array), thres=threshold)
    number_beats = len(indexes)
    duration_beats = time_array[len(time_array) - 1]
    avg_beats = (number_beats/duration_beats)*60

    return avg_beats




