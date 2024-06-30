from .funciones import dibujar_titulo

def actulizar_pantalla_preguntas(ventana, background,texto,tamaño_texto, color_texto, color_fondo, posicion, pregunta,comodin):
    ventana.blit(background,(0,0)) 
    dibujar_titulo(ventana,texto, tamaño_texto, color_texto, color_fondo,posicion)
    
    # muestra las preguntas en ventana
    pregunta.mostrar_preguntas(ventana)
    
    # botones comodines 
    comodin.mostrar_boton(ventana)
    
def actualizar_pantalla_menu(ventana, background,texto, tamaño_texto, color_texto, color_fondo,posicion, boton ):
    ventana.blit(background,(0,0)) 
    dibujar_titulo(ventana,texto,tamaño_texto, color_texto,color_fondo,posicion)
    ## Se dibujan los botones en cada iteración del bucle principal.
    boton.mostrar_boton(ventana) 
            
