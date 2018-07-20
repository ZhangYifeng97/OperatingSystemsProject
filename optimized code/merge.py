import time
import os
import csv
import pandas as pd
import time

start = time.clock()

r_output = "../csv/output_2/R_merge.csv"

for filename in os.listdir("../csv/"):
    if ".csv" in filename:
        print(filename)
        file_input = "../csv/{}".format(filename)
        copy_name = "../csv/copy/{}".format(filename)
        if filename != os.listdir("../csv")[0]:
            pf = pd.read_csv(file_input,dtype = {"Size": str, "Timestamp": str, "Response": str})
            pf.to_csv("../csv/copy/{}".format(filename), header = 0, index = 0)
        else:
            pf = pd.read_csv(file_input,dtype = {"Size": str, "Timestamp": str, "Response": str})
            pf.to_csv("../csv/copy/{}".format(filename), index = 0)
        open(r_output, 'a').write(open(copy_name,'r').read())
end = time.clock()
print("merge:", (end - start))
