from agno.agent import Agent 
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

#Carregar a chave de API
load_dotenv()

bancoDados = SqliteDb(db_file="temp/registros.db")

#Crio o modelo de IA
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um especialista em pesquisas acadêmicas, e possui a melhor didática do mundo para ensino e contextualização prática",
    add_history_to_context=True,
    db=bancoDados,
    session_id="2d74ac75-2b92-465c-a5ae-d56ecd5bb793",
    num_history_runs=3,
    tools=[DuckDuckGoTools(),TavilyTools],
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerando agente...\nAté mais tarde 🤖")
        break
    else: 
        agente.print_response(pergunta)