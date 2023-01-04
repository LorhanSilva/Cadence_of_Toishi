from PPlay.window import *
from PPlay.sprite import *
from Mapa import mapa

def des_mapa(map, x, y):
    for i in range(len(map)):
        for lin in map[i]:
            if (lin.x >= x) and (lin.x + 16 <= 700 + x) and (lin.y >= y) and (lin.y + 16 <= 700 + y):
                lin.draw()

janela = Window(700, 700)
janela.set_title("Cadence of Toishi")
janela.set_background_color((255, 255, 255))

arvore_verde = Sprite("sprites/construcoes/castelo_00.png", 1)
arvore_verde.x = janela.width/2 - arvore_verde.width/2
arvore_verde.y = janela.width/2 - arvore_verde.width/2
#arvore_verde.draw()

espadao = Sprite("sprites/bioma/sand_16_transparent.png",1)
espadao.x = 0
espadao.y = 0
#espadao.draw()

espada = Sprite("sprites/itens/espada.png",1)
espada.x = 700 - 256
espada.y = 700 - 256
#espada.draw()

teclado = Window.get_keyboard()
map = []
inicio = True
pos_relat_x = 0
pos_relat_y = 0
while True:
    if teclado.key_pressed("LEFT"):
        pos_relat_x = pos_relat_x + 20 * janela.delta_time()
    if teclado.key_pressed("DOWN"):
        pos_relat_y = pos_relat_y + 20 * janela.delta_time()
    if inicio:
        map = mapa()
        des_mapa(map, pos_relat_x, pos_relat_y)
        inicio = False
    if teclado.key_pressed("ESC"):
        janela.close()
    des_mapa(map, pos_relat_x, pos_relat_y)
    arvore_verde.draw()
    #espadao.draw()
    #espada.draw()
    janela.delta_time()
    janela.update()