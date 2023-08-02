'''
Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.
'''

a = int(input("Qual o seu salário?"))

aum = 0.15

tot = float(a + (a * aum))

print("Aqui está o valor do seu salário depois do aumento: R$", tot )