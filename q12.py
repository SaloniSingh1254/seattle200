import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('users.csv')

# Convert hireable values to boolean to handle cases where hireable might be True/False or 'true'/'false' as strings
df['hireable'] = df['hireable'].astype(str).str.lower() == 'true'

# Calculate the average following for hireable and non-hireable users
hireable_avg_following = df[df['hireable'] == True]['following'].mean()
non_hireable_avg_following = df[df['hireable'] == False]['following'].mean()

# Calculate the difference
difference = hireable_avg_following - non_hireable_avg_following

# Print the result
print(f"Difference in average following (hireable - non-hireable): {difference:.3f}")
