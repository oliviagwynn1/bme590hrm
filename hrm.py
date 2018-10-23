import numpy as np

def csv(f):
    import csv

    with open(f) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        time = []
        voltage = []
        #Read file row by row
        rowNr = 0
        for row in reader:
            if rowNr >= 0:
                time.append(float(row[0]))
                voltage.append(float(row[1]))
            rowNr = rowNr + 1
        return time, voltage


def validate(data):
#    time_array = np.array(data[0])
#    voltage_array = np.array(data[1])

    ##Check lengths of time and voltage are the same


    ##Check time has no negative data
    ###Convert to numpy array and find where values are negative, and produce array of True, False etc
    ###Use np.where(file) to find index of false values
#    for value in time_array:
#        if value < 0:
#            return false
#    return true
#    return time_array

    ##Check voltage does not exceed 300mv
    pass

def mean_hr_bpm(metrics):
    # Estimated average heart rate over a user-specified number of minutes (can choose a default interval)
    mean_hr_bmp_val = 'Fill this in.'
    return mean_hr_bmp_val

def voltage_extremes(metrics):
    # Tuple containing minimum and maximum lead voltages
    voltage_extremes_val = 'Fill this in.'
    return voltage_extremes_val

def duration(metrics):
    # Time duration of the ECG strip
    duration_val = "Fill this in."
    return duration_val

def num_beats():
    # Number of detected beats in the strip
    num_beats_val = "Fill this in."
    return num_beats_val

def beats():
    # Numpy array of times when a beat occurred
    beats_val = 'Fill this in.'
    return beats_val

def create_metrics():
    metrics = {}
    return metrics

def add_word(metrics):
    #metrics["mean_hr_bpm"] = mean_hr_bpm()
    #metrics["voltage_extremes"] = voltage_extremes()
    #metrics["duration"] = duration()
    #metrics["num_beats"] = num_beats()
    #metrics["beats"] = beats()
    #return metrics
    pass


if __name__ == "__main__":
    data = csv('test_data1.csv')
    time = data[0]
    voltage = data[1]
    print(time)
    print(voltage)
    metrics = create_metrics()
    metrics = add_word(metrics)
    print(metrics)