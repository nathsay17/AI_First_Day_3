import os
import openai
import numpy as np
import pandas as pd
import json
import base64
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from openai.embeddings_utils import get_embedding
import faiss
import streamlit as st
import warnings
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
from strings import home_string, about_string, System_Prompt, Bestiary_Prompt
from background import apply_background

warnings.filterwarnings("ignore")

st.set_page_config(page_title="The Witcher 3", page_icon="🐺", layout="wide")

#Background
def get_base64_image(image_path):
    with open(image_path, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()
    return encoded_image

bg1 = get_base64_image("images/background1.jpg")
bg2 = get_base64_image("images/background2.jpg")
bg3 = get_base64_image("images/background4.jpg")
bg4 = get_base64_image("images/background5.jpg")


with st.sidebar :
    st.image('images/logo1.png')
    st.image('images/logo0.png')
    
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai.api_key.startswith('sk-') and len(openai.api_key)==164):
        st.warning('Please enter your OpenAI API token!', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    options = option_menu(
        "Table of Knowledge", 
        ["Home", "About", "Talk to Geralt", "Bestiary"],
        icons = ['heart', 'chat', 'play', 'clipboard'],
        menu_icon = "book", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        }
    )
    st.image('images/logo3.png')

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None #Placeholder for your chat session initialization


if options == "Home":
    st.markdown(apply_background(bg1), unsafe_allow_html=True)
    st.markdown(home_string, unsafe_allow_html=True)

elif options == "About":
    st.markdown(apply_background(bg2), unsafe_allow_html=True)
    st.markdown('<h1 class="outlined-text"></h1>', unsafe_allow_html=True)
    st.markdown(about_string, unsafe_allow_html=True)

elif options == "Talk to Geralt":
    st.markdown(apply_background(bg3), unsafe_allow_html=True)
    st.markdown('<h1 class="outlined-text">Talk to Geralt</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="outlined-text">In this segment, you can talk to Geralt of Rivia (AI generated). You may ask anything related to the video game "The Witcher 3: Wild Hunt". </h2>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,3,1])
    
    with col2:
        user_query = st.text_input("Witcher Wiki", placeholder="Query : ")
        submit_button = st.button("Summon the Query")
        
        if submit_button:
            with st.spinner("Conjuring the Chronicle"):
                
                user_message = user_query
                struct = [{'role' : 'system', 'content' : System_Prompt}]
                struct.append({"role": "user", "content": user_message})
                chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
                response = chat.choices[0].message.content
                struct.append({"role": "assistant", "content": response})
                st.success("Insight generated successfully")
                st.subheader("Response:")
                st.write(response)

elif options == "Bestiary":
    st.markdown(apply_background(bg4), unsafe_allow_html=True)
    st.title("Bestiary")

    struct = [{'role' : 'system', 'content' : Bestiary_Prompt}]
    chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
    response = chat.choices[0].message.content
    struct.append({"role": "assistant", "content": response})
    st.write(response)
