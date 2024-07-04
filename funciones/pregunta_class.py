from .dibujar import dibujar_texto, get_font
import random

class Pregunta: 
    def __init__(self, diccionario: dict) -> None: 
        # variables de instancia
        self.pregunta = diccionario["pregunta"] 
        self.opciones = diccionario["opciones"]
        self.correcta = diccionario["correcta"]
        self.dificultad = diccionario["dificultad"]
        self.posicion_x_inicial = 400
        self.posicion_y_inicial = 550  # posicion inicial
       
    
    def mostrar_preguntas(self,ventana, color_texto:tuple):
        """mostrar preguntas

        Args:
            ventana (tuple): ventana del juego
            color_texto(tuple): color para el texto
        """
        dibujar_texto(ventana, self.pregunta, 10, color_texto,None,(600,430))

    def retornar_preguntas(self):
        return self.pregunta
    
    def retornar_opciones(self) -> list:
        """retornan opciones

        Returns:
            list: lista de opciones
        """
        return self.opciones
    
    def capturar_mouse_movimiento(self, mouse_posicion:tuple) -> str:  
        """Capturar el movimiento del mouse  

        Args:
            mouse_posicion (tuple): posicion del mouse en el momento

        Returns:
            str: opcion elegida
        """
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

    def es_correcta(self,opcion:str) -> bool:
        """Determinar la correcta

        Args:
            opcion (str): opcion elegida

        Returns:
            bool: True si es la opcion correcta | False si es la incorrecta
        """
        retorno = False 
        if opcion == self.correcta:
            retorno = True
            
        return retorno
    
    def determinar_ganancia(self, matriz_ganancias:list[int], ganancia_facil:int, ganancia_media:int, ganancia_dificil:int, numero_pregunta:int, ultima_ganancia:int) -> list:
        """Determinar ganancia

        Args:
            matriz_ganancias (list[int]): matriz con ganancias generadas
            ganancia_facil (int): ganancia en dificultad facil
            ganancia_media (int): ganancia en dificultad media
            ganancia_dificil (int): ganancia en dificultad dificil
            numero_pregunta (int): numero de la pregunta
            ultima_ganancia (int): ultima ganancia generada

        Returns:
            list: matriz establecida con la ganancia actualizada
        """
        if self.dificultad == "facil":
            ganancia = ganancia_facil 
        elif self.dificultad == "medio":
            ganancia = ganancia_media
        else:
            ganancia = ganancia_dificil
        
        matriz_ganancias[numero_pregunta][0] = ultima_ganancia + ganancia
        
        return matriz_ganancias
    
    #comodines
    def obtener_dos_respuestas(self) -> list: 
        """Obtener dos respuestas

        Returns:
            list: lista con 2 opciones incorrectas vacia 
        """
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
    
    def obtener_pista(self, lista_pista:list[dict]) -> str:
        """obtener pista

        Args:
            lista_pista (list[dict]): lista con diccionarios que contienen las preguntas y pistas

        Returns:
            pista: str de la pista
        """
        
        for diccionario in lista_pista:
            if self.pregunta == diccionario["pregunta"]:
                pista = diccionario["pista"]
                break
        
        return pista
    
    def crear_porcenajes(self,lista_porcentaje:list) -> list: 
        """Crear porcentajes

        Args:
            lista_porcentaje (list): lista vacia

        Returns:
            list: listas con porcentajes generados de forma aleatoria
        """
        # correcta = set(filter(lambda opciones: opciones == self.correcta, self.opciones)) #una manera de obtener la correcta 
        
        porcentaje_uno = random.randint(0,100)
        porcentaje_dos = random.randint(0,100 - porcentaje_uno) 
        porcentaje_tres = random.randint(0,100 - porcentaje_uno - porcentaje_dos) 
        porcentaje_cuatro = 100 - porcentaje_uno - porcentaje_dos - porcentaje_tres
        
        lista_porcentaje = [porcentaje_uno, porcentaje_dos, porcentaje_tres, porcentaje_cuatro]
        
        return lista_porcentaje
    
