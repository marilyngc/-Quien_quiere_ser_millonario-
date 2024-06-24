import pygame
class Button():
    def __init__(self, posicion, texto_input, font, base_color, hover_color):
        self.posicion_x = posicion[0]
        self.posicion_y = posicion[1]
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.texto_input = texto_input
        #creo el tipo de texto
        self.texto = self.font.render(self.texto_input, True, self.base_color)
        # Rectangulo de cada texto
        self.texto_rect = self.texto.get_rect(center=(self.posicion_x, self.posicion_y))
    
    
    def draw(self, ventana):

        # Dibujar el texto del botón sobre la imagen
        ventana.blit(self.texto, self.texto_rect)
    
    def mouse_movimiento(self, mouse_posicion):
        # utiliza collidepoint para verificar si el mouse está sobre el botón.
        # compara las posiciones 
        return self.texto_rect.collidepoint(mouse_posicion)    
    
    def actualizar_color_texto(self,mouse_posicion):
        if self.mouse_movimiento(mouse_posicion):
            self.texto = self.font.render(self.texto_input,True,self.hover_color)
        else:
            self.texto = self.font.render(self.texto_input, True, self.base_color)    
        
        
        
        
