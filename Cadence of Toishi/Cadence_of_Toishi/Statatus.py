from PPlay.sprite import *
from PPlay.window import *
'''ordem dos atributos é : VIDA(0), xp(1), vida(2), forca(3), def(4), agili(5)'''


def ler_status():
    st = open("STATUS/status.txt", 'r')
    mons_st = open("STATUS/status_mons.txt", 'r')
    atrib_mons = mons_st.readlines()
    stats = st.readlines()
    atributos = []
    mons_a = []
    for i in range(len(stats)):
        atributos.append(int(stats[i].strip()))
        mons_a.append(int(atrib_mons[i].strip()))
    st.close()
    mons_st.close()
    return atributos, mons_a


status, monstro_atr = ler_status()


def atualiza_XP():
    status[1] += 5


def atrib_joga():
    at = open("STATUS/status.txt", 'r')
    s = at.readlines()
    atrib = []
    for i in s:
        atrib.append(int(i.strip()))
    at.close()
    return atrib


def vida_tx(x, y):
    vida = []
    tam = 0
    qtd_vida = 20
    for i in range(qtd_vida):
        spr_v = Sprite("sprites/itens/vida_tx.png", 1)
        spr_v.x = x + 15 + tam
        spr_v.y = y + 15
        vida.append(spr_v)
        tam += 21
    return vida


def XP_tx(XP, x, y):
    xp_sprite = []
    quant = XP//5
    tam = 21
    for i in range(quant):
        tx = Sprite("sprites/itens/xp_tx.png", 1)
        tx.x = x + 15 + tam*i
        tx.y = y + 15
        xp_sprite.append(tx)
    return xp_sprite


def vida_tx_mosntro(x, y):
    vi = []
    t = 5
    qt = 20
    for i in range(qt):
        v_m = Sprite("sprites/itens/sprite_vida_monstro.png", 1)
        v_m.x = x + t*i
        v_m.y = y
        vi.append(v_m)
    return vi


def des_vida_mons(v_tx, x, y):
    t = 5
    for i in range(len(v_tx)):
        v_tx[i].x = x + t*i
        v_tx[i].y = y
        v_tx[i].draw()


def mostro_status(mostro, nivel):
    vidas = []
    for x in mostro:
        vidas.append(100 * nivel)
    return vidas