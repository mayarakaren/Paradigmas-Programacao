#Crie uma classe Animal com métodos falar() e correr(). Crie subclasses Cachorro e Gato que sobrescrevem o método falar() para emitir sons diferentes.

class Animal:
    def falar(self):
        pass

    def correr(self):
        print("Animal está correndo")

class Cachorro(Animal):
    def falar(self):
        print("Cachorro late")

class Gato(Animal):
    def falar(self):
        print("Gato mia")

cachorro1 = Cachorro()
gato1 = Gato()
cachorro1.falar()
gato1.falar()
