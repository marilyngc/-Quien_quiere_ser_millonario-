from .pregunta_class import *

# def establecer_preguntas(lista_con_diccionario: list[dict]) -> list[Pregunta]:
#     preguntas = []
    
#     for diccionario in lista_con_diccionario: 
#         pregunta = Pregunta(diccionario)
#         preguntas.append(pregunta)
#     print(preguntas)
#     return preguntas

N = 3
M = 3

matriz = [[0]*N for _ in range(M)]

def establecer_matriz(matriz:list):
    
    for i in range(M):
        for j in range(N): 
            if i == 0:
                matriz[i][j] = 10000
            elif i == 1:
                matriz[i][j] = 50000
            else:
                matriz[i][j] = 273333
    
    return matriz

def preguntas_progresivas(diccionario:dict, valor):
    for i in range(len(diccionario)):
        if valor == i:
            pregunta = Pregunta(diccionario[i])
            break
        
    return pregunta

def sumar_matriz(matriz:list):
    suma = 0
    for i in range(M):
        for j in range(N):
            suma += matriz[i][j]
                
            
    return suma