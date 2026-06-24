import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# ---------------- UI ----------------
st.set_page_config(page_title="Spam Detector", layout="wide")

st.title("🚀 Spam Detection AI")
st.write("Modern UI • Interactive Graphs • History Tracking")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("sms.tsv", sep='\t', names=['label', 'message'])

# ---------------- PREVIEW ----------------
st.subheader("📂 Dataset Preview")
st.write(df.head())

# ---------------- PREPROCESS ----------------
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['message'])
y = df['label']

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ----------------
model = MultinomialNB()
model.fit(X_train, y_train)

# ---------------- ACCURACY ----------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.subheader("📊 Model Accuracy")
st.success(f"{accuracy:.2f}")

# ---------------- CONFUSION MATRIX ----------------
st.subheader("🧠 Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig_cm = ff.create_annotated_heatmap(
    z=cm,
    x=["Predicted Ham", "Predicted Spam"],
    y=["Actual Ham", "Actual Spam"],
    colorscale='Blues'
)

st.plotly_chart(fig_cm, use_container_width=True)

# ---------------- INTERACTIVE GRAPHS ----------------
st.subheader("📊 Data Insights")

col1, col2 = st.columns(2)

counts = df['label'].value_counts().reset_index()
counts.columns = ['label', 'count']

# PIE CHART
with col1:
    st.markdown("### 🥧 Spam vs Ham")
    fig_pie = px.pie(counts, names='label', values='count', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

# BAR CHART
with col2:
    st.markdown("### 📊 Count Comparison")
    fig_bar = px.bar(counts, x='label', y='count')
    st.plotly_chart(fig_bar, use_container_width=True)

# ---------------- HISTORY STORAGE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- USER INPUT ----------------
st.subheader("✍️ Test Your Message")

user_input = st.text_input("Enter a message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        msg_vec = vectorizer.transform([user_input])
        result = model.predict(msg_vec)[0]

        # Save to history
        st.session_state.history.append({
            "message": user_input,
            "result": result
        })

        if result == 'spam':
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is NOT spam!")

# ---------------- SHOW HISTORY ----------------
st.subheader("🕒 Prediction History")

if len(st.session_state.history) == 0:
    st.info("No history yet")
else:
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)

    if st.button("Clear History"):
        st.session_state.history = []
        st.success("History cleared!")