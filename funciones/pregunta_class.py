from .funciones import dibujar_titulo, get_font

BLANCO = (255, 255, 255)

class Pregunta: 
    def __init__(self, diccionario: dict) -> None:
        self.pregunta = diccionario["pregunta"]
        self.opciones = diccionario["opciones"]
        self.correcta = diccionario["correcta"]
        self.dificultad = diccionario["dificultad"]
        self.posicion_x = 550
        self.posicion_y = 200  # posicion inicial
  
      
    def mostrar_preguntas(self,ventana):
        dibujar_titulo(ventana, self.pregunta, 10, BLANCO,None,(550,150))
                # Reiniciar la posición Y para las opciones
        self.posicion_y = 200
        # recorre las opciones
        for opciones in self.opciones:
            dibujar_titulo(ventana, opciones, 13, BLANCO, None,(self.posicion_x, self.posicion_y))

            self.posicion_y += 50
            
    
    def mouse_movimiento(self, mouse_posicion):
        retorno = None # Si no se clickeó ninguna opción, devuelve None
        self.posicion_y = 200
        for opcion in self.opciones:
            texto_renderizado = get_font(20).render(opcion, True, (255, 255, 255))
            texto_rect = texto_renderizado.get_rect(center=(self.posicion_x, self.posicion_y))
            
            if texto_rect.collidepoint(mouse_posicion):
                retorno = opcion # devuelve la opcion que clikeó
            self.posicion_y += 50   
                
        return retorno       
      
    def es_correcta(self,opcion) -> bool:
        retorno = False 
        if opcion == self.correcta:
            # print("repuesta correcta :D")
            retorno = True
        # else:
            # print("respuesta incorrecta :C")
            
        return retorno
    
    def determinar_ganancia(self, lista_ganancia:list[int], ganancia_facil:int, ganancia_media:int, ganancia_dificil:int) -> list:
     
        if self.dificultad == "facil":
            lista_ganancia.append(ganancia_facil)
        elif self.dificultad == "medio":
            lista_ganancia.append(ganancia_media)
        else:
            lista_ganancia.append(ganancia_dificil)
            
        return lista_ganancia