import streamlit as st
import base64

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def render_header():
    logo_base64 = get_base64_image("assets/logo_neotranslate.png", layout="wide")
    st.markdown(f"""
        <div style='display: flex; justify-content: center; align-items: center; padding: 2rem 0;'>
            <img src="data:image/png;base64,{logo_base64}" style='height: 160px;' />
        </div>
    """, unsafe_allow_html=True)

def apply_style():
    st.markdown("""
        <style>
            .main {
                background-color: #ffffff;
                font-family: 'Campton', sans-serif;
            }
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            .stButton>button {
                background-color: #FFD54F;
                color: #333333;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 0.6rem 1.2rem;
                box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
                transition: 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #FFC107;
                transform: scale(1.03);
            }
            .stTextInput>div>input,
            .stTextArea>div>textarea {
                background-color: #ffffff;
                border: 1.5px solid #FFD54F;
                border-radius: 8px;
                padding: 0.5rem;
                box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
            }
            .stExpander {
                border: 1px solid #FFD54F;
                border-radius: 8px;
                box-shadow: 1px 1px 4px rgba(0,0,0,0.05);
                background-color: #ffffff;
            }
            section[data-testid="stSidebar"] {
                background-color: #ffffff;
                padding: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)
