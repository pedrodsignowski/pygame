#Imports
import pygame
import os
from sys import exit
from random import randrange
import random
from pygame.locals import* # Dispensa a necessidade de pygame. para teclas, botões
from os import sys
import json
from pathlib import Path  # caminho completo do arquivo


#Inicialização
pygame.init()
#Fonte
fonte = pygame.font.SysFont('arial', 50,True,False)
fonte2= pygame.font.SysFont('arial', 30,True,False)
fonte3= pygame.font.SysFont('arial', 24,True,False)

#Variavéis
telacomprimento=600
telaalturain=400
vezes = 0
veses = 0
vezzes= 0
vesses= 0
stun  = 0
stun2 = 0
stun3 = 0
stun4 = 0
x = 0
y = 0
dire1 = "esquerda"
xx = telacomprimento-50
yy = 0
dire2 = "direita"
xxx = telacomprimento-50
yyy = telaalturain-50
dire3 = "cima"
xxxx = 0
yyyy = telaalturain-50
dire4 = "baixo"

mouse = pygame.mouse.set_cursor(*pygame.cursors.arrow)

#Relogio
relogio = pygame.time.Clock() # Cria um relogio q roda o mesmo tick para pcs diferentes

#Tela
tela= pygame.display.set_mode((telacomprimento,telaalturain)) # Cria a janela
corDaTela= (255,255,255)

#Escrituras
mensagem = "Jogo"
mensagemMenuJogar= "Jogar"
mensagemMenuGacha="Gacha"

corDaMensagem = (255,0,0)
formatacao_texto = fonte.render(mensagem, True, (255, 255, 255), corDaMensagem)# Título do jogo
formatacao_textoMenuJogar = fonte.render(mensagemMenuJogar, True, (255, 255, 255), corDaMensagem)#Botão Jogar
formatacao_textoMenuGacha = fonte.render(mensagemMenuGacha, True, (255, 255, 255), corDaMensagem)#Botão Gacha

retanguloMensagemJogar= pygame.draw.rect(tela,corDaMensagem,(230,150,125,46))# Retângulo p hitbox Jogar      hitboxataque = pygame.draw.rect(tela,(200,180,0),(xhit,yhit,60,60))
retanguloMensagemGacha= pygame.draw.rect(tela,corDaMensagem,(230,250,147,37))# Retangulo para hitbox Gacha(tela,cor,posição e tamanho
retanguloMenu = pygame.draw.rect(tela,(255,255,255),(telacomprimento-50,1,50,50))
xa = randrange(50,telacomprimento-50,50)
ya = randrange(50,telaalturain-50,50)

#Imagens
botaoMenu= pygame.image.load('img/menu.png')
botaoMenu=pygame.transform.scale(botaoMenu,(50,50))
#Título janela
pygame.display.set_caption('Jogo')
#Subfunções

def aleatorizarbloco():
        global xa,ya
        xa = randrange(50,telacomprimento-50,50)
        ya = randrange(50,telaalturain-50,50)
def ataque1():
    global x,y,stun,stun2,stun3,stun4,dire1,blocoazul2,blocoazul3,blocoazul4
    if stun == 0:
        xhit,yhit = x,y
        if dire1 == "direita":
            xhit+=50
        if dire1 == "esquerda":
            xhit-=50
        if dire1 == "baixo":
            yhit+=50
        if dire1 == "cima":
            yhit-=50
        hitboxataque = pygame.draw.rect(tela,(200,180,0),(xhit,yhit,60,60))
        if hitboxataque.colliderect(blocoazul2):
            stun2 = 900
        if hitboxataque.colliderect(blocoazul3):
            stun3 = 900
        if hitboxataque.colliderect(blocoazul4):
            stun4 = 900
def ataque2():
    global xx,yy,stun,stun2,stun3,stun4,dire2,blocoazul,blocoazul3,blocoazul4
    if stun2 == 0:
        xhit,yhit = xx,yy
        if dire2 == "direita":
            xhit+=50
        if dire2 == "esquerda":
            xhit-=50
        if dire2 == "baixo":
            yhit+=50
        if dire2 == "cima":
            yhit-=50
        hitboxataque = pygame.draw.rect(tela,(200,180,0),(xhit,yhit,60,60))
        if hitboxataque.colliderect(blocoazul):
            stun = 900
        if hitboxataque.colliderect(blocoazul3):
            stun3 = 900
        if hitboxataque.colliderect(blocoazul4):
            stun4 = 900
