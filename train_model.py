import pandas as pd
import joblib
import string
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("career_guidance_dataset.csv")

# Preprocessing function
def preprocess(text):
    text = text.lower()
    return ''.join([char for char in text if char not in string.punctuation])

# Clean the questions
df["cleaned_question"] = df["question"].apply(preprocess)

# Fit TF-IDF on questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned_question"])

# Save vectorizer and dataframe
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(df, "qa_dataframe.pkl")

print("✅ Vectorizer and QA DataFrame saved!")