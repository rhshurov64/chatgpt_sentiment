import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('sentiment_analysis_results.csv')

# Split the data into training and testing sets
X = data['content'][:10000]
y = data['labels'][:10000]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a random forest classifier
classifier = RandomForestClassifier()
classifier.fit(X_train_vectorized, y_train)

# Predict on the test set
y_pred = classifier.predict(X_test_vectorized)

# Generate classification report
report = classification_report(y_test, y_pred, output_dict=True)

# Save the predictions to a new file
data['predictions'] = classifier.predict(vectorizer.transform(data['content']))
data.to_csv('sentiment_analysis_results_with_predictions.csv', index=False)

# Save precision, recall, f1-score, accuracy, and support to another file
metrics_df = pd.DataFrame(report).transpose()
metrics_df.to_csv('classification_metrics.csv', index=True)


print("Success!")