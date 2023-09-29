#Crie uma classe Livro com os atributos titulo, autor e ano. Crie uma subclasse Ebook com um atributo adicional formato. Crie um método para exibir as informações do livro ou do ebook.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_info(self):
        print(f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}")

class Ebook(Livro):
    def __init__(self, titulo, autor, ano, formato):
        super().__init__(titulo, autor, ano)
        self.formato = formato

    def exibir_info(self):
        print(f"Ebook: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Formato: {self.formato}")

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
ebook1 = Ebook("Python Crash Course", "Eric Matthes", 2019, "PDF")
livro1.exibir_info()
ebook1.exibir_info()
