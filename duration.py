def duration(time_array):
    """Time duration of the ECG strip"""
    length = len(time_array) - 1
    duration_val = time_array[length]
    return duration_val
