
import os
import csv

#list_csv_files = os.listdir("Data")
#print(list_csv_files[0])

# create a function to calculate the stock rate
def function(a):
    # open csv files
    with open(a, 'r') as my_file:
        lines = csv.reader(my_file)
        i=0
        data=[]
        result=[]
        for line in lines:
            i+=1
            if i > 1:
                for k in range(1,7):
                    line[k]=float(line[k])
                change = ((line[4] - line[1]) / line[1])
                result += [change]
                data += [line[0], line[1], line[2], line[3], line[4], line[5], line[6]]

    with open("OutputData/output.csv", 'w') as my_output_file:
        to_write = csv.writer(my_output_file, delimiter=",")
        to_write.writerow(["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume", "Calculation"])
        to_write.writerow(
            [str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5]), str(data[6]),
             result[0]])
        for x in range(1, len(result) - 1):
            to_write.writerow([str(data[7 * x]), str(data[7 * x + 1]), str(data[7 * x + 2]), str(data[7 * x + 3]),
                               str(data[7 * x + 4]), str(data[7 * x + 5]), str(data[7 * x + 6]), result[x]])















