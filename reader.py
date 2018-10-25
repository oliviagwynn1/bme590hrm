import matplotlib.pyplot as plt
#a= [[1,2], [1,], [c,9], [j,hello]]

def csv2(f):
    import csv
    import numpy as np

    with open(f) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')


        time = []
        voltage = []

        #Read file row by row
        for row in reader:
            time.append(float(row[0]))
            voltage.append(float(row[1]))
            #except ValueError:
            #    print("Input data is missing a numeric value")
            
            #del time[row]
            #del voltage[row]
        return np.array(time), np.array(voltage)

if __name__ == "__main__":
    data = csv2('test_data1.csv')
    time = data[0]
    voltage = data[1]

    plt.plot(time, voltage)
    plt.show()