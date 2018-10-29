import logging
from logging import config
from reader import csv_reader
from validate import validate
from beats import beats_test
from num_beats import num_beats_test
from duration import duration
from mean_hr_bpm import mean_beats
from voltage_extremes import voltage_extremes
from metrics import create_metrics
from convert_json import convert_json


def add_word(metrics):
    """returns metrics

    This function adds words to the metrics dictionary.

    This function requires the import of the csv_reader, validate,
    beats_test, num_beats_test, duration, mean_beats, voltage_extremes,
    create_metrics functions. It adds the results from the calculated
    variables into the dictionary to create keys.

    :param metrics: dictionary called metrics
    :type metrics: dictionary
    :return: metrics
    :rtype: dictionary
    """
    metrics["mean_hr_bpm"] = mean_heart_rate
    metrics["voltage_extremes"] = voltage_extremes
    metrics["duration"] = duration
    metrics["num_beats"] = num_beats
    metrics["beats"] = beats

    return metrics


if __name__ == "__main__":
    data_file = 'test_data1.csv'
    logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)
    data = csv_reader(data_file)
    time_array = data[0]
    voltage_array = data[1]
    validate(time_array, voltage_array)
    beats = beats_test(threshold=0.7, voltage_array=voltage_array,
                       time_array=time_array
                       )
    num_beats = num_beats_test(threshold=0.7, voltage_array=voltage_array)
    duration = duration(time_array=time_array)
    mean_heart_rate = mean_beats(threshold=0.7, voltage_array=voltage_array,
                                 time_array=time_array
                                 )
    voltage_extremes = voltage_extremes(voltage_array=voltage_array)
    my_dictionary = create_metrics()
    my_dictionary = add_word(my_dictionary)
    logging.info(my_dictionary)
    convert_json(my_dictionary, f=data_file)





