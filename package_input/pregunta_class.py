class Pregunta: 
    def __init__(self, tematica:dict) -> None:
        self.pregunta = tematica["pregunta"]
        self.opciones = tematica["opciones"]
        self.correcta = tematica["correcta"]
        self.dificultad = tematica["dificultad"]
        
    def es_correcta(diccionario_tematica:dict):
        
        pass