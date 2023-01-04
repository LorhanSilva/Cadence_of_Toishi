from PPlay.window import *
from PPlay.sprite import *
from Statatus import vida_tx_mosntro
from Spolio import gera_item_bau
''''função que retorna todos os objetos do mapa em uma matriz'''


def mapa(n_mapa):
    if n_mapa == 1:
        mp = open("MAPAS/mapa.txt", 'r')
    elif n_mapa == 2:
        mp = open("MAPAS/mapa_2.txt", 'r')
    cood = mp.readlines()
    mat_mapa = []
    mini_m = []
    objetos = []
    mostros = []
    vida_monstro = []
    baus = []
    NPC = []
    tam_s = 128
    for i in range(len(cood)):
        tmp = []
        mini_tmp = []
        j = 0
        for ls in cood[i]:
            if ls == " ":
                textura = Sprite("sprites/bioma/grass_16/grama_tx_00.png", 1)
                textura.x = j * tam_s
                textura.y = i * tam_s
                tmp.append(textura)
            elif ls == "/":
                textura_00 = Sprite("sprites/bioma/ground_blue_yellow_16/limite_bioma_00.png", 1)
                textura_00.x = j * tam_s
                textura_00.y = i * tam_s
                objetos.append(textura_00)
                tmp.append(textura_00)
            elif ls == "-":
                estrada_01 = Sprite("sprites/bioma/brown_grass_16/estrada_terra_01.png", 1)
                estrada_01.x = j * tam_s
                estrada_01.y = i * tam_s
                tmp.append(estrada_01)
            elif ls == "+":
                areia_tx02 = Sprite("sprites/bioma/sand_16/areia_tx_02.png", 1)
                areia_tx02.x = j * tam_s
                areia_tx02.y = i * tam_s
                tmp.append(areia_tx02)
            elif ls == "=":
                areia_tx03 = Sprite("sprites/bioma/melt_16/areia_02.png", 1)
                areia_tx03.x = j * tam_s
                areia_tx03.y = i * tam_s
                tmp.append(areia_tx03)
            elif ls == "1":
                casa_01 = Sprite("sprites/construcoes/construcao_01.png", 1)
                casa_01.x = j * tam_s
                casa_01.y = i * tam_s - 384
                tmp.append(casa_01)
                objetos.append(casa_01)
                j -= 1
            elif ls == "2":
                casa_02 = Sprite("sprites/construcoes/construcao_02.png", 1)
                casa_02.x = j * tam_s
                casa_02.y = i * tam_s - 384
                tmp.append(casa_02)
                objetos.append(casa_02)
                j -= 1
            elif ls == "3":
                casa_03 = Sprite("sprites/construcoes/construcao_03.png", 1)
                casa_03.x = j * tam_s
                casa_03.y = i * tam_s - 384
                tmp.append(casa_03)
                objetos.append(casa_03)
                j -= 1
            elif ls == "4":
                casa_04 = Sprite("sprites/construcoes/construcao_04.png", 1)
                casa_04.x = j * tam_s
                casa_04.y = i * tam_s - 384
                tmp.append(casa_04)
                objetos.append(casa_04)
                j -= 1
            elif ls == "A":
                arvore_tx_00 = Sprite("sprites/bioma/arvore_tx_00.png", 1)
                arvore_tx_00.x = j * tam_s
                arvore_tx_00.y = i * tam_s - 256
                tmp.append(arvore_tx_00)
                objetos.append(arvore_tx_00)
                j -= 1
            elif ls == "M":
                monstro_01 = Sprite("sprites/monstros/mostro_01.png", 4)
                monstro_01.set_total_duration(800)
                monstro_01.x = j * tam_s
                monstro_01.y = i * tam_s - 92
                vida_monstro.append(vida_tx_mosntro(j*tam_s, i*tam_s-92))
                mostros.append(monstro_01)
                j -= 1
            elif ls == "N":
                npc = Sprite("sprites/personagens/npc_missao.png", 4)
                npc.set_total_duration(800)
                npc.x = j * tam_s
                npc.y = i * tam_s - 92
                NPC.append(npc)
                objetos.append(npc)
                j -= 1
            elif ls == "B":
                bau_00 = Sprite("sprites/itens/bau_comum.png", 1)
                bau_00.x = j * tam_s
                bau_00.y = i * tam_s - 56
                objetos.append(bau_00)
                baus.append(bau_00)
                j -= 1
            j += 1
        mat_mapa.append(tmp)
        mini_m.append(mini_tmp)
    mp.close()
    return mat_mapa, objetos, mostros, vida_monstro, baus, NPC


'''funcao que da um hide em todos os objetos do mapa'''


def des_mapa(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            map[i][j].hide()


'''funcao que da unhide em objetos na tela e atualiza'''


def atu_pos_mapa(map, vel_x, vel_y, res):
    for i in range(len(map)):
        for j in range(len(map[i])):
            ob = map[i][j]
            ob.move_x(vel_x)
            ob.move_y(vel_y)
            if (ob.x >= -384) and (ob.x + ob.width/2 <= res[0]+384) and (ob.y >= -384) and (ob.y + ob.width/2 <= res[1]+384):
                ob.unhide()
                ob.draw()


def atu_mapa(map, res):
    for i in range(len(map)):
        for j in range(len(map[i])):
            ob = map[i][j]
            if (ob.x >= -384) and (ob.x + ob.width/2 <= res[0]+384) and (ob.y >= -384) and (ob.y + ob.width/2 <= res[1]+384):
                ob.unhide()
                ob.draw()


def mostra_tela(map, pos_x, pos_y):
    if pos_x < 0:
        pos_x = 0
    if pos_y < 0:
        pos_y = 0
    xi = int(pos_x // 2304)
    yi = int(pos_y // 1464)
    xf = xi + 18
    yf = yi + 12
    for i in range(xi, xf):
        for j in (yi, yf):
            map[i][j].unhide()
            map[i][j].draw()

