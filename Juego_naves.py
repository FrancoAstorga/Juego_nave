import pygame,sys,random
from pygame.locals import *

#Varables
posX=None
posY=None
ventana_x=1024
ventana_y=576
j=0
aleatorio=0
tamaño_boton=(200,40)
espacio=0
lista_rectangulos=[]


#colores
blanco=(255,255,255)
negro=(0,0,0)
amarillo=(255,255,0)
naranja=(255,128,0)
rojo=(254,0,0)
verde=(57,255,20)
gris=(125,127,125)


#Jugando-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
def MoverMouse(x,y):
	imagen_mouse=pygame.image.load("imagenes/Apocalypse Cursor.png")
	ventana.blit(imagen_mouse,(x,y))

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

#Botones------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
def Definir_espaciado(espaciado):
	global espacio
	espacio=tamaño_boton[1]+espaciado


def Boton(tamaño,color,texto,tamFuente,pos):
	global espacio
	centro=ventana_x/2

	#Dibujo boton
	aux=pygame.Rect(centro-tamaño[0]/2,ventana_y/2+espacio*pos,tamaño[0],tamaño[1])
	pygame.draw.rect(ventana,color,aux)

	#Texto en el Boton
	fuente_letra=pygame.font.SysFont("Comic Sans MS",tamFuente)
	texto=fuente_letra.render(texto,0,blanco)		
	textoRect=texto.get_rect()
	textoRect.center=(centro-tamaño[0]/2+(tamaño[0]/2),ventana_y/2+espacio*pos+(tamaño[1]/2))
	ventana.blit(texto,textoRect)
	
	return aux

def Cambio_color_boton(lista):
	i=0
	lista_aux=["Iniciar","Reglas","Salir"]

	#Si el mouse colision con algun rectangulo , cambia de color
	while i < len(lista):

		if Hubo_Colision(lista[i])==True:
			#Si cambia de color , vemos en que rectangulo esta para poenrle el texto
			Boton(tamaño_boton,gris,lista_aux[i],20,i)	
		else:
			#Sino colisiona siguen igual
			if i==0:
				pygame.draw.rect(ventana,verde,lista[0])
				Boton(tamaño_boton,verde,"Iniciar",20,0)	
			if i==1:
				pygame.draw.rect(ventana,naranja,lista[1])
				Boton(tamaño_boton,naranja,"Reglas",20,1)
			if i==2:	
				pygame.draw.rect(ventana,rojo,lista[2])
				Boton(tamaño_boton,rojo,"Salir",20,2)

		
		i=i+1
			
#-------------------------------------------------------------------------------------------------------------------
#Logica#------------------------------------------------------------------------------------------------------------

def Hubo_Colision(rectangulo):
	bandera=False
	rectangulo_colision=pygame.Rect(0,0,10,10)
	rectangulo_colision.left,rectangulo_colision.top = pygame.mouse.get_pos()
	if rectangulo_colision.colliderect(rectangulo):
		bandera=True 

	return bandera	




#----------------------------------------------------------------------------------------------------------
#Menu principal#------------------------------------------------------------------------------------------------------
def Menu():
	ventana.fill(negro)	
	#Configuracion botones
	Definir_espaciado(10)
	
	lista_rectangulos.append(Boton(tamaño_boton,verde,"Iniciar",20,0))
	lista_rectangulos.append(Boton(tamaño_boton,naranja,"Reglas",20,1))
	lista_rectangulos.append(Boton(tamaño_boton,rojo,"Salir",20,2))
	
	#-----------------------------------------------------------------------------------------------------------------------------------
	while True:

		for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
			if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT 
				pygame.quit() # detengo todos los módulos de pygame
				sys.exit() # cerramos la ventana

	#Colision----------------------------------------------------------------------------------------------
		Cambio_color_boton(lista_rectangulos)

		pygame.display.update()          



#Inicio--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
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

