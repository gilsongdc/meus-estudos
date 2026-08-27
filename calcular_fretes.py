print ("-----------------")
print("Calcular frete ")
print ("-----------------")

cacular_cubagem = lambda x : x * 300

while True:
    peso_caixa = float(input("Digite o valor do peso da caixa: "))

    frete = cacular_cubagem(peso_caixa)

    print (frete)
