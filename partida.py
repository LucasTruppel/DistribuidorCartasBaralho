from baralho import Baralho
from pessoa import Pessoa


class Partida:
    def __init__(self):
        self.baralho = Baralho()
        self.jogadores = []
        self.quant_jogadores = 0

    def adicionar_jogadores(self, quantidade):
        for i in range(quantidade):
            self.quant_jogadores += 1
            self.jogadores.append(Pessoa(self.quant_jogadores))

    '''
    def distribuir_cartas(self):
        ultimo_jogador = 0
        while self.baralho.quant_cartas > 0:
            carta = self.baralho.cartas[0]
            if ultimo_jogador >= self.quant_jogadores:
                ultimo_jogador = 0
            jogador = self.jogadores[ultimo_jogador]
            jogador.mao.append(carta)
            self.baralho.cartas.remove(carta)
            self.baralho.quant_cartas -= 1
            ultimo_jogador += 1
    '''

    def distribuir_cartas(self):
        while self.baralho.quant_cartas > 0 and self.baralho.quant_cartas >= self.quant_jogadores:
            for jogador in self.jogadores:
                carta = self.baralho.cartas[0]
                jogador.mao.append(carta)
                self.baralho.cartas.remove(carta)
                self.baralho.quant_cartas -= 1

    def mostrar_maos_jogadores(self):
        for pessoa in self.jogadores:
            print(f'Jogador {pessoa.numero}:')
            for carta in pessoa.mao:
                print(carta.numero, carta.naipe)
            print()
