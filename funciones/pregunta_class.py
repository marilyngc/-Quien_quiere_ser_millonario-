from .dibujar import dibujar_titulo, get_font
import random
from functools import reduce 

BLANCO = (255, 255, 255)



class Pregunta: 
    def __init__(self, diccionario: dict) -> None: # este metodo inicial se llama a llamar sin que lo lllame
        # variables de instancia
        self.pregunta = diccionario["pregunta"] # -> atributos - son las que tienen un objeto
        self.opciones = diccionario["opciones"]
        self.correcta = diccionario["correcta"]
        self.dificultad = diccionario["dificultad"]
        self.posicion_x_inicial = 400
        self.posicion_y_inicial = 550  # posicion inicial
       
    
    def mostrar_preguntas(self,ventana):
        dibujar_titulo(ventana, self.pregunta, 10, BLANCO,None,(600,430))

    def retornar_opciones(self):
        return self.opciones
    
    def mouse_movimiento(self, mouse_posicion)  :  
        retorno = None  # Si no se clickeó ninguna opción, devuelve None
        posicion_y = self.posicion_y_inicial
        posicion_x = self.posicion_x_inicial
    
        contador = 0
    
        for opcion in self.opciones:
            if contador < 2:
                texto_renderizado = get_font(20).render(opcion, True, (255, 255, 255))
                texto_rect = texto_renderizado.get_rect(center=(posicion_x, posicion_y))
                if texto_rect.collidepoint(mouse_posicion):
                    retorno = opcion  # devuelve la opcion que clikeó
                posicion_y += 80
            else:
                # Cambiar a la segunda columna
                posicion_x += 400
                posicion_y = self.posicion_y_inicial  # Resetear Y para la nueva columna
                texto_renderizado = get_font(20).render(opcion, True, (255, 255, 255))
                texto_rect = texto_renderizado.get_rect(center=(posicion_x, posicion_y))
                if texto_rect.collidepoint(mouse_posicion):
                    retorno = opcion  # devuelve la opcion que clikeó
                posicion_y += 80
                contador = 0
            contador += 1
    
        return retorno

    def es_correcta(self,opcion) -> bool:
        retorno = False 
        if opcion == self.correcta:
            retorno = True
            
        return retorno
    
    def determinar_ganancia(self, matriz_ganancias:list[int], ganancia_facil:int, ganancia_media:int, ganancia_dificil:int, numero_pregunta:int, ultima_ganancia:int) -> list:
        if self.dificultad == "facil":
            ganancia = ganancia_facil 
        elif self.dificultad == "medio":
            ganancia = ganancia_media
        else:
            ganancia = ganancia_dificil
        
        matriz_ganancias[numero_pregunta][0] = ultima_ganancia + ganancia
        
        return matriz_ganancias
    
    #comodines
    def obtener_dos_respuestas(self): 
        i = 0
        contador = 0
        opciones_ciencuenta = [""] * len(self.opciones)
      
        for i in range(len(self.opciones)):
            if self.es_correcta(self.opciones[i]) == False and contador < 1:
                opciones_ciencuenta[i] = self.opciones[i]
                contador += 1
            elif self.es_correcta(self.opciones[i]):
                opciones_ciencuenta[i] = self.opciones[i]
        
        return opciones_ciencuenta
    
    def crear_pista(self, lista_pista):
        for diccionario in lista_pista:
            if self.pregunta == diccionario["pregunta"]:
                pista = diccionario["pista"]
                break
        
        return pista
    
    def crear_porcenajes(self,lista_porcentaje:list) -> list: 
        # correcta = set(filter(lambda opciones: opciones == self.correcta, self.opciones)) #una manera de obtener la correcta 
        
        porcentaje_uno = random.randint(0,100)
        porcentaje_dos = random.randint(0,100 - porcentaje_uno) 
        porcentaje_tres = random.randint(0,100 - porcentaje_uno - porcentaje_dos) 
        porcentaje_cuatro = 100 - porcentaje_uno - porcentaje_dos - porcentaje_tres
        
        lista_porcentaje = [porcentaje_uno, porcentaje_dos, porcentaje_tres, porcentaje_cuatro]
        
        return lista_porcentaje
    
