import csv
import datetime
import itertools
import os

path1 = 'C:/Users/aZhen\Desktop/3931 individual project/data/failed_processedData.csv'
path2 = 'C:/Users/aZhen\Desktop/3931 individual project/data/failed_processedData_NoNull.csv'
path3 = 'C:/Users/aZhen\Desktop/3931 individual project/data/unfailed_processedData.csv'
path4 = 'C:/Users/aZhen\Desktop/3931 individual project/data/unfailed_processedData_NoNull.csv'
path5 = 'C:/Users/aZhen\Desktop/3931 individual project/data/unfailed_processedData_withNulls.csv'
path6 = 'C:/Users/aZhen\Desktop/3931 individual project/data/unfailed_processedData_withNulls_NullProcessed.csv'
path7 = 'C:/Users/aZhen\Desktop/3931 individual project/data/failed_processedData_IDFiltered.csv'
path8 = 'C:/Users/aZhen\Desktop/3931 individual project/data/failed_processedData_IDFiltered_NoNull.csv'
group = []
count = 0
nullcount = 0
with open(path7, 'r', newline='') as csvfile1:
    with open(path8,'a', newline='') as csvfile2:
        csv_reader1 = csv.reader(csvfile1)
        for row in csv_reader1:
            count += 1
            if row[0] == 'null':
                line = ['-1' for i in range(105)]
                line.append('1')
            else:
                line = [j if j != '' else '-1' for j in row ]
                line.append('0')
            csv_writer = csv.writer(csvfile2)
            csv_writer.writerow(line)
