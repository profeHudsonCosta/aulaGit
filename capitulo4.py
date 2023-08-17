#Script 4.1
'''
Tupla1 = ("1", "2", "3", "4", "5")
Tupla2 = ("A",)
NaoEhTupla = ("A")

print("Tupla 1: ", Tupla1)
print("A Tupla 1 é do tipo: ", type(Tupla1))
print("Tupla 2: ", Tupla2)
print("A Tupla 2 é do tipo: ", type(Tupla2))
print("O tamanho da Tupla 1 é: ", len(Tupla1))

print("Não é tupla: ", NaoEhTupla)
print("NaoEhTupla é do tipo: ", type(NaoEhTupla))
print("O tamanho da variável NaoEhTupla é: ", len(NaoEhTupla), "\n")
'''

#Script 4.2
'''
Tupla1 = ('5', '6', '8', '1')

print("Tupla 1: ", Tupla1)
print("O primeiro elemento da Tupla 1 é: ", Tupla1[0])
print("O primeiro elemento da Tupla1 é do tipo: ", type(Tupla1[0]))
print("O segundo elemento da Tupla 1 é: ", Tupla1[1])
print("Imprime o primeiro e o segundo elemento da Tupla1: ", Tupla1[:2], "\n")
print("O último elemento da Tupla1 é: ", Tupla1[-1])
print("O penúltimo elemento da Tupla1 é ", Tupla1[-2])
print("Imprime o penúltimo e o último elemento da Tupla1: ", Tupla1[-2:])
print("Tupla1 em ordem inversa é: ", Tupla1[::-1])
'''

#Script 4.3
'''
valor = int(input("Entre com o valor desejado para saque: "))

notas = (100, 50, 20, 10, 5)

notas100 = int(valor/notas[0])
valor = valor % notas[0]
print("Entregar ", notas100, "notas de ", notas[0])
notas50 = int(valor/notas[1])
valor = valor % notas[1]
print("Entregar ", notas50, "notas de ", notas[1])
notas20 = int(valor/notas[2])
valor = valor % notas[2]
print("Entregar ", notas20, "notas de ", notas[2])
notas10 = int(valor/notas[3])
valor = valor %notas[3]
print("Entregar ", notas10, " notas de ", notas[3])
notas5 = int(valor/notas[4])
valor = valor % notas[4]
print("Entregar ", notas5, " notas de ", notas[4])
'''

#Script 4.4
'''
valor = int(input("Entre com o valor desejado para saque: "))
notas = (100, 50, 20, 10, 5)

for i in range(0, len(notas)):
    quantidade = int(valor/notas[i])
    valor = valor % notas[i]
    if quantidade != 0:
        print(i + 1, "- Entregar ", quantidade, "notas de ", notas[i])
'''
#Script 4.5
'''
valor = int(input("Entre com o valor desejado para saque: "))
notas = (100, 50, 20, 10, 5)
i = 0
while (i < len(notas)):
    quantidade = int(valor/notas[i])
    valor = valor % notas[i]
    if quantidade != 0:
        print(i + 1, "- Entregar ", quantidade, "notas de ", notas[i])
    i = i + 1
'''

#script 4.6
'''
valor = int(input("Entre com o valor desejado para saque: "))
notas = (100, 50, 20, 10, 5)

for nota in notas:
    quantidade = int(valor/nota)
    valor = valor % nota
    if quantidade != 0:
        print("Entregar ", quantidade, " notas de ", nota)
'''

#Script 4.7
'''
tupla = ("A", "B", "C")

for i, v in enumerate(tupla):
    print(i, " - ", v)
'''

#Exercicio 4.1
'''
entrada = (1000, 2000, 5, 15000, 12, 1, 0.5, -2, 1000)
soma =0

for valor in entrada:
    if valor < 100:
        soma = soma + valor
print("A soma dos números menores que 100 é ", soma)
'''

#Exercício 4.2
'''
import math

Vendas = (120, 130, 100, 110, 90, 120, 111, 80, 140, 120, 90, 120)

media = 0
variancia = 0
desvio = 0
soma = 0
somaVari = 0
quantVendas = len(Vendas)

for venda in Vendas:
    soma = soma + venda

media = soma/quantVendas

#Calculo da variância
for venda in Vendas:
    somaVari = somaVari + (venda - media)**2

variancia = somaVari/len(Vendas)

desvio = math.sqrt(variancia)

print("Valor médio das vendas: ", media)
print("A variância das vendas é: ", variancia)
print("O desvio padrão das vendas é: ", desvio)
'''

