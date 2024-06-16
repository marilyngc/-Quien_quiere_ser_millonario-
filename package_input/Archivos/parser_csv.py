import re
def leer_archivos(path:str, lista):
    try:
        with open(path, "r", encoding="utf-8") as archivo:
           
            for linea in archivo:
              
                registro = re.split(",|\n",linea)
                diccionario = {
                    "id": registro[0],
                    "pregunta": registro[1],
                    "comodin": registro[2],
                    "tipo": registro[3],
                    "detalle": registro[4]
     
                }
               
               
                lista.append(diccionario)
        return lista
               
                
    except:
        return "A ocurrido un error al generar la lista en el archivo"  
    
