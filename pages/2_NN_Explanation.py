import streamlit as st

st.title("Neural Network Model Explanation")

st.markdown("""
## 1. Dataset

The same IMDB dataset is used for Neural Network training.

After preprocessing and TF-IDF transformation, the feature vectors are used as input to the neural network.

---

## 2. Neural Network Architecture

The model architecture:

- Dense layer (128 units, ReLU activation)
- Dropout (0.3)
- Dense layer (64 units, ReLU activation)
- Output layer (1 unit, Sigmoid activation)

---

## 3. Theory

Neural Networks are inspired by biological neurons.
Each Dense layer performs:

Output = Activation(Wx + b)

ReLU activation introduces non-linearity.
Sigmoid activation is used for binary classification.

---

## 4. Training Configuration

- Optimizer: Adam
- Loss Function: Binary Crossentropy
- Epochs: 5
- Batch size: 32

Adam optimizer combines RMSProp and Momentum techniques.

Binary crossentropy is suitable for binary classification problems.

---

## 5. Model Development Steps

1. Preprocess text data
2. Convert text to TF-IDF vectors
3. Split data into train/test sets
4. Build neural network architecture
5. Compile model
6. Train model
7. Evaluate model performance

---

## 6. References

- TensorFlow Documentation: https://www.tensorflow.org
- Deep Learning Book – Ian Goodfellow
- Kaggle IMDB Dataset
""")