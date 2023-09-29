#Crie uma classe Calendario que representa uma data com os atributos dia, mes e ano. Adicione um método para verificar se a data é válida.

class Calendario:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def data_valida(self):
        if 1 <= self.mes <= 12:
            if self.mes in [4, 6, 9, 11]:
                return 1 <= self.dia <= 30
            elif self.mes == 2:
                if (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0):
                    return 1 <= self.dia <= 29
                else:
                    return 1 <= self.dia <= 28
            else:
                return 1 <= self.dia <= 31
        else:
            return False

data1 = Calendario(29, 2, 2020)
data2 = Calendario(31, 4, 2022)
print("Data 1 válida?", data1.data_valida())
print("Data 2 válida?", data2.data_valida())
