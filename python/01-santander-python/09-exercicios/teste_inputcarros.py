print("=================================")
print("Cadastro de carro (dicionario)")
print("=================================")

marca_digitada =  input ("Digite a marca do seu carro: ")
modelo_digitado =  input("Digite o modelo do seu carro: ")
ano_digitado =  int(input ("Digite o ano do seu carro"))

carro = {
    "marca": marca_digitada,
    "modelo": modelo_digitado,
    "ano": ano_digitado
}

print("\n--- visualisando Dados do Cadastro ---")
print("Marca do Carro:", carro ["marca"])
print("Modelo:", carro["modelo"])
print("ano do carro:",carro["ano"])


print ("\n--- ficha Completa na Nuvem ---")
print (carro)

