from PPlay.window import *
from PPlay.sprite import *
import random


def janel_missoes(resolucao, n_map):

    janela_mapa = Window(resolucao[0], resolucao[1])
    janela_mapa.set_title("Configurações")
    janela_mapa.set_background_color((217, 210, 0))
    mouse = janela_mapa.get_mouse()

    mouse.hide()
    posicao_mouse = mouse.get_position()
    cursor = Sprite("sprites/itens/mouse_icone.png", 1)
    cursor.x = posicao_mouse[0]
    cursor.y = posicao_mouse[1]
    cursor.draw()
    cursor_click = Sprite("sprites/itens/mouse_icone_click.png", 1)
    cursor_click.x = cursor.x
    cursor_click.y = cursor.y

    sair = Sprite("sprites/itens/sair_inventario.png", 1)
    sair.x = resolucao[0] - resolucao[0] / 4
    sair.y = resolucao[1] / 5
    sair.draw()
    sair_click = Sprite("sprites/itens/sair_inventario_click.png", 1)
    sair_click.x = sair.x
    sair_click.y = sair.y

    sel_mp1 = Sprite("sprites/itens/selecao_mp1.png", 1)
    sel_mp1.x = sel_mp1.width/2
    sel_mp1.y = 100
    sel_mp1.draw()
    sel_mp1_click = Sprite("sprites/itens/selecao_mp1_click.png", 1)
    sel_mp1_click.x = sel_mp1.x
    sel_mp1_click.y = sel_mp1.y

    sel_mp2 = Sprite("sprites/itens/selecao_mp2.png", 1)
    sel_mp2.x = sel_mp1.x
    sel_mp2.y = sel_mp1.y + sel_mp2.width
    sel_mp2.draw()
    sel_mp2_click = Sprite("sprites/itens/selecao_mp2_click.png", 1)
    sel_mp2_click.x = sel_mp2.x
    sel_mp2_click.y = sel_mp2.y
    while True:
        janela_mapa.set_background_color((217, 210, 0))

        if mouse.is_over_object(sel_mp1):
            sel_mp1_click.draw()
            n_map = 1
        else:
            sel_mp1.draw()
        if mouse.is_over_object(sel_mp2):
            sel_mp2_click.draw()
            n_map = 2
        else:
            sel_mp2.draw()

        if mouse.is_over_object(sair):
            sair_click.draw()
            if mouse.is_button_pressed(1):
                return n_map
        else:
            sair.draw()
        posicao_mouse = mouse.get_position()
        cursor.x = posicao_mouse[0]
        cursor.y = posicao_mouse[1]
        cursor.draw()
        cursor_click.x = cursor.x
        cursor_click.y = cursor.y
        if mouse.is_button_pressed(1):
            cursor_click.draw()
        else:
            cursor.draw()
        janela_mapa.update()
