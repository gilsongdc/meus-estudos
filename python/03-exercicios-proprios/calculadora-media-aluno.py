aluno = input("Qual o nome do aluno ? ")
nota1 = float(input("Qual a primeira nota ? "))
nota2 = float(input("Qual a segunda nota ? "))
media=(nota1+nota2)/2
print(f"O aluno: {aluno},\nTeve uma Média de: {media}. ")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

