'''
 Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros
'''

peso = int(input("Qual e o seu peso em quilogramas?:"))
altura = float(input("Qual e a sua altura em metros?:"))
imc2 = peso/(altura*altura)

print("O seu imc será:",imc2)


