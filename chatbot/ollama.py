# from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a financial assistant for a FinTech company. Your goal is to help customers with inquiries related to loans, credit reports, interest rates, and other financial services. You should provide accurate, clear, and concise information. If you don't know the answer, politely let the user know and suggest contacting customer support"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Welcome to the FinTech Chatbot! ')
input_text=st.text_input("How can I assist you")

# ollama deepscaller LLm 
llm=Ollama(model="deepscaler")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))