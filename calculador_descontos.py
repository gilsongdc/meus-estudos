print("========")
print("Compras")
print("========")

valor = float(input("Digite o valor da compra: "))

if valor >= 100.00:
    print("🎉 Parabéns! Você ganhou frete grátis e 10% de desconto!")
else:
    print("👍 Compra realizada! Adicione mais itens para ganhar frete grátis na próxima.")
