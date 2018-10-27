def length(time_array, voltage_array):
    """Check lengths of time and voltage are the same"""
    time_length = len(time_array)
    voltage_length = len(voltage_array)
    if time_length != voltage_length:
        raise Exception

if __name__ == "__main__":
    import numpy as np
    length(time_array=np.array([0,1,2]), voltage_array=np.array([-1,3,4]))
