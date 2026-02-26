import streamlit as st

st.title("Machine Learning Model Explanation")

st.markdown("""
## 1. Dataset Source
The IMDB Dataset was downloaded from Kaggle:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

The dataset contains 50,000 movie reviews labeled as positive or negative.

---

## 2. Dataset Features
- review: Text review of the movie
- sentiment: Target label (positive / negative)

This dataset is unstructured text data.

---

## 3. Data Preparation Process

The dataset required preprocessing because raw text contains noise.

Steps:
1. Remove HTML tags
2. Convert text to lowercase
3. Remove punctuation
4. Remove extra whitespace
5. Convert sentiment labels into binary (0 = negative, 1 = positive)
6. Apply TF-IDF vectorization (5000 features)

TF-IDF converts text into numerical feature vectors.

---

## 4. Machine Learning Ensemble Model

This project uses an Ensemble Learning approach combining three different models:

- Logistic Regression
- Multinomial Naive Bayes
- Linear Support Vector Machine (SVM)

These models are combined using Hard Voting.

### Why Ensemble?
Ensemble learning improves performance by combining multiple classifiers to reduce variance and bias.

---

## 5. Training Process

- Data split: 80% training / 20% testing
- Vectorization using TF-IDF
- Model training using Scikit-learn
- Evaluation using Accuracy score

---

## 6. References

- Scikit-learn Documentation: https://scikit-learn.org
- Kaggle IMDB Dataset
- Jurafsky & Martin, Speech and Language Processing
""")