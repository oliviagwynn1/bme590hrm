import numpy as np

time_array = [0, 9, 50]
#time_array = np.array(time)
#print(time_array)

def duration(time_array):
    """Time duration of the ECG strip"""
    length = len(time_array) - 1
    duration_val = time_array[length]
    return duration_val
print(duration(time_array))