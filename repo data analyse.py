import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the data from a CSV file
# Assume your CSV has columns: login, full_name, created_at, stargazers_count, watchers_count, language, has_projects, has_wiki, license_name
data = pd.read_csv('repositories.csv')

# Convert has_projects and has_wiki to boolean
data['has_projects'] = data['has_projects'].astype(bool)
data['has_wiki'] = data['has_wiki'].astype(bool)

# Summary statistics
print(data.describe())

# Group by has_projects and has_wiki, and calculate the mean stars
project_wiki_summary = data.groupby(['has_projects', 'has_wiki'])['stargazers_count'].mean().reset_index()

# Rename columns for better understanding
project_wiki_summary.columns = ['Has Projects', 'Has Wiki', 'Average Stars']

# Print the summary DataFrame
print("\nSummary of Average Stars by Projects and Wiki Presence:")
print(project_wiki_summary)

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='Has Projects', y='Average Stars', hue='Has Wiki', data=project_wiki_summary)
plt.title('Impact of Projects and Wikis on Repository Stars')
plt.xlabel('Has Projects')
plt.ylabel('Average Stars')
plt.legend(title='Has Wiki', loc='upper right')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()

# Statistical Tests
# Perform ANOVA to check if there are significant differences in stars
anova_results = stats.f_oneway(
    data[data['has_projects'] == True][data['has_wiki'] == True]['stargazers_count'],
    data[data['has_projects'] == True][data['has_wiki'] == False]['stargazers_count'],
    data[data['has_projects'] == False][data['has_wiki'] == True]['stargazers_count'],
    data[data['has_projects'] == False][data['has_wiki'] == False]['stargazers_count']
)

print(f'ANOVA Results: F-statistic={anova_results.statistic}, p-value={anova_results.pvalue}')
