#Crie uma classe Triangulo com os atributos lado1, lado2 e lado3. Adicione um método para verificar se é um triângulo válido e outro método para calcular a área.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def eh_triangulo_valido(self):
        return (self.lado1 + self.lado2 > self.lado3) and (self.lado1 + self.lado3 > self.lado2) and (self.lado2 + self.lado3 > self.lado1)

    def calcular_area(self):
        if self.eh_triangulo_valido():
            s = (self.lado1 + self.lado2 + self.lado3) / 2
            return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        else:
            return "Não é um triângulo válido"

triangulo1 = Triangulo(3, 4, 5)
print("Área do Triângulo:", triangulo1.calcular_area())
