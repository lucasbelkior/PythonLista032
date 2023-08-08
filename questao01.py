'''
 Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''



conta = int(input(("Qual o valor a ser pago?")))

valor = (conta*10/100)+100

print("O valor a ser pago é:",conta,"+ 10% de acrescimo do garçom")
print("Assim totalizando:",valor, "Reais")
