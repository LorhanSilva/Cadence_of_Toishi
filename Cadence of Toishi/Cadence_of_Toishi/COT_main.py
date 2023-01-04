from PPlay.window import *
from PPlay.sprite import *
from COT_menu import menu
from Mapa import *
from Statatus import *
from Combate import *
from Inventario import Tela_inventario
from Spolio import gera_item_bau, iten_inicial
from COT_Saves import jane_save
from COT_missoes import janel_missoes

resolucao = [1700, 1000]
janela = Window(resolucao[0], resolucao[1])
janela.set_title("CADENCE OF TOISHI")
janela.set_background_color((60, 60, 255))
teclado = Window.get_keyboard()
mouse = Window.get_mouse()

'''sprite do jogador'''
jogador = Sprite("sprites/personagens/personagem_mov_frente_00.png", 1)
jogador.x = resolucao[0] / 2 - jogador.width / 2
jogador.y = resolucao[1] / 2 - jogador.width / 2
jogador.draw()

'''Sprites de animacao do jogador'''
mov = 0
jogador_mov_cima = Sprite("sprites/personagens/personagem_mov_cima.png", 8)
jogador_mov_cima.set_total_duration(1000)
jogador_mov_cima.x = jogador.x
jogador_mov_cima.y = jogador.y

jogador_mov_baixo = Sprite("sprites/personagens/personagem_mov_baixo.png", 8)
jogador_mov_baixo.set_total_duration(1000)
jogador_mov_baixo.x = jogador.x
jogador_mov_baixo.y = jogador.y

jogador_mov_direita = Sprite("sprites/personagens/personagem_mov_direita.png", 8)
jogador_mov_direita.set_total_duration(1000)
jogador_mov_direita.x = jogador.x
jogador_mov_direita.y = jogador.y

jogador_mov_esquerda = Sprite("sprites/personagens/personagem_mov_esquerda.png", 8)
jogador_mov_esquerda.set_total_duration(1000)
jogador_mov_esquerda.x = jogador.x
jogador_mov_esquerda.y = jogador.y

jogador_mov_diagonal_diba = Sprite("sprites/personagens/personagem_mov_diagonal_diba.png", 6)
jogador_mov_diagonal_diba.set_total_duration(1000)
jogador_mov_diagonal_diba.x = jogador.x
jogador_mov_diagonal_diba.y = jogador.y

jogador_mov_diagonal_dici = Sprite("sprites/personagens/personagem_mov_diagonal_dici.png", 6)
jogador_mov_diagonal_dici.set_total_duration(1000)
jogador_mov_diagonal_dici.x = jogador.x
jogador_mov_diagonal_dici.y = jogador.y

jogador_mov_diagonal_esqba = Sprite("sprites/personagens/personagem_mov_diagonal_esqba.png", 6)
jogador_mov_diagonal_esqba.set_total_duration(1000)
jogador_mov_diagonal_esqba.x = jogador.x
jogador_mov_diagonal_esqba.y = jogador.y

jogador_mov_diagonal_esqci = Sprite("sprites/personagens/personagem_mov_diagonal_esqci.png", 6)
jogador_mov_diagonal_esqci.set_total_duration(1000)
jogador_mov_diagonal_esqci.x = jogador.x
jogador_mov_diagonal_esqci.y = jogador.y

'''icones e imformacoes da tela'''
mouse.hide()
posicao_mouse = mouse.get_position()

cursor = Sprite("sprites/itens/mouse_icone.png", 1)
cursor.x = posicao_mouse[0]
cursor.y = posicao_mouse[1]
cursor.draw()
cursor_click = Sprite("sprites/itens/mouse_icone_click.png", 1)
cursor_click.x = cursor.x
cursor_click.y = cursor.y

icone_conf = Sprite("sprites/itens/icone_conf.png", 1)
icone_conf.x = icone_conf.width/2
icone_conf.y = 0
icone_conf.draw()
icone_conf_click = Sprite("sprites/itens/icone_conf_click.png", 1)
icone_conf_click.x = icone_conf.x
icone_conf_click.y = icone_conf.y

icone_missao = Sprite("sprites/itens/icone_missoes.png", 1)
icone_missao.x = icone_conf.x + icone_conf.width + icone_conf.width/2
icone_missao.y = icone_conf.y
icone_missao.draw()
icone_missao_click = Sprite("sprites/itens/icone_missoes_click.png", 1)
icone_missao_click.x = icone_conf.x + icone_conf.width + icone_conf.width/2
icone_missao_click.y = icone_conf.y

icone_inventario = Sprite("sprites/itens/icone_inventario.png", 1)
icone_inventario.x = icone_missao.x + icone_missao.width + icone_inventario.width/2
icone_inventario.y = icone_conf.y
icone_missao.draw()
icone_inventario_click = Sprite("sprites/itens/icone_inventario_click.png", 1)
icone_inventario_click.x = icone_missao.x + icone_missao.width + icone_inventario.width/2
icone_inventario_click.y = icone_conf.y

