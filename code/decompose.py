import csv
import os
import operator

def decompose(filename):
    file_input = "../csv/{}".format(filename)
    r_output = "../csv/output/R.csv"
    w_output = "../csv/output/W.csv"

    trace = csv.reader(open(file_input, 'r'))
    next(trace)

    for row in trace:
        if row[2] == 'R':
            write = csv.writer(open(r_output, 'a'))
            write.writerow(row)
        elif row[2] == 'W':
            write = csv.writer(open(w_output, 'a'))
            write.writerow(row)

if __name__ == "__main__":
    for filename in os.listdir("../csv"):
        decompose(filename)
