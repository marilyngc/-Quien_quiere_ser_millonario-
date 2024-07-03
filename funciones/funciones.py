from .pregunta_class import *
from functools import reduce

def preguntas_progresivas(diccionario:dict, valor):
    pregunta = None
    if valor <= len(diccionario):
        for i in range(len(diccionario)):
            if valor == i:
                pregunta = Pregunta(diccionario[i])
                break
        
    return pregunta

def determinar_ultima_ganancia(matriz:list, criterio): 
    ultimo_valor = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if criterio(matriz[i][j]):
                ultimo_valor = matriz[i][j]
    

    return ultimo_valor

