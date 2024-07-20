#Importing modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st

st.title("Chatbot of Llama2")
user_input = st.text_input("Ask any questions please!!") #Input from user


user_prompt=ChatPromptTemplate.from_messages([
    ("system","You are  a good helpful assistant"),
    ("user","Question:{question}")
])

llm1 = Ollama(model="llama2")

chain  = user_prompt|llm1 #combines the llama3 and user input 

if user_input:
    st.write(chain.invoke({"question":user_input}))



