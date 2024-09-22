
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_H = pd.read_csv('ddinter_downloads_code_H.csv')
data_D = pd.read_csv('ddinter_downloads_code_D.csv')
data_B = pd.read_csv('ddinter_downloads_code_B.csv')
data_A = pd.read_csv('ddinter_downloads_code_A.csv')

# Combine all datasets into a single DataFrame
combined_data = pd.concat([data_H, data_D, data_B, data_A], ignore_index=True)

# 1. Distribution of Drug Interaction Severity Levels
plt.figure(figsize=(8,6))
sns.countplot(data=combined_data, x='Level', order=['Minor', 'Moderate', 'Major'])
plt.title('Distribution of Drug Interaction Severity Levels')
plt.xlabel('Interaction Severity')
plt.ylabel('Count')
plt.savefig('figure_1.png')

# 2. Top 10 Most Frequent Drugs (Drug_A) Involved in Interactions
top_10_drug_A = combined_data['Drug_A'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_10_drug_A.values, y=top_10_drug_A.index, palette="viridis")
plt.title('Top 10 Most Frequent Drugs (Drug_A) Involved in Interactions')
plt.xlabel('Number of Occurrences')
plt.ylabel('Drug_A')
plt.savefig('figure_2.png')

# 3. Distribution of Interaction Severity Levels for Top 10 Drugs (Drug_A)
top_drug_A = combined_data['Drug_A'].value_counts().head(10).index.tolist()
plt.figure(figsize=(12,8))
sns.countplot(data=combined_data[combined_data['Drug_A'].isin(top_drug_A)], x='Drug_A', hue='Level', order=top_drug_A, palette="Set2")
plt.title('Distribution of Interaction Severity Levels for Top 10 Drugs (Drug_A)')
plt.xlabel('Drug_A')
plt.ylabel('Count of Interactions')
plt.savefig('figure_3.png')

print("Figures saved as figure_1.png, figure_2.png, figure_3.png")
