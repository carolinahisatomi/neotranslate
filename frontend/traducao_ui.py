
import streamlit as st
from backend.tradutor import traduzir_texto, traduzir_com_memoria
from backend.memoria import carregar_memoria
from backend.inmetro import adicionar_textos_inmetro, adicionar_texto_reciclagem
from formatador_docx import adicionar_secoes_padrao
from backend.traducao import traduzir_docx_com_tudo
from backend.glossario import aplicar_glossario, carregar_glossario
glossario_dict = carregar_glossario()
from docx import Document
from docx.shared import Pt
from io import BytesIO
import csv

TIPOS_INVERSOR = {
    "Inversor Off-grid",
    "Inversor On-grid",
    "Inversor Carregador",
    "Inversor Híbrido"
}

def interface_traducao():
    st.title("NeoTranslate - Tradutor de Manuais")

    st.markdown("### 🗂️ Envie o arquivo em .docx")
    arquivo = st.file_uploader("📤 Arraste ou clique para enviar o manual (.docx)")

    tipo_equipamento = st.selectbox("Selecione o tipo de equipamento", [
        "🔋 Bateria de Lítio",
        "🔌 Inversor Off-grid",
        "⚡ Inversor On-grid",
        "🔄 Inversor Carregador",
        "🌐 Inversor Híbrido",
        "📟 Controlador de Carga MPPT",
        "☀️ Painel Solar",
        "🔋 Estação de Energia",
        "📁 Outros"
    ])

    exige_inmetro = st.checkbox("Este produto exige INMETRO?")

    # ✅ Botão grande e centralizado com estilo
    st.markdown("""
        <style>
            .translate-btn {
                display: flex;
                justify-content: center;
                padding-top: 2rem;
                padding-bottom: 2rem;
            }
            .translate-btn button {
                background-color: #FFD54F;
                color: #333333;
                font-weight: bold;
                font-size: 1.2rem;
                padding: 1rem 2rem;
                border: none;
                border-radius: 12px;
                box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
                cursor: pointer;
                transition: 0.2s ease;
            }
            .translate-btn button:hover {
                background-color: #FFC107;
                transform: scale(1.03);
            }
        </style>
    """, unsafe_allow_html=True)

    # Exibe botão com estilo
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Iniciar tradução", key="start_translation"):
            if arquivo and arquivo.name.lower().endswith(".docx"):
                traduzir_docx_com_tudo(
                    arquivo=arquivo,
                    exige_inmetro=exige_inmetro,
                    tipo_equipamento=tipo_equipamento,
                    aplicar_glossario_func=lambda texto: aplicar_glossario(texto, glossario_dict)
                )
            elif not arquivo:
                st.warning("📂 Por favor, envie um arquivo antes de iniciar a tradução.")
            else:
                st.error("❌ O arquivo enviado não é .docx.")