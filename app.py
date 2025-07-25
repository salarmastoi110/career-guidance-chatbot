import streamlit as st
import joblib
import string
from sklearn.metrics.pairwise import cosine_similarity

# Load saved data
vectorizer = joblib.load("vectorizer.pkl")
df = joblib.load("qa_dataframe.pkl")

# Preprocessing function
def preprocess(text):
    text = text.lower()
    return ''.join([char for char in text if char not in string.punctuation])

# Streamlit UI
st.set_page_config(page_title="Career Chatbot", page_icon="🤖")
st.title("🎓Career Guidance Assistant🤖")
st.write("Developed by Salaar Mastoi | AI & Data Science Specialist")
st.write("Looking for career guidance? Ask your question below:")

user_input = st.text_input("Ask me anything about your career path:")

if user_input:
    cleaned_input = preprocess(user_input)
    user_vect = vectorizer.transform([cleaned_input])
    
    # Calculate similarity with all dataset questions
    dataset_vect = vectorizer.transform(df["cleaned_question"])
    similarities = cosine_similarity(user_vect, dataset_vect)

    # Find the most similar question
    top_index = similarities.argmax()
    best_answer = df.iloc[top_index]["answer"]

    st.success(f"📘 **Answer:** {best_answer}")