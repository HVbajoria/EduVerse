import streamlit as st
import streamlit.components.v1 as components
from auth0_component import login_button

domain = "dev-qzlbx0jqzsgjkeaf.us.auth0.com"
clientId = "MxxNJ7qlS1CLzusDdY10wIjYYStaswk4"
auth0_client_secret = "AhmJasxlnHfhl2Eop4krFvO_JEW9OTmuD7twFoU6xpX6ZBbMsKnUDMziuc4ZGRg2"

st.set_page_config( 
     page_title="EduVerse", 
     page_icon="🏫",
     layout="wide", 
     initial_sidebar_state="expanded", 
 ) 

hide_default_format = """ 
        <style> 
        footer {visibility: hidden;} 
        </style> 
        """ 
st.markdown(hide_default_format, unsafe_allow_html=True) 

def gradient_text(text, color1, color2):
    gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 42px;
    """
    return f'<span style="{gradient_css}">{text}</span>'

def gradient(text, color1, color2):
    gradient_css = f"""
        background: -webkit-linear-gradient(left, {color2}, {color1});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 22px;
    """
    return f'<span style="{gradient_css}">{text}</span>'

color1 = "#0d3270"
color2 = "#0fab7b"
text = "EduVerse"
  
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("images/logo.png", width=200)

styled_text = gradient_text(text, color1, color2)
st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)

text="Empowering Mind, Unlocking Knowledge"
styled_text = gradient(text, color1, color2)
st.write(f"<div style='text-align:center;'>{styled_text}</div>",unsafe_allow_html=True)

st.subheader("Weclome "+st.session_state["username"]+" 👋")
  
st.markdown(""" 

1. **Chat & Learn**: Empower your knowledge with a chatbot that lets you create a smart knowledge base, ask questions, and save the conversation using Azure Conversational AI service.
              
2. **VideoLink**: Dive into learning with ease! Our Video Searcher finds the most relevant learning videos on any topic using the Azure Bing Search API service.
   
3. **Keyword-Powered Notes**: Take notes like a pro! Our Note Maker extracts keywords and lets you download them in bold format - powered by Azure Keyword Extractor Feature.
   
4. **LinguaBrief**: Unlock the power of instant translation and summarization with our Text Summarizer, backed by Azure AI Text Summarizer and Translator.
 """)


footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/harshavardhan-bajoria/" target="_blank">Harshavardhan Bajoria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
