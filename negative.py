
def neg(time_array):
    """This functions checks if any value in the time array is
    negative.

    The function requires input of a time array from the read csv file.
    The for loop runs through the time array to see if any input is
    below zero. If so, an exception is raise.
    """

    for num in time_array:
        if num < 0:
            raise Exception


if __name__ == "__main__":
    import numpy as np
    neg(time_array=np.array([0,1,2]))