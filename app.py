
import streamlit as st
import joblib

# Load the trained machine learning model
data = joblib.load("spam_detector.pkl")

model = data["model"]
tfidf = data["tfidf"]

# Website configuration
st.set_page_config(
    page_title="Spam Email Detector",
    page_icon="📧",
    layout="centered"
)

# Website title
st.title("📧 Spam Email Detector")
st.write("Check whether an email is Spam or Genuine (Ham).")

# Email input
email_text = st.text_area(
    "Enter your email message below:",
    height=200,
    placeholder="Paste your email content here..."
)

# Prediction button
if st.button("Check Email"):
    if email_text.strip():
        # Convert email into numerical features
        email_tfidf = tfidf.transform([email_text])

        # Predict email category
        prediction = model.predict(email_tfidf)[0]

        # Display result
        if prediction == 1:
            st.error("🚨 This email is SPAM!")
        else:
            st.success("✅ This email is GENUINE (HAM)!")

        # Show prediction confidence
        probabilities = model.predict_proba(email_tfidf)[0]
        confidence = probabilities[int(prediction)] * 100

        st.write(f"Prediction confidence: **{confidence:.2f}%**")
    else:
        st.warning("Please enter an email message first.")

st.caption("Note: Predictions are not a guarantee. Always be careful with suspicious emails and links.")
