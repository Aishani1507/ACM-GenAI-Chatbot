# ACM-GenAI-Chatbot
Name:Aishani Kapoor
Id: 2025A3RM2259H

I have created a chatbot that can talk consistensively with the user
It has 3 personnas:
*RoastBot:* Always responds with witty or sarcastic roasts, no matter what the user says.
*ShakespeareBot:* Responds to all queries in old-English, Shakespeare-style prose.
*Emoji Translator Bot:* Converts everything into emoji-speak.
Conversation memory using LangChain
Clean and interactive Streamlit UI

Libraries Used
streamlit
langchain
langchain_groq
python-dotenv
(Kindly please install them before running the code)

The app uses LangChain's LLMChain with ConversationBufferMemory to maintain chat history.
A persona-specific instruction is put into the prompt template.
The selected persona alters the bot's tone and style accordingly.
Chat history is stored in st.session_state for display.


##To run the program please use the commond
For Apple Use: streamlit run /location of file
Eg: streamlit run /Users/apple/Downloads/bot/chatbot.py
For Windows Use: python -m streamlit run chatbot.py
