        st.session_state.user_input = ""  # Clear input after sendingpip install --upgrade pip setuptools wheel

st.text_input("You:", key="user_input", on_change=respond)

with st.expander(" Chat History", expanded=True):
    for speaker, message in st.session_state.chat_history:
        st.markdown(f"**{speaker}:** {message}")