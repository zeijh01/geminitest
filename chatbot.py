# st_chatbot.py
import google.generativeai as genai 
import streamlit as st

st.title("Gemini-Bot")

def load_model():
    genai.configure(api_key='AIzaSyDS8L-sX2WkwgBuDbr_6b0VbhzJQmbMVP8')
    model = genai.GenerativeModel('gemini-pro')
    print("model loaded...")
    return model

model = load_model()

#2차시

if "chat_session" not in st.session_state:    
    st.session_state["chat_session"] = model.start_chat(history=[]) 

for content in st.session_state.chat_session.history:
    with st.chat_message("ai" if content.role == "model" else "user"):
        st.markdown(content.parts[0].text)

if prompt := st.chat_input("메시지를 입력하세요."):    
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("ai"):
        response = st.session_state.chat_session.send_message(prompt)        
        st.markdown(response.text)