#Script 4.8
'''
a = [1, 2, 3]
b = ["Maria", 13.7, 8]
c = [[1, "Maçã"], [2, "Banana"]]

print(b[0])
d = a[2]
e = c[0]
print(e)
f = e[0]
g = c[0][0]
print(f,g)
'''

#Script 4.9
'''
tabela = [[1, "Paulo", 2.5],
          [2, "Maria", 12],
          [3, "José", 27]]

tempo_Paulo = tabela[0][2]
tempo_Maria = tabela[1][2]
tempo_Jose = tabela[2][2]

fim_Paulo = tempo_Paulo
fim_Maria = fim_Paulo + tempo_Maria
fim_Jose = fim_Maria + tempo_Jose

print("O pedido do Paulo termina em ", fim_Paulo)
print("O pedido da Maria termina em ", fim_Maria)
print("O pedido do José termina em ", fim_Jose)
'''

#Script 4.11
'''
tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]

for aluno in tabela:
    print(aluno[0])
print("--------------------")
for nome, frequencia, notafinal in tabela:
    print(nome, frequencia, notafinal)
'''

#Exercício 4.3
''''
tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]
for aprovados in tabela:
    if aprovados[1] >= 75 and aprovados[2] >= 60:
        print(aprovados[0])
'''

#exercício 4.4
'''
cont = 0
tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]
for reprovados in tabela:
    if reprovados[1] < 75 and reprovados[2] < 60:
        cont = cont + 1

print(cont, " alunos ficaram reprovados")
'''

#Exercício 4.5
'''
tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]
contRepNotas = 0
contRepFaltas = 0

for reprovados in tabela:
    if (reprovados[1] < 75):
        contRepFaltas = contRepFaltas + 1
    
    if (reprovados[2] < 60):
        contRepNotas = contRepNotas + 1

percNotas = (len(tabela)*contRepNotas)/100
percFreq = (len(tabela) * contRepFaltas)/100

print("Reprovados por faltas: ", contRepFaltas)
print("Reprovados notas: ", contRepNotas)
print("Percentual de alunos reprovados por nota: ", percNotas, "%")
print("Percentaul de alunos reprovados por falta: ", percFreq, "%")
'''
#Exercício 4.6
'''
tabela = [["Alexandre", 90, 80], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]

maiorNota = tabela[0][2]
alunoMaiorNota = tabela[0][0]

for buscaMaior in tabela:    
    if buscaMaior[2] > maiorNota:
        maiorNota = buscaMaior[2]
        alunoMaiorNota = buscaMaior[0]

print("A maior nota foi ", maiorNota, "e o aluno que tirou ela foi: ", alunoMaiorNota)
'''

#Exercício 4.7
'''
import math

tabela = [["Alexandre", 90, 100], ["Bruna", 100, 95], ["Diego", 30, 80], ["Felipe", 40, 10], ["Gabriela", 75, 60]]

somaNotas = 0
contRep = 0
somaNotasVar = 0

for media in tabela:
    somaNotas = somaNotas + media[2]
    if (media[1] < 75) and (media[2] < 60):
        contRep = contRep +1

#print(len(tabela))
#print(somaNotas)
media = somaNotas/len(tabela)
for vari in tabela:
    somaNotasVar = somaNotasVar + (vari[2] - media)**2

variancia = somaNotasVar/len(tabela)

desvioPadrao = math.sqrt(variancia)

percRep = (len(tabela)*contRep)/100

print("A média aritimética da turma é: ", media)
print("O desvio padrão da turma é: ", desvioPadrao)
print("O percentual de reprovações é: ", percRep, "%")
'''

#Script 4.13
'''
listaVazia = []
listaVazia.append(1)
listaVazia.append(4)
listaVazia.append(92)

print(listaVazia)
'''
#Script 4.14
'''
Matriz =[]

N = int(input("Entre com o número de linhas da matriz: "))
M = int(input("Entre com o número de colunas da matriz: "))

for i in range(0,N):
    Matriz.append([])
    for j in range(0,M):
        el = int(input("Entre com o elemento da linha " + str(i+1) + " e coluna " + str(j + 1) + ": "))
        Matriz[i].append(el)

print(Matriz)
'''

