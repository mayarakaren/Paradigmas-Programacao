#Crie uma função mapear_palavras que receba uma lista de palavras e retorne uma lista com o comprimento de cada palavra.

mapear_palavras = lambda lista: list(map(lambda x: len(x), lista))
palavras = ["python", "java", "javascript", "ruby"]
resultado = mapear_palavras(palavras)
print(resultado)
