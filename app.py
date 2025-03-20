import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

# Load the pre-trained model
with open('emotions.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Initialize the vectorizer
vectorizer = TextVectorization(max_tokens=50, output_mode='int')

# Streamlit UI
st.title("Emotion Analyzer AI")
st.write("Enter text below to analyze emotions.")

# Create a form for user input
with st.form(key="emotion_form"):
    user_input = st.text_area("Enter your text here:")
    submit_button = st.form_submit_button(label="Analyze Emotion")

# Process input when button is clicked
if submit_button:
    if not user_input.strip():
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        # Adapt the vectorizer to the user input
        user_input_list = [user_input]  # TextVectorization expects a list
        vectorizer.adapt(user_input_list)  # Train vectorizer on input

        # Vectorize the input text
        vectorized_texts = vectorizer(user_input_list)

        # Predict using the loaded model
        predictions = loaded_model.predict(vectorized_texts)

        # Apply threshold and generate binary labels
        threshold = 0.25
        bin_labels = (predictions >= threshold).astype(int)
        labels_text = ['positive' if label == 1 else 'negative' for label in bin_labels.flatten()]

        # Display the result
        st.subheader("Prediction:")
        st.write(f"🔹 **Emotion:** {labels_text[0]}")
