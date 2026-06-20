import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade",["Professor de Python","Professor de História","Cientista maluco"])

descricao = {
    "Professor de Python":"Você é um professor de Python que responde com exemplos e contexto",
    
    "Professor de História":"Você é um professor de história que ensina de forma clara, simples e objetiva.",
    
    "Cientista maluco":"Você é um cientista maluco que sempre está em busca de novas inovações e projetos"
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools(),WikipediaTools()],
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
        
    st.session_state.mensagem.append({"role":"user","content":pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner(f"{personalidade} pensando..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
    
    st.session_state.mensagem.append
    ({"role":"assistant","content":resposta.content})
