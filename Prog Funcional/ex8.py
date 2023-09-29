#Escreva uma função calcular_media que calcule a média de uma lista de números usando a função reduce.

from functools import reduce

calcular_media = lambda lista: reduce(lambda x, y: x + y, lista) / len(lista)
notas = [7.5, 8.0, 6.5, 9.0, 8.5]
resultado = calcular_media(notas)
print(resultado)
