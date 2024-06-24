from .pregunta_class import Pregunta

def establecer_preguntas(lista_con_diccionario: list[dict]) -> list[Pregunta]:
    preguntas = []
    
    for diccionario in lista_con_diccionario: 
        pregunta = Pregunta(diccionario)
        preguntas.append(pregunta)
    print(preguntas)
    return preguntas