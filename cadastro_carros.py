print("=================================")
print("Cadastro de carro (dicionario)")
print("=================================")

cliente = {
    "marca": "Volkswagen",
    "modelo":"Polo",
    "ano":2020
}

print("\n--- visualisando Dados do Cadastro ---")
print("Marca do Carro:",cliente["marca"])
print("Modelo:", cliente["modelo"])
print("ano do carro:",cliente["ano"])

print("\n--- Testando os metodos do santander ---")
print("Campos de ficha (chaves):",cliente.keys())
print("Dados salvos (valores):", cliente.values())
cliente.update({"status":"Ativo"})

print ("\n--- ficha Atualizada ---")
print (cliente)
