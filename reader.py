import matplotlib.pyplot as plt

def csv2(f):
    import csv
    import numpy as np

    with open(f) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        time = []
        voltage = []
        errors = 0

        #Read file row by row
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
    data = csv2('test_data29.csv')
    time = data[0]
    voltage = data[1]

    plt.plot(time, voltage)
    plt.show()