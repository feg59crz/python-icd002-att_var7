#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 16:07:35 2023

@author: fernando.cruz7
"""

while True:
    try:
        arroz = 5 * float(input("Digite o preço do quilo de arroz: "))
        feijão = 3 * float(input("Digite o preço do quilo de feijão: "))
        açúcar = 2 * float(input("Digite o preço do quilo de açúcar: "))
        batata = 3 * float(input("Digite o preço do quilo de batata: "))
        óleo = 5 * float(input("Digite o preço do litro de óleo: "))
        agua_sal = 1 * float(input("Digite o preço do pacote de bolacha de água e sal: "))
        maizena = 1 * float(input("Digite o preço do pacote de bolacha maizena: "))
        banana = 1.5 * float(input("Digite o preço da dúzia de banana: "))
        couveflor = 2 * float(input("Digite o preço do maço de couve-flor: "))
        leite_pó = 2 * float(input("Digite o preço da lata de leite em pó: "))
        break
    except Exception:
        print(Exception)
        continue
print("")
while True:
    try:
        limite = float(input("Digite o valor limite do pagamento em dinheiro: "))
        break
    except Exception:
        print(Exception)
        continue

print("")
print("O preço dos 5kg de arroz é R$ "+ "{:.2f}".format( arroz ))
print("O preço dos 3kg de feijão é R$ "+ "{:.2f}".format( feijão ))
print("O preço dos 2kg de açúcar é R$ "+ "{:.2f}".format( açúcar ))
print("O preço dos 3kg de batata é R$ "+ "{:.2f}".format( batata ))
print("O preço dos 5L de óleo é R$ "+ "{:.2f}".format( óleo ))
print("O preço do pacote de bolacha de água e sal é R$ "+ "{:.2f}".format( agua_sal ))
print("O preço do pacote de bolacha maizena é R$ "+ "{:.2f}".format( maizena ))
print("O preço de uma dúzia e meia de banana é R$ "+ "{:.2f}".format( banana ))
print("O preço de dois maços de couve-flor é R$ "+ "{:.2f}".format( couveflor ))
print("O preço de duas latas de leite em pó é R$ "+ "{:.2f}".format( leite_pó ))
print("")

valor_total = arroz + feijão + açúcar + batata + óleo + agua_sal
valor_total += maizena + banana + couveflor + leite_pó
print("")
print("Valor total da compra: R$ "+ "{:.2f}".format( valor_total ))
print("")
if valor_total <= limite:
    print("Pagamento em Dinheiro!")
else:
    print("Pagamento em parcelas com uso de cartão")
    
