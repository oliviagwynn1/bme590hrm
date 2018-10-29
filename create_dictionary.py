
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
    myDictionary = create_metrics()
    myDictionary = add_word(myDictionary)
    logging.info(myDictionary)
    convert_json(myDictionary, f=data_file)





