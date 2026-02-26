import streamlit as st
import joblib
import tensorflow as tf

st.title("Test Neural Network Model")

tfidf = joblib.load("tfidf.pkl")
model = tf.keras.models.load_model("neural_model.h5")

user_input = st.text_area("Enter your movie review:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a review before predicting.")
    else:
        vector = tfidf.transform([user_input]).toarray()
        prediction = model.predict(vector)

        if prediction[0][0] > 0.5:
            st.success("Positive Review")
        else:
            st.error("Negative Review")