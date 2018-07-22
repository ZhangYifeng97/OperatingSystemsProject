import time
import os
import mmap
import sys
import csv

start = time.clock()

def counting(mode):
    l = []
    r_file = csv.reader(open("../csv/output/{}.csv".format(mode), 'r'))
    # insert a blank row
    next(r_file)
    current_size = 0
    for i in r_file:
        current_size = i[5]
        break
    counter = 0
    for row in r_file:
        if row[5] == current_size:
            counter += 1
        else:
            l.append("{},{}\n".format(counter,current_size))
            counter = 1
            current_size = row[5]
    # process the last size, which would be omitted in the for loop
    csv.writer(open("../csv/output/{}.csv".format(mode), 'a')).writerow([])
    string = "".join(l)
    open("../csv/output/{}.csv".format(mode), 'a').write(string)
    csv.writer(open("../csv/output/{}.csv".format(mode), 'a')).writerow([counter, current_size])

counting('R')
counting('W')
end = time.clock()
print(end - start)
