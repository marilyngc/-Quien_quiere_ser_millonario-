class Pregunta: 
    def __init__(self, diccionario: dict) -> None:
        
        self.pregunta = diccionario['pregunta']
        self.opciones = diccionario["opciones"]
        self.correcta = diccionario["correcta"]
        self.dificultad = diccionario["dificultad"]
    
    
    def es_correcta(lista_diccionarios:list[dict], respuesta:str):
        
        retorno = False
        for pregunta in lista_diccionarios:
            if pregunta.correcta == respuesta:
                retorno = True
                break
            
        return retorno
    
    