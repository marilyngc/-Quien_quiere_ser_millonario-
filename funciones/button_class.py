# from .dibujar import  dibujar_imagen
import pygame
class Button(): #mostrar 
    def __init__(self, posicion,orientacion,imagen_url):
        self.posicion_x_inicial = posicion[0]
        self.posicion_y_inicial = posicion[1]
        self.orientacion = orientacion
        # rectangulo de cada imagen
        self.recta = []
        self.imagen_load = []
        self.imagen = imagen_url
        for i in range(len(self.imagen)):
            imagen_load = pygame.image.load(self.imagen[i])
            recta_imagenes  = imagen_load.get_rect(center=(self.posicion_x_inicial, self.posicion_y_inicial))
            self.imagen_load.append(imagen_load)
            self.recta.append(recta_imagenes)
        # Actualizar las posiciones iniciales de los rectángulos
        self.actualizar()
        
    def actualizar(self):
        """Mostrar un boton en pantalla

        Args:
            ventana (tuple): tamano de la ventana
        """
        # dibuja de manera vertical
        if self.orientacion == "Vertical":
            self.posicion_y = self.posicion_y_inicial
            for rect in self.recta:
                rect.center = (self.posicion_x_inicial, self.posicion_y)
                self.posicion_y += 150  # Espacio entre imágenes
        elif self.orientacion == "Horizontal":
            self.posicion_x = self.posicion_x_inicial
            for rect in self.recta:
                rect.center = (self.posicion_x, self.posicion_y_inicial)
                self.posicion_x += 200 # Espacio entre imágenes
                
    def mostrar_boton(self, ventana):
        for i in range(len(self.imagen_load)):
            imagen_load = self.imagen_load[i]
            imagen_recta = self.recta[i]
        
            ventana.blit(imagen_load, imagen_recta)
    
    def capturar_mouse_movimiento(self, mouse_posicion:tuple) -> str:
        """Capturar el mouse en movimiento

        Args:
            mouse_posicion (tuple): posicion del mouse

        Returns:
            str: texto en donde se realizo la colision | None si no se realizo
        """
        # utiliza collidepoint para verificar si el mouse está sobre el botón.

        retorno = False
        for i in range(len(self.recta)):
            if self.recta[i].collidepoint(mouse_posicion):
                retorno = f"Imagen {i + 1}"
           
        return retorno    
    
		    
    
        
        
        
        
