from .dibujar import dibujar_texto, get_font
import random

class Pregunta: 
    def __init__(self, diccionario: dict, tamano_fuente,color_texto,) -> None: 
        # variables de instancia
        self.pregunta = diccionario["pregunta"] 
        self.opciones = diccionario["opciones"]
        self.correcta = diccionario["correcta"]
        self.dificultad = diccionario["dificultad"]
        self.posicion_x_inicial = 400
        self.posicion_y_inicial = 550  # posicion inicial
        self.tamano_fuente = tamano_fuente
        self.color_texto = color_texto
        # rectangulo de cada opcion
        self.recta = []
        self.texto = []
        for i in range(len(self.opciones)):
            texto = get_font(tamano_fuente).render(self.opciones[i], True, color_texto)
            recta_texto  = texto.get_rect(center=(self.posicion_x_inicial, self.posicion_y_inicial))
            self.texto.append(texto)
            self.recta.append(recta_texto)
        self.actualizar_rectas()
    
    def mostrar_preguntas(self,ventana, color_texto:tuple):
        """mostrar preguntas

        Args:
            ventana (tuple): ventana del juego
            color_texto(tuple): color para el texto
        """
        dibujar_texto(ventana, self.pregunta, 10, color_texto,None,(600,430))
        
    def actualizar_rectas(self):
                
    # Reiniciar la posición Y para las opciones
        posicion_x = self.posicion_x_inicial
        posicion_y = self.posicion_y_inicial
        contador = 0
        # Recorrer las opciones
        for recta in self.recta:
            if contador < 2:
                recta.center = (posicion_x, posicion_y)
                posicion_y += 80
            else:
                # Cambiar a la segunda columna
                posicion_x += 400
                posicion_y = self.posicion_y_inicial  # Resetear Y para la nueva columna
                recta.center = (posicion_x, posicion_y)
                posicion_y += 80
                contador = 0
            contador += 1
            
    def mostrar_opciones(self,ventana):
        for i in range(len(self.opciones)):
            texto_render = self.texto[i]
            texto_recta = self.recta[i]
            ventana.blit(texto_render,texto_recta)
                
    
    def capturar_mouse_movimiento(self, mouse_posicion:tuple) -> str:  
        """Capturar el movimiento del mouse  

        Args:
            mouse_posicion (tuple): posicion del mouse en el momento

        Returns:
            str: opcion elegida
        """
        retorno = None  # Si no se clickeó ninguna opción, devuelve None
     
        for i in range(len(self.recta)):
            if self.recta[i].collidepoint(mouse_posicion):
                retorno = self.opciones[i]
                break
    
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
        
        porcentaje_uno = random.randint(0,100)
        porcentaje_dos = random.randint(0,100 - porcentaje_uno) 
        porcentaje_tres = random.randint(0,100 - porcentaje_uno - porcentaje_dos) 
        porcentaje_cuatro = 100 - porcentaje_uno - porcentaje_dos - porcentaje_tres
        
        lista_porcentaje = [porcentaje_uno, porcentaje_dos, porcentaje_tres, porcentaje_cuatro]
        
        return lista_porcentaje
    
