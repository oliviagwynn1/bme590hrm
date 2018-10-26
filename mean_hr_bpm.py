def mean_beats(threshold=0.7, voltage_array=None, time_array=None):
    import peakutils
    indexes = peakutils.indexes((voltage_array), thres=threshold)
    number_beats = len(indexes)
    duration_beats = time_array[len(time_array) - 1]
    avg_beats = (number_beats/duration_beats)*60
    return avg_beats




