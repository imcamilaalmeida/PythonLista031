'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é
c = (f – 32) x 5 : 9 , onde
c é a temperatura
em graus Celsius e
f em Fahrenheit.
'''

print("")

f = float(input("Informe uma temperatura graus Fahrenheit:"))

#c = (f – 32) x 5 : 9

c = (f - 32) * 5 / 9

print("")

print("A temperatura convertida em graus Celsius é de:", c, "ºC")