# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
# ---------------- Heatmap ----------------
# Load Iris dataset
df = sns.load_dataset('iris')
# Compute correlation matrix only for numeric columns
corr = df.select_dtypes(include='number').corr()
# Plot Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap of Iris Dataset')
plt.show()
# ---------------- Treemap ----------------
# Load sample dataset for Treemap
df_treemap = px.data.tips() # Using Tips dataset
# Plot Treemap
fig = px.treemap(
 df_treemap,
 path=['day', 'sex'], # Hierarchy: day > sex
 values='total_bill', # Size of rectangles
 color='total_bill', # Color based on value
 color_continuous_scale='RdBu'
)
fig.update_layout(title='Treemap of Total Bill by Day and Sex')
fig.show()
# ---------------- Regression Plot ----------------
# Regression plot between 'sepal_length' and 'petal_length'
plt.figure(figsize=(8,6))
sns.regplot(x='sepal_length', y='petal_length', data=df, color='green')
plt.title('Regression Plot: Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()
