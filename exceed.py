
def exceed(voltage_array, value=300):
    """This function checks if the voltage exceeds a given value.

    It requires an input parameter of voltage_array from the csv file
    read in, as well as a specified value to check if the voltage
    exceeds it. The for loop runs through the voltage_array, to
    determine if any number in the voltage array does exceed the given
    value. If so, an exception is raised.
    """

    for val in voltage_array:
        if val > value:
            raise Exception



