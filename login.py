print("-" * 50)
print("Sistema de autenticação")
print("-" * 50)

nomeUsuario = input("Digite o seu nome: ")
senhaUsuario = input("Digite a sua senha: ")

if nomeUsuario == "Platini" and senhaUsuario == "1234":
    print("Acesso liberado!")
else: 
    print("Acesso negado! Verifique as informações de login e tente novamente!")

