import streamlit as st
import joblib

st.title("Test Machine Learning Model")

model = joblib.load("ensemble_model.pkl")
tfidf = joblib.load("tfidf.pkl")

user_input = st.text_area("Enter your movie review:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a review before predicting.")
    else:
        vector = tfidf.transform([user_input])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.success("Positive Review")
        else:
            st.error("Negative Review")