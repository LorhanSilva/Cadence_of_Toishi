from PPlay.sprite import *
import random
'''Funçoes para gerar spolios de conquista no jogo'''
'''primeiro 1: arma, 2: artefato, 3: pocao
   armas 1: espada, 2: arco, 3: cetro'''


def gera_item_bau(itens, bonus_iten):
    p1 = random.randint(1, 3)
    bonus = random.randint(1, 4) * 100
    if p1 == 1:
        tipo = random.randint(1, 3)
        itens.append(p1*10 + tipo)
        bonus_iten.append(bonus + 2)
    elif p1 == 2:
        itens.append(p1)
        bonus_iten.append(bonus + 3)
    elif p1 == 3:
        itens.append(p1)
        bonus_iten.append(100)


def iten_inicial(itens, bonus):
    it = open("SAVES/save_itens.txt", 'r')
    tmp = it.readlines()
    for i in tmp:
        itens.append(int(i[:i.index("/")]))
        bonus.append(int(i[i.index("/")+1:].strip()))
    it.close()
