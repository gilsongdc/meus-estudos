
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
setor = input("Qual o setor de armazenamento: ")

mercadoria = {
    "produto":nome_produto,
    "quantidade":quantidade,
    "setor":setor
}
print("\n Salvando dados no arquivo de texto ...")

with open("relatorio_estoque.txt", "a")as arquivo:
    arquivo.write(f"PRODUTO:{mercadoria['produto']} | QTD: {mercadoria['quantidade']} | SETOR: {mercadoria['setor']}\n")

print("dados salvos com sucesso!")

print("\n lendo historico completo do estoque: ")
print("---------------------------------------")

with open("relatorio_estoque.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
    
    
