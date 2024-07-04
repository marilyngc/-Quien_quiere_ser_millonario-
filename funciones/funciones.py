from .pregunta_class import Pregunta


def obtener_preguntas_progresivas(lista_diccionario:list[dict], cantidad_preguntas:int) -> Pregunta:
    """Obtener las preguntas progresivas 

    Args:
        lista_diccionario (list[dict]): lista con los diccionarios de los datos necesarios de las preguntas
        cantidad_preguntas (int): cantidad de preguntas hasta el momento

    Returns:
        Pregunta: el diccionario como una instancia de clase
    """
    pregunta = None
    if cantidad_preguntas <= len(lista_diccionario):
        for i in range(len(lista_diccionario)):
            if cantidad_preguntas == i:
                pregunta = Pregunta(lista_diccionario[i])
                break
        
    return pregunta

def determinar_ultima_ganancia(matriz:list, criterio) -> int: 
    """determinar la ultima ganancia

    Args:
        matriz (list): matriz con la ganancia
        criterio (lambda): criterio como funcion lambda 

    Returns:
        int: ultimo valor de la matriz
    """
    ultimo_valor = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if criterio(matriz[i][j]):
                ultimo_valor = matriz[i][j]
                break

    return ultimo_valor

