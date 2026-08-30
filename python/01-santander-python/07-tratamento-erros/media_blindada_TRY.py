print("====================================")
print("🛡️ PROGRAMA BLINDADO INDIVIDUALMENTE")
print("====================================")

while True:
    # Loop para garantir que a nota 1 seja um número válido
    while True:
        try:
            nota1 = float(input("Digite sua primeira nota (ou -1 para sair): "))
            break  # Se deu certo, sai deste loop menor e vai para a nota 2
        except ValueError:
            print("❌ Erro de digitação! São válidos apenas números!")

    # Se digitar -1, quebra o loop principal e fecha o programa
    if nota1 == -1:
        print("🏁 Sistema encerrado!")
        break

    # Loop para garantir que a nota 2 seja um número válido
    while True:
        try:
            nota2 = float(input("Digite sua segunda nota: "))
            break  # Se deu certo, sai deste loop menor e calcula a média
        except ValueError:
            print("❌ Erro de digitação! São válidos apenas números!")

    media = (nota1 + nota2) / 2
    print(f"Sua média é: {media}\n")
