import re
def validate_number(mensaje:str,numero: int | float,minimo: int | float,maximo: int | float, reintentos: int ,tipo:type) -> float|int|None:
    contador_intentos = 0
    while numero < minimo or numero > maximo:
        print(f"intento numero: {contador_intentos}")
        numero = input(f"ERROR {mensaje} "); 
        numero = tipo(numero);        
        
        if contador_intentos == reintentos:
            print("se agotaron los intentos")
        contador_intentos += 1
    return numero    

def get_int(mensaje:str, minimo:int, maximo:int, reintentos:int) -> int|None:
    while True:
        try:
            numero = input(mensaje)
            numero = int(numero)

            if type(numero) is int:
                return validate_number(mensaje,numero,minimo,maximo,reintentos,int)

        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            exit()  # Sale del programa limpiamente

        except ValueError:
            print("ERROR: debe ingresar un número entero.")
            
def get_float(mensaje:str, minimo:int, maximo:int, reintentos:int) -> float|None:
    while True:
        try:
            numero = input(mensaje)
            numero = float(numero)

            if type(numero) is float:
                return validate_number(mensaje,numero,minimo,maximo,reintentos,float)

        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            exit()  # Sale del programa limpiamente

        except ValueError:
            print("ERROR: debe ingresar un número decimal.")

def validar_caracteres(mensaje: str) -> str:
    while True:  # Bucle para solicitar la entrada hasta que sea válida
        try:
            cadena_ingresada = input(mensaje)
            cadena_ingresada = cadena_ingresada.capitalize()

            # Validar que la cadena tenga menos de 20 caracteres
            if len(cadena_ingresada) > 20:
                print("ERROR: La cadena debe tener menos de 20 caracteres.")
                continue  # Volver a solicitar la entrada
            
            # Validar que la cadena contenga solo letras (sin números ni símbolos)
            if not re.match("^[a-zA-Z]+$", cadena_ingresada):
                print("ERROR: La cadena debe contener solo letras.")
                continue  # Volver a solicitar la entrada
            else:
                return cadena_ingresada   
         
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            exit()  # Sale del programa limpiamente

