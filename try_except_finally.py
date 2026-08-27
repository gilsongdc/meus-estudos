print("====================================")
print("🛡️ PROGRAMA BLINDADO CONTRA ERROS")
print("====================================")

# 1. O Python VAI TENTAR executar o bloco abaixo
try:
    # Se o usuário digitar 'vinte' em vez de 20, a linha abaixo daria um erro clássico (ValueError)
    idade = int(input("Digite a sua idade em números: "))
    print(f"Muito bem! Sua idade é {idade} anos.")

# 2. SE o usuário digitar letras, o ValueError acontece e o except captura o erro!
except ValueError:
    print("❌ Erro: Você digitou letras! Digite apenas números inteiros.")

# 3. Este bloco SEMPRE roda no final, dando erro ou não
finally:
    print("🏁 Verificação de segurança concluída.")
