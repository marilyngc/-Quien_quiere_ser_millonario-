import json

# Cargar el archivo JSON
def parsear_json(path:str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        preguntas_respuestas = json.load(file)
        
    return preguntas_respuestas    




