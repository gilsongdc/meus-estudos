print("Bem vindo a Tabuada Interativa")
while True:
    nome = input("Digite seu nome: \n'ou sair para fechar o programa: ")
    if nome == "sair":
        break
    while True:
        try:
            numero = int(input("Digite um numero: "))
            break
        except ValueError:
            print("Apenas numeros  inteiros ! ")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")






