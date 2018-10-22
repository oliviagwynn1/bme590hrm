def csv(f):
    import csv

    with open(f) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        dict = {}
        dict["time"] = []
        dict["voltage"] = []
        #Read file row by row
        rowNr = 0
        for row in reader:
            if rowNr >= 0:
                dict["time"].append(float(row[0]))
                dict["voltage"].append(float(row[1]))
            rowNr = rowNr + 1
        return dict


if __name__ == "__main__":
    data = csv('test_data1.csv')
    print(data)