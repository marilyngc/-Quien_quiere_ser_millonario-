import pygame, sys
from funciones.button_class import Button
from funciones.pregunta_class import Pregunta

from funciones.boton_prueba import Button_prueba

from Archivos.parser_json import parsear_json
from Archivos.parser_csv import leer_archivos

from funciones.funciones import dibujar_titulo
from funciones.preguntas_funciones import *
from funciones.actualizar import actulizar_pantalla_preguntas, actualizar_pantalla_menu

from funciones.manejar_eventos import evento, evento_video_juegos

pygame.init() # inicializado pygame
path_comodines = "Archivos\documentos\comodines2.csv"
path_preguntas ="Archivos\documentos\preguntas_respuestas.json"

## json
preguntas_respuestas = parsear_json(path_preguntas)

## csv
lista_pistas = leer_archivos(path_comodines)
# print(pistas)

## colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)

ANCHO_VENTANA = 1100
LARGO_VENTANA = 600
TAMAÑO_VENTANA = (ANCHO_VENTANA, LARGO_VENTANA)
ventana = pygame.display.set_mode(TAMAÑO_VENTANA) # pixeles

pygame.display.set_caption("Quien quiere ser millonario") # titulo de la ventana

# traigo la imagen
icono = pygame.image.load("imagenes\icono\icono_milonario.png")

# seteo el icono
pygame.display.set_icon(icono)

# creo imagen de la superficie
background = pygame.image.load("imagenes\Background.png")
background = pygame.transform.scale(background, (TAMAÑO_VENTANA))

background_jugar = pygame.image.load("imagenes\Background_jugar.jpg")
background_jugar = pygame.transform.scale(background_jugar, (TAMAÑO_VENTANA))


def perdedor():
    
    clock = pygame.time.Clock()
    lista_botones = ["Si","No"]
    boton = Button((450,400),lista_botones, 20,BLANCO, None,ROJO,"Horizontal",None)

    while True:
        mouse_posicion = pygame.mouse.get_pos()
        actualizar_pantalla_menu(ventana, background,"Perdiste!",30,BLANCO, None,(550,100), boton)

        dibujar_titulo(ventana,"Quieres jugar de nuevo?", 30, BLANCO, None,(550,300))

        boton_clickeado = evento(boton,lista_botones ,ventana, mouse_posicion)
        if boton_clickeado == "Si":
            main_menu()
        elif boton_clickeado == "No":
            pygame.quit()  
            sys.exit()                 
    
        pygame.display.update()
        
        clock.tick(15)

def video_juegos():
    #TODO ESTO LUEGO EN UNA FUNCION
    valor = 0
    lista_ganancia = []
    lista_comodines = ["Publico","50-50","Llamada"]
    # comodines
    comodin = Button((400,550),lista_comodines,20,BLANCO, None,ROJO, "Horizontal",None)

    clock = pygame.time.Clock()
    tiempo_inicial = pygame.time.get_ticks()
    
    # bandera_cincuenta = True
    # bandera_llamada = True
    # bandera_publico = True
    lista_banderas = [True, True, True]
    
    
    while True:
        pregunta = preguntas_progresivas(preguntas_respuestas["videojuegos"],valor)
        mouse_posicion = pygame.mouse.get_pos()
        
        actulizar_pantalla_preguntas(ventana, background, "Estamos en video juegos",30,BLANCO, None, (550,100), pregunta, comodin)

        evento = evento_video_juegos(pregunta, comodin, lista_ganancia, mouse_posicion, ventana, lista_pistas, lista_banderas)
        if evento == "correcta":
            tiempo_inicial = pygame.time.get_ticks()
            valor += 1
        elif evento == "incorrecta":
            perdedor()    
         
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = round((tiempo_actual - tiempo_inicial) * 0.001)
        if tiempo_transcurrido == 30:
            perdedor()

        if valor == len(preguntas_respuestas["videojuegos"]):
            break
        
        # mostrar contador
        dibujar_titulo(ventana,str(tiempo_transcurrido),20,BLANCO, None,(70,100) )    
       
        pygame.display.update()
        
        clock.tick(15)

def componentes(): #OPCIONAL
    clock = pygame.time.Clock()
    while True:
        # menu_mouse_posicion = pygame.mouse.get_pos()
        
        ventana.blit(background,(0,0)) 
        dibujar_titulo(ventana,"Estamos en componentes", 30, BLANCO, None,(550,100))
        
        # EVENTOS
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
    
            elif evento.type == pygame.MOUSEBUTTONDOWN :
                pass
        
        pygame.display.update()
        clock.tick(15)
        
def jugar():
    clock = pygame.time.Clock()
    #Los botones se crean fuera del bucle principal para evitar recrearlos en cada iteración.
    lista_menu_jugar = ["VIDEO JUEGOS","COMPONENTES","REGRESAR"]
    boton = Button((550,250), lista_menu_jugar, 30, BLANCO,None, ROJO, "Vertical",None)

    while True:
        mouse_posicion = pygame.mouse.get_pos()
        actualizar_pantalla_menu(ventana, background_jugar,"Elige una categoria", 30, BLANCO, None,(550,100),boton)

        boton_clickeado = evento(boton,lista_menu_jugar ,ventana, mouse_posicion)
        if boton_clickeado == "VIDEO JUEGOS":
            video_juegos()  
        elif boton_clickeado == "COMPONENTES":
            componentes()   
        elif boton_clickeado == "REGRESAR":
            main_menu()    
    
        pygame.display.update()
        
        clock.tick(15)

def main_menu():
    clock = pygame.time.Clock()
    lista_botones = ["JUGAR","SALIR"]
    #Los botones se crean fuera del bucle principal para evitar recrearlos en cada iteración.
    boton = Button_prueba((550,300), lista_botones,30,BLANCO,None, ROJO, "Vertical","imagenes\play_rect.png")

    while  True: # blucle infinito
        menu_mouse_posicion = pygame.mouse.get_pos()
        actualizar_pantalla_menu(ventana, background, "Bienvenido!", 30, BLANCO, None,(550,100),boton)
        
        # EVENTOS
        boton_clickeado = evento(boton,lista_botones ,ventana, menu_mouse_posicion)
        if boton_clickeado == "JUGAR":
            jugar()
        elif boton_clickeado == "SALIR":
            pygame.quit()  
            sys.exit()                 
            
        pygame.display.update()
        clock.tick(15)
    
main_menu()          
        