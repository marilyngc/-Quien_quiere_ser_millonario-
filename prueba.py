from funciones.pregunta_class import *
from funciones.preguntas_funciones import *
from Archivos.parser_json import *
from funciones.comodines import *
path_preguntas ="Archivos\documentos\preguntas_respuestas.json"
preguntas_respuestas = parsear_json(path_preguntas)

# def establecer_preguntas(lista_con_diccionario: list[dict]) -> list[Pregunta]:
#     preguntas = []
    
#     for diccionario in lista_con_diccionario: 
#         pregunta = Pregunta(diccionario)
#         preguntas.append(pregunta)

#     return preguntas
    
# videojuegos = establecer_preguntas(preguntas_respuestas["videojuegos"])
# componentes = establecer_preguntas(preguntas_respuestas["componentes_computadora"])

# respuesta = "ROM (Memoria de Solo Lectura)"

# retorno = Pregunta.es_correcta(componentes,respuesta)
# print(retorno)

#GUARDAMOS LOS VALORES EN UNA MATRIZ

# def preguntas_progresivas(diccionario:dict, valor):
#     for i in range(len(diccionario)):
#         if valor == i:
#             pregunta = Pregunta(diccionario[i])
#             break
        
#     return pregunta

# valor = 1
# pregunta = preguntas_progresivas(preguntas_respuestas["videojuegos"], valor)
# print(pregunta)

# N = 3
# M = 3

# matriz = [[0]*N for _ in range(M)]

# matriz_con_valores = establecer_matriz(matriz)
# print(matriz_con_valores)

# ganacia = sumar_matriz(matriz_con_valores)
# print(ganacia)

# eliminar_opciones(preguntas_respuestas["videojuegos"])