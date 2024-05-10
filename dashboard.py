import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
data = pd.read_csv('data.csv')

# Data preprocessing (if needed)
# For demonstration, let's assume we have columns 'x' and 'y'

# Create Matplotlib plots
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'])
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

# Create Plotly interactive plot
fig = px.scatter(data, x='x', y='y', title='Interactive Scatter Plot')
fig.show()
