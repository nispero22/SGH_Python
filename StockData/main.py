import csv

# import GOOG.csv files
with open("Data/GOOG.csv", 'r') as my_file:
    lines = csv.reader(my_file)
    i=0
    result_GOOG=[]
    for line in lines:
        i+=1
        if i > 1:
            line[1]=float(line[1])
            line[4]=float(line[4])
            change = ((line[4] - line[1]) / line[1])
            result_GOOG = result_GOOG + [change]

# import IBM.csv files
with open("Data/IBM.csv", 'r') as my_file:
    lines = csv.reader(my_file)
    i=0
    result_IBM=[]
    for line in lines:
        i+=1
        if i > 1:
            line[1]=float(line[1])
            line[4]=float(line[4])
            change = ((line[4] - line[1]) / line[1])
            result_IBM = result_IBM + [change]

# import MSFT.csv files
with open("Data/MSFT.csv", 'r') as my_file:
    lines = csv.reader(my_file)
    i=0
    result_MSFT=[]
    for line in lines:
        i+=1
        if i > 1:
            line[1]=float(line[1])
            line[4]=float(line[4])
            change = ((line[4] - line[1]) / line[1])
            result_MSFT = result_MSFT + [change]

# write in a csv file
with open("Output Data/output_GOOG.csv", 'w') as my_output_file:
    to_write = csv.writer(my_output_file, delimiter=",")
    to_write.writerow(["GOOG", "IBM", "MSFT"])
    for x in range(0, len(result_GOOG)-1):
        to_write.writerow([result_GOOG[x], result_IBM[x], result_MSFT[x]])






