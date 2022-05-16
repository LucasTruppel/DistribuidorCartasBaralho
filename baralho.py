import random
from carta import Carta


class Baralho:
    def __init__(self):
        self.cartas = []
        self.quant_cartas = 52
        self.numeros = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.naipes = ['copas', 'espadas', 'ouros', 'paus']

        for naipe in self.naipes:
            for numero in self.numeros:
                self.cartas.append(Carta(numero, naipe))

    def mostrar_baralho(self):
        if self.quant_cartas == 0:
            print('Nenhuma carta no baralho.')
        else:
            print('Cartas no baralho:')
            for carta in self.cartas:
                print(carta.numero, carta.naipe)
        print()

    def embaralhar(self):
        random.shuffle(self.cartas)
