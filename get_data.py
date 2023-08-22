import pandas as pd
import csv
import os 
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

serial_number = input("SN: ")
file_name = input("File Name: ")

os.getcwd()

airpods = pd.read_csv(file_name)
df = pd.read_csv(file_name)
df_filtered = df[df['Serial Number'].str.contains(serial_number)]
df_filtered = df_filtered[(df_filtered['Input Device'] == 'Channel 4')]
# print(df_filtered)
df_filtered.to_csv('my_file.csv', index=False)
column_indices = np.r_[0:4, 6:110]
df_between = df_filtered.iloc[:, column_indices]
print(df_between)
column_indices = np.r_[0:4, 6:110]

df_between.to_csv("less_col.csv", index=False)

# open the csv file for reading
with open('less_col.csv', 'r') as file:

    # create a csv reader object
    csv_reader = csv.reader(file)

    # create a list to store the rows
    rows = []

    # iterate over each row in the csv file
    for row in csv_reader:

        # append the row to the rows list
        rows.append(row)

# get specific rows and columns

selected_rows = rows[1:4]  # get rows 2-4 (index starts at 0)
selected_cols = [row[2] for row in rows]  # get column 3 (index starts at 0)
list1 = selected_rows[0][4:]
list2 = selected_rows[1][4:]
list3 = selected_rows[2][4:]
floatList1 = []
floatList2 = []
floatList3 = []
for i in list1:
	floatList1.append(float(i))

for i in list2:
	floatList2.append(float(i))

for i in list3:
	floatList3.append(float(i))


	


	# print the selected rows and columns
	# print(selected_cols)

# use zip to iterate over the lists simultaneously and add the elements
sums = [sum(values) for values in zip(floatList1, floatList2, floatList3)]

# calculate the averages by dividing the sums by the number of lists
averages = [s / 3 for s in sums]

# print the averages
print(serial_number,': ',averages)

