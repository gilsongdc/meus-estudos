print("====================================")
print("📝 CRIANDO E ESCREVENDO EM UM ARQUIVO")
print("====================================")

# 1. Usamos o 'with open' no modo "w" (escrita)
# Isso vai criar um arquivo chamado 'meu_teste.txt' na mesma pasta do seu script
with open("meu_teste.txt", "w") as arquivo:
    arquivo.write("Primeira linha do meu arquivo criado pelo Python!\n")
    arquivo.write("Gilson Dev esteve aqui gravando dados de forma profissional.\n")

print("🎉 Arquivo criado e salvo com sucesso!")

print("\n====================================")
print("📖 LENDO O ARQUIVO QUE FOI CRIADO")
print("====================================")

# 2. Agora abrimos o mesmo arquivo no modo "r" (leitura) para ler o que salvamos
with open("meu_teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
