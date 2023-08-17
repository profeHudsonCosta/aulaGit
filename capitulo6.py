#Script 6.1
'''
class Clientes:
    entrada = ""
    principal = ""
    sobremesa = ""
    bebidas = []

joaquim = Clientes()
ana = Clientes()

ana.entrada = "Salada"
joaquim.entrada = "Sopa"
print(joaquim.entrada)
'''

#Script 6.2
'''
class Clientes:
    entrada = ""
    principal = ""
    sobremesa = ""
    bebidas = []

    def setEntrada(self, entrada):
        self.entrada = entrada

    def getEntrada(self):
        return(self.entrada)

joaquim = Clientes()
joaquim.setEntrada("Salada")
print(joaquim.getEntrada())
'''

#Script 6.3 e Exercício 6.1
'''
class Cliente:
    entrada = ""
    principal = ""
    sobremesa = ""
    bebidas = []

    def setEntrada(self, entrada):
        self.entrada = entrada
    
    def getEntrada(self):
        return(self.entrada)
    
    def setPrincipal(self, principal):
        self.principal = principal

    def getPrincipal(self):
        return(self.principal)
    
    def setSobremesa(self, sobremesa):
        self.sobremesa = sobremesa

    def getSobremesa(self):
        return(self.sobremesa)
    
    def setBebidas(self, novaBebida):
        self.bebidas.append(novaBebida)

    def getBebidas(self):
        return(self.bebidas)
    
    def setMenu(self):
        self.setEntrada("Sopa")
        self.setPrincipal("Massa")
        self.setSobremesa("Sorvete")
        self.setBebidas("Vinho")
    
    def listaPedido(self):
        pedido = {"Entrada":self.getEntrada(), 
                "Principal":self.getPrincipal(),
                "Sobremesa":self.getSobremesa(),
                "Bebidas":self.getBebidas()}
        
        return(pedido)

joaquim = Cliente()
joaquim.setMenu()
print(joaquim.listaPedido())
'''
#Script 6.4
'''
class Pedido:
    descricao =""
    valor = 0
    def __init__(self) -> None:
        print("O pedido foi criado.")

pedido1 = Pedido()
'''

#Script 6.5
'''
class Pedido:
    descricao = ""
    valor = 0

    def __init__(self, descricao) -> None:
        self.descricao = descricao
        print("Pedido criado:", descricao)

pedido1 = Pedido("Pizza")
'''
#Exercicio 6.6
'''
class Som:
    frequencia = 0

    def setFreq(self, freq):
        self.frequencia = freq
    
    def getFreq(self):
        return(self.frequencia)

class NotaMusical(Som):
    nome = ""

    def __init__(self) -> None:
        super().__init__()
        print("Nota musical criada!")

    def setNome(self, nomeNota):
        self.nome = nomeNota
      
    def getNome(self):
        return(self.nome)


notaDo = NotaMusical()
notaDo.setFreq(132)
notaDo.setNome("Do")

notaRe = NotaMusical()
notaRe.setNome("Ré")
notaRe.setFreq(148)

notaMi = NotaMusical()
notaMi.setNome("Mi")
notaMi.setFreq(166.3)

notas = []

notas.append(notaDo)
notas.append(notaMi)
notas.append(notaRe)

for i in notas:
    print("Dados da nota: ")
    print("Nome: ", i.getNome())
    print("Frequencia: ", i.getFreq())
'''

#Script 6.9
'''
class minhaClasse:
    def __init__(self) -> None:
        self.nome = ""
        self.idade = -1

    def __str__(self) -> str:
        ret = "{0} ({1} anos)".format(self.nome, self.idade)
        return(ret)

mc = minhaClasse()
mc.nome = "João"
mc.idade = 51

print(mc)
'''

#Script 6.10

class minhaClasse:
    def __init__(self) -> None:
        self.nome = ""
        self.idade = -1
        self.sexo = ""
    
    def __repr__(self) -> str:
        ret = "[{0}, {1}, {2}]".format(self.nome, self.idade, self.sexo)

        return ret


mc = minhaClasse()
mc.nome = "Hudson"
mc.idade = 47
mc.sexo = "Masculino"

print(repr(mc))