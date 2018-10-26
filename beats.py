
def beats_test(threshold=0.7, voltage_array=None, time_array=None):
    import peakutils
    indexes = peakutils.indexes((voltage_array), thres=threshold)
    time_of_beats = time_array[indexes]
    return time_of_beats







