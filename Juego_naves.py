import pygame,sys,random
from pygame.locals import *

#Varables
ventana_x=1024
ventana_y=576
j=0
aleatorio_meteorito=0
aleatorio_2=0
aleatorio_3=0
aleatorio_meteorito2=0
aleatorio_meteorito3=0
tamaño_boton=(200,40)
espacio=0
lista_rectangulos=[]
espacio_reglas=0
booleano_menu=False
contador_animacion=0
contador_animacion2=0
timer=0
aleatorioX_1=100
aleatorioY_1=100
aleatorioX_2=100
aleatorioY_2=100
aleatorioX_3=100
aleatorioY_3=100
color_meteorito=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

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
def moverNave(x,y):
	imagen_nave=pygame.image.load("imagenes/nave.png")
	ventana.blit(imagen_nave,(x,y))

def Fondo():
	pygame.mouse.set_visible(0)
	fondo=pygame.image.load("imagenes/Fondo_estrellas.jpg")
	ventana.blit(fondo,(0,0))

def Contador_ganar(limite):
	global timer
	if timer<limite:
		fuente_timer=pygame.font.SysFont("Comic Sans MS",20)
		texto=fuente_timer.render("Distancia: "+str(timer),0,amarillo)
		ventana.blit(texto,(880,10))
		timer+=1

def Meteoritos(y,demora):
	global j,aleatorio
	i=0
	meteorito=pygame.Rect(0,0,100,100)

	#Efecto de caida de rectangulos
	while i<demora:
		if i==demora-1:
			aux=meteorito.move(aleatorio_meteoritos,j)
			pygame.draw.rect(ventana,amarillo,aux)
			if j==y:
				j=0
				aleatorio_meteoritos=random.randint(0,1024)
			j=j+1	
		i=i+1

def MeteoritosFacil(y,demora,velocidad):
	global j,aleatorio_meteorito,aleatorio_meteorito2,aleatorio_meteorito3,color_meteorito,aleatorioX_1,aleatorioY_1,aleatorioX_2,aleatorioY_2,aleatorioX_3,aleatorioY_3


	#Son 3 meteoritos
	meteorito=pygame.Rect(10,0,aleatorioX_1,aleatorioY_1)
	meteorito2=pygame.Rect(350,0,aleatorioX_2,aleatorioY_2)
	meteorito3=pygame.Rect(690,0,aleatorioX_3,aleatorioY_3)

	
	
	#Primer meteorito------------------------------------				
	i=0
	while i<demora:
		aux=meteorito.move(aleatorio_meteorito,j)
		aux2=meteorito2.move(aleatorio_meteorito2,j)
		aux3=meteorito3.move(aleatorio_meteorito3,j)

		pygame.draw.rect(ventana,color_meteorito,aux)
		pygame.draw.rect(ventana,color_meteorito,aux2)
		pygame.draw.rect(ventana,color_meteorito,aux3)
		
		if j>=y:
			j=0
			color_meteorito=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
			#cambiamos los tamaños
			aleatorioY_1=random.randint(100,300)
			aleatorioY_2=random.randint(100,300)
			aleatorioY_3=random.randint(100,300)
			aleatorioX_1=random.randint(100,300)
			aleatorioX_2=random.randint(100,300)
			aleatorioX_3=random.randint(100,300)
			
			#restamos el tamaño de la pantalla donde empieza el rectangulo 
			aleatorio_meteorito=random.randint(0,300)
			aleatorio_meteorito2=random.randint(0,300)
			aleatorio_meteorito3=random.randint(0,300)

			
		if i==demora-1:
			j=j+velocidad		
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
			#Si hubo click se pone en uno
			if pygame.mouse.get_pressed()[0]==1:
				if i==0:
					Iniciar()
				if i==1:
					Reglas()
				if i==2:
					pygame.quit() # detengo todos los módulos de pygame
					sys.exit()
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

#Opciones del menu-----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
def Iniciar():


	while True: # bucle infinito

		for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
			if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT
				pygame.quit() # detengo todos los módulos de pygame
				sys.exit() # cerramos la ventana

		#MOVIMIENTO NAVE
		posX,posY=pygame.mouse.get_pos() # tomo las coodenadas (x,y), solo permite tomar la imagen desde la esquina superior izquierda

		Fondo()
		moverNave(posX-23,posY-15)

		MeteoritosFacil(ventana_y,10,5)

		Contador_ganar(500)

		pygame.display.update() # la ventana se va a estar actualizando




def Reglas():
	global booleano_menu
	booleano_menu=True

	rectangulo_colision=pygame.Rect(0,0,10,10)

	lista_marciano=cargarImagenesSimuAnimacion()
	ventana.fill(negro)

	while True:

		for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
			if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT 
				pygame.quit() # detengo todos los módulos de pygame
				sys.exit()

		

		Colocar_Texto(10,0,"1-Si te tocan los rectangulos moris bro",32,naranja)
		Colocar_Texto(10,100,"2-Tenes 3 vidas",32,naranja)
		Colocar_Texto(10,200,"3-Si llegas a los 1000m ganas",32,naranja)

		boton_volver=Colocar_boton("Volver al menu",30,770,470,240,70,rojo)
		rectangulo_colision.left,rectangulo_colision.top = pygame.mouse.get_pos()

		mostrarImagenesSimuAnimacion(lista_marciano,4)


		#Si el mouse toca el boton
		if rectangulo_colision.colliderect(boton_volver):
			Colocar_boton("Volver al menu",30,770,470,240,70,gris) 
			if pygame.mouse.get_pressed()[0]==1:
				Menu()

		pygame.display.update()
			


