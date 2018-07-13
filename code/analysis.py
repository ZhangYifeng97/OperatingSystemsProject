import sys

if __name__ == "__main__":
    # insert a blank row
    csv.writer(open("../csv/output/R.csv", a)).writerow([counter, current_size])
    r_file = csv.reader(open("../csv/output/R.csv", r))
    current_size = r_file[0][5]
    counter = 0
    for row in r_file:
        if row[5] == current_size:
            counter += 1
        else:
            csv.writer(open("../csv/output/R.csv", a)).writerow([counter, current_size])
            counter = 0
            current_size = row[5]
    # process the last size, which would be omitted in the for loop
    csv.writer(open("../csv/output/R.csv", a)).writerow([counter, current_size])
