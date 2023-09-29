#Crie uma classe Retangulo com os atributos largura e altura. Adicione métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

retangulo1 = Retangulo(5, 3)
print("Área:", retangulo1.calcular_area())
print("Perímetro:", retangulo1.calcular_perimetro())
