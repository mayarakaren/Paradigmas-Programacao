#Escreva uma função filtrar_pares que receba uma lista de números e retorne apenas os números pares.

filtrar_pares = lambda lista: list(filter(lambda x: x % 2 == 0, lista))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = filtrar_pares(numeros)
print(resultado)
