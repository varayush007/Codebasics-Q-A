import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db


st.title("FAQ BOT")
btn = st.button("Create Knowledgebase")

if btn:
    create_vector_db()

question = st.text_input("Question:")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.subheader("Answer")
    st.write(response["result"])



