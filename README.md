<h1 align="center">🎯 Career Chatbot - AI Career Guidance System</h1>

<p align="center">
An intelligent chatbot that helps students make smart career decisions based on their interests, skills, and preferences – all powered by <strong>Machine Learning</strong> & <strong>Streamlit</strong>.
</p>

---

## 🚀 Key Features
- 🤖 Predicts suitable careers based on user input
- 📄 Trained on a CSV dataset of career intents
- 🧠 Uses TF-IDF vectorizer and ML classifier
- 💬 Interactive and clean chatbot interface (Streamlit)
- 💾 Model and vectorizer saved for quick reuse
- 📊 Easy to extend with more career data

---

career_chatbot_project/
├── app.py
├── train_model.py
├── career_guidance_dataset.csv
├── intent_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md  ✅


## 🔧 Setup Instructions

### ✅ 1. Clone the Project

```bash
git clone https://github.com/salarmastoi110/career_chatbot_project

cd career_chatbot_project

✅ 2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate  # For Windows

✅ 3. Install Requirements
pip install -r requirements.txt

▶️ Run the Career Chatbot
streamlit run app.py

It will launch a web UI in your browser where you can enter career-related questions like:

What should I become if I love coding?
I enjoy designing – what career suits me?
Which field has a good future after FSC?


💡 Tech Stack
Tool	Purpose
Python 3.9+	Core Programming Language
Streamlit	Web UI
scikit-learn	ML Modeling (TF-IDF + Classifier)
Pandas	Data handling (CSV)
Pickle	Save ML model/vectorizer

🌐 Demo Screenshot
<p align="center"> <img src="Demo.PNG" alt="Career Chatbot Screenshot"> </p>


📬 Contact  Salar Mastoi
📧 salarhussainmastoi@gmail.com
🔗 GitHub | LinkedIn

<p align="center"><i>Made with 💡 to help students discover their dream careers.</i></p> ```
