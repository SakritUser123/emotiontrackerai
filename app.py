import streamlit as st
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import pickle
# Add a button to Streamlit

# Load the pre-trained model
with open('LogisticRegModel.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
with open('WorkVector.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

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

        # Predict using the loaded model (unchanged logic)
        predictions = loaded_model.predict_proba(vectorizer.transform([user_input]))[0][1]
        
        import streamlit as st

         # Free sample MP3
        import streamlit as st

# List of online MP3 URLs
        happy_music = [
        "https://soundcloud.com/mozart/sets/mozart-piano-sonatas?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
        "https://soundcloud.com/katyakramer-lapin/sets/satie-debussy-beethoven-bach?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
        "https://soundcloud.com/larah-armstrong-342920891/sets/mozart-for-study-stay-in-the?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
        "https://soundcloud.com/focusmusicconsord/sets/bach-beethoven-mozart-for?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
        "https://soundcloud.com/friendlythug/happy-new-year?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"# WAV but works
        
    ]






        emotion = "The Decimal Given Is How Sure The Model Thinks The statement is positive if the decimal is greater than 0.50 then, it is more likely to be positive!"
        emotion_response = predictions 
        emoji = ''
        if emotion_response > 0.50:
            emoji = '😊'
        if emotion_response < 0.50:
            emoji = '😔'
        if emotion_response == 0.50:
            emoji = '🤔'
            
        
        
        
        import random
        
            
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(emotion)
            st.markdown(emotion_response)
            st.markdown(emoji)
            
            
        if predictions > 0.50:
            random_song = random.choice(happy_music)
            st.audio(random_song)

        # Store assistant response in chat history
        st.session_state.messages.append({"role": "assistant", "content": emotion_response})



