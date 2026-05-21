import streamlit as st
import pickle
import re

from nltk.corpus import stopwords

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open('fake_news_model.pkl', 'rb'))

vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# ---------------- CLEAN FUNCTION ---------------- #

def clean_text(text):

    string = ""

    text = text.lower()

    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)

    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", " ", text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^A-Za-z0-9]+', ' ', text)

    for word in text.split():

        if word not in stopwords.words('english'):
            if word not in string:
                string += word + " "

    return string

# ---------------- UI ---------------- #

st.title("Fake News Detection NLP Project")

st.write("Enter News Article Text Below")

news = st.text_area("News Text")

if st.button("Predict"):

    cleaned_news = clean_text(news)

    vector_input = vectorizer.transform([cleaned_news])

    prediction = model.predict(vector_input)

    if prediction[0] == 1:
        st.error("Fake News")
    else:
        st.success("Real News")