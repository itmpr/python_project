import csv
import pandas as pd
import  numpy as np

#file_1 = 'DISGENET_ALLL.txt'
#file_2 = 'allf.eigenstratgeno'
#file_3 = 'output.csv'
file_1_rows = []
#file_2_rows = []

f = pd.read_csv('allf.eigenstratgeno', nrows=1)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

# print(f.head(10))

with open('allf.eigenstratgeno', newline='\n') as f:
    reader = csv.reader(f)
    file_1_rows.append(
        ['204', '205', '535', '1271', '2463', '2464', '2465', '3727', '4855', '7482', '7775', '10945', '11387', '12567',
         '12568'])
    i = 0
    for row in reader:
        i +=1
        try:
            # row = row[0].split('\t')
            #print(len(row),len(row[0]))
            #[[16389]]
            file_1_rows.append(
                [row[0][204], row[0][205],row[0][535], row[0][1271], row[0][2463], row[0][2464], row[0][2465], row[0][3727],
                 row[0][4855], row[0][7482], row[0][7775], row[0][10945], row[0][11387], row[0][12567], row[0][12568]])
        except Exception as e:
            print(i)
            file_1_rows.append(['None'])
            print(e)

# open the file in the write mode
with open('output', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for element in file_1_rows:
        writer.writerow(element)

exit(0)

#pd.set_option('display.max_columns', None)
# print('204')
# print(f.iloc[204])
# 233exit(0)
