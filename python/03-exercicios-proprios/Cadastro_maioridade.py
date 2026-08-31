while True:
    nome = input("Qual e seu nome: ")
    try:
        idade = int(input("Qual e sua idade: "))
        break
    except ValueError:
        print("Por favor apenas numeros inteiros ! ")
cidade = input("Qual a sua cidade: ")

print("--------------------")
print("DADOS CADASTRADOS")
print("--------------------")
print("\nNome",nome,"\nIdade",idade,"\nCidade",cidade)

if idade >= 50 :
    print("STATUS : Voce é um idoso(a) ! ")
elif idade >= 18 :
    print("STATUS : Voce e maior de idade ! ")
else:
    print("STATUS : Voce é menor de idade ! ")



