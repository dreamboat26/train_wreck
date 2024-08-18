from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

#Testing

load_dotenv()


# Set up the GEMINI API MODEL
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key='AIzaSyAhIOrkXfbcD_LP0uhxoDIYbjy8MMTTarA')
model = genai.GenerativeModel('gemini-pro')

# function to translate roles between Gemini-pro and streamlit
def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role
    
# initialize chat session in streamlit
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title('AI CHATBOT')

#display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

#User's question field
user_prompt = st.chat_input('Enter your Question')
if user_prompt:
    #add the users question to the chat
    st.chat_message('user').markdown(user_prompt)

    #get response from chatbot
    response = st.session_state.chat_session.send_message(user_prompt)

    #display the AI response
    with st.chat_message('assistant'):
        st.markdown(response.text)