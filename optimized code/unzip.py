import gzip
import os
import time
start = time.clock()
def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace(".gz", "")
    g_file = gzip.GzipFile("../{}".format(file_name))
    open("../csv/{}".format(f_name), "wb+").write(g_file.read())
    g_file.close()

if __name__ == "__main__":
    for filename in os.listdir(".."):
        if ".gz" in filename:
            un_gz(filename)
            # print(filename)
end = time.clock()
print("uzip:", (end - start))
