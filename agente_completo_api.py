#Importando bibliotecas e frameworks necessários para o projeto
import streamlit as st
from datetime import datetime
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv
import requests

#Utilizamos para carregar as chaves de API no arquivo .env
load_dotenv()

#Criando nossas funções (habilidades/skills)
def get_moedas():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    #Estrutura de try/except
    try:
        dados = requests.get(url)
        resposta = dados.json()
        #Estamos convertendo o timestamp (segundos) para uma data legível
        timestamp = resposta['time_last_updated']
        data_convertida = datetime.fromtimestamp(timestamp)
        #Conversões (VERIFICAR MOEDA BASE)
        dolar = 1 / resposta['rates']['USD']
        euro = 1 / resposta['rates']['EUR']
        #Toda função retorna algum valor
        return f"{dolar:.2f} USD = 1 BRL | {euro:.2f} EUR = 1 BRL. Dados atualizados foram atualizados em {data_convertida}"
    except:
        return "Cotação não realizada. Tente novamente"

personalidade = st.sidebar.selectbox(
    "Personalidade",
    [
        "Professor de Python",
        "Professor de História",
        "Cientista Maluco",
        "Conversor de Moedas"
    ]
)

descricao = {
    "Professor de Python": "Você é um professor de Python que responde com exemplos e contexto.",

    "Professor de História": "Você é um professor de história que ensina de forma clara, simples e objetiva.",

    "Cientista Maluco": "Você é um cientista maluco que sempre está em busca de novas inovações e projetos.",

    "Conversor de Moedas": "Você é especialista em conversão de moedas e câmbio."
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools()],
    markdown=True
)

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []
   
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if st.sidebar.button("Limpar conversas"):
     st.session_state.mensagem = []
     st.rerun()
     
st.title("Sistema MultiAgentes")

pergunta = st.chat_input("Pergunte ao Agente")

if pergunta:

    with st.chat_message("user"):
        st.markdown(pergunta)

    st.session_state.mensagem.append(
        {"role":"user","content":pergunta}
    )

    with st.chat_message("assistant"):
        with st.spinner(f"{personalidade} pensando..."):

            contexto = ""

            if personalidade == "Conversor de Moedas":

                if (
                    "dólar" in pergunta.lower()
                    or "dolar" in pergunta.lower()
                    or "euro" in pergunta.lower()
                    or "real" in pergunta.lower()
                    or "moeda" in pergunta.lower()
                ):
                    contexto = get_moedas()

            resposta = agente.run(pergunta + contexto)

            st.markdown(resposta.content)

    st.session_state.mensagem.append(
        {"role":"assistant","content":resposta.content}
    )