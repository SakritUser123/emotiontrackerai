import streamlit as st
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization
import pickle
# Add a button to Streamlit


tabs = ["Home","Smaller Emotion","Larger Emotion"]
selected_tab = st.sidebar.radio("Select A Model",tabs)
if selected_tab == "Home":
    st.title("Home Page")
    st.write("Use The navigation bar to navigate the various models on the website!")
    


    st.write("You can donate to this website it will help out a lot!")
    st.markdown("""
---
Contact: [veerendrasakthi.prabhurajan@gmail.com]  
GitHub: [The repository for this website!](https://github.com/SakritUser123/E-COLI-AI-Detector)
""")
if selected_tab == 'Smaller Emotion':
    # Load the pre-trained model
    with open('LogisticRegModel.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    with open('WorkVector.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    
    # Set up Streamlit UI
    st.set_page_config(page_title="Emotion Analyzer AI", page_icon="😃")
    st.title("💬 Emotion Analyzer AI")
    st.link_button("💻 Pay $3 on Venmo 🤖😊", "https://venmo.com/SakritUser123?txn=pay&amount=3")
    st.sidebar.title("Models")
    
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
    
            emotion = "The Decimal Given Is How Sure The Model Thinks The statement is positive if the decimal is greater than 0.50 then, it is more likely to be positive!"
            emotion_response = predictions 
            emoji = ''
            res = ''
            if emotion_response > 0.50:
                emoji = '😊'
                res = 'Wow! That is great to hear.You can listen to this song to match your emotion.'
            if emotion_response < 0.50:
                emoji = '😔'
                res = 'Oh no! Thats sad to hear .You can feel better be feeling this song that matches your emotion!'
            if emotion_response == 0.50:
                emoji = '🤔'
                
                
            
            
                
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(emotion)
                st.markdown(emotion_response)
                st.markdown(emoji)
                st.markdown(res)
                
            
    
            # Store assistant response in chat history
            st.session_state.messages.append({"role": "assistant", "content": emotion_response})
    


