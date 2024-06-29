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

# Función para actualizar el temporizador usando Clock
# def mostrar_temporizador(ventana):
#     clock = pygame.time.Clock()  # Crear un objeto Clock
#     for segundos in range(30):
        
#         texto_puntos = Button(posicion=(550,300), texto_input= f"{segundos}", font=get_font(30), base_color=BLANCO, hover_color=ROJO)
#         texto_puntos.draw(ventana)
#         pygame.display.flip()
#         clock.tick(1)

# dibuja texto
def dibujar_titulo(ventana, mensaje,tamaño_fuente ,color_texto, color_fondo, posicion): 
        menu_texto = get_font(tamaño_fuente).render(mensaje, True, color_texto, color_fondo)
        menu_recta = menu_texto.get_rect(center = (posicion[0], posicion[1]))
        ventana.blit(menu_texto,menu_recta)  

def verificar_ingreso_datos(bandera:bool) -> bool: 
    """Verificar el ingreso de los datos

    Args:
        bandera (bool): bandera que indica el ingreso

    Returns:
        bool: True si se ingresaron los datos | False si no se ingresaron los datos y un print avisandolo
    """
    retorno = True
    if bandera == False:
        print("Ya utilizo el comodin")
        retorno = False
    
    return retorno