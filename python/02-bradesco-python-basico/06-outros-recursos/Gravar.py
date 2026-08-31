arquivo = open("arqText.txt", 'w')

arquivo.write("Curso Python \n")
arquivo.write("Aula pratica")
arquivo.close()

# leitura do aquivo texto

leitura=open("arqText.txt", 'r')
print(leitura.read())
leitura.close()