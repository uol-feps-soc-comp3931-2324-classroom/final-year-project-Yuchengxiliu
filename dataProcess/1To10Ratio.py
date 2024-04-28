import csv
import os

ratenum = 1
rate = ['1-1/', '1-10/']
failnum = 1
isfailed = ['un','']

path1 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MA1_' + isfailed[0]+'failed_processedData.csv'
path2 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MA2_' + isfailed[0]+'failed_processedData.csv'
path3 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MB1_' + isfailed[0]+'failed_processedData.csv'
path4 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MB2_' + isfailed[0]+'failed_processedData.csv'
path5 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MC1_' + isfailed[0]+'failed_processedData.csv'
path6 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MC2_' + isfailed[0]+'failed_processedData.csv'
path11 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MA1_' + isfailed[1]+'failed_processedData.csv'
path21 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MA2_' + isfailed[1]+'failed_processedData.csv'
path31 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MB1_' + isfailed[1]+'failed_processedData.csv'
path41 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MB2_' + isfailed[1]+'failed_processedData.csv'
path51 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MC1_' + isfailed[1]+'failed_processedData.csv'
path61 = 'C:/Users/aZhen/Desktop/3931 individual project/data/' + rate[ratenum] + 'divide_without_idfilter/MC2_' + isfailed[1]+'failed_processedData.csv'

def count_needed_rows(num):
    while(num%7 != 1):
        num+=1
    return num


def count_csv_rows(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        return sum(1 for row in csv.reader(csvfile))


def equalize_csv_rows_1_1(file_path1, file_path2):
    # 计算两个文件的行数
    count1 = count_csv_rows(file_path1)
    count2 = count_csv_rows(file_path2)

    # 确定哪个文件行数较多
    if count1 > count2:
        # 删除file1的多余行
        remove_extra_rows(file_path1, count2)
    elif count2 > count1:
        # 删除file2的多余行
        remove_extra_rows(file_path2, count1)


def remove_extra_rows(file_path, num_rows_to_keep):
    # 读取文件内容
    with open(file_path, 'r', newline='') as csvfile:
        reader = list(csv.reader(csvfile))

    # 只保留需要的行数
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(reader[:num_rows_to_keep])

def remove1_10(file_path):
    count = count_csv_rows(file_path)
    need = count_needed_rows(count//10)
    remove_extra_rows(file_path,need)




pathGroup1 = [path1, path2, path3, path4, path5, path6]
pathGroup2 = [path11, path21, path31, path41, path51, path61]
# 调用函数使两个CSV文件行数相同
# for i in range(6):
#     equalize_csv_rows_1_1(pathGroup1[i], pathGroup2[i])
for i in range(6):
    remove1_10(pathGroup2[i])
