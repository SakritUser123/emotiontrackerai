import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization

# Load the pre-trained model
with open('emotions.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Initialize the vectorizer
vectorizer = TextVectorization(max_tokens=50, output_mode='int')

# Set up Streamlit UI
st.set_page_config(page_title="Emotion Analyzer AI", page_icon="😃")
st.title("💬 Emotion Analyzer AI")
st.link_button("💻 Pay $3 on Venmo 🤖😊", "https://venmo.com/SakritUser123?txn=pay&amount=3")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Field
user_input = st.chat_input("Enter your text here...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Store user message in chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    if user_input.strip():
        # Vectorize input text (unchanged logic)
        user_input_list = [user_input]
        vectorizer.adapt(user_input_list)  # Train vectorizer on input
        vectorized_texts = vectorizer(user_input_list)

        # Predict using the loaded model (unchanged logic)
        predictions = loaded_model.predict(vectorized_texts)
        threshold = 0.25
        bin_labels = (predictions >= threshold).astype(int)
        labels_text = ['positive' if label == 1 else 'negative' for label in bin_labels.flatten()]
        import streamlit as st

         # Free sample MP3
        import streamlit as st

# List of online MP3 URLs
        happy_music = [
        "https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav",  # WAV but works
        "https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav",
        "https://samplelib.com/lib/preview/mp3/sample-3s.mp3",
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Happy-Background-Music.mp3"
    ]






        
        emotion_response = f"**Emotion:** {labels_text[0]} I will play happy music now!😊 Here is the audio:" if labels_text[0] == "positive" else f"**Emotion:** {labels_text[0]} 😢"
        
        import random
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(emotion_response)
        if predictions >= threshold:
            random_song = random.choice(happy_music)
            st.audio(random_song)
            st.write(f"Now playing: [Click here to open]({random_song})")

        # Store assistant response in chat history
        st.session_state.messages.append({"role": "assistant", "content": emotion_response})


