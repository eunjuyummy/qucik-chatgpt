import streamlit as st

st.title("Chatgpt")

st.text_input("Prompt")

if Prompt:
  # call chatgpt api
  # response
  message = "Response"
  st.text(message)
