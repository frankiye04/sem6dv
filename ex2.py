import pandas as pd
# Creating a sample dataset
data = {
 'Name': ['Asha', 'Balu', 'Cathy', 'David', 'Elan', 'Faruk'],
 'Department': ['CSE', 'ECE', 'CSE', 'EEE', 'ECE', 'CSE'],
 'Mark': [85, 78, 92, 66, 74, 88],
 'Age': [19, 20, 19, 21, 20, 19]
}
df = pd.DataFrame(data)
# Display DataFrame
print("DataFrame:")
print(df)
# Information about dataset
print("\nInfo:")
print(df.info())
# Shape of dataset
print("\nShape of DataFrame:")
print(df.shape)
# First 5 rows
print("\nHead:")
print(df.head())
# Last 5 rows
print("\nTail:")
print(df.tail())
# Data types of columns
print("\nData Types:")
print(df.dtypes)
# Statistical description
print("\nDescribe:")
print(df.describe())
# Grouping data based on Department
print("\nGroup by Department (Average Marks):")
print(df.groupby('Department')['Mark'].mean())
##Sample Output (Expected):
DataFrame:
 Name Department Mark Age
0 Asha CSE 85 19
1 Balu ECE 78 20
2 Cathy CSE 92 19
3 David EEE 66 21
4 Elan ECE 74 20
5 Faruk CSE 88 19
