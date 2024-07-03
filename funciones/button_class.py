from .dibujar import dibujar_texto, dibujar_imagen,get_font
import pygame
class Button(): #mostrar 
    def __init__(self, posicion, lista_texto, tamano_fuente, color_texto, color_fondo,hover_color, orientacion,image):
        self.posicion_x_inicial = posicion[0]
        self.posicion_y_inicial = posicion[1]
        self.tamano_fuente = tamano_fuente
        self.color_texto = color_texto
        self.color_fondo = color_fondo
        self.hover_color = hover_color
        self.texto_input = lista_texto
        self.orientacion = orientacion
        self.image = image
        
    def mostrar_boton(self, ventana:tuple):
        """Mostrar un boton en pantalla

        Args:
            ventana (tuple): tamano de la ventana
        """
        # dibuja de manera vertical
        if self.orientacion == "Vertical":
            # Reiniciar la posición Y para las opciones
            self.posicion_y = self.posicion_y_inicial
            for texto in self.texto_input:
                if self.image:
                    dibujar_imagen(ventana,self.image,(self.posicion_x_inicial, self.posicion_y))
                  
                dibujar_texto(ventana, texto, self.tamano_fuente, self.color_texto, self.color_fondo, (self.posicion_x_inicial, self.posicion_y))

                self.posicion_y += 150
        # dibuja de manera horizontal       
        elif self.orientacion == "Horizontal":  
            # Reiniciar la posición Y para las opciones
            self.posicion_x = self.posicion_x_inicial
            for texto in self.texto_input:
                if self.image:
                    dibujar_imagen(ventana,self.image,(self.posicion_x, self.posicion_y_inicial))
                    
                dibujar_texto(ventana, texto, self.tamano_fuente, self.color_texto, self.color_fondo, (self.posicion_x, self.posicion_y_inicial))

                self.posicion_x += 200                
            
    
    def capturar_mouse_movimiento(self, mouse_posicion:tuple) -> str:
        """Capturar el mouse en movimiento

        Args:
            mouse_posicion (tuple): posicion del mouse

        Returns:
            str: texto en donde se realizo la colision | None si no se realizo
        """
        # utiliza collidepoint para verificar si el mouse está sobre el botón.
        retorno = None
        if self.orientacion == "Vertical":
            self.posicion_y = self.posicion_y_inicial
            # compara las posiciones 
            for texto in self.texto_input:
                #creo el tipo de texto
                texto_renderizado = get_font(self.tamano_fuente).render(texto, True, self.color_texto)
                # Rectangulo de cada texto
                texto_recta = texto_renderizado.get_rect(center=(self.posicion_x_inicial, self.posicion_y))

                if texto_recta.collidepoint(mouse_posicion):
                    retorno = texto 
                self.posicion_y += 150   
        
        elif self.orientacion == "Horizontal":   
            self.posicion_x = self.posicion_x_inicial
            # compara las posiciones 
            for texto in self.texto_input:
                #creo el tipo de texto
                texto_renderizado = get_font(self.tamano_fuente).render(texto, True, self.color_texto)
                # Rectangulo de cada texto
                texto_recta = texto_renderizado.get_rect(center=(self.posicion_x, self.posicion_y_inicial))

                if texto_recta.collidepoint(mouse_posicion):
                    retorno = texto 
                self.posicion_x += 200       
                
        return retorno           
    
    def actualizar_color_texto(self, boton:str, ventana:tuple):
        """Actualizar el color del texto

        Args:
            boton (str): boton al momento de pararse en el mouse
            ventana (tuple): ventana del juego
        """
        # dibuja de manera vertical
        if self.orientacion == "Vertical":
            # Reiniciar la posición Y para las opciones
            self.posicion_y = self.posicion_y_inicial
            for texto in self.texto_input:
                if boton == texto:
                    dibujar_texto(ventana, texto, self.tamano_fuente, self.hover_color, self.color_fondo, (self.posicion_x_inicial, self.posicion_y))
                self.posicion_y += 150
                
         # dibuja de manera Horizontal
        elif self.orientacion == "Horizontal":    
            # Reiniciar la posición Y para las opciones
            self.posicion_x = self.posicion_x_inicial
            for texto in self.texto_input:
                if boton == texto:
                    dibujar_texto(ventana, texto, self.tamano_fuente, self.hover_color, self.color_fondo, (self.posicion_x, self.posicion_y_inicial))
                self.posicion_x += 200   
                
        
        
        
        
