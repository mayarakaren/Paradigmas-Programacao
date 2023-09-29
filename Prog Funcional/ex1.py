#Crie uma função lambda que eleve todos os elementos de uma lista ao quadrado.

quadrado = lambda x: x ** 2
lista = [1, 2, 3, 4, 5]
resultado = list(map(quadrado, lista))
print(resultado)
