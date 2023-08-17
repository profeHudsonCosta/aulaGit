#Script 5.1
'''
def soma(a,b):
    return(a + b)

a = 12

numero1 = 1
numero2 = 2

print(soma(numero1, numero2))
'''

#Script 5.2
'''
def ola():
    print("Olá mundo!")

ola()
'''

#Script5.3
'''
def incremento(n):
    print(n + 1)

incremento(1)

#Script5.5
def polinomio(a, b, c, x):
    ret = (a*x)**2 + b*x + c
    print(ret, end=" - ")

polinomio(1,2, 3, 1)
polinomio(a=1, b=2, c=3, x=1)
polinomio(b=2, a=1, c=3,x=1)
'''

#Script 5.6
'''
def multiplica(a,b =2):
    print(a*b)

multiplica(3,3)
multiplica(3)
'''

#SCript 5.7
'''
def multiplicaTudo(*n, c):
    print(n)
    ret = 1
    for i in n:
        ret = ret * i
    ret = ret + c
    print(ret)

multiplicaTudo(1, 2, 3, 4, c=10)
'''

#Script 5.8
'''
def funcao1(x):
    x = x + 1

def funcao2(x):
    x[0] = x[0] + 1

x = 10
funcao1(x)
print("O Valor de X: ", x)

x = [10]
funcao2(x)
print("Valor de x: ", x)
'''

#Script 5.9
'''
def perde_escopo(x):
    print("Posição na memória onde está armazenado x: ", hex(id(x)))
    x[0] = 100
    print("Posição na memória onde está armazenado x: ", hex(id(x)))

    x = -1
    x = [200]
    print("Posição na memória onde está armazenado x: ", hex(id(x)))

x = [1]
print("Posição inicial onde x está armazenado: ", hex(id(x)))
perde_escopo(x)
'''

#Script 5.13
'''
def recursivo(val):
    print("Função chamada. val = ", val)
    if val == 1:
        print("Função retorna ", 1)
        return 1
    else:
        resposta = val + recursivo(val - 1)
        print("Função retorna ", resposta)
        return(resposta)

print(recursivo(5))
'''

def media(a, b):
    return (a + b)/2

n1 = int(input("Informe o 1o número: "))
n2 = int(input("Informe o 2o número: "))

mn1n2 = media(n1, n2)

print("A média dos números informados é: ", mn1n2)
