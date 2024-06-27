import random
from Archivos.parser_json import parsear_json
from .pregunta_class import *
from .funciones import get_font, dibujar_titulo
path_preguntas ="Archivos\documentos\preguntas_respuestas.json"



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

def mostrar_porcentajes(lista_porcentajes:list, ventana, color_texto, coordenadas):
    coordenada_x = coordenadas[0]
    coordenada_y = coordenadas[1]
    for i in range(len(lista_porcentajes)): #IMAGEN DINAMICA
        porcentaje = f"{lista_porcentajes[i]}"
        dibujar_titulo(ventana, str(porcentaje),20, color_texto,None, (coordenada_x, coordenada_y))
        coordenada_x +=50 
        print(lista_porcentajes[i])

def crear_pista(diccionario_pregunta, lista_pista): 
    
    for diccionario in lista_pista:
        if diccionario_pregunta["pregunta"] == lista_pista["pregunta"]:
            print(lista_pista["pista"])
    

