#Crie uma função dobrar_elementos que dobre o valor de todos os elementos de uma lista usando map.

dobrar_elementos = lambda lista: list(map(lambda x: x * 2, lista))
numeros = [1, 2, 3, 4, 5]
resultado = dobrar_elementos(numeros)
print(resultado)
