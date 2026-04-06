# Importing necessary library
import pandas as pd
# Import dataset
data = pd.read_csv("sample.csv")
# Display first five rows
print("Dataset Preview:")
print(data.head())
# Export dataset to new file
data.to_csv("output_dataset.csv", index=False)
print("Dataset exported successfully.")
#Sample Dataset (sample.csv)
Name,Department,Marks
Arun,CSE,85
Priya,ECE,90
Ravi,EEE,78
John,MECH,88
Meena,CIVIL,91
