import csv
import os
import operator

r_input = "./R.csv"
w_input = "./W.csv"
r_output = "./R_sorted.csv"
w_output = "./W_sorted.csv"

r = csv.reader(open(r_input, 'r'))
w = csv.reader(open(w_input, 'r'))

# convert csv.reader to list[]
r = [row for row in r]
w = [row for row in w]

# convert string to int
for i in range(len(r)):
    r[i][0] = float(r[i][0])
    r[i][5] = int(r[i][5])
for i in range(len(w)):
    w[i][0] = float(w[i][0])
    w[i][5] = int(w[i][5])

r_sortedlist = sorted(r, key=operator.itemgetter(5,0))
w_sortedlist = sorted(w, key=operator.itemgetter(5,0))


for row in r_sortedlist:
    write = csv.writer(open(r_output, 'a'))
    write.writerow(row)

for row in w_sortedlist:
    write = csv.writer(open(w_output, 'a'))
    write.writerow(row)
