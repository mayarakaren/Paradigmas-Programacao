#Escreva uma função somar_elementos que use a função reduce para somar todos os elementos de uma lista.

from functools import reduce

somar_elementos = lambda lista: reduce(lambda x, y: x + y, lista)
numeros = [1, 2, 3, 4, 5]
resultado = somar_elementos(numeros)
print(resultado)
