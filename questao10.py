'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula
prestação =
valor + (valor x (taxa : 100) x tempo em dias).
'''

print("")

valor = float(input("Qual o valor da sua prestação?"))

print("")

tempo = float(input("Qual a quantidade de dias de atraso?"))

print("")

taxa = float(input("Qual a taxa?"))

print("")

tot = valor + (valor * (taxa / 100) * tempo)

print("O valor da sua prestação em atraso é de: R$", tot)