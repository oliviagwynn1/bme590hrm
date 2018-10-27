def length(time_array, voltage_array):
    """This function checks if the time and voltage arrays are of equal
    lengths.

    The function requires input of a time_array and voltage_array,
    from the csv file read in. The first two lines in the function
    determine the length of the time and voltage arrays, respectively.
    The if statement checks to see if they are unequal, if so, it raises
    and exception.
    """

    time_length = len(time_array)
    voltage_length = len(voltage_array)

    if time_length != voltage_length:
        raise Exception
