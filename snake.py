#!/usr/bin/env python

import pygame
import random
import time


pygame.init()
azul = (50,100,213)
laranja = (205,102,0)
verde = (0,255,0)
amarelo = (255,255,102)

dimensoes = (600,600)

##VALORES INICIAIS
x=300
y=300

d=20

lista_cobra = [[x,y]]

dx = 0
dy = 0

x_comida= round(random.randrange(0,600-d)/20) * 20
y_comida= round(random.randrange(0,600-d)/20) * 20

fonte=pygame.font.SysFont("hack",35)

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake do Marcelo Chaves')

tela.fill(azul)

clock = pygame.time.Clock()


def desenha_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
      pygame.draw.rect(tela,laranja,[unidade[0],unidade[1],d,d])
def mover_cobra(dx,dy,lista_cobra):    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
                
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
                
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy
    
    lista_cobra.append([x_novo,y_novo])
   
    del lista_cobra[0]
    
    return dx,dy,lista_cobra

def verifica_comida(dx,dy,x_comida,y_comida,lista_cobra):
    
    head = lista_cobra[-1] 
    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo,y_novo])
    
        x_comida= round(random.randrange(0,600-d)/20) * 20
        y_comida= round(random.randrange(0,600-d)/20) * 20
    
    pygame.draw.rect(tela,verde,[x_comida,y_comida,d,d])
    return x_comida, y_comida, lista_cobra

def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]
    
    if x not in range(600) or y not in range(600):
        return -1

def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]
    for x,y in corpo:
        if x == head[0] and y == head[1]:
            return -1

def atualizar_pontos(lista_cobra):
    pontos = str(len(lista_cobra))
    score = fonte.render("Pontuacao: " + pontos,True, amarelo)
    tela.blit(score,[0,0])

rodadas = 2
while rodadas > 0:

    i = 0
    j = 0
    dx = 0
    dy = 0

    x_comida= round(random.randrange(0,600-d)/20) * 20
    y_comida= round(random.randrange(0,600-d)/20) * 20
    mover_cobra(0,0,lista_cobra)
    
    x = 300
    y = 300

    d = 20

    lista_cobra = [[x,y]]
    
    tela.fill(azul)
    teste1 = fonte.render("INICIO DO JOGO", True, amarelo)
    tela.blit(teste1,[0,0])

    pygame.display.update()

    pygame.time.wait(4000)

    while i != -1 or j != -1:

        pygame.display.update()
        desenha_cobra(lista_cobra)
        dx,dy,lista_cobra = mover_cobra(dx,dy,lista_cobra)
        x_comida,y_comida,lista_cobra = verifica_comida(dx,dy,x_comida,y_comida,lista_cobra)
        print(lista_cobra)
        i = verifica_parede(lista_cobra)
        j = verifica_mordeu_cobra(lista_cobra)
        atualizar_pontos(lista_cobra)
        if i == -1 or j == -1:
            break
        clock.tick(10)
    
    tela.fill(azul)
    teste = fonte.render("GAME OVER! Espere 4 segundos para recomeçar.", True, amarelo)
    tela.blit(teste,[0,0])
    pygame.display.update()

    rodadas = rodadas - 1
    pygame.time.wait(4000)

