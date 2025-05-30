import os
import pandas as pd
import streamlit as st
from backend.memoria import PASTA_MEMORIA


def interface_memoria():
    st.markdown("""
        <div style='padding: 1rem 0; text-align: center;'>
            <h2 style='margin: 0; font-weight: normal; color: #333;'>Gerenciador de Memória de Tradução</h2>
        </div>
    """, unsafe_allow_html=True)

    arquivos = [f for f in os.listdir(PASTA_MEMORIA) if f.endswith(".csv")]
    if not arquivos:
        st.warning("Nenhum arquivo de memória encontrado.")
        return

    arquivo_escolhido = st.selectbox("Escolha um arquivo de memória para editar", arquivos)
    caminho = os.path.join(PASTA_MEMORIA, arquivo_escolhido)
    df = pd.read_csv(caminho, encoding="utf-8", on_bad_lines='skip')

    st.caption("Edite abaixo as traduções corrigidas. Clique em 💾 para salvar ou 🗑️ para excluir uma linha.")

    indices_para_excluir = []
    novas_traducoes = []

    for i, row in df.iterrows():
        with st.expander(f"{i+1}. {row['original'][:60]}..."):
            st.markdown(f"**Original:** {row['original']}")
            st.markdown(f"**Tradução automática:** {row['traducao_automatica']}")
            nova = st.text_area("✏️ Tradução corrigida", value=row['traducao_corrigida'], key=f"edit_{i}")
            novas_traducoes.append(nova)

            if st.button("🗑️ Excluir esta linha", key=f"delete_{i}"):
                indices_para_excluir.append(i)

    if indices_para_excluir:
        df.drop(index=indices_para_excluir, inplace=True)
        df.reset_index(drop=True, inplace=True)
        novas_traducoes = [t for i, t in enumerate(novas_traducoes) if i not in indices_para_excluir]
        st.warning(f"{len(indices_para_excluir)} linha(s) marcadas para exclusão. Clique em 💾 para salvar.")

    if st.button("💾 Salvar alterações"):
        df["traducao_corrigida"] = novas_traducoes
        df.to_csv(caminho, index=False, encoding="utf-8")
        st.success("Memória atualizada com sucesso!")

    st.markdown("<br><br>", unsafe_allow_html=True)
