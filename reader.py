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
        return np.array(time), np.array(voltage)