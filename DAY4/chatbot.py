import streamlit as st
import ollama
st.title("😊:rainbow[Welcome to my chatbot app!!!]")
with st.sidebar:
    st.header("chat settings   ")
    if st.button("clear chat🚮"):
        st.session_state.messages=[]
        st.success("chat cleared")
    personalities={
        "😊kid":"Answer the questions like you are explaining to a 5 years old kid.give answers in 2 lines only.",
        "🧑‍🤝‍🧑Friend":"Answer the questions in friendly and casual manner.give answers in 2 lines only.",
        "🧑🏾‍🏫proffessor":"answer the questions in deep manner.give answers in 2 lines only"
    }
    personality=st.selectbox("select a persnality",personalities.keys()) 
    uploaded_file=st.file_uploader("upload a text file..")
    try:
        if uploaded_file:
            st.success("file uploaded successfully")
            if st.button("dispaly"): 
                context=uploaded_file.read().decode("utf-8")
                st.write(context)
    except:
        st.error("Error") 
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question 
    })
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[{"role":"system","content":personalities[personality]}]
                    +st.session_state.messages
        )
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["message"]["content"]
    })
    with st.chat_message("assistant"):
        st.write(response["message"]["content"])