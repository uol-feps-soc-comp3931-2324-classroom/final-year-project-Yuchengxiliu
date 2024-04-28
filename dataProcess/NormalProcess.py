import csv
import datetime
import itertools
import os


path1 = 'E:\individual project\\2019DATA\\20190101.csv'
path2 = 'E:\individual project\\2019DATA\\20190102.csv'
failpath = 'E:\individual project\\ssd_failure_label.csv'
faildata = []
num2 = []

import pandas as pd

# 加载损坏硬件列表
failure_df = pd.read_csv('E:/individual project/ssd_failure_label.csv')

# 将损坏硬件的ID存储在集合中以便快速查找
failure_ids_set = set(failure_df['disk_id'])

# 定义一个函数来检查ID是否在损坏列表中
def is_id_in_failure_list(check_id):
    return check_id in failure_ids_set


with open(failpath, 'r', newline='') as csvfile:
    # 创建CSV阅读器对象
    csv_reader = csv.reader(csvfile)

    # 逐行读取CSV内容并打印
    cont = 0
    for row in csv_reader:
        if cont != 0:
            faildata.append(row)
            pass
        cont += 1

contFail = 0
for i in faildata:
    contFail +=1
    print ('contFail= ',contFail)
    dateStr = ''
    for num in range(0, 10):
        if num != 4 and num != 7:
            dateStr += i[1][num]
    date = datetime.datetime.strptime(dateStr, '%Y%m%d')
    dates = []
    for j in range(7):
        previous_date = date - datetime.timedelta(days=j)
        dates.append(previous_date.strftime('%Y%m%d'))

    maindata = []
    findID = None
    findType = None
    for dateFileStr in dates:
        # print('row+1')
        contAdd = 0
        if dateFileStr[3] == '9':
            dataPath = 'E:\individual project\\2019DATA\\' + dateFileStr + '.csv'
        else:
            dataPath = 'E:\individual project\\2018DATA\\' + dateFileStr + '.csv'

        if not os.path.exists(dataPath):
            maindata.append(['null'])
        else:
            with open(dataPath, 'r', newline='') as csvfile:
                # 创建CSV阅读器对象
                csv_reader = csv.reader(csvfile)

                sliced_reader = itertools.islice(csv_reader, contFail, None)
                # 逐行读取CSV内容并打印
                for row in sliced_reader:
                    # if row[0] == i[2]:
                    # print('row2', row[2], '-----i0', i[0])
                    if row[0] == 'disk_id':
                        continue
                    if findID == None:
                        if not is_id_in_failure_list(row[0]):
                            findID = row[0]
                            findType = row[2]
                            maindata.append(row)
                            contAdd += 1
                    else:
                        if row[0] == findID and row[2] == findType:
                            maindata.append(row)
                            # print('added')
                            contAdd += 1
                if contAdd == 0:
                    maindata.append(['null'])

    processedDataPath = 'E:\individual project\\unfailed_processedData_withNulls.csv'

    with open(processedDataPath, 'a', newline='') as csvfile:
        # 创建CSV写入器对象
        csv_writer = csv.writer(csvfile)

        # 写入数据
        csv_writer.writerows(maindata)


# # print (dates)
#
# i = faildata[0]
# dateStr = ''
# for num in range(0, 10):
#     if num != 4 and num != 7:
#         dateStr += i[1][num]
# date = datetime.datetime.strptime(dateStr, '%Y%m%d')
# dates = []
# for j in range(7):
#     previous_date = date - datetime.timedelta(days=j)
#     dates.append(previous_date.strftime('%Y%m%d'))
#
# maindata = []
# for dateFileStr in dates:
#     # print('row+1')
#     contAdd = 0
#     if dateFileStr[3] == '9':
#         dataPath = 'E:\individual project\\2019DATA\\' + dateFileStr + '.csv'
#     else:
#         dataPath = 'E:\individual project\\2018DATA\\' + dateFileStr + '.csv'
#
#     with open(dataPath, 'r', newline='') as csvfile:
#         # 创建CSV阅读器对象
#         csv_reader = csv.reader(csvfile)
#         # 逐行读取CSV内容并打印
#         for row in csv_reader:
#             # if row[0] == i[2]:
#             # print('row2', row[2], '-----i0', i[0])
#             if row[0] == i[2] and row[2] == i[0]:
#                 maindata.append(row)
#                 # print('added')
#                 contAdd += 1
#         if contAdd == 0:
#             maindata.append(['null'])
#     processedDataPath = 'E:\individual project\\processedData.csv'
#
#
#     with open(processedDataPath, 'a', newline='') as csvfile:
#         # 创建CSV写入器对象
#         csv_writer = csv.writer(csvfile)
#
#         # 写入数据
#         csv_writer.writerows(maindata)