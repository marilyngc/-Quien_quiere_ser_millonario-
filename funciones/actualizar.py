from .dibujar import dibujar_titulo
from .dibujar import mostrar_ganancias, mostrar_porcentajes,mostrar_opciones


def actulizar_pantalla_preguntas(ventana, background,background_opciones,texto,tamaño_texto, color_texto, color_fondo, posicion, pregunta,comodin, ganancia, recurso_comodin):
    ventana.blit(background,(0,0)) 
    ventana.blit(background_opciones,(0,0)) 
    dibujar_titulo(ventana,texto, tamaño_texto, color_texto, color_fondo,posicion)
    mostrar_ganancias(ganancia, ventana)
    # muestra las preguntas en ventana

    bandera = True
    
    pregunta.mostrar_preguntas(ventana)
    if recurso_comodin != "":
        if recurso_comodin[1] == "Publico":
            mostrar_porcentajes(recurso_comodin[0], ventana, color_texto, (400,200))
        elif recurso_comodin[1] == "50-50":    
            # opciones 50-50
            mostrar_opciones(ventana, recurso_comodin[0],(440,550))
            bandera = False
        else :
            dibujar_titulo(ventana, recurso_comodin[0], tamaño_texto, color_texto, color_fondo, (550,200))
                
    if bandera:    
        # preguntas y opcines originales
        lista_opciones = pregunta.retornar_opciones()
        mostrar_opciones(ventana,lista_opciones,(440,550))
    
    # botones comodines 
    comodin.mostrar_boton(ventana)
    
    
    
def actualizar_pantalla_menu(ventana, background,texto, tamaño_texto, color_texto, color_fondo,posicion, boton ):
    ventana.blit(background,(0,0)) 
    dibujar_titulo(ventana,texto,tamaño_texto, color_texto,color_fondo,posicion)
    ## Se dibujan los botones en cada iteración del bucle principal.
    boton.mostrar_boton(ventana) 
            
