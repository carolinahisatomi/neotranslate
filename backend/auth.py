import streamlit as st

USUARIOS = {
    "neosolar": "tradutor123",
    "engenharia": "manual2024"
}

def autenticar():
    if st.session_state.get("autenticado"):
        return  # ✅ Já está autenticado, não faz nada

    st.subheader("🔐 Acesso Restrito")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state["autenticado"] = True
            st.experimental_rerun()  # ✅ Recarrega a tela sem o login
        else:
            st.error("Usuário ou senha inválidos.")

with st.sidebar:
    if st.button("🚪 Sair"):
        st.session_state["autenticado"] = False
        st.experimental_rerun()