'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número
'''

a= int(input("Informe um numero:"))
b= int(input("Informe outro numero:"))
somados2 = a+b
sub12 = a-b
sub21 = b-a
multi = a*b
div = a/b
resto = a % b

print("a soma dos dois números é:",somados2)
print("a subtração do primeiro pelo segundo número é:",sub12)
print("a subtração do segundo pelo primeiro número é", sub21)
print(" a multiplicação entre os dois números é", multi)
print("a divisão do primeiro pelo segundo número é",div,"Com resto",resto)
