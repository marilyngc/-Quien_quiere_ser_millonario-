import random
from Archivos.parser_json import parsear_json
from pregunta_class import *
path_preguntas ="package_input\Archivos\documentos\preguntas_respuestas.json"



## json
preguntas_respuestas = parsear_json(path_preguntas)

for pregunta_texto in preguntas_respuestas["videojuegos"]:
    pregunta = Pregunta(pregunta_texto)
    break
    
def crear_porcenajes(lista_porcentaje:list) -> list: 

    for i in range(4):
        porcentaje = random.randint(0,100)
        lista_porcentaje.append(porcentaje)

    return lista_porcentaje

lista_porcentaje = []
crear_porcenajes(lista_porcentaje)
print(lista_porcentaje)

def eliminar_opciones(diccionario_preguntas): 
    determinar = pregunta.es_correcta(diccionario_preguntas)
    print(determinar)
    if determinar:
        pass

eliminar_opciones(preguntas_respuestas["videojuegos"])