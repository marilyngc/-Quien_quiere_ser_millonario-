from package_input.inputs import determinar_formato_ganancia
import pygame


def get_font(tamano:int) -> str:
    """Obtener fuente

    Args:
        tamano (int): tamaño de la fuente

    Returns:
        str: fuente del texto
    """
    
    return pygame.font.Font("font\Font.ttf",tamano) # definir la configuracion de la fuente

def dibujar_imagen(ventana:tuple, image_url:str ,posicion:tuple):
    """Dibuja una imagen

    Args:
        ventana (tuple): ventana del juego
        image_url (str): el path relativo
        posicion (tuple): posicion en tuplas
    """
    imagen = pygame.image.load(image_url)
    imagen_rectangulo = imagen.get_rect(center= (posicion[0], posicion[1]))
    ventana.blit(imagen,imagen_rectangulo)

def renderizar_texto(self, texto:str) -> str:
    """Texto renderizado

    Args:
        texto (str): texto a renderizar

    Returns:
        str: texto renderizado
    """
    #creo el tipo de texto
    texto_renderizado = get_font(self.tamano_fuente).render(texto, True, self.color_texto)
    # Rectangulo de cada texto
    return  texto_renderizado.get_rect(center=(self.posicion_x_inicial, self.posicion_y))
    
# dibuja texto
def dibujar_texto(ventana:tuple, mensaje:str ,tamano_fuente:int ,color_texto:tuple , color_fondo:tuple, posicion:tuple):
    """Dibuja un texto en pantalla

    Args:
        ventana (tuple): ventana del juego
        mensaje (str): mensaje a escribir
        tamano_fuente (int): tamaño de la fuente
        color_texto (tuple): color para el texto
        color_fondo (tuple): color para el fondo
        posicion (tuple): posicion para escribir el texto
    """
    texto = get_font(tamano_fuente).render(mensaje, True, color_texto, color_fondo)
    texto_rectangulo = texto.get_rect(center = (posicion[0], posicion[1]))
    ventana.blit(texto,texto_rectangulo)  
        
def mostrar_opciones(ventana:tuple, lista_opciones:list, posiciones:tuple):
    """Muestra las opciones

    Args:
        ventana (tuple): ventana del juego
        lista_opciones (list): lista con las opciones de las posibles respuestas
        posiciones (tuple): posicion donde comienzan a dibujarse las respuestas
    """
    # Reiniciar la posición Y para las opciones
    posicion_x_inicial = posiciones[0]
    posicion_y_inicial = posiciones[1]

    posicion_x = posicion_x_inicial
    posicion_y = posicion_y_inicial
    contador = 0
    # Recorrer las opciones
    for opcion in lista_opciones:
        if contador < 2:
            dibujar_texto(ventana, opcion, 15,(255,255,255), None, (posicion_x, posicion_y))
            posicion_y += 80
        else:
            # Cambiar a la segunda columna
            posicion_x += 400
            posicion_y = posicion_y_inicial  # Resetear Y para la nueva columna
            dibujar_texto(ventana, opcion, 15,(255,255,255), None, (posicion_x, posicion_y))
            posicion_y += 80
            contador = 0
        contador += 1
            
def mostrar_porcentajes(lista_porcentajes:list, ventana:tuple, color_texto:tuple, coordenadas:tuple):
    """Mostrar porcentajes en pantalla

    Args:
        lista_porcentajes (list): lista con los porcentajes
        ventana (tuple): ventana del juego
        color_texto (tuple): color para el texto
        coordenadas (tuple): coordenadas para empezar a escribir el texto
    """
    coordenada_x = coordenadas[0]
    coordenada_y = coordenadas[1]
    lista_abcd = ["A","B","C","D"]
    if lista_porcentajes != None:
        for i in range(len(lista_porcentajes)):
            porcentaje = f"{lista_abcd[i]} = {lista_porcentajes[i]}%"
            dibujar_texto(ventana, str(porcentaje),20, color_texto,None, (coordenada_x, coordenada_y))
            coordenada_x +=150

def mostrar_ganancias(matriz_ganancias:list, ventana:tuple):
    """Mostrar ganancias

    Args:
        matriz_ganancias (list): matriz con las ganancias
        ventana (tuple): ventana de la pantalla
    """
    posicion_x = 1000
    posicion_y = 90
    
    for i in range(len(matriz_ganancias) -1, -1, -1): 
        for j in range(len(matriz_ganancias[i])):
            dibujar_texto(ventana,f"{determinar_formato_ganancia(str(matriz_ganancias[i][j])):3}", 20, (255,255,255), None, (posicion_x, posicion_y))   
            posicion_y +=32
            
def mostrar_ultima_ganancia(ganancia:int, ventana:tuple, posicion:tuple): 
    """Mostrar la ultima ganancia

    Args:
        ganancia (int): ultima ganancia generada
        ventana (tuple): ventana del juego
        posicion (tuple): posicion en la cual escribir
    """
    dibujar_texto(ventana, ganancia, 20, (255,255,255), None, posicion)
    
    