def ataque3():
    global xxx,yyy,stun,stun2,stun3,stun4,dire3,blocoazul,blocoazul2,blocoazul4
    if stun3 == 0 :
        xhit,yhit = xxx,yyy
        if dire3 == "direita":
            xhit+=50
        if dire3 == "esquerda":
            xhit-=50
        if dire3 == "baixo":
            yhit+=50
        if dire3 == "cima":
            yhit-=50
        hitboxataque = pygame.draw.rect(tela,(200,180,0),(xhit,yhit,60,60))
        if hitboxataque.colliderect(blocoazul):
            stun = 900
        if hitboxataque.colliderect(blocoazul2):
            stun2 = 900
        if hitboxataque.colliderect(blocoazul4):
            stun4 = 900
def ataque4():
    global xxxx,yyyy,stun,stun2,stun3,stun4,dire4,blocoazul,blocoazul2,blocoazul3
    if stun4 == 0:
        xhit,yhit = xxxx,yyyy
        if dire4 == "direita":
            xhit+=50
        if dire4 == "esquerda":
            xhit-=50
        if dire4 == "baixo":
            yhit+=50
        if dire4 == "cima":
            yhit-=50
        hitboxataque = pygame.draw.rect(tela,(200,180,0),(xhit,yhit,60,60))
        if hitboxataque.colliderect(blocoazul):
            stun = 900
        if hitboxataque.colliderect(blocoazul2):
            stun2 = 900
        if hitboxataque.colliderect(blocoazul3):
            stun3 = 900
def andar():
    global x,y,dire1,stun
    if stun == 0:
        if pygame.key.get_pressed()[K_a]:
            x-=1
            dire1 = "esquerda"
        if pygame.key.get_pressed()[K_d]:
            x+=1
            dire1 = "direita"
        if pygame.key.get_pressed()[K_s]:
            y+=1
            dire1 = "baixo"
        if pygame.key.get_pressed()[K_w]:
            y-=1
            dire1 = "cima"
def andar2():
    global xx,yy,dire2,stun2
    if stun2 == 0:
        if pygame.key.get_pressed()[K_LEFT]:
            xx-=1
            dire2 = "esquerda"
        if pygame.key.get_pressed()[K_RIGHT]:
            xx+=1
            dire2 = "direita"
        if pygame.key.get_pressed()[K_DOWN]:
            yy+=1
            dire2 = "baixo"
        if pygame.key.get_pressed()[K_UP]:
            yy-=1
            dire2 = "cima"
def andar3():
    global xxx,yyy,dire3,stun3
    if stun3 == 0:
        if pygame.key.get_pressed()[K_j]:
            xxx -= 1
            dire3 = "esquerda"
        if pygame.key.get_pressed()[K_l]:
            xxx += 1
            dire3 = "direita"
        if pygame.key.get_pressed()[K_k]:
            yyy += 1
            dire3 = "baixo"
        if pygame.key.get_pressed()[K_i]:
            yyy -= 1
            dire3 = "cima"
def andar4():
    global xxxx,yyyy,dire4,stun4
    if stun4 == 0:
        if pygame.key.get_pressed()[K_KP1]:
            xxxx -= 1
            dire4 = "esquerda"
        if pygame.key.get_pressed()[K_KP3]:
            xxxx += 1
            dire4 = "direita"
        if pygame.key.get_pressed()[K_KP2]:
            yyyy += 1
            dire4 = "baixo"
        if pygame.key.get_pressed()[K_KP5]:
            yyyy -= 1  
            dire4 = "cima"
