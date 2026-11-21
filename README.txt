# 📧 Spam Email Detector

## About the Project
Spam Email Detector is a Machine Learning project that classifies email messages as Spam or Genuine (Ham).

It uses Natural Language Processing (NLP) and the Multinomial Naive Bayes algorithm to detect unwanted emails.

## Technologies Used
- Python
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Streamlit
- Joblib

## Dataset
The project uses the Combined Enron Spam/Ham Email Dataset from Kaggle.

## Model Performance
- Accuracy: **98.36%**
- Training emails: 24,076
- Testing emails: 6,019

## Features
- Enter email messages for checking
- Predict Spam or Genuine emails
- Display prediction confidence
- Simple web interface

## Project Structure
```text
Spam-Email-Detector/
├── spam_detector.pkl
├── app.py
├── requirements.txt
└── README.md
```

## How to Run Locally

1. Install Python.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

## Disclaimer
Predictions are not guaranteed. Always use caution when handling suspicious emails and links.

## Author
Machine Learning Project – Spam Email Detector
