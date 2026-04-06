import pandas as pd
# Load dataset
data = pd.read_csv("student_data.csv")
print("Original Dataset:")
print(data.head())
# Dropping useless variables
clean_data = data.drop(['Address', 'PhoneNumber'], axis=1)
print("\nDataset After Removing Useless Variables:")
print(clean_data.head())
#Output
Original Dataset:
 RollNo Name Age Marks Address PhoneNumber
0 101 Arun 20 87 Chennai 9876543210
1 102 Banu 21 78 Madurai 8765432109
2 103 Charles 20 67 Trichy 7654321098
