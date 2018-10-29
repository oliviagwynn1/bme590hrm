
def voltage_extremes(voltage_array):
    """returns voltage_extremes_val

    This function calculates the minimum and maximum voltages.

    The first two line of this function calculate the minimum and
    maximum voltages in the array, respectively. The third line creates
    a tuple containing the voltage extremes.

    :param voltage_array: array of voltage values
    :type voltage_array: ndarray
    :return: voltage_extremes_val
    :rtype: tuple
    """

    import logging
    from logging import config

    logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)

    voltage_min = min(voltage_array)
    voltage_max = max(voltage_array)
    voltage_extremes_val = (voltage_min, voltage_max)
    logging.info(voltage_extremes_val)

    return voltage_extremes_val
