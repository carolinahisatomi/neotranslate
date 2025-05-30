import time
import deepl
import streamlit as st
from backend.glossario import aplicar_glossario
from difflib import SequenceMatcher

# Tradutor global (espera que você defina isso no app.py)
translator = None

# Define o glossário global
glossario_dict = {}

def configurar_tradutor(deepl_api_key, glossario):
    global translator, glossario_dict
    translator = deepl.Translator(deepl_api_key)
    glossario_dict = glossario

def traduzir_texto(texto):
    if not texto.strip():
        return ""

    texto = aplicar_glossario(texto, glossario_dict)
    try:
        result = translator.translate_text(texto, source_lang="EN", target_lang="PT-BR")
        return result.text
    except deepl.TooManyRequestsException:
        st.warning("⏳ O DeepL recebeu muitas requisições. Aguardando 10 segundos...")
        time.sleep(10)
        try:
            result = translator.translate_text(texto, source_lang="EN", target_lang="PT-BR")
            return result.text
        except deepl.TooManyRequestsException:
            st.error("❌ O DeepL continua sobrecarregado. Tente novamente mais tarde.")
            st.stop()
    except deepl.DeepLException as e:
        st.error(f"Erro na tradução: {e}")
        st.stop()

def consultar_memoria(texto, memoria, threshold=0.95):
    for original, traducao_corrigida in memoria:
        similaridade = SequenceMatcher(None, texto.strip().lower(), original.strip().lower()).ratio()
        if similaridade >= threshold:
            return traducao_corrigida
    return None

def traduzir_com_memoria(texto, memoria):
    from_memoria = consultar_memoria(texto, memoria)
    if from_memoria:
        return from_memoria, True
    return traduzir_texto(texto), False