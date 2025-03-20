import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

# Load the pre-trained model
with open('emotions.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Initialize the vectorizer
vectorizer = TextVectorization(max_tokens=50, output_mode='int')

# Page Title
st.set_page_config(page_title="Emotion Analyzer AI", page_icon="😃")
st.title("💬 Emotion Analyzer AI")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Field
user_input = st.chat_input("Enter your text here...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    if user_input.strip():
        # Vectorize the input text
        user_input_list = [user_input]
        vectorizer.adapt(user_input_list)  # Train vectorizer on input
        vectorized_texts = vectorizer(user_input_list)

        # Predict using the model
        predictions = loaded_model.predict(vectorized_texts)
        threshold = 0.25
        bin_labels = (predictions >= threshold).astype(int)
        labels_text = ['positive' if label == 1 else 'negative' for label in bin_labels.flatten()]
        emotion_response = f"**Emotion:** {labels_text[0]} 😊" if labels_text[0] == "positive" else f"**Emotion:** {labels_text[0]} 😢"

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(emotion_response)

        # Save assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": emotion_response})

