import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(
    page_title="MindCare AI",
    page_icon="🧠",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 MindCare AI")
st.subheader("Mental Wellness Support Chatbot")

# Sidebar
with st.sidebar:

    st.header("About")

    st.write("""
    MindCare AI provides emotional support,
    stress management tips, and motivational guidance.
    """)

    st.warning("This chatbot is not a medical professional.")

    # Daily motivation
    if st.button("Daily Motivation"):

        st.success(
            "Believe in yourself. Small progress is still progress."
        )

    # Clear chat
    if st.button("Clear Chat"):

        st.session_state.messages = []

# Initialize chat history
if "messages" not in st.session_state:

    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# User input
user_input = st.chat_input(
    "Share your thoughts here..."
)

# When user sends message
if user_input:

    # Display user message
    st.chat_message("user").markdown(user_input)

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Generate AI response
    with st.spinner("MindCare AI is thinking..."):

        response = get_response(
            user_input,
            st.session_state.messages
        )

    # Display AI response
    with st.chat_message("assistant"):

        st.markdown(response)

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })