print("=================================")
print("Cadastro de cliente (dicionario)")
print("=================================")

cliente = {
    "nome": "Gilson dev",
    "cidade":"Campo largo",
    "codigo":1024
}

print("\n--- visualisando Dados do Cadastro ---")
print("Nome do Cliente:",cliente["nome"])
print("Cidade:", cliente["cidade"])
print("Código interno",cliente["codigo"])

print("\n--- Testando os metodos do santander ---")
print("Campos de ficha (chaves):",cliente.keys())
print("Dados salvos (valores):", cliente.values())
cliente.update({"status":"Ativo"})

print ("\n--- ficha Atualizada ---")
print (cliente)
