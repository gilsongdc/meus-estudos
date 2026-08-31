nome = input("Digite seu nome: ")
while True:
    try:
        nota1 = float(input("Digite a Primera nota:"))
        break
    except ValueError:
        print("Apenas numeoros com ponto fluante ex 7.2 ,  10.00")
while True:
    try:
        nota2 = float(input("Digite a Segunda nota:"))
        break
    except ValueError:
        print("Apenas numeoros com ponto fluante ex 7.2 ,  10.00")

media = (nota1 + nota2) / 2

print ("\nNome:",nome,"\nMedia",f"{media:.2f}")

if media >= 6.0:
    print("Aprovado")
elif media >= 4.0:
    print("Média de 4 até abaixo de 6 → Exame")
else:
    print("Média abaixo de 4 =  REPROVADO")



