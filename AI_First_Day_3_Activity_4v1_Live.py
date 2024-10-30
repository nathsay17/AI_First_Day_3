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

warnings.filterwarnings("ignore")

st.set_page_config(page_title="AI First Chatbot Template", page_icon="", layout="wide")

#Background
def get_base64_image(image_path):
    with open(image_path, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()
    return encoded_image

bg1 = get_base64_image("images/background3.jpg")
bg2 = get_base64_image("images/background1.jpg")
bg3 = get_base64_image("images/background2.jpg")
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
        "Dashboard", 
        ["Home", "Talk to Geralt", "Model"],
        icons = ['book', 'globe', 'tools'],
        menu_icon = "book", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        }
    )
    st.image('images/logo2.png')

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None #Placeholder for your chat session initialization

if options == "Home":
    st.markdown('<h1 class="outlined-text">Welcome to the world of Witcher 3!</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="outlined-text">Write Text</h2>', unsafe_allow_html=True)
    st.markdown(
        f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg2}");
            background-size: contain;  /* Adjust to 'contain' */
            background-position: center;  /* Adjust these values for positioning */
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .outlined-text {{
            color: white;  /* Text color */
            text-shadow: 
                -1px -1px 0 #000,  
                1px -1px 0 #000,
                -1px 1px 0 #000,
                1px 1px 0 #000;  /* Outline color */
            font-size: 24px;  /* Adjust font size as needed */
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

elif options == "Talk to Geralt":
    #st.image("")
    st.markdown('<h1 class="outlined-text">Talk to Geralt</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="outlined-text">In this segment, you can talk to Geralt of Rivia (AI generated). You may ask anything related to the video game "The Witcher 3: Wild Hunt". </h2>', unsafe_allow_html=True)
    st.markdown(
        f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg4}");
            background-size: contain;  /* Adjust to 'contain' */
            background-position: center;  /* Adjust these values for positioning */
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .outlined-text {{
            color: white;  /* Text color */
            text-shadow: 
                -1px -1px 0 #000,  
                1px -1px 0 #000,
                -1px 1px 0 #000,
                1px 1px 0 #000;  /* Outline color */
            font-size: 24px;  /* Adjust font size as needed */
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

elif options == "Model":
    st.title("News Summarizer Tool")
    col1, col2, col3 = st.columns([1,2,1])
    st.markdown(
        f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg4}");
            background-size: contain;  /* Adjust to 'contain' */
            background-position: center;  /* Adjust these values for positioning */
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .outlined-text {{
            color: white;  /* Text color */
            text-shadow: 
                -1px -1px 0 #000,  
                1px -1px 0 #000,
                -1px 1px 0 #000,
                1px 1px 0 #000;  /* Outline color */
            font-size: 24px;  /* Adjust font size as needed */
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

    with col2:
        News_Article = st.text_input("News Article", placeholder="News : ")
        submit_button = st.button("Generate Summary")

        if submit_button:
            with st.spinner("Generating Summary"):
                System_Prompt = """You are a helpful assistant named "Bud," specializing in summarizing news articles with the polish and clarity of a news anchor. Follow a structured approach to deliver concise, engaging, and informative summaries:

Step 1: Article Analysis
Identify the core event, issue, or topic covered in the article.
Determine the key details, such as who, what, when, where, why, and how.
Recognize any significant quotes or statements that provide context or impact.
Step 2: Summarization
Headline Statement: Start with a strong, engaging opening sentence that captures the essence of the article, similar to a news anchor's lead-in.
Main Point: Summarize the main story in 1-2 sentences, conveying the key message in a way that's clear and impactful.
Details: Follow up with essential facts, including important figures, quotes, or developments that add depth to the story.
Background (if necessary): Provide relevant context to help the audience understand the significance of the news.
Closing Remark: End with a brief statement to wrap up the summary, possibly highlighting potential implications or next steps.
Step 3: Tone and Style
Use a professional, authoritative tone, similar to a news anchor's delivery, ensuring a balance between informative and engaging content.
Maintain a neutral stance without inserting personal opinions.
Aim for clarity and conciseness, keeping the summary around 50-100 words.
Edge Cases
Simplify complex or technical terms to make the news accessible to a broad audience."""

                user_message = News_Article
                struct = [{'role' : 'system', 'content' : System_Prompt}]
                struct.append({"role": "user", "content": user_message})
                chat = openai.ChatCompletion.create(model="gpt-4o-mini", messages = struct)
                response = chat.choices[0].message.content
                struct.append({"role": "assistant", "content": response})
                st.success("Insight generated successfully")
                st.subheader("Summary:")
                st.write(response)
