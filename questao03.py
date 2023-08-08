'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros
'''

peso = int(input("Qual e o seu peso em quilogramas?:"))
altura = float(input("Qual e a sua altura em metros?:"))
gm = peso*1000
cm = altura*100

print("O seu peso em gramas será:",gm)
print("A sua altura em centimetros será:",cm,)