def jogo():
    global pontos
    global telacomprimento,telaalturain,veses,vezes,vezzes,vesses,stun,stun2,stun3,stun4,blocoazul,blocoazul2,blocoazul3,blocoazul4
    global x,y,xx,yy,xxx,yyy,xxxx,yyyy,xa,ya
    bananinha = 0       
    #Pega os pontos do arquivo .json
    arquivo= open("pontos.json","r")
    dados= json.load(arquivo)
    arquivo.close()
    vezes= dados["Bloco Azul:"]
    veses= dados['Bloco Verde:']
    vezzes = dados['Bloco Amarelo:']
    vesses = dados['Bloco Vermelho:']
    posicaoHorizontalPlacar = telacomprimento -75
    posicaoHorizontalPlacar2 = telacomprimento -78
    posicaoVerticalPlacar= telaalturain-55
    posicaoVerticalPlacar2= telaalturain-58
    while True:
        pontos={"Bloco Azul:":vezes,
                "Bloco Verde:":veses,
                "Bloco Amarelo:":vezzes,
                "Bloco Vermelho:":vesses}#Dicionario
        textoo = fonte.render(str(vezes) ,True,(  0,  0,  0))    
        textoo2= fonte.render(str(veses) ,True,(  0,  0,  0))
        textoo3= fonte.render(str(vezzes),True,(  0,  0,  0))
        textoo4= fonte.render(str(vesses),True,(  0,  0,  0))
        texto  = fonte.render(str(vezes) ,True,(147,228,246))
        texto2 = fonte.render(str(veses) ,True,(114,243,140))
        texto3 = fonte.render(str(vezzes),True,(235,248,109))  
        texto4 = fonte.render(str(vesses),True,(255, 97, 91))
        relogio.tick(300)
        tela.fill(corDaTela)
        retanguloBotaoMenu= pygame.draw.rect(tela,(255,255,255),(550,1,50,50))
        tela.blit(botaoMenu,(telacomprimento-50,1))#menu pausa
        tela.blit(textoo2,(posicaoHorizontalPlacar2,3))#Sombra placar verde 
        tela.blit(textoo,(43,3))#Sombra placar azul 23
        tela.blit(textoo4,(43,posicaoVerticalPlacar))#Sombra placar vermelho altura 
        tela.blit(textoo3,(posicaoHorizontalPlacar2,posicaoVerticalPlacar2))#Sombra placar amarelo 
        tela.blit(texto2,(posicaoHorizontalPlacar,0))#Verde
        tela.blit(texto,(40,0))#Azul
        tela.blit(texto3,(posicaoHorizontalPlacar,posicaoVerticalPlacar))#amarelo    
        tela.blit(texto4,(40,posicaoVerticalPlacar))#Vermelho
        if stun> 0:stun -=1
        if stun2>0:stun2-=1
        if stun3>0:stun3-=1
        if stun4>0:stun4-=1
        blocoazul4 = pygame.draw.rect(tela,(255,97 ,91 ),(xxxx,yyyy,50,50))
        blocoazul3 = pygame.draw.rect(tela,(235,248,109),(xxx ,yyy ,50,50))
        blocoazul2 = pygame.draw.rect(tela,(114,243,140),(xx  ,yy  ,50,50))
        blocoazul  = pygame.draw.rect(tela,(147,228,246),(x   ,y   ,50,50))
        blocoverme = pygame.draw.rect(tela,(136,135,135),(xa  ,ya  ,50,50))
  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    ataque1()
                elif event.key == K_RETURN:
                    ataque2()
                elif event.key == K_u:
                    ataque3()
                elif event.key == K_KP4:
                    ataque4()
            elif event.type==pygame.MOUSEBUTTONDOWN and retanguloBotaoMenu.collidepoint(event.pos) and event.button==1: #primeiro vem o .type e depois a tecla ou mouse
                            menuPausa()
        andar ()
        andar2()
        andar3()
        andar4()    
        
        if blocoazul.colliderect(blocoverme):
            aleatorizarbloco()
            vezes = vezes + 1
            print (vezes)    
        if blocoazul2.colliderect(blocoverme):
            aleatorizarbloco()
            veses += 1
            print(veses)
        if blocoazul3.colliderect(blocoverme):
            aleatorizarbloco()
            vezzes += 1
            print(vezzes)
        if blocoazul4.colliderect(blocoverme):
            aleatorizarbloco()
            vesses += 1
            print(vesses)
        
        if x<0:
            x=0
        if x>telacomprimento-50:
            x=telacomprimento-50
        if y<0:
            y=0
        if y>telaalturain-50:
            y=telaalturain-50
        if xx<0:
            xx=0
        if xx>telacomprimento-50:
            xx=telacomprimento-50
        if yy<0:
            yy=0
        if yy>telaalturain-50:
            yy=telaalturain-50
        if xxx<0:
            xxx=0
        if xxx>telacomprimento-50:
            xxx=telacomprimento-50
        if yyy<0:
            yyy=0
        if yyy>telaalturain-50:
            yyy=telaalturain-50
        if xxxx<0:
            xxxx=0
        if xxxx>telacomprimento-50:
            xxxx=telacomprimento-50
        if yyyy<0:
            yyyy=0
        if yyyy>telaalturain-50:
            yyyy=telaalturain-50 
        pygame.display.update()
           
