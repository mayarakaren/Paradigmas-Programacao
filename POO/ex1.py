#Crie uma classe chamada Carro com os atributos marca, modelo e ano. Adicione um método para imprimir as informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def imprimir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

carro1 = Carro("Ford", "Focus", 2020)
carro1.imprimir_info()
