# Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Create sample dataset
data = pd.DataFrame({
 'Department': ['CSE','CSE','CSE','ECE','ECE','ECE','MECH','MECH','MECH'],
 'Marks': [75, 88, 90, 65, 70, 72, 80, 85, 78]
})
# Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x='Department', y='Marks', data=data)
plt.title("Boxplot of Marks by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.show()
# Violin Plot
plt.figure(figsize=(8,5))
sns.violinplot(x='Department', y='Marks', data=data)
plt.title("Violin Plot of Marks by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.show()
