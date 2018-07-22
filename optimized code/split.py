import os
import sys
import mmap
import time
import csv
m = mmap.mmap(os.open('../csv/output_2/R_sorted.csv',os.O_RDWR), 0)
m.readline()
start = time.clock()
file = csv.reader(open('../csv/output_2/R_sorted.csv','r'))
next(file)
header = "Timestamp,Response,IOType,LUN,Offset,Size\n"
open("../csv/output_2/R.csv","w+").write(header)
open("../csv/output_2/W.csv","w+").write(header)
l = []
row = m.readline()
while(row):
    if b'R' in row:
        l.append(row.decode("utf-8"))
    else:
        break
    row = m.readline()
str = "".join(l)
open("../csv/output_2/R.csv","a").write(str)
print("R finish")

l = []
while(row):
    l.append(row.decode("utf-8"))
    row = m.readline()
str = "".join(l)
open("../csv/output_2/W.csv","a").write(str)
# print(m.readline())
end = time.clock()

print("split:", (end-start))
