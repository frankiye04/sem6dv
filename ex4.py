import pandas as pd
# Creating a dataset with missing values
data = {
 'Name': ['Arun', 'Babu', 'Chitra', 'Divya', 'Elango'],
 'Age': [21, 22, None, 23, 22],
 'Marks': [85, None, 75, 88, 90]
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
# Identifying missing values
print("\nMissing Value Check:")
print(df.isnull())
# Filling missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print("\nDataset After Filling Missing Values:")
print(df)
