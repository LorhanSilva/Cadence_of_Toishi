from PPlay.window import *
from PPlay.sprite import *


def des_itens(itens, x, y):
    tam = 0
    cont = 0
    no_inventario = []
    for i in range(len(itens)):
        if itens[i] == 2:
            artefato = Sprite("sprites/itens/icones_de_itens/item_inverntario_artefato.png", 1)
            artefato.x = x + tam
            artefato.y = y
            no_inventario.append(artefato)
            cont += 1
        elif itens[i] == 3:
            pocao = Sprite("sprites/itens/icones_de_itens/item_inverntario_pocao.png", 1)
            pocao.x = x + tam
            pocao.y = y
            no_inventario.append(pocao)
            cont += 1
        elif itens[i] > 10:
            tmp = itens[i] % 10
            if tmp == 1:
                espada = Sprite("sprites/itens/icones_de_itens/item_inverntario_espada.png", 1)
                espada.x = x + tam
                espada.y = y
                no_inventario.append(espada)
            elif tmp == 2:
                arco = Sprite("sprites/itens/icones_de_itens/item_inverntario_arco.png", 1)
                arco.x = x + tam
                arco.y = y
                no_inventario.append(arco)
            elif tmp == 3:
                cetro = Sprite("sprites/itens/icones_de_itens/item_inverntario_cetro.png", 1)
                cetro.x = x + tam
                cetro.y = y
                no_inventario.append(cetro)
            cont += 1
        tam += 64
        if cont == 10:
            cont = 0
            tam = 0
            y -= 70
    return no_inventario


def des_info(bonus, p, janela, x, y):
    if bonus[p] % 10 == 3:
        janela.draw_text("Bonus: +{} DEF".format(bonus[p]//10), x, y, 20, (0, 0, 0), "Arial", True)
    if bonus[p] % 10 == 2:
        janela.draw_text("Bonus: +{} ATK".format(bonus[p]//10), x, y, 20, (0, 0, 0), "Arial", True)
    if bonus[p] == 100:
        janela.draw_text("Restaura +{} VIDA".format(bonus[p]), x, y, 20, (0, 0, 0), "Arial", True)


def equipa_iten(itens, p, equipado, atrib, equipamento):
    if itens[p] == 2:
        artefato = Sprite("sprites/itens/icones_de_itens/item_inverntario_artefato.png", 1)
        artefato.x = equipado[0].x
        artefato.y = equipado[0].y - equipado[0].width
        if len(equipado) == 1:
            equipado.append(artefato)
        else:
            equipado[1] = artefato
    elif itens[p] > 10:
        tmp = itens[p] % 10
        if tmp == 1:
            espada = Sprite("sprites/itens/icone_arma_equipada_espada.png", 1)
            espada.x = equipado[0].x
            espada.y = equipado[0].y
            equipado[0] = espada
        elif tmp == 2:
            arco = Sprite("sprites/itens/icone_arma_equipada_arco.png", 1)
            arco.x = equipado[0].x
            arco.y = equipado[0].y
            equipado[0] = arco
            equipamento[0] = 2
        elif tmp == 3:
            cetro = Sprite("sprites/itens/icone_arma_equipada_cetro.png", 1)
            cetro.x = equipado[0].x
            cetro.y = equipado[0].y
            equipado[0] = cetro
            equipamento[0] = 1


def des_atrib(atrib, janela, x, y):
    janela.draw_text("NIVEL: {}".format(atrib[0]), x, y, 20, (0, 0, 0), "Arial", True)
    janela.draw_text("XP: {}".format(atrib[1]), x, y+25, 20, (0, 0, 0), "Arial", True)
    janela.draw_text("VIDA: {}".format(atrib[2]), x, y+50, 20, (0, 0, 0), "Arial", True)
    janela.draw_text("ATK: {}".format(atrib[3]), x, y+75, 20, (0, 0, 0), "Arial", True)
    janela.draw_text("DEF: {}".format(atrib[4]), x, y+100, 20, (0, 0, 0), "Arial", True)


def Tela_inventario(resolucao, itens, bonus, equipado, atrib, equipamento):
    janela_inventario = Window(resolucao[0], resolucao[1])
    janela_inventario.set_title("Inventario")
    janela_inventario.set_background_color((105, 0, 191))

    inventario = Sprite("sprites/itens/inventario.png", 1)
    inventario.x = resolucao[0] / 2 - inventario.width / 2
    inventario.y = resolucao[1] / 2 - inventario.width / 2
    inventario.draw()

    img_jogador = Sprite("sprites/personagens/personagem_mov_frente_00.png")
    img_jogador.x = inventario.x + 60
    img_jogador.y = inventario.y + 50
    img_jogador.draw()

    sair_inv = Sprite("sprites/itens/sair_inventario.png", 1)
    sair_inv.x = inventario.x + inventario.width
    sair_inv.y = inventario.y
    sair_inv.draw()
    sair_inv_click = Sprite("sprites/itens/sair_inventario_click.png", 1)
    sair_inv_click.x = sair_inv.x
    sair_inv_click.y = sair_inv.y

    mouse = Window.get_mouse()
    posicao_mouse = mouse.get_position()
    cursor = Sprite("sprites/itens/mouse_icone.png", 1)
    cursor.x = posicao_mouse[0]
    cursor.y = posicao_mouse[1]
    cursor.draw()
    cursor_click = Sprite("sprites/itens/mouse_icone_click.png", 1)
    cursor_click.x = cursor.x
    cursor_click.y = cursor.y

    intens_no_inventario = des_itens(itens, inventario.x + 30, inventario.y + 620)

    while True:

        janela_inventario.set_background_color((105, 0, 191))
        inventario.draw()
        for i in intens_no_inventario:
            p = intens_no_inventario.index(i)
            i.draw()
            if mouse.is_over_object(i):
                des_info(bonus, p, janela_inventario, inventario.x + inventario.width/2 + 50, inventario.y+50)
                if mouse.is_button_pressed(1):
                    equipa_iten(itens, p, equipado, atrib, equipamento)
        des_atrib(atrib, janela_inventario, inventario.x + inventario.width/3, inventario.y + 50)
        if mouse.is_over_object(sair_inv):
            sair_inv.draw()
            if mouse.is_button_pressed(1):
                return
        else:
            sair_inv_click.draw()
        img_jogador.draw()
        posicao_mouse = mouse.get_position()
        cursor.x = posicao_mouse[0]
        cursor.y = posicao_mouse[1]
        cursor_click.x = cursor.x
        cursor_click.y = cursor.y
        if mouse.is_button_pressed(1):
            cursor_click.draw()
        else:
            cursor.draw()
        janela_inventario.update()
