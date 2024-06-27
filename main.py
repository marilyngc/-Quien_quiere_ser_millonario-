import pygame, sys
from funciones.button_class import Button
from funciones.pregunta_class import Pregunta

from Archivos.parser_json import imprimir_preguntas,parsear_json
from Archivos.parser_csv import leer_archivos

from funciones.funciones import *
from funciones.preguntas_funciones import *

pygame.init() # inicializado pygame
path_comodines = "Archivos\documentos\comodines.csv"
path_preguntas ="Archivos\documentos\preguntas_respuestas.json"

## json
preguntas_respuestas = parsear_json(path_preguntas)

## csv
# print("comodines")
# lista_comodines = []
# imprimir_comodines = leer_archivos(path_comodines,lista_comodines)
# print(imprimir_comodines)

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

    while True:
        ventana.blit(background,(0,0)) 
        dibujar_titulo(ventana,"Perdiste!", 30, BLANCO, None,(550,100))
        
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
                
        pygame.display.update()
        
        clock.tick(15)

def video_juegos():
    #TODO ESTO LUEGO EN UNA FUNCION
    valor = 0
    lista_ganancia = []

    clock = pygame.time.Clock()
    
    tiempo_inicial = pygame.time.get_ticks()
    while True:
        pregunta = preguntas_progresivas(preguntas_respuestas["videojuegos"],valor)
        mouse_posicion = pygame.mouse.get_pos()
        
        ventana.blit(background,(0,0)) 
        dibujar_titulo(ventana,"Estamos en video juegos", 30, BLANCO, None,(550,100))
        
        # muestra las preguntas en ventana
        pregunta.mostrar_preguntas(ventana)
        
        # EVENTOS
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
    
            elif evento.type == pygame.MOUSEBUTTONDOWN :
                opcion_clickeada = pregunta.mouse_movimiento(mouse_posicion)
                if opcion_clickeada :
                    if pregunta.es_correcta(opcion_clickeada):
                        tiempo_inicial = pygame.time.get_ticks()
                        valor += 1
                        ganancia = pregunta.determinar_ganancia(lista_ganancia, 10000,50000,273333)
                        print(ganancia)
                    else : 
                        perdedor()
                        
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        
        if tiempo_transcurrido == 30:
            pygame.quit()  
            sys.exit()   
            
        print(tiempo_transcurrido * 0.001)
        pygame.display.update()
        
        clock.tick(15)

def componentes():
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
    videojuegos_tema_boton = Button(posicion=(350,300), texto_input= "VIDEO JUEGOS", font=get_font(30), base_color=BLANCO, hover_color=ROJO) #setea los botones desde la clase button
    componentes_tema_boton = Button(posicion=(750,300), texto_input= "COMPONENTES", font=get_font(30), base_color=BLANCO, hover_color=ROJO)
    regresar_boton = Button( posicion=(550,400), texto_input= "REGRESAR", font=get_font(30), base_color="#d7fcd4", hover_color=ROJO)
    
    while True:
        menu_mouse_posicion = pygame.mouse.get_pos()
        ventana.blit(background_jugar,(0,0)) 
        dibujar_titulo(ventana,"Elige una categoria", 30, BLANCO, None,(550,100))
        
        # Se dibujan los botones en cada iteración del bucle principal.
        videojuegos_tema_boton.draw(ventana)
        componentes_tema_boton.draw(ventana)
        regresar_boton.draw(ventana)
        
        # EVENTOS
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
    
            elif evento.type == pygame.MOUSEBUTTONDOWN :
                if videojuegos_tema_boton.mouse_movimiento(menu_mouse_posicion):
                    video_juegos()
                if componentes_tema_boton.mouse_movimiento(menu_mouse_posicion):
                    componentes()
                if regresar_boton.mouse_movimiento(menu_mouse_posicion):
                    main_menu()
            elif evento.type == pygame.MOUSEMOTION:
                videojuegos_tema_boton.actualizar_color_texto(menu_mouse_posicion)
                componentes_tema_boton.actualizar_color_texto(menu_mouse_posicion)
                regresar_boton.actualizar_color_texto(menu_mouse_posicion)

        pygame.display.update()

def main_menu():
    clock = pygame.time.Clock()
    #Los botones se crean fuera del bucle principal para evitar recrearlos en cada iteración.
    jugar_boton = Button(posicion=(550,300), texto_input= "JUGAR", font=get_font(30), base_color=BLANCO, hover_color=ROJO)
    salir_boton = Button( posicion=(550,400), texto_input= "SALIR", font=get_font(30), base_color="#d7fcd4", hover_color=ROJO)
    
    while  True: # blucle infinito
        
        ventana.blit(background,[0,0]) 
        
        menu_mouse_posicion = pygame.mouse.get_pos()
        
        menu_texto = get_font(60).render("Bienvenido!",True,BLANCO)
        # POSICION
        menu_recta = menu_texto.get_rect(center = (550, 100))
        
        ## Se dibujan los botones en cada iteración del bucle principal.
        jugar_boton.draw(ventana)
        salir_boton.draw(ventana)
        
        ventana.blit(menu_texto,menu_recta)  
             
        # EVENTOS
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN:    
                if jugar_boton.mouse_movimiento(menu_mouse_posicion):
                    jugar()
                if salir_boton.mouse_movimiento(menu_mouse_posicion):
                    pygame.quit()  
                    sys.exit() 
            elif evento.type == pygame.MOUSEMOTION:
                jugar_boton.actualizar_color_texto(menu_mouse_posicion)
                salir_boton.actualizar_color_texto(menu_mouse_posicion)


        pygame.display.update()
        clock.tick(15)
    
main_menu()          
        