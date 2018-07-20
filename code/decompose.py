import csv
import os
import operator
import time

r_output = "../csv/output/R.csv"
w_output = "../csv/output/W.csv"

header = "Timestamp,Response,IOType,LUN,Offset,Size\n"
open(r_output,"w+").write(header)
open(w_output,"w+").write(header)

def decompose(filename):
    file_input = "../csv/{}".format(filename)
    trace = csv.reader(open(file_input, 'r'))
    next(trace)

    for row in trace:
        if row[2] == 'R':
            write = csv.writer(open(r_output, 'a'))
            write.writerow(row)
        elif row[2] == 'W':
            write = csv.writer(open(w_output, 'a'))
            write.writerow(row)

start = time.clock()
if __name__ == "__main__":
    for filename in os.listdir("../csv"):
        if ".csv" in filename:
            print(filename)
            decompose(filename)

end = time.clock()
print(end - start)
