import numpy as np

time = [0,-1,2,3,4,5]
voltage = [-5,3,9,10,305,-3, 0]
time_array = np.array(time)
voltage_array = np.array(voltage)

class Error(Exception):
    """Raise error"""
    pass

class DifferentLengthArrays(Error):
    """This error is for arrays of different lengths."""
    pass

class NegativeTimeData(Error):
    """This error is for time arrays with negative values."""
    pass

class VoltageDataHigh(Error):
    """This error is for voltages that exceed 300mv."""
    pass


def length():
    """Check lengths of time and voltage are the same"""
    time_length = len(time_array)
    voltage_length = len(voltage_array)
    if time_length != voltage_length:
        raise DifferentLengthArrays

def neg():
    """Check time has no negative data"""
    for num in time_array:
        if num < 0:
            raise NegativeTimeData

def exceed():
    """Check voltage does not exceed 300mv"""
    for val in voltage_array:
        if val > 300:
            raise VoltageDataHigh


if __name__ == "__main__":
    try:
        length()
    except DifferentLengthArrays:
        print("Arrays are different lengths.")

    try:
        neg()
    except NegativeTimeData:
        print("Time array has negative values.")

    try:
        exceed()
    except VoltageDataHigh:
        print("Voltage exceeds 300mv.")