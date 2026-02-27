import os

from main import Chatbot
import streamlit as st
    
st.set_page_config(page_title="Random Fortune Telling Bot")
with st.sidebar:
    st.title('Random Fortune Telling Bot')

apikey = st.text_input("Plz give your Groq API Key", type="password")

try:
    if apikey and apikey.strip():
        bot = Chatbot(api_key=apikey)
except Exception as e:
    st.text(f"Plz enter your API key to initialize the bot.")

def generate_response(input):
    if bot and input.strip():
        result = bot.rag_chain.invoke(input)
        return result
    else:
        return "Please enter your API key and a question."

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, let's unveil your future"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Getting your answer from mystery stuff.."):
            response = generate_response(input) 
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)