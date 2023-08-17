'''
Numero = int(input("Entre com o número: "))

Resposta = "O número é par"

if (Numero % 2 == 1):
    Resposta = "O número é impar"

print(Resposta)

a = int(input("Digite um número entre 0 e 10: "))

print(a)

if (a >= 0) and (a < 4):
    print("O númro qu você  dditou é maior ou igual a 0 e meor que 4")
elif (a >= 4) and (a < 8):
    print("O número que você digitou é maior ou igual a 4 e menor que 8")
else:
    print("O número que você digitou é maior ou igual a 8")
'''

#Pedra-papel-tesoura sem dicionário
'''
from random import randint

print("Jogo Pedra-Papel-Tesoura")
print("Digite 1 para jogar Pedra, 2 para Pape e 3 para jogar Tesoura")
jog = input("Escolha sua jogada: ")
jog = int(jog)
jog_comp = randint(1,3)
print("Computador jogou", jog_comp)
if(jog == jog_comp):
    print("Empate")
elif((jog== 1) and (jog_comp == 3)) or ((jog == 2) and (jog_comp==1)) or ((jog== 3) and (jog_comp == 2)):
    print("Você ganhou!")
else:
    print("Você perdeu :-(")
'''

#Pedra-papel-tesoura com dicionpario
'''
regras_empate = {1:1, 2:2, 3:3}
regras_ganha = {1:3, 2:1, 3:2}

print("Jogo Pedra-Papel-Tesoura")
print("Digite 1 para jogar Pedra, 2 para Papel e 3 para jogar Tesoura")
jog = input("Escolha sua jogada: ")
jog = int(jog)

print(jog)
print(regras_empate[jog])

jog_comp = randint(1,3)
print("Computador jogou", jog_comp)
if (regras_empate[jog] == jog_comp):
    print("Empate")
elif (regras_ganha[jog] == jog_comp):
    print("Você ganhou!")
else:
    print("Você perdeu!")
'''

#Exercicio 3.1
'''
v01 = int(input("Informe o 1o valor: "))
v02 = int(input("Informe o 2o valor: "))
v03 = int(input("Informe o 3o valor: "))

if (v01 < v02) and (v01 < v03):
    print("O menor valor é: ", v01)
elif (v02 < v03) and (v02 < v03):
    print("O menor valor é: ", v02)
else: 
    print("O menor valor é ", v03)
'''
#Exercício 3.3
'''
val01 = int(input("Informe o 1o valor: "))
val02 = int(input("Informe o 2o valor: "))
val03 = int(input("Informe o 3o valor: "))

if (val01 < val02) and (val02 < val03):
    print(val01, " - ", val02, " - ", val03)
elif (val01 < val03) and (val03 < val02):
    print(val01, " - ", val03, " - ", val02)
elif (val02 < val01) and (val01 < val03):
    print(val02, " - ", val01, " - ", val03)
elif (val02 < val03) and (val03 < val01):
    print(val02, " - ", val03, " - ", val01)
elif(val03 < val01) and (val01 < val02):
    print(val03, " - ", val01, " - ", val02)
elif (val03 < val02) and (val02 < val01):
    print(val03, " - ", val02, " - ", val01)
'''
#Exercício 3.4
'''
lado01 = int(input("Informe o 1o lado: "))
lado02 = int(input("Informe o 2o lado: "))
lado03 = int(input("Informe o 3o lado: "))

if (lado03 < lado01 + lado02) and (lado02 < lado01 + lado02) and (lado01 < lado02 + lado03):
    if(lado01 == lado02) and (lado02 == lado03):
        print("Triangulo Equilátero")
    elif((lado01 == lado02) and (lado01 != lado03)) or ((lado03 == lado02) and (lado02 != lado01)) or ((lado01 == lado03) and (lado01 != lado02)):
        print("Triângulo Isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Os valores informados não correspondem a um triâgulo")
'''
#Exercício 3.5
'''
import math 

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))

if (a != 0):
    delta = b**2 - 4*a*c
    print("O delta vale: ", delta)
    if (delta > 0):
         x1 = int((-b - math.sqrt(delta))/2*a)
         x2 = int((-b + math.sqrt(delta))/2*a)

         print("As raizes da equação são: ")
         print("X1: ", x1)
         print("X2: ", x2)
    elif (delta == 0):
         x = int((-b + math.sqrt(delta))/2*a)
         print("A raíz da equação é: ", x)
    else:
        print("Não há raizes reais para a equação!")
else:
        print("Valores não pertencem a uma equação do 2o Grau")
'''

#script 3.6
'''
from random import randint

num_sorteado = randint(1,100)

num_tentativas_max =  10

num_tentativas = 0

num_digitado = 0

while (num_tentativas < num_tentativas_max) and (num_sorteado != num_digitado):
    print("Você tem ", num_tentativas_max - num_tentativas, " chances.")
    num_digitado = int(input("Qual o número escolhido pelo computador: "))
    num_tentativas += 1

    if (num_sorteado < num_digitado):
        print("O número sorteado é menor que ", num_digitado)
    elif (num_sorteado > num_digitado):
        print("O número sorteado é maior que ", num_digitado)

if (num_sorteado == num_digitado):
    print("Parabéns, você acertou o número escolhido pelo computador em ", num_tentativas, " vezes.")
else:
    print("Não foi desta vez. Você perdeu. Não acertou o número escolhido")
'''
#Exercicio 3.6
'''
num = 0
soma = 0
cont = 0
maior = 0
menor = 0

while (num >= 0):
    num = int(input("Informe um número inteiro positivo ou -1 para encerrar o laço: "))
    if (cont == 0):
        menor = num

    if (num >= 0):
        cont = cont + 1
        soma = soma + num
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num

media = soma/cont

print("Soma dos números inseridos: ", soma)
print("Média dos números inseridos: ", media)
print("Maior número inserido: ", maior)
print("Menor número inserido: ", menor)
'''

#Exercicio 3.7
'''
num = int(input("Informe um número inteiro positivo: "))
cont = num
cont2 = 0

while (cont > 0):
    resto = num % cont
    if (resto == 0):
        cont2 = cont2 + 1
    
    cont = cont - 1

if (cont2 > 2):
    print("O número ", num, "não é primo.")
    print("O número ", num, "é divisível por ", cont2, "números.")
else:
    print("O numero ", num, "é primo")
'''
#script 3.7
'''
for x in range(4):
    print(x, end=" ")

print()

for x in range(1,4):
    print(x, end=" ")

print()

for x in range(1,8,2):
    print(x, end = " ")

print()

for x in range(8,1, -2):
    print(x, end=" ")
'''

#script 3.8
'''
for x in range(3):
    for y in range(3):
        if (x <= y):
            break
        print(x,y)
'''
#exercicio 3.12
'''
fat = 1
num = int(input("Informe um número natural positivo: "))

for num in range(num, 0, -1):
    fat = (num*fat)

print(fat)
'''

#exercicio 3.14
periodo = int(input("Informe o período do investimento: "))
taxa = float(input("Informe a taxa de juros aplicada: "))
valor = float(input("Informe o valor investido: "))
for x in range(periodo):
    print(x, "o mês")
    print("Juros simples: ")
    vf = valor * (1 + taxa * x)
    print(vf)

    print("Juros compostos: ")
    vf = valor * (1 + taxa)**x
    print(vf)
