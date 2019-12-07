import pygame,sys,random
from pygame.locals import *

#Varables
posX=None
posY=None
ventana_x=1024
ventana_y=576
j=0
aleatorio=0
tamaño_boton=(100,50)
espacio=0
multi=0


#colores
blanco=(255,255,255)
negro=(0,0,0)
amarillo=(255,255,0)
naranja=(255,128,0)
rojo=(254,0,0)
verde=(57,255,20)

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

	#Efecto de caida de rectangulos
	while i<demora:
		if i==demora-1:
			aux=meteorito.move(aleatorio,j)
			pygame.draw.rect(ventana,amarillo,aux)
			if j==y:
				j=0
				aleatorio=random.randint(0,1024)
			j=j+1	
		i=i+1


def Definir_espaciado(espaciado):
	global espacio
	espacio=tamaño_boton[1]+espaciado


def Boton(tamaño,color,texto,tamFuente):
	global espacio,multi
	centro=ventana_x/2
	#Dibujo boton
	aux=pygame.Rect(centro-tamaño[0]/2,ventana_y/2+espacio*multi,tamaño[0],tamaño[1])
	pygame.draw.rect(ventana,color,aux)

	#Texto en el Boton
	fuente_letra=pygame.font.SysFont("Comic Sans",tamFuente)
	texto=fuente_letra.render(texto,0,blanco)		
	ventana.blit(texto,(centro-tamaño[0]/2+5,ventana_y/2+espacio*multi+10))

	multi=multi+1

def Menu():
	ventana.fill(negro)	
	#Configuracion botones------------------------------------------------------------------------------------------------------------

	Definir_espaciado(10)

	Boton(tamaño_boton,verde,"Iniciar",40)
	Boton(tamaño_boton,naranja,"Reglas",40)
	Boton(tamaño_boton,rojo,"Salir",40)
	#-----------------------------------------------------------------------------------------------------------------------------------

	while True:
		for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
			if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT 
				pygame.quit() # detengo todos los módulos de pygame
				sys.exit() # cerramos la ventana
		pygame.display.update()          





pygame.init()

ventana = pygame.display.set_mode((ventana_x,ventana_y)) # creo un objeto ventana con sus medidas
pygame.display.set_caption("Battle Rows") # pongo un titulo o mensaj



while True: # bucle infinito

    #MOVIMIENTO NAVE---------------------------------------------
    posX,posY=pygame.mouse.get_pos() # tomo las coodenadas (x,y) del mouse 
   

    #FUNCIONES--------------------------------------------------
    Menu()
    
    """
    Fondo()
    moverNave(posX-23,posY-15)
    Meteoritos(ventana_x,ventana_y,160)
	"""

    pygame.display.update() # la ventana se va a estar actualizando



    """
 fuente_letra=pygame.font.SysFont("Comic Sans",45)
  textoAuxiliar=fuente_letra.render("Jugador 2, elija una opción",0,negro)
  ventana.blit(textoAuxiliar,(230,240))
  """