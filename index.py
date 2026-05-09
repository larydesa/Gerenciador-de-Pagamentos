print("{:=^40}".format(" LOJAS LARISSA "))
price = float(input("Preço das compras: "))
print('''FORMAS DE PAGAMENTO
      [1] á vista dinheiro/cheque
      [2] a vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''')
option = int(input("Qual é a opção: "))
if option == 1:
  total = price - (price * 10 / 100)
  print("Sua compra será de R${} á vista".format(total))
elif option == 2:
  total = price - (price * 5 / 100)
  print("Sua compra será de R${} á vista no cartão".format(total))
elif option == 3:
  total = price
  installments = total / 2
  print("Sua compra será parcelada em 2x de R${:.2f}".format(installments))
elif option == 4:
  total = price + (price * 20 / 100)
  total_installments = int(input("Quantas parcelas: "))
  installments = total / total_installments
  print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(total_installments, installments))
  print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(price, total))
