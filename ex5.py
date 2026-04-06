import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Sample Data
data = {
 'Student': ['A', 'B', 'C', 'D', 'E'],
 'Marks1': [78, 85, 92, 74, 88],
 'Marks2': [82, 79, 90, 69, 85]
}
df = pd.DataFrame(data)
# Scatter Plot
plt.scatter(df['Marks1'], df['Marks2'])
plt.title("Scatter Plot - Marks1 vs Marks2")
plt.xlabel("Marks1")
plt.ylabel("Marks2")
plt.show()
# Bar Chart
plt.bar(df['Student'], df['Marks1'])
plt.title("Bar Chart - Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks1")
plt.show()
# Pie Chart
plt.pie(df['Marks1'], labels=df['Student'], autopct='%1.1f%%')
plt.title("Pie Chart - Percentage of Marks")
plt.show()
# Pair Plot
sns.pairplot(df)
plt.show()
