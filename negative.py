def neg(time_array):
    """Check time has no negative data"""
    for num in time_array:
        if num < 0:
            raise Exception


if __name__ == "__main__":
    import numpy as np
    neg(time_array=np.array([0,1,2]))