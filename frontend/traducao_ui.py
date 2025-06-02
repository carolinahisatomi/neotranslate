
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

    if arquivo:
        if not arquivo.name.lower().endswith(".docx"):
            st.error("❌ Apenas arquivos com extensão `.docx` são suportados. Por favor, envie um documento do Word.")
            return

        if st.button("Iniciar Tradução"):
            traduzir_docx_com_tudo(
                arquivo=arquivo,
                exige_inmetro=exige_inmetro,
                tipo_equipamento=tipo_equipamento,
                aplicar_glossario_func=lambda texto: aplicar_glossario(texto, glossario_dict)
            )

    st.markdown("<br><br>", unsafe_allow_html=True)