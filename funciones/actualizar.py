from .dibujar import dibujar_texto
from .dibujar import mostrar_ganancias, mostrar_porcentajes,mostrar_opciones
from .pregunta_class import Pregunta
from .button_class import Button

def actulizar_pantalla_preguntas(ventana:tuple, background:str, background_opciones:str, tamano_texto:int, color_texto:tuple, color_fondo:tuple, pregunta:Pregunta, comodin:Button, ganancia:list, recurso_comodin:list|None):
    """Actualizar pantalla juego

    Args:
        ventana (tuple): tamaño de la ventana del juego
        background (str): url del fondo 
        background_opciones (str): url del fondo para opciones
        tamano_texto (int): tamaño para el texto
        color_texto (tuple): color para el texto
        color_fondo (tuple): color de fondo poara el texto
        pregunta (Pregunta): la pregunta con la instancia de clase
        comodin (Button): comodines con la instancia de clase
        ganancia (list): matriz con las ganancias
        recurso_comodin (list | None): list lista con los recursos de los comodines | None si no se clickeo un comodin
    """
    ventana.blit(background,(0,0)) 
    ventana.blit(background_opciones,(0,0)) 
    mostrar_ganancias(ganancia, ventana)
    
    bandera = True
    
    pregunta.mostrar_preguntas(ventana,color_texto)
    if recurso_comodin != None:
        if recurso_comodin[1] == "Publico":
            mostrar_porcentajes(recurso_comodin[0], ventana, color_texto, (400,200))
        elif recurso_comodin[1] == "50-50":    
            # opciones 50-50
            mostrar_opciones(ventana, recurso_comodin[0],(440,550))
            bandera = False
        else :
            dibujar_texto(ventana, recurso_comodin[0], tamano_texto, color_texto, color_fondo, (550,200))
                
    if bandera:    
        # preguntas y opcines originales
        lista_opciones = pregunta.retornar_opciones()
        mostrar_opciones(ventana,lista_opciones,(400,550))
    
    # botones comodines 
    comodin.mostrar_boton(ventana)
    
def actualizar_pantalla_menu(ventana:tuple, background:str, texto:str, tamano_texto:int, color_texto:tuple, color_fondo:tuple,  posicion:tuple, boton:Button):
    """Actualiza la pantalla del menu

    Args:
        ventana (tuple): ventana del juego
        background (str): url de la imagen de fondo
        texto (str): texto a escribir
        tamano_texto (int): tamaño del texto
        color_texto (tuple): color para el texto
        color_fondo (tuple): color para el fondo del texto
        posicion (tuple): posicion en la cual escribir el texto
        boton (Button): boton con la instancia de la clase (objeto)
    """
    ventana.blit(background,(0,0)) 
    dibujar_texto(ventana,texto,tamano_texto, color_texto,color_fondo,posicion)
    ## Se dibujan los botones en cada iteración del bucle principal.
 
    boton.mostrar_boton(ventana) 
            
