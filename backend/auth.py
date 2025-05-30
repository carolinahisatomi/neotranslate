import streamlit as st

USUARIOS = {
    "engenharia": "manual2025"  # usuário: senha
}

def autenticar():
    st.session_state["autenticado"] = False

    with st.form("login"):
        st.subheader("🔐 Acesso Restrito")
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        entrar = st.form_submit_button("Entrar")

        if entrar:
            if usuario in USUARIOS and USUARIOS[usuario] == senha:
                st.session_state["autenticado"] = True
                st.experimental_rerun()
            else:
                st.error("Usuário ou senha inválidos.")