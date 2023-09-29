#Crie uma classe Pessoa com os atributos nome e idade. Crie uma subclasse Aluno que tenha um atributo adicional matricula. Crie um método para exibir as informações da pessoa ou do aluno.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}")

pessoa1 = Pessoa("Ana", 25)
aluno1 = Aluno("João", 20, "2023001")
pessoa1.exibir_info()
aluno1.exibir_info()
