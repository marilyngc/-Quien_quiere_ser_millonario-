from .dibujar import dibujar_titulo
from .dibujar import mostrar_ganancias, mostrar_porcentajes
from .manejar_eventos import obtener_evento_comodines

def actulizar_pantalla_preguntas(ventana, background,background_opciones,texto,tamaño_texto, color_texto, color_fondo, posicion, pregunta,comodin, ganancia, recurso_comodin):
    ventana.blit(background,(0,0)) 
    ventana.blit(background_opciones,(0,0)) 
    dibujar_titulo(ventana,texto, tamaño_texto, color_texto, color_fondo,posicion)
    mostrar_ganancias(ganancia, ventana)
    # muestra las preguntas en ventana
    
    mostrar_porcentajes(recurso_comodin, ventana, color_texto, (550,600))
    # dibujar_titulo(ventana, recurso_comodin, tamaño_texto, color_texto, color_fondo, (550,200))
    
    pregunta.mostrar_preguntas(ventana)
    
    # botones comodines 
    comodin.mostrar_boton(ventana)
    
    
    
def actualizar_pantalla_menu(ventana, background,texto, tamaño_texto, color_texto, color_fondo,posicion, boton ):
    ventana.blit(background,(0,0)) 
    dibujar_titulo(ventana,texto,tamaño_texto, color_texto,color_fondo,posicion)
    ## Se dibujan los botones en cada iteración del bucle principal.
    boton.mostrar_boton(ventana) 
            
