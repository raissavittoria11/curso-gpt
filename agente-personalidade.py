from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

#Carregar a chave de API
load_dotenv()

#Crio o modelo de IA
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é um especialista em pesquisas acadêmicas, e possui a melhor didática do mundo para ensino e contextualização prática",
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")
    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar']:
        print("Encerando agente...\nAté mais tarde 🤖")
        break
    else: 
        agente.print_response(pergunta)