def menu():
    while True:
        relogio.tick(300)
        tela.fill((corDaTela))
        tela.blit(formatacao_texto, (230, 20))# Carregar Título
        tela.blit(formatacao_textoMenuJogar,(230,150))#Carregar Jogar
        tela.blit(formatacao_textoMenuGacha,(230,250))# Carregar Gacha
        pygame.display.update()
        for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and retanguloMensagemJogar.collidepoint(event.pos) and event.button==1:
                        jogo()
                    elif event.type == pygame.MOUSEBUTTONDOWN and retanguloMensagemGacha.collidepoint(event.pos):
                        tela.fill(corDaTela)
                        os.system('start https://spinthewheel.io/pt/wheels/M9loF8Nirf2f6lNjodDicz0xJmU9MA==')#Loop infinito
def menuPausa():
    global x,y,xx,yy,xxx,yyy,xxxx,yyyy,xa,ya
    global pontos
    escuro = pygame.Surface(tela.get_size(), pygame.SRCALPHA)
    fundo=tela.copy()
    escuro.fill((0, 0, 0, 150))
    botaoVoltar= fonte3.render("Voltar ao menu principal",True,(255,255,255),corDaMensagem)
    botaoPontos= fonte3.render("Reinicia pontos",True,(255,255,255),corDaMensagem)
    botaoRetomarJogo= fonte3.render("Voltar ao jogo",True,(255,255,255),corDaMensagem)
    retanguloBotoRetomarJogo= pygame.draw.rect(tela,(corDaMensagem),(230,210,161, 27))
    retanguloBotao= pygame.draw.rect(tela,(corDaMensagem),(170,150,281, 27)) 
    retanguloBotoMenu=pygame.draw.rect(tela,(corDaMensagem),(220,180,189, 27)) 
    #print(fonte3.size("Reiniciar pontos")) 

    while True:
        relogio.tick(300)
        tela.blit(fundo, (0, 0))
        tela.blit(escuro, (0, 0)) 
        tela.blit(botaoVoltar,((170,150))) 
        tela.blit(botaoPontos,(220,180))
        tela.blit(botaoRetomarJogo,(230,210))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN and retanguloBotao.collidepoint(event.pos) and event.button==1:  #Voltar ao menu princiapl
                x,y,xx,yy,xxx,yyy,xxxx,yyyy,xa,ya=0,0,telacomprimento-50,0,telacomprimento-50,telaalturain-50,0,telaalturain-50,randrange(50,telacomprimento-50,50),randrange(50,telaalturain-50,50)
                with open("pontos.json","w") as arquivo:
                    json.dump(pontos,arquivo)
                menu()#Chamar menu antes de salvar travava o codigo por causa do while true de menu()
            if event.type==MOUSEBUTTONDOWN and event.button==1 and retanguloBotoMenu.collidepoint(event.pos):#Reinicia os pontos
                x,y,xx,yy,xxx,yyy,xxxx,yyyy,xa,ya=0,0,telacomprimento-50,0,telacomprimento-50,telaalturain-50,0,telaalturain-50,randrange(50,telacomprimento-50,50),randrange(50,telaalturain-50,50)
                vezes,veses,vezzes,vesses=0,0,0,0

                pontos={"Bloco Azul:":vezes,
                                "Bloco Verde:":veses,
                                "Bloco Amarelo:":vezzes,
                                "Bloco Vermelho:":vesses}#Dicionario
                with open("pontos.json","w") as arquivo:#Tem que existir um jeito melhor de fazer isso
                    json.dump(pontos,arquivo)
                jogo()
            if event.type==MOUSEBUTTONDOWN and event.button==1 and retanguloBotoRetomarJogo.collidepoint(event.pos):#Continua o jogo
                with open("pontos.json","w") as arquivo:#Tem que existir um jeito melhor de fazer isso
                    json.dump(pontos,arquivo)
                jogo()

while True:
    menu()
    pygame.display.update()
#will update the contents of the entire display 

#Loop infinito



