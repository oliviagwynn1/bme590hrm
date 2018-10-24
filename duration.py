import numpy as np

time = [0,1,2,3,4,5,6,10]
time_array = np.array(time)


def duration(time_array):
    """Time duration of the ECG strip"""
    length = len(time_array)
#    return length
    duration_val = time_array[7]
    return duration_val
print(duration(time_array))