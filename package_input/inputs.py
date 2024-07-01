import re
def verificar_ingreso_datos(bandera:bool) -> bool: 
    """Verificar el ingreso de los datos

    Args:
        bandera (bool): bandera que indica el ingreso

    Returns:
        bool: True si se ingresaron los datos | False si no se ingresaron los datos y un print avisandolo
    """
    retorno = True
    if bandera == False:
        print("Ya utilizo el comodin")
        retorno = False
    
    return retorno


