
def voltage_extremes(voltage_array):
    """This function calculates the minimum and maximum voltages.

    This function requires the input of a voltage_arrray from the file
    read. The first two line of this function calculate the minimum and
    maximum voltages in the array, respectively. The third line creates
    a tuple containing the voltage extremes.
    """

    voltage_min = min(voltage_array)
    voltage_max = max(voltage_array)
    voltage_extremes_val = (voltage_min, voltage_max)

    return voltage_extremes_val
