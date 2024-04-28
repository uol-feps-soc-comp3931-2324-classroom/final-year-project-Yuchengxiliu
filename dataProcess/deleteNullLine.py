import csv
'''
path1 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MA1_unfailed_processedData.csv'
path2 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MA2_unfailed_processedData.csv'
path3 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MB1_unfailed_processedData.csv'
path4 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MB2_unfailed_processedData.csv'
path5 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MC1_unfailed_processedData.csv'
path6 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MC2_unfailed_processedData.csv'
path11 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull_noNullLine/MA1_unfailed_processedData.csv'
path21 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull_noNullLine/MA2_unfailed_processedData.csv'
path31 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull_noNullLine/MB1_unfailed_processedData.csv'
path41 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull_noNullLine/MB2_unfailed_processedData.csv'
path51 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull_noNullLine/MC1_unfailed_processedData.csv'
path61 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull_noNullLine/MC2_unfailed_processedData.csv'
pathS1 = 'C:/Users/aZhen/Desktop/3931 individual project/data/failed_processedData_NullProcessed.csv'

pathS11 = 'C:/Users/aZhen/Desktop/3931 individual project/data/failed_processedData_NullProcessed_allNullDeleted.csv'
pathS2 = 'C:/Users/aZhen/Desktop/3931 individual project/data/unfailed_processedData_withNulls_NullProcessed.csv'
pathS21 = 'C:/Users/aZhen/Desktop/3931 individual project/data/unfailed_processedData_withNulls_NullProcessed_allNullDeleted.csv'
'''

ratenum = 1
rate = ['1-1/', '1-10/']
failnum = 1
isfailed = ['un','']

path1 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull/MA1_' + isfailed[failnum]+'failed_processedData.csv'
path2 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull/MA2_' + isfailed[failnum]+'failed_processedData.csv'
path3 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull/MB1_' + isfailed[failnum]+'failed_processedData.csv'
path4 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull/MB2_' + isfailed[failnum]+'failed_processedData.csv'
path5 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull/MC1_' + isfailed[failnum]+'failed_processedData.csv'
path6 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull/MC2_' + isfailed[failnum]+'failed_processedData.csv'
path11 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull_noNullLine/MA1_' + isfailed[failnum]+'failed_processedData.csv'
path21 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull_noNullLine/MA2_' + isfailed[failnum]+'failed_processedData.csv'
path31 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull_noNullLine/MB1_' + isfailed[failnum]+'failed_processedData.csv'
path41 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull_noNullLine/MB2_' + isfailed[failnum]+'failed_processedData.csv'
path51 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull_noNullLine/MC1_' + isfailed[failnum]+'failed_processedData.csv'
path61 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter_deleteNull_noNullLine/MC2_' + isfailed[failnum]+'failed_processedData.csv'


paths1= 'C:/Users/aZhen/Desktop/3931 individual project/data/1-1/divide_without_idfilter_deleteNull_noNullLine/special case/MC1_failed_processedData--.csv'
paths2= 'C:/Users/aZhen/Desktop/3931 individual project/data/1-1/divide_without_idfilter_deleteNull_noNullLine/special case/MC1_unfailed_processedData--.csv'
paths11= 'C:/Users/aZhen/Desktop/3931 individual project/data/1-1/divide_without_idfilter_deleteNull_noNullLine/special case/MC1_failed_processedData.csv'
paths21= 'C:/Users/aZhen/Desktop/3931 individual project/data/1-1/divide_without_idfilter_deleteNull_noNullLine/special case/MC1_unfailed_processedData.csv'
pathGroup1 = [path1, path2, path3, path4, path5, path6]
pathGroup2 = [path11, path21, path31, path41, path51, path61]

with open(paths2, 'r', newline='') as csvfile1:
    with open(paths21, 'w', newline='') as csvfile2:
        csv_reader = csv.reader(csvfile1)
        csv_writer = csv.writer(csvfile2)
        for row in csv_reader:
            if not row[0] == '-1':
                csv_writer.writerow(row)

'''
for i in range(6):
    with open(pathGroup1[i],'r', newline='') as csvfile1:
        with open(pathGroup2[i], 'w', newline='')as csvfile2:
            csv_reader = csv.reader(csvfile1)
            csv_writer = csv.writer(csvfile2)
            for row in csv_reader:
                if not row[0] == '-1':
                    csv_writer.writerow(row)
'''


