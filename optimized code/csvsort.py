import time
import pandas as pd

start = time.clock()
file_input = "../csv/output_2/R_merge.csv"
file_output="../csv/output_2/R_sorted.csv"
# csvsort("../csv/output_2/R_merge.csv", [3,5,0], output_filename="../csv/output_2/R_sorted.csv")
# print(pd.read_csv(file_input))
df = pd.read_csv(file_input,  dtype = {"Size": str, "Timestamp": str, "Response": str})
df["copy"] = df["Timestamp"]
df.to_csv(file_output, index = 0)
del df

df = pd.read_csv(file_output,  dtype = {"Size": int, "Timestamp": str, "Response": str})
df = df.sort_values(by=["IOType", "Size", "copy"])
df.drop(["copy"],axis = 1, inplace = True)
df.to_csv(file_output, index = 0)
end = time.clock()
print("csvsort:",(end - start))
