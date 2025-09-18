# Import necessary libraries
import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv(find_dotenv())
# Using Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize  memory if not already present
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True, input_key="input")
    
# Initialize chat history for storing conversation logs
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# Set default persona if not already selected
if "persona" not in st.session_state:
    st.session_state.persona = "Default"
    
#Persona instructions
persona_prompt = {
    "RoastBot": "You are RoastBot, a sarcastic and witty chatbot who roasts everything the user says.",
    "ShakespeareBot": "You are ShakespeareBot, who speaks in poetic old-English prose.",
    "Emoji Translator Bot": "You are EmojiBot, who translates everything into emoji-speak.",
    "Default": "You are a helpful and friendly chatbot."
}
# language model 
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0.7
)
# Define the prompt template
template = """{persona_instruction}

Conversation history:
{history}
User: {input}
Bot:"""

prompt = PromptTemplate(
    input_variables=["persona_instruction", "history", "input"],
    template=template
)
# Create the LLM chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=st.session_state.memory
)

# Configure Streamlit page layout and title
st.set_page_config(page_title="Persona ChatBot", layout="centered")
st.title("Persona ChatBot")

# Sidebar for selecting  persona
with st.sidebar:
    st.header("Bot Settings")
    st.session_state.persona = st.selectbox(
        "Choose your Bot Persona:",
        ["Default", "RoastBot", "ShakespeareBot", "Emoji Translator Bot"]
    )
#  user input and generate bot response
def respond():
    user_input = st.session_state.user_input
    if user_input:
        response = chain.run({
            "input": user_input,
            "persona_instruction": persona_prompt[st.session_state.persona]
        })
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append((st.session_state.persona, response))
        st.session_state.user_input = ""
        
# Input field for user messages
st.text_input("You:", key="user_input", on_change=respond)

# Display chat history
with st.expander(" Chat History", expanded=True):
    for speaker, message in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {message}")
        
        
#To run the program please use the commond
#For Mac Use: streamlit run /location of file
# Eg: streamlit run /Users/apple/Downloads/bot/chatbot.py

#For windows Use: python -m streamlit run chatbot.py
