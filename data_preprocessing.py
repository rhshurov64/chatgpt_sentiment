import pandas as pd
import re

# Read the dataset from the file
data = pd.read_csv('Twitter Jan Mar.csv')

# Convert 'content' column to string type
data['content'] = data['content'].astype(str)

# Clean the data
data['content'] = data['content'].apply(lambda x: re.sub(r'http\S+|www.\S+|pic.twitter.com\S+', '', x))  # Remove URLs
data['content'] = data['content'].apply(lambda x: re.sub(r'@[A-Za-z0-9]+', '', x))  # Remove usernames
data['content'] = data['content'].apply(lambda x: re.sub(r'#', '', x))  # Remove hashtags
data['content'] = data['content'].apply(lambda x: re.sub(r'\s+', ' ', x))  # Remove extra spaces
data['content'] = data['content'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))  # Remove symbols and characters except alphabets
data['content'] = data['content'].apply(lambda x: x.lower())  # Convert text to lowercase

# Remove duplicate values based on 'content' column
data.drop_duplicates(subset=['content'], keep='first', inplace=True)

# Save the cleaned data to another file
data.to_csv('clean_data.csv', index=False)

print("Success!")
