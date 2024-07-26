import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set font to Arial
plt.rcParams['font.family'] = 'Arial'

# Read CSV file
df = pd.read_csv('database.csv')

# Extract columns for correlation analysis
data_for_analysis = df.iloc[:, 1:]

# Calculate Pearson correlation matrix
correlation_matrix = data_for_analysis.corr(method='pearson')

# Print correlation matrix
print(correlation_matrix)

# Visualize correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', linewidths=.5)
plt.title('Pearson Correlation Matrix', fontsize=16)
plt.xticks(fontsize=10, rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.tight_layout() 
plt.show()
