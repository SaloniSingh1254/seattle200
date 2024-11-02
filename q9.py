import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the CSV file into a DataFrame
df = pd.read_csv('users.csv')

# Select relevant columns and drop rows with missing values for public_repos and followers
df = df[['public_repos', 'followers']].dropna()

# Reshape the data for the regression model
X = df[['public_repos']]  # Independent variable
y = df['followers']       # Dependent variable

# Initialize and fit the regression model
model = LinearRegression()
model.fit(X, y)

# Get the slope (coefficient) of the regression line
slope = model.coef_[0]

# Print the slope rounded to 3 decimal places
print(f"Regression slope of followers on repos: {slope:.3f}")
