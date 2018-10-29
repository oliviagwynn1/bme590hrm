
def csv_reader(data_file):
    """returns np.array(time), np.array(voltage)

    This function reads in csv files.

    The for loop reads each row of the time and voltage lists and
    converts them from strings to floats. If a string can't be
    converted, a ValueError is raised and that index is skipped. The
    error count variable adds all up the number of times a ValueError
    is raised, if it exceeds 10 errors, the file cannot be read in.
    After the time and voltage lists are converted to floats, the lists
    are converted into numpy arrays.

    :param data_file: csv file being read in
    :type data_file: csv file
    :return: np.array(time), np.array(voltage)
    :rtype: ndarray
    """

    import csv
    import numpy as np

    with open(data_file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        time = []
        voltage = []
        errors = 0

        for row in reader:
            try:
                t = (float(row[0]))
                v =(float(row[1]))
            except ValueError:
                errors += 1
                if errors > 10:
                    print("Data is inaccurate, please input new data.")
                    break
                continue

            time.append(t)
            voltage.append(v)

        return np.array(time), np.array(voltage)


if __name__ == "__main__":

    import matplotlib.pyplot as plt

    data = csv_reader('test_data8.csv')

    plt.plot(data[0], data[1])
    plt.show()



