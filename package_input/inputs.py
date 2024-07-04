
def verificar_ingreso_datos(bandera:bool) -> bool: 
    """Verificar el ingreso de los datos

    Args:
        bandera (bool): bandera que indica el ingreso

    Returns:
        bool: True si se ingresaron los datos | False si no se ingresaron los datos y un print avisandolo
    """
    retorno = True
    if bandera == False:
        print("Ya utilizo el comodin") # lo dejamos para defender oralmente
        retorno = False
    
    return retorno

def determinar_formato_ganancia(cadena:str) -> str:
    """Determinar el formato de la ganancia

    Args:
        cadena (str): cadena con el valor a mostrar

    Returns:
        str: la cadena con un formato establecido
    """
    nueva_cadena = ""
    cadena_intermedia = ""
    cadena_formateada = ""
    
    for i in range(len(cadena)-1, -1, -1):
        nueva_cadena += cadena[i]
    
    for i in range(len(cadena)):
        cadena_intermedia += nueva_cadena[i]
        if (i+1) % 3 == 0 and (i+1) != len(cadena): #le sumo uno para poder hacer el resto por 3 y verifico que si es el ultimo no lo agregue 
            cadena_intermedia += "."
    
    for i in range(len(cadena_intermedia)-1, -1, -1):
        cadena_formateada += cadena_intermedia[i]
        
    cadena_formateada = "$" + cadena_formateada
    return cadena_formateada