b_vida = Sprite("sprites/itens/barra_vazia.png", 1)
b_vida.x = resolucao[0] / 2 - b_vida.width / 2
b_vida.y = resolucao[1] - b_vida.width / 4
b_vida.draw()

frame_equipamento = Sprite("sprites/itens/frame_inten_equipado.png", 1)
frame_equipamento.x = b_vida.x - frame_equipamento.width
frame_equipamento.y = b_vida.y
frame_equipamento.draw()

espada_equipada = Sprite("sprites/itens/icone_arma_equipada_espada.png", 1)
espada_equipada.x = frame_equipamento.x + 8
espada_equipada.y = frame_equipamento.y + 7

'''Mapa inf.'''
n_mapa = 1
MAPA, objetos, mostros, vida_monstro, baus, NPC = mapa(n_mapa)
des_mapa(MAPA)
pos_rel_x = 0
pos_rel_Y = 0
vel_relativa_x = 0
vel_relativa_Y = 0
vel_relativa = 7

itens = []
bonus = []
iten_inicial(itens, bonus)
iten_equipado = [espada_equipada]
equipamento = [1]
'''Status'''
atributos = atrib_joga()
vida_sprite = vida_tx(b_vida.x, b_vida.y)
vida = int(status[1])
"""COMBATE"""
mons_perto = []
disparos = []
temp_atk = 7 // atributos[5]
direcao_x = 0
direcao_y = 0
dir_disp_x = 0
dir_disp_y = 0
combate = False
tempo_atk_mons = 0
'''Marcador de tempo'''
tempo_geral = 0
quadros = 0
FPS = 0
intervalo_atk = 0

'''Inicio'''
inicio = True

