import os
import pandas as pd
from langchain_community.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

class AgenteNotasFiscais:
    def __init__(self, cabecalho_file, itens_file):
        self.df_cabecalho = pd.read_csv(cabecalho_file)
        self.df_itens = pd.read_csv(itens_file)

    def get_dataframes(self):
        return self.df_cabecalho, self.df_itens

def criar_agente_csv():
    cabecalho = pd.read_csv("dados/202401_NFs_Cabecalho.csv")
    itens = pd.read_csv("dados/202401_NFs_Itens.csv")
    df = pd.merge(itens, cabecalho, on="chave", how="left")
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo")
    agente = create_pandas_dataframe_agent(llm, df, verbose=True)
    return agente
