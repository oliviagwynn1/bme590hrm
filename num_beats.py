
def num_beats_test(threshold=0.7, voltage=None):
    import peakutils
    indexes = peakutils.indexes(voltage, thres=threshold)
    number_beats = len(indexes)
    return number_beats