#Exercio 4.8
'''
Matriz =[]

N = int(input("Entre com o número de linhas da matriz: "))
M = int(input("Entre com o número de colunas da matriz: "))

for i in range(0,N):
    Matriz.append([])
    for j in range(0,M):
        el = int(input("Entre com o elemento da linha " + str(i+1) + " e coluna " + str(j + 1) + ": "))
        Matriz[i].append(el)
        print(Matriz)
'''
#Exercicio 4.9
'''
MatrizA =[]

N = int(input("Entre com o número de linhas da matriz: "))
M = int(input("Entre com o número de colunas da matriz: "))

for i in range(0,N):
    MatrizA.append([])
    for j in range(0,M):
        el = int(input("Entre com o elemento da linha " + str(i+1) + " e coluna " + str(j + 1) + ": "))
        MatrizA[i].append(el)

for elem in MatrizA:
    print(elem)
'''
#Exercio 4.10
'''
MatrizA = []
MatrizT = []

L = int(input("Informe o número de linhas da Matriz A: "))
C = int(input("Informe o número de colunas da Matriz A: "))

for i in range(0,L):
    MatrizA.append([])
    for j in range(0,C):
        el = int(input("Entre com o elemento da linha " + str(i+1) + " e coluna "+ str(j + 1) + ": "))
        MatrizA[i].append(el)

print("Matriz A")
for elem in MatrizA:
    print(elem)

for i in range(0,C):
    MatrizT.append([])
    for j in range(0,L):
        MatrizT[i].append(MatrizA[j][i])

print("Matriz transposta de A")
for elem in MatrizT:
    print(elem)
'''

#Script 4.15
'''
A = [1, 5, 8, 3]

B = A

print("Lista B")
print(B)
A.reverse()
print("A lsiat B também inverteu a ordem")
print(B)

B = A.copy()

A.sort()

print("Lista A")
print(A)
print("Nota que não alterou a lista B")
print(B)
'''
#Exercicio 4.14
'''
listaAlunosNotas = []
quantAlunos = 0

quantAlunos = int(input("Informe a quantidade de alunos: "))

for aluno in range(0, quantAlunos):
    listaAlunosNotas.append([])
    print(aluno + 1,"o -", end="")
    nome = input("Informe o nome do aluno: ")
    nota = float(input("Informe a nota do aluno: "))
    listaAlunosNotas[aluno].append(nome)
    listaAlunosNotas[aluno].append(nota)

print("Exibição de acordo com a inserção:")
print("Alunos", end= " ")
print("\t Notas")
for i in listaAlunosNotas:
    print(i[0], end= " ")
    print("\t", i[1])

print("Exibição de acordo com o enunciado:")
print("Alunos", end= " ")
print("\t Notas")
listaAlunosNotas.reverse()
listaAlunosNotas.sort(reverse=True)
for i in listaAlunosNotas:
    print(i[0], end= " ")
    print("\t", i[1])
'''

#Script 4.16
'''
orig = ["1", "2", "3", "4"]
print(orig)
li = [int(i) for i in orig]
print(li)
'''

#Script 4.17
'''
listaOriginal = [1, 2, 3, 4]
print("Lista original: ", listaOriginal)
dobro = [2*i for i in listaOriginal]
print("Lista original multipliada por 2: ", dobro)

selec = [i for i in listaOriginal if i >= 3]
print("Lista original com os valores maior que 3: ", selec)
'''

#Script 4.18
'''
listaOrig = ["Maria", "Paulo", "João", "Maria", "Ana", "João"]

nomes = set(listaOrig)

print("A lista original possui os seguintes nomes: ")
print(listaOrig)

print("Removendo os repetidos, temos: ")
print(nomes)
'''

#Script 4.19
'''
dicionario = {"Caderno": 10,
              "Lapiseira":15,
              "Borracha":5}

print("O caderno custa R$ " + str(dicionario["Caderno"]))
print("A lapiseira custa R$ " + str(dicionario["Lapiseira"]))
print("A borracha custa R$ " + str(dicionario["Borracha"]))
'''

#Script 4.20
'''
dicVazio = {}
dicVazio["Caderno"] = 10
dicVazio["Lapiseira"] = 15
dicVazio["Borracha"] = 5

print(dicVazio)
'''

#Script 4.21
'''
dicionario = {"key1":15, "key2":10, "key3":128}

for k, v in dicionario.items():
    print(k, v)
'''

#Script 4.22 e exercício 4.16

dist = {1:{2:1, 3:2, 4:3, 5:4}, 
        2:{1:2, 5:3},
        3:{1:2, 4:2},
        4:{1:3, 5:1, 3:2},
        5:{1:4, 4:1, 2:3}}

print("A distância entre 5 e 4 é ", dist[5][4])

somaDist = 0
flag = 1
while flag != -1:
    p1 = int(input("Informe o 1o ponto: "))
    p2 = int(input("Informe o 2o ponto: "))
    somaDist = somaDist + dist[p1][p2]
    flag = int(input("Digite -1 para sair: "))

print("A distância percorrida é: ", somaDist)