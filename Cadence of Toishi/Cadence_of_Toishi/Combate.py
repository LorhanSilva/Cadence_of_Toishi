from PPlay.sprite import *
from Statatus import *
import random
#from COT_main import atributos

'''ordem dos atributos é : xp(0), vida(1), forca(2), def(3), agili(4)'''


def cria_disparos(equip, x, y):
    if equip[0] == 2:
        flexa = Sprite("sprites/itens/disparo_arco.png", 1)
        flexa.x = x
        flexa.y = y
        return flexa
    elif equip[0] == 1:
        disp = Sprite("sprites/itens/disparo_cetro.png", 1)
        disp.x = x
        disp.y = y
        return disp


def desconta_vida_mons(vida_mons, mons, m, p, atributos):
    dano = (status[3] - monstro_atr[4])//(monstro_atr[2]//20)
    for i in range(dano):
        if len(vida_mons[p]) <= 1:
            vida_mons.pop(p)
            mons.remove(m)
            atributos[1] += 5
        else:
            vida_mons[p].remove(vida_mons[p][-1])


def desconta_vida_jogador(vida):
    if len(vida) != 0:
        vida.pop(-1)


def comb(disparos, dx, dy, monstro, vida_mons, res, atributos):
    vel_disp = 10
    for i in disparos:
        i.draw()
        i.move_x(vel_disp*dx)
        i.move_y(vel_disp*dy)
        for m in monstro:
            j = monstro.index(m)
            if i.collided(m):
                disparos.remove(i)
                desconta_vida_mons(vida_mons, monstro, m, j, atributos)
        if (i.x <= 0) or (i.x >= res[0]) or (i.y <= 0) or (i.y >= res[1]):
            disparos.remove(i)


def monstro_mov(m, velx, vely, jogador, mouse, tempo, vida_sprite, vida_mons, res):
    vel_mos = 5
    distancia = 150
    mons_perto = []
    for i in range(len(m)):
        m[i].move_x(velx)
        m[i].move_y(vely)
        if (m[i].x >= 0) and (m[i].x + m[i].width / 2 <= res[0]) and (m[i].y >= 0) and (m[i].y + m[i].width / 2 <= res[1]):
            mons_perto.append(m[i])
            if tempo >= 5:
                if distancia == 150:
                    distancia = 64
                    vel_mos = 15
            else:
                distancia = 150
                vel_mos = 5
            if m[i].collided(jogador):
                desconta_vida_jogador(vida_sprite)
            if m[i].x < jogador.x - distancia:
                m[i].move_x(vel_mos)
            if m[i].x + m[i].width/2 > jogador.x + jogador.width/2 + distancia:
                m[i].move_x(-vel_mos)
            if m[i].y < jogador.y - distancia:
                m[i].move_y(vel_mos)
            if m[i].y + m[i].width/2 > jogador.y + jogador.width/2 + distancia:
                m[i].move_y(-vel_mos)
            m[i].draw()
            m[i].update()
            des_vida_mons(vida_mons[i], m[i].x, m[i].y)
