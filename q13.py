import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file into a DataFrame
df = pd.read_csv('users.csv')

# Drop rows without a bio
df = df[df['bio'].notna()]

# Calculate the word count for each bio
df['bio_word_count'] = df['bio'].str.split().str.len()

# Prepare the data for regression
X = df[['bio_word_count']]  # Independent variable (bio word count)
y = df['followers']         # Dependent variable (followers)

# Initialize and fit the regression model
model = LinearRegression()
model.fit(X, y)

# Get the slope (coefficient) of the regression line
slope = model.coef_[0]

# Print the slope rounded to 3 decimal places
print(f"Regression slope of followers on bio word count: {slope:.3f}")
