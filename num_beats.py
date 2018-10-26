
def num_beats_test(threshold=0.7, voltage_array=None):
    import peakutils
    indexes = peakutils.indexes(voltage_array, thres=threshold)
    number_beats = len(indexes)
    return number_beats