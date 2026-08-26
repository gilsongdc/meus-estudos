print("-----------------------")
print ("Ecoador de palavras")
print("-----------------------")

palavra = ("sair")

while True:
    chute = input("Digite algo (ou'sair' para fechar):")
    if chute == palavra:
        print("Até logo!")
        break
    else:
        print("Voce digitou?", chute)
