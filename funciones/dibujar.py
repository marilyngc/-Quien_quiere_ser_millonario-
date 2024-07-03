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

def mostrar_porcentajes(lista_porcentajes:list, ventana, color_texto, coordenadas):
    coordenada_x = coordenadas[0]
    coordenada_y = coordenadas[1]
    
    for i in range(len(lista_porcentajes)):
        porcentaje = f"{lista_porcentajes[i]}%"
        dibujar_titulo(ventana, str(porcentaje),20, color_texto,None, (coordenada_x, coordenada_y))
        coordenada_x +=50 
        print(lista_porcentajes[i])

def mostrar_ganancias(matriz_ganancias:list, ventana):
    
    posicion_x = 1000
    posicion_y = 100
    
    for i in range(len(matriz_ganancias) -1, -1, -1): 
            for j in range(len(matriz_ganancias[i])):
                dibujar_titulo(ventana,f"{determinar_formato_ganancia(str(matriz_ganancias[i][j])):3}", 20, (255,255,255), (0,0,0), (posicion_x, posicion_y))   
                posicion_y += 50
                
def mostrar_ultima_ganancia(ganancia:int, ventana, posicion): 
    
    dibujar_titulo(ventana, ganancia, 20, (255,255,255), None, posicion)