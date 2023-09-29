#Crie uma classe Aluno com os atributos nome e notas. Adicione métodos para calcular a média das notas e verificar se o aluno foi aprovado (média >= 7).

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 7:
            return f"{self.nome} foi aprovado com média {media}"
        else:
            return f"{self.nome} foi reprovado com média {media}"

aluno1 = Aluno("Maria", [8, 7, 9])
print(aluno1.verificar_aprovacao())
