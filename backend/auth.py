import streamlit as st

USUARIOS = {
    "neosolar": "tradutor123",
    "engenharia": "manual2024"
}

def autenticar():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.subheader("🔐 Acesso Restrito")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if usuario in USUARIOS and USUARIOS[usuario] == senha:
                st.session_state["autenticado"] = True
            else:
                st.error("Usuário ou senha inválidos.")