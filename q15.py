import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('users.csv')

# Convert hireable values to boolean
df['hireable'] = df['hireable'].astype(str).str.lower() == 'true'

# Calculate the total number of users in each category
total_hireable = df[df['hireable'] == True].shape[0]
total_non_hireable = df[df['hireable'] == False].shape[0]

# Calculate the number of users with email addresses in each category
email_hireable = df[df['hireable'] == True]['email'].notna().sum()
email_non_hireable = df[df['hireable'] == False]['email'].notna().sum()

# Calculate the fractions
fraction_hireable = email_hireable / total_hireable if total_hireable > 0 else 0
fraction_non_hireable = email_non_hireable / total_non_hireable if total_non_hireable > 0 else 0

# Calculate the difference
difference = fraction_hireable - fraction_non_hireable

# Print the result rounded to 3 decimal places
print(f"Difference in fractions of users with email (hireable - non-hireable): {difference:.3f}")
