print("------------------")
print("Validação de senha")
print("------------------")

senha = ("1234")
while True:
    # 1. Pede a senha e salva na variável 'chute'
    chute = input( "Digite sua senha: ")

     # 2. Testa se a senha digitada é igual à correta
    if chute == senha:
        print("Acesso Permitido! Bem vindo ! ")
        break # Se acertou, o break quebra o while e o programa fecha

    else:
        print("Senha incorreta ! Tente novamente...")
    
         
