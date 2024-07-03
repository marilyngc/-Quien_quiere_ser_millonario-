from package_input.inputs import determinar_formato_ganancia
import pygame

def get_font(tamaño):
    return pygame.font.Font("font\Font.ttf",tamaño) # definir la configuracion de la fuente

def dibujar_imagen(ventana,image_url,posicion):
    menu_imagen = pygame.image.load(image_url)
    menu_recta = menu_imagen.get_rect(center= (posicion[0], posicion[1]))
    ventana.blit(menu_imagen,menu_recta)

def renderizar_texto(self,texto):
    #creo el tipo de texto
    texto_renderizado = get_font(self.tamaño_fuente).render(texto, True, self.color_texto)
    # Rectangulo de cada texto
    return  texto_renderizado.get_rect(center=(self.posicion_x_inicial, self.posicion_y))
    
# dibuja texto
def dibujar_titulo(ventana, mensaje,tamaño_fuente ,color_texto, color_fondo, posicion): 
        menu_texto = get_font(tamaño_fuente).render(mensaje, True, color_texto, color_fondo)
        menu_recta = menu_texto.get_rect(center = (posicion[0], posicion[1]))
        ventana.blit(menu_texto,menu_recta)  
        
def mostrar_opciones(ventana, lista_opciones, posiciones):
     # Reiniciar la posición Y para las opciones
     posicion_x_inicial = posiciones[0]
     posicion_y_inicial = posiciones[1]

     posicion_x = posicion_x_inicial
     posicion_y = posicion_y_inicial
     contador = 0
     # Recorrer las opciones
     for opcion in lista_opciones:
         if contador < 2:
             dibujar_titulo(ventana, opcion, 15,(255,255,255), None, (posicion_x, posicion_y))
             posicion_y += 80
         else:
             # Cambiar a la segunda columna
             posicion_x += 400
             posicion_y = posicion_y_inicial  # Resetear Y para la nueva columna
             dibujar_titulo(ventana, opcion, 15,(255,255,255), None, (posicion_x, posicion_y))
             posicion_y += 80
             contador = 0
         contador += 1
            

def mostrar_porcentajes(lista_porcentajes:list, ventana, color_texto, coordenadas):
    coordenada_x = coordenadas[0]
    coordenada_y = coordenadas[1]
    lista_abcd = ["A","B","C","D"]
    if lista_porcentajes != None:
        for i in range(len(lista_porcentajes)):
            porcentaje = f"{lista_abcd[i]} = {lista_porcentajes[i]}%"
            dibujar_titulo(ventana, str(porcentaje),20, color_texto,None, (coordenada_x, coordenada_y))
            coordenada_x +=150


def mostrar_ganancias(matriz_ganancias:list, ventana):
    
    posicion_x = 1000
    posicion_y = 100
    
    for i in range(len(matriz_ganancias) -1, -1, -1): 
            for j in range(len(matriz_ganancias[i])):
                dibujar_titulo(ventana,f"{determinar_formato_ganancia(str(matriz_ganancias[i][j])):3}", 20, (255,255,255), (0,0,0), (posicion_x, posicion_y))   
                posicion_y += 50
                
def mostrar_ultima_ganancia(ganancia:int, ventana, posicion): 
    
    dibujar_titulo(ventana, ganancia, 20, (255,255,255), None, posicion)
    
    