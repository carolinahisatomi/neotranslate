import os
import json
import streamlit as st
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

from frontend.layout import render_header, apply_style
from frontend.traducao_ui import interface_traducao
from frontend.memoria_ui import interface_memoria
from backend.glossario import carregar_glossario
from backend.inmetro import configurar_textos_descarte
from backend.tradutor import configurar_tradutor
from backend.auth import autenticar

# Configuração inicial
st.set_page_config(page_title="NeoTranslate", page_icon="assets/logo_neotranslate.png", layout="wide")
apply_style()
render_header()

# Carrega variáveis de ambiente e configura tradutor e glossário
load_dotenv()
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
glossario_dict = carregar_glossario()
configurar_tradutor(DEEPL_API_KEY, glossario_dict)

# Carrega textos de descarte do JSON
with open("textos_descarte.json", encoding="utf-8") as f:
    textos_descarte = json.load(f)
configurar_textos_descarte(textos_descarte)

#Login
def main():
    autenticar()

    if not st.session_state.get("autenticado", False):
        st.stop()

    # Menu lateral
    with st.sidebar:
            modo = option_menu(
                menu_title="",
                options=["Traduzir Documento", "Gerenciar Memória"],
                icons=["translate", "database"],
                default_index=0,
                styles={
                    "container": {"padding": "0.5rem", "background-color": "transparent"},
                    "icon": {"color": "#666666", "font-size": "18px"},
                    "nav-link": {"font-size": "13px", "text-align": "left", "margin": "4px 0", "--hover-color": "#f0f0f0", "color": "#33333300"},
                    "nav-link-selected": {"background-color": "#eaeaea00", "color": "#FFFFFFFF", "font-weight": "bold"}
                }
            )

    if modo == "Traduzir Documento":
            interface_traducao()
    elif modo == "Gerenciar Memória":
            interface_memoria()
            
if __name__ == "__main__":
    main()