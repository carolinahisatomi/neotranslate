# NeoTranslate - Tradutor de Manuais Técnicos

NeoTranslate é um app em Streamlit para traduzir documentos `.docx` com preservação de layout, glossário técnico, INMETRO e memória de tradução.

## 📁 Estrutura do projeto

```
tradutor-manuais/
├── app.py
├── requirements.txt
├── glossario.csv
├── textos_descarte.json
├── assets/
├── memoria_traducao/
├── backend/
│   ├── glossario.py
│   ├── inmetro.py
│   ├── memoria.py
│   ├── tradutor.py
│   └── traducao.py
├── frontend/
│   ├── layout.py
│   ├── memoria_ui.py
│   └── traducao_ui.py
└── .streamlit/
    └── secrets.toml
```

## ✅ Pré-requisitos

- Python 3.8+
- Conta no [Streamlit Cloud](https://streamlit.io/cloud)
- Conta no GitHub

## 🧪 Instalação local

```bash
# Clone o repositório
https://github.com/seu-usuario/tradutor-manuais.git
cd tradutor-manuais

# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Rode localmente
streamlit run app.py
```

## ☁️ Deploy no Streamlit Cloud

1. Suba este repositório para o seu GitHub
2. Acesse [streamlit.io/cloud](https://streamlit.io/cloud)
3. Clique em **"New app"** e selecione o repositório
4. No painel de deploy, crie o arquivo `.streamlit/secrets.toml` com:

```toml
DEEPL_API_KEY = "sua_chave_da_api"
```

5. Clique em **Deploy**. Seu app estará disponível publicamente!

## 📘 Funcionalidades

- Upload de arquivos `.docx`
- Tradução automática com DeepL
- Aplicação de glossário técnico
- Inclusão de seções do INMETRO
- Memória de tradução com revisão manual
- Interface visual com opção de exclusão de linhas

## 🔐 Segurança

- A chave da API do DeepL deve ser colocada apenas em `.streamlit/secrets.toml`
- Nunca suba seu `.env` no GitHub

## 🧩 Dependências principais

- streamlit
- python-docx
- deepl
- pandas
- python-dotenv
- streamlit-option-menu

## 📞 Suporte

Em caso de dúvidas ou sugestões, abra uma Issue ou envie um e-mail para: [carolina.hisatomi@neosolar.com.br](mailto:carolina.hisatomi@neosolar.com.br)