#-------------------------------------------------------------------------------------------------------------------
#Logica#------------------------------------------------------------------------------------------------------------

def Hubo_Colision(rectangulo):
	bandera=False
	rectangulo_colision=pygame.Rect(0,0,10,10)
	rectangulo_colision.left,rectangulo_colision.top = pygame.mouse.get_pos()
	if rectangulo_colision.colliderect(rectangulo):
		bandera=True 

	return bandera

def Colocar_imagen(x,y,ruta):	
	imagen_aux=pygame.image.load(ruta)
	ventana.blit(imagen_aux,(x,y))

def Colocar_Texto(x,y,texto,tamFuente,color):
	fuente_aux=pygame.font.SysFont("Comic Sans MS",tamFuente)
	texto=fuente_aux.render(texto,0,color)
	ventana.blit(texto,(x,y))


def Colocar_boton(texto,tamFuente,boton_x,boton_y,largo,alto,color_boton):
	boton_aux=pygame.Rect(boton_x,boton_y,largo,alto)
	pygame.draw.rect(ventana,color_boton,boton_aux)
	fuente_letra=pygame.font.SysFont("Comic Sans MS",tamFuente)
	texto=fuente_letra.render(texto,0,negro)		
	textoRect=texto.get_rect()
	textoRect.center=(boton_x+largo/2,boton_y+alto/2)
	ventana.blit(texto,textoRect)
	return boton_aux

#------------------------------------------------------------------------------------------------------
#Animacion#------------------------------------------------------------------------------------------------------

def cargarImagenesSimuAnimacion():
    listaImagenesMarciano=[]
    i=1

    while i< 96: 
        nombreImag = "animacion_marciano/"+"Frame "+"("+str(i)+")"+".jpg"
        imagMarciano = pygame.image.load(nombreImag)
        listaImagenesMarciano.append(imagMarciano)
        i+=1
    return listaImagenesMarciano


def mostrarImagenesSimuAnimacion(listaImagenesMarciano,limite):
    global contador_animacion,contador_animacion2
    if contador_animacion>limite : 
          ventana.blit(listaImagenesMarciano[contador_animacion2],(510,100))
          contador_animacion=0 
          if contador_animacion2<45:
              contador_animacion2+=1 
    
    if contador_animacion2==45:
    	contador_animacion2=0          
    contador_animacion+=1     
          





#----------------------------------------------------------------------------------------------------------
#Menu principal#------------------------------------------------------------------------------------------------------

def LLuvia_estrellas(y,demora):
	global j,aleatorio_2,aleatorio_3
	i=0
	multicolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	#cae de lugares aleatorios y elegimos la cantidad de estrellas
	estrella=pygame.Rect(0,0,6,45)
	estrella_2=pygame.Rect(0,0,6,45)
	
	#Efecto de caida de rectangulos
	while i<demora:
		aux=estrella.move(aleatorio_2,j)
		pygame.draw.rect(ventana,multicolor,aux)
		if j==y:#Cuando llega al final vuelve al principio
			j=0
			aleatorio_2=random.randint(0,1024)
		j=j+1

		i=i+1

	while i<demora+20:
		aux_2=estrella_2.move(aleatorio_3,j)
		pygame.draw.rect(ventana,multicolor,aux_2)
		if j==y:#Cuando llega al final vuelve al principio
			j=0
			aleatorio_3=random.randint(0,1024)
		j=j+1

		i=i+1
	




def Titulo():
	multicolor=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	fuente_letra=pygame.font.SysFont("Comic Sans MS",50)
	texto=fuente_letra.render("Battle Rows",0,multicolor)
	textoRect=texto.get_rect()
	textoRect.center=(ventana_x/2,30)
	ventana.blit(texto,textoRect)

def Menu():
	#Configuracion botones
	Definir_espaciado(10)
	#Solo lo agrega la primera vez
	if booleano_menu==False:
		lista_rectangulos.append(Boton(tamaño_boton,verde,"Iniciar",20,0))
		lista_rectangulos.append(Boton(tamaño_boton,naranja,"Reglas",20,1))
		lista_rectangulos.append(Boton(tamaño_boton,rojo,"Salir",20,2))
	
	i=0
	bandera_Imagen=False
	#-----------------------------------------------------------------------------------------------------------------------------------
	while True:

		for evento in pygame.event.get():# recorro la lista de eventos que tiene pygame
			if evento.type == QUIT: # si evento que ocurrio es del tipo QUIT 
				pygame.quit() # detengo todos los módulos de pygame
				sys.exit() # cerramos la ventana	

		ventana.fill(negro)
		#Titulo
		Titulo()
		#Imagenes-----------------------------------------------------------------------------------------
		Colocar_imagen(800,320,"imagenes/alien_1.jpg")
		#Movimiento de imagen
		Colocar_imagen(i,70,"imagenes/alien_2.png")
		#Movimiento de izquierda a derecha de la nave--------------------------------------------------------
		if i<=ventana_x-130 and bandera_Imagen==False:
			i=i+2
			if i==ventana_x-130:
				bandera_Imagen=True
		if i>=0 and bandera_Imagen==True:
			i=i-2	
			if i==0:
				bandera_Imagen=False
		#------------------------------------------------------------------------------------------------------		
		#Colision----------------------------------------------------------------------------------------------
		Cambio_color_boton(lista_rectangulos)
		#Con numero grandes va muy rapido
		LLuvia_estrellas(ventana_y,10)
		

		pygame.display.update()          


#Inicio/Main--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
pygame.init()

ventana = pygame.display.set_mode((ventana_x,ventana_y)) # creo un objeto ventana con sus medidas
pygame.display.set_caption("Battle Rows") # pongo un titulo o mensaj

Menu()


