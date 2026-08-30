while True:
    Nome = input("Qual o seu nome? (Ou digite 'sair' para fechar):")
    if Nome == 'sair':
        break
    peso = float(input("Qual o seu peso ?"))
    altura = float(input("Qual a sua altura ?"))
    imc = peso / (altura ** 2)
    print("\nO seu nome é:", Nome ,"\nO seu peso é: ", peso ,"\nA sua altura é: ", altura , f"\nE seu IMC é: {imc:.2f}" )