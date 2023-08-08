'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês
'''

nome= input("Ola vendedor,qual o seu nome?:")
salario = int(input("Qual o seu salario fixo?:"))
total = int(input("Qual o seu total de vendas feitas no mes em dinheiro?:"))
comissao = (total*15/100)+100
salariocompleto = salario+comissao

print("Vendedor", nome)
print("O seu salario fixo e",salario)
print("A comissao será",comissao)
print("o salario completo e",salariocompleto)
