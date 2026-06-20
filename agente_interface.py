import streamlit as st 
from agno.models.openai import OpenAIChat 
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

agente = Agent( #Tupla pois não mudaremos os parâmetros do agente
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um professor de Python",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

st.title("Agente de I.A. 🤖")

pergunta = st.chat_input("Pergunte alguma coisa")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        with st.spinner("Agente pensando..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)




 


