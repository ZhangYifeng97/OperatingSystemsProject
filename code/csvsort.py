import time
import pandas as pd

start = time.clock()
r_input = "../csv/output/R.csv"
w_input = "../csv/output/W.csv"

# csvsort("../csv/output_2/R_merge.csv", [3,5,0], output_filename="../csv/output_2/R_sorted.csv")
# print(pd.read_csv(file_input))
df = pd.read_csv(r_input, dtype = {"Size": int, "Timestamp": float})
print("here")

df = df.sort_values(by=["Size", "Timestamp"])
df.to_csv(r_input, index = 0)

df = pd.read_csv(w_input, dtype = {"Size": int, "Timestamp": float})
df = df.sort_values(by=["Size", "Timestamp"])
df.to_csv(w_input, index = 0)

end = time.clock()
print(end - start)
