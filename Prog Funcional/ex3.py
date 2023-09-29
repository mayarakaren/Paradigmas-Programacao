#Implemente uma função recursiva para calcular o fatorial de um número.

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(5)
print(resultado)
