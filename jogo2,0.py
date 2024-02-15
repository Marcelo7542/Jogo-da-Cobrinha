import pygame
from pygame.locals import *
from sys import *
import random

xr = random.randint(0,500)
yr = random.randint(0,500)

pontos = 0
pygame.init()

largura = 500
altura = 500
velocidade = 10
x_controle = velocidade
y_controle = 0
comprimento_da_cobra = 3
lista = []
x=int(largura/2)
y=int(altura/2)
morto = False

window = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Tela')

pygame.mixer.music.set_volume(0.7)
musica_de_fundo = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

barulho = pygame.mixer.Sound('coin.wav')
fonte = pygame.font.SysFont('Consolas', 40, True, True)


relogio = pygame.time.Clock()

def reiniciar():
    global pontos, comprimento_da_cobra, x, y, lista, corpo, xr, yr, morto
    pontos = 0
    comprimento_da_cobra = 5
    x=int(largura/2)
    y=int(altura/2)
    lista = []
    corpo = []
    xr = random.randint(0,500)
    yr = random.randint(0,500)
    morto = False
def tamanho(lista):
    for xey in lista:
        pygame.draw.rect(window,(0,255,0),(xey[0],xey[1], 20, 20))
while True:
    relogio.tick(40)
    window.fill((0,0,0))
    mensagem = f"pontos: {pontos}"
    text = fonte.render(mensagem,False,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            elif event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            elif event.key == K_DOWN :
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
            elif event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
    '''if pygame.key.get_pressed()[K_LEFT]:
        x -= 8
    if pygame.key.get_pressed()[K_RIGHT]:
        x += 8
    if pygame.key.get_pressed()[K_DOWN]:
        y += 8
    if pygame.key.get_pressed()[K_UP]:
        y -= 8'''
   
    x += x_controle
    y += y_controle
    cobra = pygame.draw.rect(window, (0,250,0), (x,y,20,20))
    retvermelho = pygame.draw.rect(window, (250,0,0), (xr,yr,20,20))
    
    if retvermelho.colliderect(cobra):
        xr = random.randint(0,500)
        yr = random.randint(0,500)
        pontos += 1
        barulho.play()
        comprimento_da_cobra += 1
        
    corpo = []
    corpo.append(x)
    corpo.append(y)
    lista.append(corpo)
    
    tamanho(lista)
    
    if lista.count(corpo) > 1:
        fonte2 = pygame.font.SysFont("arial", 15, True, True)
        mensagem = 'Game Over, Clique "R" para reiniciar o jogo'
        texto = fonte2.render(mensagem,True, (0,0,0))
        ret = text.get_rect()
        morto = True
        while morto:
            window.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
            ret.center = (largura//2,altura//2)
            window.blit(texto, ret)
            pygame.display.update()
    if len(lista) >= comprimento_da_cobra:
        del lista[0]
    if x > largura:
        x = 0
    if x < 0:
        x = largura
    if y > altura:
        y = 0
    if y < 0:
        y = altura
    window.blit(text, (250,0))
    
    pygame.display.update()