# Fake News Detection using NLP and Machine Learning

## Overview

This project is a **Fake News Detection System** built using **Natural Language Processing (NLP)** and **Machine Learning**.  
The model analyzes news article text and predicts whether the news is **Fake** or **Real**.

The project uses:
- Text preprocessing techniques
- TF-IDF Vectorization
- Logistic Regression
- Streamlit Web Application

---

## Features

- News text preprocessing using NLP
- Stopwords removal
- Text cleaning using Regular Expressions
- TF-IDF feature extraction
- Machine Learning based classification
- Interactive Streamlit web application
- Real-time Fake/Real prediction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- SpaCy
- Streamlit
- Matplotlib
- Seaborn

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing
4. Stopword Removal
5. TF-IDF Vectorization
6. Train-Test Split
7. Logistic Regression Model Training
8. Model Evaluation
9. Streamlit Deployment

---

## Dataset

The dataset contains:
- Fake News Articles
- Real News Articles

Files used:
- `Fake.csv`
- `True.csv`

---

## Project Structure

```text
Fake_News_Detection_NLP/
│
├── DATA/
│   ├── Fake.csv
│   └── True.csv
│
├── Notebook/
│   └── Fake_news_Detect_NLP.ipynb
│
├── app.py
├── main.py
├── fake_news_model.pkl
├── tfidf_vectorizer.pkl
└── README.md
```

## Streamlit Web App
The project includes an interactive Streamlit web application where users can:
Enter any news article text
Predict whether the news is Fake or Real
Get instant classification results

## Author 
Vedant Uplap
