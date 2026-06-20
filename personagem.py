# Desafio 1: O Criador de Personagens RPG 
# Objetivo: Lidar com múltiplos inputs sequenciais e estruturar o código.
# Enunciado:
# Você está criando um jogo e precisa montar o personagem do jogador. Peça para o usuário digitar três coisas, uma de cada vez:
# O nome do personagem 
# A classe do personagem (mago, guerreiro, etc)
# O tipo de skin que o personagem irá possuir (grátis, plus ou pro).
# Agora, exiba no console as três informações.

nome = input("Digite o nome do seu personagem: ")
classe = input("Digite a classe do seu personagem: ")
skin = input("Digite a skin do seu personagem: ")

print(f"Olá! O nome do seu personagem é {nome}, ele está na classe {classe}, e possui uma skin {skin}")
