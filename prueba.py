from package_input.pregunta_class import *
from package_input.Archivos.parser_json import *
path_preguntas ="package_input\Archivos\documentos\preguntas_respuestas.json"
preguntas_respuestas = parsear_json(path_preguntas)

def establecer_preguntas(lista_con_diccionario: list[dict]) -> list[Pregunta]:
    preguntas = []
    
    for diccionario in lista_con_diccionario: 
        pregunta = Pregunta(diccionario)
        preguntas.append(pregunta)

    return preguntas
    
videojuegos = establecer_preguntas(preguntas_respuestas["videojuegos"])
componentes = establecer_preguntas(preguntas_respuestas["componentes_computadora"])

respuesta = "ROM (Memoria de Solo Lectura)"

retorno = Pregunta.es_correcta(componentes,respuesta)
print(retorno)

#GUARDAMOS LOS VALORES EN UNA MATRIZ
