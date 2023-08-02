'''
Fazer um algoritmo que pergunte 1 número e apresente:
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''

import math

print("")

a = int(input("Informe um número:"))

print("")

print("O número que você informou:", a, ", o quadrado é:", a * a, "e a raiz quadrada é:", float(math.sqrt(a)))