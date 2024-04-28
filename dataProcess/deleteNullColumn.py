import pandas as pd

path1 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter/MA1_unfailed_processedData.csv'
path2 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter/MA2_unfailed_processedData.csv'
path3 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter/MB1_unfailed_processedData.csv'
path4 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter/MB2_unfailed_processedData.csv'
path5 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter/MC1_unfailed_processedData.csv'
path6 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter/MC2_unfailed_processedData.csv'
path11 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MA1_unfailed_processedData.csv'
path21 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MA2_unfailed_processedData.csv'
path31 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MB1_unfailed_processedData.csv'
path41 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MB2_unfailed_processedData.csv'
path51 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MC1_unfailed_processedData.csv'
path61 = 'C:/Users/aZhen/Desktop/3931 individual project/data/divide_without_idfilter_deleteNull/MC2_unfailed_processedData.csv'
pathS1 = 'C:/Users/aZhen/Desktop/3931 individual project/data/failed_processedData_NullProcessed.csv'
pathS11 = 'C:/Users/aZhen/Desktop/3931 individual project/data/failed_processedData_NullProcessed_allNullDeleted.csv'
pathS2 = 'C:/Users/aZhen/Desktop/3931 individual project/data/unfailed_processedData_withNulls_NullProcessed.csv'
pathS21 = 'C:/Users/aZhen/Desktop/3931 individual project/data/unfailed_processedData_withNulls_NullProcessed_allNullDeleted.csv'

pathGroup1 = [path1, path2, path3, path4, path5, path6]
pathGroup2 = [path11, path21, path31, path41, path51, path61]

for i in range (6):

    num = i

    df = pd.read_csv(pathGroup1[num])
    for column in df.columns:
        if df[column].eq(-1).all():
            df.drop(column, axis=1, inplace=True)

    df.to_csv(pathGroup2[num],index=False)


