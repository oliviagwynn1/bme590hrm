
import create_metrics


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