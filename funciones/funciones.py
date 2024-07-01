import pygame


## colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)



tiempo_total = 30
# crear fuente
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

