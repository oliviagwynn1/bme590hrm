
def mean_beats(threshold=0.7, voltage_array=None, time_array=None):
    import peakutils
    indexes = peakutils.indexes(thres=threshold, voltage_array, time_array)
    number_beats = len(indexes)
    duration_beats = len(time_array)
    avg_beats = number_beats/duration_beats
    return avg_beats


if __name__ == "__main__":
    import numpy as np
    print(mean_beats(voltage_array=np.array([2,10,9,100]), time_array=np.array([0,2,4,6])))

