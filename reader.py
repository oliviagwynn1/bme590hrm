def csv_reader(data_file):
    import csv
    import numpy as np

    with open(data_file) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        time = []
        voltage = []
        errors = 0

        """Reads file row by row"""
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
    data = csv_reader('test_data32.csv')



