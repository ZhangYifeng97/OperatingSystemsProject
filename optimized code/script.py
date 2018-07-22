import os
import time
a = time.clock()
os.system("python3 unzip.py")
os.system("python3 merge.py")
os.system("python3 csvsort.py")
os.system("python3 split.py")
os.system("python3 statistic.py")
b = time.clock()
print("during time:",(b - a))
