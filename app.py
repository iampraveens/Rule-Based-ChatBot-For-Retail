import os
import streamlit as st 
import requests
from io import BytesIO
from PIL import Image

from prediction import process_input
from html_templates import css, user_template, bot_template

url = "https://cdn-icons-png.flaticon.com/512/6231/6231457.png"
response = requests.get(url)
image = Image.open(BytesIO(response.content))
page_title = 'Rule Based ChatBot for retail'
page_icon = image
layout = 'centered'

st.set_page_config(page_title=page_title,
                   page_icon=page_icon,
                   layout=layout
                   )

hide_style = '''
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            <style>
            
            '''
header_style = '''
             <style>
             .navbar {
                 position: fixed;
                 top: 0;
                 left: 0;
                 width: 100%;
                 z-index: 1;
                 display: flex;
                 justify-content: center;
                 align-items: center;
                 height: 80px;
                 background-color: #2b313e;
                 box-sizing: border-box;
             }
             
             .navbar-brand {
                 color: white !important;
                 font-size: 23px;
                 text-decoration: none;
                 margin-right: auto;
                 margin-left: 50px;
             }
             
             .navbar-brand img {
                margin-bottom: 6px;
                margin-right: 1px;
                width: 40px;
                height: 40px;
                justify-content: center;
            }
            
            /* Add the following CSS to change the color of the text */
            .navbar-brand span {
                color: #EF6E04;
                justify-content: center;
            }
            
             </style>
             
             <nav class="navbar">
                 <div class="navbar-brand">
                <img src="https://cdn-icons-png.flaticon.com/512/6231/6231457.png" alt="Logo">
                    Rule Based ChatBot for retail
                 </div>
             </nav>
               '''
st.markdown(hide_style, unsafe_allow_html=True)
st.markdown(header_style, unsafe_allow_html=True)
st.write(css, unsafe_allow_html=True)

user_input = st.chat_input(placeholder="How can I help you!!")
if user_input:
    response = process_input(user_input)
    st.write(user_template.replace("{{MSG}}", user_input), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", response), unsafe_allow_html=True)