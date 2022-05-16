from partida import Partida

# O código embaralha as cartas do baralho e distribui igualmente entre os jogadores.

# Seleção da quantidade de jogadores.
pronto = False
while not pronto:
    print('Quantas pessoas vão jogar?')
    quantidade_pessoas = input()
    if quantidade_pessoas.isnumeric() and quantidade_pessoas != '0':
        quantidade_pessoas = int(quantidade_pessoas)
        pronto = True
    else:
        print('Número inválido. Tente Novamente.\n')

# Embaralha e distribui as cartas.
partida = Partida()
partida.adicionar_jogadores(quantidade_pessoas)  # Seleciona a quantidade de jogadores.
partida.baralho.embaralhar()
partida.distribuir_cartas()
partida.mostrar_maos_jogadores()
partida.baralho.mostrar_baralho()

print('Digite algo para fechar:')
input()
