from PPlay.window import *
from PPlay.sprite import *
from COT_Saves import mostra_save, reset_save

def jane_conf(resolucao):
    janela_conf = Window(resolucao[0], resolucao[1])
    janela_conf.set_title("Configurações")
    janela_conf.set_background_color((217, 210, 0))
    mouse = janela_conf.get_mouse()

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
    sair.x = resolucao[0] - resolucao[0]/4
    sair.y = resolucao[1]/5
    sair.draw()
    sair_click = Sprite("sprites/itens/sair_inventario_click.png", 1)
    sair_click.x = sair.x
    sair_click.y = sair.y

    frame_save = Sprite("sprites/itens/frame_save.png", 1)
    frame_save.x = resolucao[1]/2
    frame_save.y = 400
    frame_save.draw()

    reset = Sprite("sprites/itens/reset_save.png", 1)
    reset.x = frame_save.x
    reset.y = frame_save.y + frame_save.width/2 + 10
    reset.draw()
    reset_click = Sprite("sprites/itens/reset_save_click.png", 1)
    reset_click.x = reset.x
    reset_click.y = reset.y

    save = mostra_save()
    while True:

        janela_conf.set_background_color((217, 210, 0))
        if mouse.is_over_object(reset):
            reset_click.draw()
            if mouse.is_button_pressed(1):
                reset_save()
        else:
            reset.draw()
        if mouse.is_over_object(sair):
            sair_click.draw()
            if mouse.is_button_pressed(1):
                return
        else:
            sair.draw()
        frame_save.draw()
        for i in range(len(save)):
            tam = 100
            janela_conf.draw_text("{}".format(save[i]), frame_save.x+30 + tam*i, frame_save.y+30, 20, (0, 0, 0), "Arial", True)

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
        janela_conf.update()




def menu(resolucao):
    janela_menu = Window(resolucao[0], resolucao[1])
    janela_menu.set_title("Menu game")
    janela_menu.set_background_color((217, 210, 0))
    mouse = janela_menu.get_mouse()

    mouse.hide()
    posicao_mouse = mouse.get_position()
    cursor = Sprite("sprites/itens/mouse_icone.png", 1)
    cursor.x = posicao_mouse[0]
    cursor.y = posicao_mouse[1]
    cursor.draw()
    cursor_click = Sprite("sprites/itens/mouse_icone_click.png", 1)
    cursor_click.x = cursor.x
    cursor_click.y = cursor.y

    titulo = Sprite("sprites/itens/titulo_COT.png", 1)
    titulo.x = resolucao[0]/2 - titulo.width/2
    titulo.y = 10
    titulo.draw()

    jogar = Sprite("sprites/itens/menu_jogar.png", 1)
    jogar.x = resolucao[0]/2 - jogar.width/2
    jogar.y = resolucao[1]/2 - jogar.width/2
    jogar.draw()
    jogar_click = Sprite("sprites/itens/menu_jogar_click.png", 1)
    jogar_click.x = jogar.x
    jogar_click.y = jogar.y


    conf = Sprite("sprites/itens/menu_conf.png", 1)
    conf.x = jogar.x
    conf.y = jogar.y + conf.width/2
    conf.draw()
    conf_click = Sprite("sprites/itens/menu_conf_click.png", 1)
    conf_click.x = conf.x
    conf_click.y = conf.y

    sair = Sprite("sprites/itens/menu_sair.png", 1)
    sair.x = jogar.x
    sair.y = conf.y + sair.width/2
    sair.draw()
    sair_click = Sprite("sprites/itens/menu_sair_click.png", 1)
    sair_click.x = sair.x
    sair_click.y = sair.y

    while True:

        janela_menu.set_background_color((217, 210, 0))
        titulo.draw()
        if mouse.is_over_object(sair):
            sair_click.draw()
            if mouse.is_button_pressed(1):
                janela_menu.close()
        else:
            sair.draw()
        if mouse.is_over_object(jogar):
            jogar_click.draw()
            if mouse.is_button_pressed(1):
                return False
        else:
            jogar.draw()
        if mouse.is_over_object(conf):
            conf_click.draw()
            if mouse.is_button_pressed(1):
                jane_conf(resolucao)
        else:
            conf.draw()
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
        janela_menu.update()