while True:
    if inicio:
        inicio = menu(resolucao)
        vida_sprite = vida_tx(b_vida.x, b_vida.y)
        MAPA, objetos, mostros, vida_monstro, baus, NPC = mapa(n_mapa)

    if teclado.key_pressed("ESC"):
        inicio = True

    if teclado.key_pressed("S") and teclado.key_pressed("D"):
        mov = 5
        pos_rel_x = pos_rel_x + vel_relativa * janela.delta_time()
        pos_rel_Y = pos_rel_Y + vel_relativa * janela.delta_time()
        vel_relativa_x = -vel_relativa
        vel_relativa_Y = -vel_relativa
        direcao_x = 1
        direcao_y = 1

    elif teclado.key_pressed("S") and teclado.key_pressed("A"):
        mov = 6
        pos_rel_x = pos_rel_x - vel_relativa * janela.delta_time()
        pos_rel_Y = pos_rel_Y + vel_relativa * janela.delta_time()
        vel_relativa_x = vel_relativa
        vel_relativa_Y = -vel_relativa
        direcao_x = -1
        direcao_y = 1
    elif teclado.key_pressed("W") and teclado.key_pressed("D"):
        mov = 7
        pos_rel_x = pos_rel_x + vel_relativa * janela.delta_time()
        pos_rel_Y = pos_rel_Y - vel_relativa * janela.delta_time()
        vel_relativa_x = -vel_relativa
        vel_relativa_Y = vel_relativa
        direcao_x = 1
        direcao_y = -1
    elif teclado.key_pressed("W") and teclado.key_pressed("A"):
        mov = 8
        pos_rel_x = pos_rel_x - vel_relativa * janela.delta_time()
        pos_rel_Y = pos_rel_Y - vel_relativa * janela.delta_time()
        vel_relativa_x = vel_relativa
        vel_relativa_Y = vel_relativa
        direcao_x = -1
        direcao_y = -1
    elif teclado.key_pressed("W"):
        mov = 1
        pos_rel_Y = pos_rel_Y - vel_relativa * janela.delta_time()
        vel_relativa_Y = vel_relativa
        direcao_y = -1
        direcao_x = 0
    elif teclado.key_pressed("D"):
        mov = 2
        pos_rel_x = pos_rel_x + vel_relativa * janela.delta_time()
        vel_relativa_x = -vel_relativa
        direcao_x = 1
        direcao_y = 0
    elif teclado.key_pressed("S"):
        mov = 3
        pos_rel_Y = pos_rel_Y + vel_relativa * janela.delta_time()
        vel_relativa_Y = -vel_relativa
        direcao_y = 1
        direcao_x = 0
    elif teclado.key_pressed("A"):
        mov = 4
        pos_rel_x = pos_rel_x - vel_relativa * janela.delta_time()
        vel_relativa_x = vel_relativa
        direcao_x = -1
        direcao_y = 0

    for i in objetos:
        if (i.x <= jogador.x+400) and (i.x + i.width/2 >= jogador.x-400) and (i.y <= jogador.y+400) and (i.y + i.width/2 >= jogador.y-400):
            if i.collided(jogador):
                if jogador.x + jogador.width/2 >= i.x:
                    vel_relativa_x = -0.4
                elif jogador.x <= i.x + i.width/2:
                    vel_relativa_x = 0.4
                if jogador.y + jogador.width/2 >= i.y:
                    vel_relativa_Y = -0.4
                elif jogador.y <= i.y + i.width/2:
                    vel_relativa_Y = 0.4

    janela.set_background_color((60, 60, 255))
    if vel_relativa != 0:
        atu_pos_mapa(MAPA, vel_relativa_x, vel_relativa_Y, resolucao)
    else:
        atu_mapa(MAPA, resolucao)

    for i in baus:
        i.move_x(vel_relativa_x)
        i.move_y(vel_relativa_Y)
        if (i.x >= 0) and (i.x <= resolucao[0]) and (i.y >= 0) and (i.y <= resolucao[1]):
            i.draw()
            if mouse.is_over_object(i) and mouse.is_button_pressed(1):
                gera_item_bau(itens, bonus)
                objetos.remove(i)
                baus.remove(i)
    if teclado.key_pressed("SPACE") and intervalo_atk >= temp_atk:
        intervalo_atk = 0
        disparos.append(cria_disparos(equipamento, jogador.x, jogador.y))
        dir_disp_x = direcao_x
        dir_disp_y = direcao_y

    if len(disparos) != 0:
        comb(disparos, dir_disp_x, dir_disp_y, mostros, vida_monstro, resolucao, atributos)

    if len(mostros) != 0:
        monstro_mov(mostros, vel_relativa_x, vel_relativa_Y, jogador, mouse, tempo_atk_mons, vida_sprite, vida_monstro, resolucao)
    if tempo_atk_mons >= 5.1:
        tempo_atk_mons = 0
    if len(vida_sprite) <= 0:
        inicio = True

    NPC[0].draw()
    NPC[0].update()
    NPC[0].move_x(vel_relativa_x)
    NPC[0].move_y(vel_relativa_Y)
    janela.draw_text("ELIMINE TODOS OS MONSTROS!!!", NPC[0].x - 100, NPC[0].y, 20, (255, 255, 255), "Arial", True)

    vel_relativa_x = 0
    vel_relativa_Y = 0

    if mouse.is_over_object(icone_missao):
        icone_missao_click.draw()
        if mouse.is_button_pressed(1):
            n_mapa = janel_missoes(resolucao, n_mapa)
            MAPA, objetos, mostros, vida_monstro, baus, NPC = mapa(n_mapa)
    else:
        icone_missao.draw()
    if mouse.is_over_object(icone_conf):
        icone_conf_click.draw()
        if mouse.is_button_pressed(1):
            jane_save(resolucao, atributos, itens, bonus)
    else:
        icone_conf.draw()
    if mouse.is_over_object(icone_inventario):
        icone_inventario_click.draw()
        if mouse.is_button_pressed(1):
            Tela_inventario(resolucao, itens, bonus, iten_equipado, atributos, equipamento)
    else:
        icone_inventario.draw()
    frame_equipamento.draw()
    for i in iten_equipado:
        i.draw()
    if mov == 0:
        jogador.draw()
    if mov == 1:
        jogador_mov_cima.draw()
        jogador_mov_cima.update()
        mov = 0
    if mov == 3:
        jogador_mov_baixo.draw()
        jogador_mov_baixo.update()
        mov = 0
    if mov == 2:
        jogador_mov_direita.draw()
        jogador_mov_direita.update()
        mov = 0
    if mov == 4:
        jogador_mov_esquerda.draw()
        jogador_mov_esquerda.update()
        mov = 0
    if mov == 5:
        jogador_mov_diagonal_diba.draw()
        jogador_mov_diagonal_diba.update()
        mov = 0
    if mov == 6:
        jogador_mov_diagonal_esqba.draw()
        jogador_mov_diagonal_esqba.update()
        mov = 0
    if mov == 7:
        jogador_mov_diagonal_dici.draw()
        jogador_mov_diagonal_dici.update()
        mov = 0
    if mov == 8:
        jogador_mov_diagonal_esqci.draw()
        jogador_mov_diagonal_esqci.update()
        mov = 0
    for i in vida_sprite:
        i.draw()
    atributos = atrib_joga()
    b_vida.draw()
    if tempo_geral > 0.1:
        FPS = quadros / tempo_geral
        quadros = 0
        tempo_geral = 0
    #janela.draw_text("FPS: {}".format(FPS//1), resolucao[0] - 100, 0, 20, (255, 0, 0), "Arial", True)
    posicao_mouse = mouse.get_position()
    cursor.x = posicao_mouse[0]
    cursor.y = posicao_mouse[1]
    cursor_click.x = cursor.x
    cursor_click.y = cursor.y
    if mouse.is_button_pressed(1):
        cursor_click.draw()
    else:
        cursor.draw()
    tempo_geral += janela.delta_time()
    tempo_atk_mons += janela.delta_time()
    intervalo_atk += janela.delta_time()
    janela.delta_time()
    quadros += 1
    janela.update()
