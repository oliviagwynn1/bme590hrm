def exceed(voltage_array):
    """Check voltage does not exceed 300mv"""
    for val in voltage_array:
        if val > 300:
            raise Exception



if __name__ == "__main__":
    import numpy as np
    exceed(voltage_array=np.array([0,1,3]))