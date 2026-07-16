import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

# ------------------ Load Environment ------------------ #

load_dotenv()

# ------------------ Model ------------------ #

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=1,
    max_tokens=20,
)

# ------------------ Page Config ------------------ #

st.set_page_config(
    page_title="AI Chat",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 AI Chat Assistant")

# ------------------ Session State ------------------ #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_mode" not in st.session_state:
    st.session_state.current_mode = "Funny"

# ------------------ Sidebar ------------------ #

with st.sidebar:

    st.header("⚙️ Settings")

    mode = st.selectbox(
        "Choose AI Mode",
        ["Angry", "Funny", "Sad"],
        index=["Angry", "Funny", "Sad"].index(st.session_state.current_mode),
    )

    if st.button("Start New Chat", use_container_width=True):

        st.session_state.current_mode = mode

        st.session_state.messages = [
            SystemMessage(
                content=f"you are {mode} ai agents and give answer according this behavior"
            )
        ]

        st.session_state.chat_history = []

        st.rerun()

# Initialize on first run
if not st.session_state.messages:
    st.session_state.messages = [
        SystemMessage(
            content=f"yoa are ${st.session_state.current_mode} ai agents and give answer according this behavior"
        )
    ]

# ------------------ Display Chat ------------------ #

for role, msg in st.session_state.chat_history:

    with st.chat_message(role):
        st.markdown(msg)

# ------------------ Chat Input ------------------ #

prompt = st.chat_input("Type your message...")

if prompt:

    if prompt.lower() == "exit":
        st.stop()

    # User message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.chat_history.append(("user", prompt))
    st.session_state.messages.append(HumanMessage(content=prompt))

    # AI Response
    result = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=result.content)
    )

    with st.chat_message("assistant"):
        st.markdown(result.content)

    st.session_state.chat_history.append(
        ("assistant", result.content)
    )