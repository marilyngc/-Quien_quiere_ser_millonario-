from .funciones import dibujar_titulo, get_font

BLANCO = (255, 255, 255)


# metodos que pertenecen a la instancia, es decir al objeto mismo
#para usarlo es atraves del objeto 
# metodos de instancia 

class Pregunta: 
    # metodo
    # por defecto python busca el iniciador 
    # init es un constructor
    def __init__(self, diccionario: dict) -> None: # este metodo inicial se llama a llamar sin que lo lllame
        # variables de instancia
        self.pregunta = diccionario["pregunta"] # -> atributos - son las que tienen un objeto
        self.opciones_originales = diccionario["opciones"]
        self.opciones = diccionario["opciones"]
        self.correcta = diccionario["correcta"]
        self.dificultad = diccionario["dificultad"]
        self.posicion_x = 450
        self.posicion_y = 200  # posicion inicial
  
    # metodo de instancia, se encuentra dentro de la clase Pregunta y le pertenece a la instancia 
    # este metodo se caracteriza por poseer obligatoriamente un parametro  que haga referencia al objeto mismo
    
    # SELF no es una palabra reservada, es un parametro que representa a la instancia
    # SELF hace referencia al objeto , osea se llama asi mismo
    #SELF equivale al nombre del objeto actual que estamos trabajando
    # con el SELF entro a la instancia
    # con metodos de instancia es posible: crear, modificar, eliminar, leer atributos del objeto. se puede llamar otros metodos de instancia dentro de ellos
    def mostrar_preguntas(self,ventana): #PASAR A OTRA CLASE
        dibujar_titulo(ventana, self.pregunta, 10, BLANCO,None,(550,150))
        # Reiniciar la posición Y para las opciones

    # Reiniciar la posición Y para las opciones
        self.posicion_y = 200
        self.posicion_x = 350

        contador = 0

        # Recorrer las opciones
        for opcion in self.opciones:
            if contador < 2:
                dibujar_titulo(ventana, opcion, 10, BLANCO, None, (self.posicion_x, self.posicion_y))
                self.posicion_y += 100
            else:
                # Cambiar a la segunda columna
                self.posicion_x += 300
                self.posicion_y = 200  # Resetear Y para la nueva columna
                dibujar_titulo(ventana, opcion, 10, BLANCO, None, (self.posicion_x, self.posicion_y))
                self.posicion_y += 100
                contador = 0
            contador += 1

    def mouse_movimiento(self, mouse_posicion):  # PASAR A OTRA CLASE
        retorno = None  # Si no se clickeó ninguna opción, devuelve None
        self.posicion_y = 200
        self.posicion_x = 350
    
        contador = 0
    
        for opcion in self.opciones:
            if contador < 2:
                texto_renderizado = get_font(20).render(opcion, True, (255, 255, 255))
                texto_rect = texto_renderizado.get_rect(center=(self.posicion_x, self.posicion_y))
                if texto_rect.collidepoint(mouse_posicion):
                    retorno = opcion  # devuelve la opcion que clikeó
                self.posicion_y += 100
            else:
                # Cambiar a la segunda columna
                self.posicion_x += 300
                self.posicion_y = 200  # Resetear Y para la nueva columna
                texto_renderizado = get_font(20).render(opcion, True, (255, 255, 255))
                texto_rect = texto_renderizado.get_rect(center=(self.posicion_x, self.posicion_y))
                if texto_rect.collidepoint(mouse_posicion):
                    retorno = opcion  # devuelve la opcion que clikeó
                self.posicion_y += 100
                contador = 0
            contador += 1
    
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
    
    def eliminar_dos_respuestas(self): #comodines
        #mejore
        i = 0
        contador = 0
        opciones_eliminadas = []
        #utilizo un while porque si elimino dentro de un for se rompe
        while i < len(self.opciones): # el valor "i" es el que se va a ir aumentando en cada iteracion
            if self.es_correcta(self.opciones[i]) == False and contador < 2:
                opciones_eliminadas.append(self.opciones.pop(i))
                contador += 1
                
            i +=1
        
        return opciones_eliminadas
    
    def crear_pista(self, lista_pista):
        
        for diccionario in lista_pista:
            if self.pregunta == diccionario["pregunta"]:
                print(diccionario["pista"])
                
                
# al llamor la clase, creamos una instancia
# pregunta = Pregunta()