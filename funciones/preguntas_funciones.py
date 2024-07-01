from .pregunta_class import *

# def establecer_preguntas(lista_con_diccionario: list[dict]) -> list[Pregunta]:
#     preguntas = []
    
#     for diccionario in lista_con_diccionario: 
#         pregunta = Pregunta(diccionario)
#         preguntas.append(pregunta)
#     print(preguntas)
#     return preguntas



def preguntas_progresivas(diccionario:dict, valor):
    pregunta = None
    if valor <= len(diccionario):
        for i in range(len(diccionario)):
            if valor == i:
                pregunta = Pregunta(diccionario[i])
                break
        
    return pregunta


# sumar_matriz = lambda matriz: sum(sum(fila) for fila in matriz)

def sumar_matriz(matriz:list): # establezco los valores ganados
    ultimo_valor = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                ultimo_valor = matriz[i][j]
                
            
    return ultimo_valor