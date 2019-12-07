import pygame,sys,random
from pygame.locals import *

#Varables
mover_x=300
posX=None
posY=None
ventana_x=1024
ventana_y=576
j=0
aleatorio=0

#colores
blanco=(255,255,255)
negro=(0,0,0)
amarillo=(255,255,0)

def moverNave(x,y):
	imagen_nave=pygame.image.load("imagenes/nave.png")
	ventana.blit(imagen_nave,(x,y))

def Fondo():
	pygame.mouse.set_visible(0)
	fondo=pygame.image.load("imagenes/Fondo_estrellas.jpg")
	ventana.blit(fondo,(0,0))

def Meteoritos(x,y,demora):
	global j,aleatorio
	i=0
	meteorito=pygame.Rect(0,0,100,100)

	#efecto de caida de rectangulos

	while i<demora:
		if i==demora-1:
			aux=meteorito.move(aleatorio,j)
			pygame.draw.rect(ventana,amarillo,aux)
			if j==y:
				j=0
				aleatorio=random.randint(0,1024)
			j=j+1	
		i=i+1





pygame.init()

ventana = pygame.display.set_mode((ventana_x,ventana_y)) # creo un objeto ventana con sus medidas
pygame.display.set_caption("Battle Rows") # pongo un titulo o mensaj



while True: # bucle infinito

    for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
        if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT  
            pygame.quit() # detengo todos los módulos de pygame
            sys.exit() # cerramos la ventana

    #MOVIMIENTO NAVE
    posX,posY=pygame.mouse.get_pos() # tomo las coodenadas (x,y), solo permite tomar la imagen desde la esquina superior izquierda
      	
    #FUNCIONES------------------
    Fondo()
    moverNave(posX-23,posY-15)

    Meteoritos(ventana_x,ventana_y,160)

    pygame.display.update() # la ventana se va a estar actualizando