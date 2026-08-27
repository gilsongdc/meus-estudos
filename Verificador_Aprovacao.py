print("--------------------------")
print("Verificador de Aprovação")
print("--------------------------")

def verificador_resultado(nota):
    if nota >= 6.0:
        return "Aprovado"
    else:
        return"Recuperação"

nota_aluno = float(input("Digite sua nota: "))

situacao_final = verificador_resultado(nota_aluno)

print("O status do aluno é:", situacao_final )

