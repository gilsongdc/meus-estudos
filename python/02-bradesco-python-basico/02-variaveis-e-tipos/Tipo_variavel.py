codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

tipo = type (salario)

print(salario)
print(tipo)


#Concatenação

codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

tipo = type (salario)

print ("Codigo: ",codigo, "Nome: ",nome , "E o salario é de: ", salario)

#Também podemos concatenar as informações na linguagem Python utilizando o sinal de soma (+).
#Neste caso, temos de converter os valores que não são string para o tipo string.
#Para isso, utilizamos o comando (str) antes da impressão da variável

codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

tipo = type (salario)

print("Codigo: "+str(codigo), "Nome: "+ str(nome) + "  Salario: "+str(salario))
