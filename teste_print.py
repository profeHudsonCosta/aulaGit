texto = input("Informe uma string qualquer: ")
contA = texto.count("a")
contE = texto.count("e")
contI = texto.count("i")
contO = texto.count("o")
contU = texto.count("u")

totalDeVogais = contA + contE + contI + contO + contU

print("a: ", contA)
print("e: ", contE)
print("i: ", contI)
print("o: ", contO)
print("u: ",contU)

print("==========================")

print("O total de vogais na string " + texto + " é ", totalDeVogais)
print(texto.upper())

print("==========================")
print("Descriptografia")
entrada = input("Informe uma string criptografada na lingua do P: ")
saida = entrada.replace("PÊ", "")
print(entrada)
print(saida)

