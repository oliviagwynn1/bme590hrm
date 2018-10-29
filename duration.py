
def duration(time_array):
    """This function find the time duration of each strip.

    It requires input of a time_array from the csv file read in. The
    first line in the functions determines the index of the last value
    in the time_array. The second line in the function finds the time
    corresponding to this index.

    :param time_array: array of time values
    :type time_array: array of floats
    :return: duration_val
    :rtype: float
    """

    import logging
    from logging import config

    logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)

    length = len(time_array) - 1
    duration_val = time_array[length]
    logging.info(duration_val)

    return duration_val