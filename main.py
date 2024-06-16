import pygame, sys
from package_input.button_class import Button
from package_input.Archivos.parser_json import imprimir_preguntas,parsear_json



pygame.init() # inicializado pygame
path_preguntas ="package_input\Archivos\documentos\preguntas_respuestas.json"

preguntas_respuestas = parsear_json(path_preguntas)
# Ejecutar la función para imprimir las preguntas y respuestas
imprimir_preguntas_preguntas = imprimir_preguntas(preguntas_respuestas)
print(imprimir_preguntas)

## colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AZUL_CLARO = (0, 150, 255)


ventana = pygame.display.set_mode((1100, 600)) # pixeles

pygame.display.set_caption("Quien quiere ser millonario") # titulo ed la ventana

# traigo la imagen
icono = pygame.image.load("imagenes\icono\icono_milonario.png")
# seteo el icono
pygame.display.set_icon(icono)

# creo imagen de la superficie
background = pygame.image.load("imagenes\Background.png")
background_jugar = pygame.image.load("imagenes\Background_jugar.jpg")

# crear fuente
def get_font(tamaño):
    return pygame.font.Font("font\Font.ttf",tamaño) # definir la configuracion de la fuente

def jugar():
    #Los botones se crean fuera del bucle principal para evitar recrearlos en cada iteración.
    selecionar_tema_boton = Button(posicion=(550,300), texto_input= "VIDEO JUEGOS", font=get_font(30), base_color=BLANCO, hover_color=ROJO)
    regresar_boton = Button( posicion=(550,400), texto_input= "REGRESAR", font=get_font(30), base_color="#d7fcd4", hover_color=ROJO)
    
    while True:
        menu_mouse_posicion = pygame.mouse.get_pos()
        ventana.blit(background_jugar,[0,0]) 
        menu_texto = get_font(30).render("Seleciona el tema",True,(0,0,0),(0,150,255))
         # POSICION
        menu_recta = menu_texto.get_rect(center = (550, 100))
        ventana.blit(menu_texto,menu_recta)  
        
        # Se dibujan los botones en cada iteración del bucle principal.
        selecionar_tema_boton.draw(ventana)
        regresar_boton.draw(ventana)
        
        # EVENTOS
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
    
            elif evento.type == pygame.MOUSEBUTTONDOWN :
                if selecionar_tema_boton.mouse_movimiento(menu_mouse_posicion):
                    pass
                if regresar_boton.mouse_movimiento(menu_mouse_posicion):
                    main_menu()
            elif evento.type == pygame.MOUSEMOTION:
                selecionar_tema_boton.actualizar_color_texto(menu_mouse_posicion)
                regresar_boton.actualizar_color_texto(menu_mouse_posicion)

        pygame.display.update()

def main_menu():
    #Los botones se crean fuera del bucle principal para evitar recrearlos en cada iteración.
    jugar_boton = Button(posicion=(550,300), texto_input= "JUGAR", font=get_font(30), base_color=BLANCO, hover_color=ROJO)
    salir_boton = Button( posicion=(550,400), texto_input= "SALIR", font=get_font(30), base_color="#d7fcd4", hover_color=ROJO)
    
    while  True: # blucle infinito
        
        ventana.blit(background,[0,0]) 
        
        menu_mouse_posicion = pygame.mouse.get_pos()
        
        menu_texto = get_font(60).render("Bienvenido!",True,BLANCO)
        # POSICION
        menu_recta = menu_texto.get_rect(center = (550, 100))
        
        ## Se dibujan los botones en cada iteración del bucle principal.
        jugar_boton.draw(ventana)
        salir_boton.draw(ventana)
        
        ventana.blit(menu_texto,menu_recta)  
             
        # EVENTOS
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT: # pregunto si presiono la X de la ventana
                pygame.quit()  
                sys.exit()     
                    
            elif evento.type == pygame.MOUSEBUTTONDOWN:    
                if jugar_boton.mouse_movimiento(menu_mouse_posicion):
                    jugar()
                if salir_boton.mouse_movimiento(menu_mouse_posicion):
                    pygame.quit()  
                    sys.exit() 
            elif evento.type == pygame.MOUSEMOTION:
                jugar_boton.actualizar_color_texto(menu_mouse_posicion)
                salir_boton.actualizar_color_texto(menu_mouse_posicion)


        pygame.display.update()
    
    
main_menu()          
        