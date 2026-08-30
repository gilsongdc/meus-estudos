idade = int(input("Digite sua idade: "))
if idade < 15 :
    print("Voce é uma criança !")
elif idade >= 15 and idade < 18:
    print("Voce tem mais de 15 anos (e menos de 18)")
elif idade == 60:
    print("Feliz aniversario de 60 anos ! ")
elif idade >= 18 and idade < 60:
    print("voce e um adulto.")
else:
    print("Voce e um idoso(adulto maior)")
