print("----------------------")
print("Verificador de login")
print("----------------------")

def checar_usuario(nome):
    if nome == "Gilson":
        return "Acesso liberado Bem vindo,DEV."
    else:
        return "Acesso negado! Usuario não cadastrado!"

while True:
    nome_digitado = input("Digite seu nome de usuario: ")

    verificacao = checar_usuario(nome_digitado)

    print(verificacao)
