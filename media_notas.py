print("====================")
print("Media da sua nota !")
print("====================")

nota1 = float(input("Adicione a sua nota: "))
nota2 = float(input("Adiciona a sua segunda nota: "))

media = (nota1+nota2) / 2
print (media)

if media >= 6.0:
    print("voce passou de ano ! Meus Parabens")
else:
    print("Reprovado!")
