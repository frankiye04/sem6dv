# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset (example data)
data = {
 'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
 'Value': [10, 12, 15, 13, 17]
}
df = pd.DataFrame(data)
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
# Set 'Date' as index
df.set_index('Date', inplace=True)
# Plot the time series data
plt.figure(figsize=(10,5))
plt.plot(df.index, df['Value'], marker='o', linestyle='-', color='b')
plt.title('Time Series Data Visualization')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
