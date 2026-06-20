# Desafio 2: Questionário do Detetive 

# Objetivo: Simular um mini-diálogo onde o programa coleta vários dados para montar um relatório.
# Enunciado:
# Crie um programa que simula um interrogatório. Faça 3 perguntas ao usuário:
# Onde ele estava ontem á noite? (Guarde em uma variável)
# O que ele estava fazendo (Guarde em uma variável)
# Quem estava com ele? (Quem estava com ele)
#  No final, imprima o "Relatório Investigativo" juntando todas as respostas para ver se a história faz sentido. 

p1 = input("Onde você estava ontem a noite? ")
print(f"Hum.... Então quer dizer que você estava no {p1}...Responda a próxima pergunta...\n")

p2 = input("O que você estava fazendo?")
print(f"Muito conveniente que no dia do ocorrido você estava {p2}")

p3 = input("Com quem você estava?")
print(f"O {p3} é considerado suspeito e cúmplice!")

