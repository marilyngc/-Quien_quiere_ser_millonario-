import pygame
import sys
from funciones.funciones import verificar_ingreso_datos
from funciones.comodines import crear_porcenajes, mostrar_porcentajes

def evento(boton,botones_validos, ventana, mouse_posicion):
    retorno = None
    boton_clikeado = boton.mouse_movimiento(mouse_posicion)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            if boton_clikeado in botones_validos:
                retorno = boton_clikeado
        
        elif evento.type == pygame.MOUSEMOTION:
            boton.actualizar_color_texto(boton_clikeado, ventana)
    
    return retorno

BLANCO = (255, 255, 255)

def evento_comodines(comodin_clickeado, pregunta, ventana, lista_pistas, lista_banderas):
    lista_porcentaje = []
    if comodin_clickeado == "Llamada" and verificar_ingreso_datos(lista_banderas[0]):
        pregunta.crear_pista(lista_pistas)
        lista_banderas[0] = False
    elif comodin_clickeado == "50-50" and verificar_ingreso_datos(lista_banderas[1]):
        lista_banderas[1] = False
        pregunta.eliminar_dos_respuestas() #ver como recuperar aquellas eliminadas
      
    elif comodin_clickeado == "Publico" and verificar_ingreso_datos(lista_banderas[2]):
        lista_banderas[2] = False
        
        porcentajes = crear_porcenajes(lista_porcentaje)
        # print(porcentajes)
        mostrar_porcentajes(porcentajes, ventana, BLANCO, (30,550))
                

def evento_video_juegos(pregunta, comodin, lista_ganancia, mouse_posicion, ventana, lista_pistas,lista_banderas):
    lista_eventos = pygame.event.get()
    opcion_correcta = False
    for evento in lista_eventos:
        if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
            pygame.quit()  
            sys.exit()     

        elif evento.type == pygame.MOUSEBUTTONDOWN :
            opcion_clickeada = pregunta.mouse_movimiento(mouse_posicion)
            comodin_clickeado = comodin.mouse_movimiento(mouse_posicion)
            
            if opcion_clickeada :
                
                if pregunta.es_correcta(opcion_clickeada):
                    opcion_correcta = "correcta"
                    ganancia = pregunta.determinar_ganancia(lista_ganancia, 10000,50000,273333)
                    print(ganancia)
                else :  
                    opcion_correcta = "incorrecta"
            
            if comodin_clickeado:
                evento_comodines(comodin_clickeado, pregunta, ventana, lista_pistas, lista_banderas)        

                
        elif evento.type == pygame.MOUSEMOTION:
            comodin.actualizar_color_texto(mouse_posicion, ventana)
    return opcion_correcta        