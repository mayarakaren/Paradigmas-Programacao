#Implemente uma função filtrar_vogais que receba uma string e retorne uma nova string contendo apenas as vogais.

filtrar_vogais = lambda s: ''.join(filter(lambda x: x in 'aeiouAEIOU', s))
texto = "Programação Funcional"
resultado = filtrar_vogais(texto)
print(resultado)
