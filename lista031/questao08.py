'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro.
'''

print("")

a = int(input("Informe a distância a percorrer na viagem, em quilômetros:"))

b = int(input("Agora, informe o valor do consumo médio do automóvel, em quilômetros por litro:"))

quant = a / b

print("")

print("A quantidade de litros que ele gastará nessa viagem é de:", quant, "litros")