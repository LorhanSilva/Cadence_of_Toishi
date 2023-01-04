"""Funcoes de save do jogo"""
from PPlay.window import *
from PPlay.sprite import *


def reset_save():
    r_stt = open("SAVES/status_inicial.txt", 'r')
    r_it = open("SAVES/itens_inicial.txt", 'r')
    stt = open("STATUS/status.txt", 'w')
    it = open("SAVES/save_itens.txt", 'w')
    base_stt = r_stt.readlines()
    base_it = r_it.readlines()
    stt.writelines(base_stt)
    it.writelines(base_it)
    r_stt.close()
    r_it.close()
    it.close()
    stt.close()


def save_inventario(itens, bonus):
    sv_i = open("SAVES/save_itens.txt", 'w')
    for i in range(len(itens)):
        sv_i.write(str(itens[i])+"/"+str(bonus[i])+"\n")
    sv_i.close()


def save_atibutus(atrib):
    st = open("STATUS/status.txt", 'w')
    for i in atrib:
        st.write(str(i) + "\n")
    st.close()


def mostra_save():
    mat = []
    it = open("SAVES/save_itens.txt", "r")
    itens = it.readlines()
    indice = ['NIVEL', 'XP', 'VIDA', 'ATK', 'DEF', 'ITENS']
    stt = open("STATUS/status.txt", 'r')
    stats = stt.readlines()
    for i in range(len(stats)-1):
        mat.append(indice[i]+": "+stats[i].strip())
    mat.append(indice[-1]+": "+str(len(itens)))
    it.close()
    stt.close()
    return mat


def salva_geral(atrib, itens, bonus):
    save_atibutus(atrib)
    save_inventario(itens, bonus)


def jane_save(resolucao, atrib, itens, bonus):
    janela_save = Window(resolucao[0], resolucao[1])
    janela_save.set_title("Configurações")
    janela_save.set_background_color((217, 210, 0))
    mouse = janela_save.get_mouse()

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

    salvar = Sprite("sprites/itens/conf_salvar.png", 1)
    salvar.x = resolucao[0]/2 - salvar.width/2
    salvar.y = resolucao[1]/5
    salvar_click = Sprite("sprites/itens/conf_salvar_click.png", 1)
    salvar_click.x = salvar.x
    salvar_click.y = salvar.y

    frame_save = Sprite("sprites/itens/frame_save.png", 1)
    frame_save.x = salvar.x - frame_save.width/4
    frame_save.y = salvar.y + frame_save.width/2
    frame_save.draw()

    save = mostra_save()
    while True:

        janela_save.set_background_color((217, 210, 0))
        if mouse.is_over_object(salvar):
            salvar_click.draw()
            if mouse.is_button_pressed(1):
                salva_geral(atrib, itens, bonus)
        else:
            salvar.draw()
        if mouse.is_over_object(sair):
            sair_click.draw()
            if mouse.is_button_pressed(1):
                return
        else:
            sair.draw()
        frame_save.draw()
        for i in range(len(save)):
            tam = 100
            janela_save.draw_text("{}".format(save[i]), frame_save.x+30 + tam*i, frame_save.y+30, 20, (0, 0, 0), "Arial", True)

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
        janela_save.update()
