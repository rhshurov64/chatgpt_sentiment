import pandas as pd
from textblob import TextBlob

# Read the dataset from the file
data = pd.read_csv('clean_data.csv')

# Remove rows with missing values in the 'content' column
data = data.dropna(subset=['content'])

# Apply sentiment analysis to the 'content' column
data['sentiment'] = data['content'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Map sentiment scores to labels
data['labels'] = data['sentiment'].apply(lambda x: 'good' if x >= 0.2 else ('bad' if x <= -0.2 else 'neutral'))

# Select only the 'content' and 'labels' columns
data = data[['content', 'labels','like_count','retweet_count']]

# Save the results to a new file
data.to_csv('sentiment_analysis_results.csv', index=False)


print("Success")