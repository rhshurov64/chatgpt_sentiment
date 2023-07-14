import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
df = pd.read_csv("sentiment_analysis_results.csv")

# Step 2: Calculate the total number of tweets
total_tweets = len(df)

# Step 3: Calculate the total number of negative, positive, and neutral tweets
total_negative = len(df[df['labels'] == 'bad'])
total_positive = len(df[df['labels'] == 'good'])
total_neutral = len(df[df['labels'] == 'neutral'])

# Step 4: Calculate the total like count for negative, positive, and neutral tweets
total_like_negative = df[df['labels'] == 'bad']['like_count'].sum()
total_like_positive = df[df['labels'] == 'good']['like_count'].sum()
total_like_neutral = df[df['labels'] == 'neutral']['like_count'].sum()

# Step 5: Calculate the total retweet count for negative, positive, and neutral tweets
total_retweet_negative = df[df['labels'] == 'bad']['retweet_count'].sum()
total_retweet_positive = df[df['labels'] == 'good']['retweet_count'].sum()
total_retweet_neutral = df[df['labels'] == 'neutral']['retweet_count'].sum()

# Create a new DataFrame for the results
results_df = pd.DataFrame({
    'Total Tweets': [total_tweets],
    'Total Negative': [total_negative],
    'Total Positive': [total_positive],
    'Total Neutral': [total_neutral],
    'Total Like Count for Negative': [total_like_negative],
    'Total Like Count for Positive': [total_like_positive],
    'Total Like Count for Neutral': [total_like_neutral],
    'Total Retweet Count for Negative': [total_retweet_negative],
    'Total Retweet Count for Positive': [total_retweet_positive],
    'Total Retweet Count for Neutral': [total_retweet_neutral]
})

# Save the results to a new file
results_df.to_csv("sentiment_analysis_results_summary.csv", index=False)

print("Results saved to sentiment_analysis_results_summary.csv.")

# Bar Chart:
# Total tweet count for each sentiment
sentiments = ['Negative', 'Positive', 'Neutral']
tweet_counts = [total_negative, total_positive, total_neutral]

plt.bar(sentiments, tweet_counts)
plt.xlabel('Sentiment')
plt.ylabel('Tweet Count')
plt.title('Total Tweet Count by Sentiment')
plt.savefig('bar_chart.png')
plt.show()


# Pie Chart:
labels = ['Negative', 'Positive', 'Neutral']
sizes = [total_negative, total_positive, total_neutral]
colors = ['red', 'green', 'blue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Percentage of Tweets by Sentiment')
plt.savefig('pie_chart.png')
plt.show()

# Line Chart
x = ['Negative', 'Positive', 'Neutral']
y_likes = [total_like_negative, total_like_positive, total_like_neutral]
y_retweets = [total_retweet_negative, total_retweet_positive, total_retweet_neutral]

plt.plot(x, y_likes, label='Like Count')
plt.plot(x, y_retweets, label='Retweet Count')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Total Like and Retweet Count by Sentiment')
plt.legend()
plt.savefig('line_chart.png')
plt.show()


# Scatter Plot
x = ['Negative', 'Positive', 'Neutral']
y_likes = [total_like_negative, total_like_positive, total_like_neutral]
y_retweets = [total_retweet_negative, total_retweet_positive, total_retweet_neutral]
sizes = [total_negative, total_positive, total_neutral]

plt.scatter(x, y_likes, s=sizes, c='red', label='Like Count')
plt.scatter(x, y_retweets, s=sizes, c='blue', label='Retweet Count')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Total Like and Retweet Count by Sentiment')
plt.legend()
plt.savefig('scatter_plot.png')
plt.show()
