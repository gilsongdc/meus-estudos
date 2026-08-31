nome = input("Digite seu nome: ")
Soma_das_notas = 0
while True:
    try:
        quantasnotas = int(input("Digite a quantidade de notas: "))
        break
    except ValueError:
        print("Valor invalido Apenas numeros")

for i in range(quantasnotas):

    while True:
        try:
            nota = int(input(f"Digite uma nota{i+1}: "))
            break
        except ValueError:
            print("Valor invalido Apenas numeros")
    Soma_das_notas +=nota
    media =  Soma_das_notas / quantasnotas
print(media)
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")