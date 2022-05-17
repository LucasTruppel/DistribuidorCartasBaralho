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

    def selecionar_quantidade_jogadores(self):
        pronto = False
        while not pronto:
            print('Quantas pessoas vão jogar?')
            quantidade_pessoas = input()
            if quantidade_pessoas.isnumeric() and quantidade_pessoas != '0':
                quantidade_pessoas = int(quantidade_pessoas)
                self.adicionar_jogadores(quantidade_pessoas)
                pronto = True
            else:
                print('Número inválido. Tente Novamente.\n')
        print()

    def comprar_carta(self, jogador):
        carta = self.baralho.cartas[0]
        jogador.mao.append(carta)
        self.baralho.cartas.remove(carta)
        self.baralho.quant_cartas -= 1

    def distribuir_todas_cartas(self):
        baralho_vazio = False
        while not baralho_vazio:
            for jogador in self.jogadores:
                if self.baralho.quant_cartas <= 0:
                    baralho_vazio = True
                    break
                self.comprar_carta(jogador)

    def distribuir_cartas_igualmente(self):
        while self.baralho.quant_cartas > 0 and self.baralho.quant_cartas >= self.quant_jogadores:
            for jogador in self.jogadores:
                self.comprar_carta(jogador)

    def selecionar_tipo_distribuicao(self):
        pronto = False
        while not pronto:
            print('Deseja distribuir todas cartas ou distribuí-las igualmente entre os jogadores?\n'
                  'Digite: 1 para todas cartas\n'
                  '        2 para igualmente')
            comando = input()
            if comando == '1':
                self.distribuir_todas_cartas()
                pronto = True
            elif comando == '2':
                self.distribuir_cartas_igualmente()
                pronto = True
            else:
                print('Número inválido. Tente Novamente.\n')
        print()

    def mostrar_maos_jogadores(self):
        for pessoa in self.jogadores:
            print(f'Jogador {pessoa.numero}:')
            for carta in pessoa.mao:
                print(carta.numero, carta.naipe)
            print()

    def jogar(self):
        self.selecionar_quantidade_jogadores()
        self.baralho.embaralhar()
        self.selecionar_tipo_distribuicao()
        self.mostrar_maos_jogadores()
        self.baralho.mostrar_baralho()
