#Crie uma classe Funcionario com atributos nome e salario. Crie uma subclasse Gerente que tenha um atributo adicional bonus. Sobrescreva o método calcular_salario() na classe Gerente para incluir o bônus.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_salario(self):
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario + self.bonus

gerente1 = Gerente("Carlos", 5000, 1000)
print("Salário do Gerente:", gerente1.calcular_salario())
