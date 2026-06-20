from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

#Todos agentes necessitam da chave de API, e a função LOAD_DOTENV faz a leitura do arquivo no .env.
load_dotenv()

agente = Agent(
    #Essa linha, define o modelo do meu agente.
    model= OpenAIChat(id="gpt-5.4-mini"),
    markdown=True
)

agente.print_response("Me conta uma curiosidade.")
