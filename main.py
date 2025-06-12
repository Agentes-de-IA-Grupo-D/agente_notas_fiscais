from agente.agente_csv import AgenteNotasFiscais
import streamlit as st
import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import os
from dotenv import load_dotenv
load_dotenv()

st.title("Agente Inteligente para CSV")

uploaded_files = st.file_uploader("Envie um ou mais arquivos CSV", type="csv", accept_multiple_files=True)

if uploaded_files:
    dataframes = [pd.read_csv(f) for f in uploaded_files]
    pergunta = st.text_input("Digite sua pergunta sobre os dados:")

    if pergunta:
        # Adiciona contexto das colunas à pergunta (mas NÃO mostra na interface)
        colunas = []
        for i, df in enumerate(dataframes):
            colunas.append(f"Colunas do arquivo {i+1}: {', '.join(df.columns)}")
        contexto = "\n".join(colunas)
        pergunta_com_contexto = contexto + "\n\n" + pergunta

        llm = ChatOpenAI(
            openai_api_key=os.getenv("GROQ_API_KEY"),
            openai_api_base="https://api.groq.com/openai/v1",
            model_name="meta-llama/llama-4-scout-17b-16e-instruct"
        )
        agent = create_pandas_dataframe_agent(
            llm,
            dataframes,
            verbose=False,
            allow_dangerous_code=True,
            max_iterations=50
        )
        resposta = agent.run(pergunta_com_contexto)
        st.write("Resposta:", resposta)
else:
    st.info("Envie pelo menos um arquivo CSV para começar.")
