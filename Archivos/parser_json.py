import json

# Cargar el archivo JSON
def parsear_json(path:str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        preguntas_respuestas = json.load(file)
        
    return preguntas_respuestas    


# Función para imprimir las preguntas y respuestas
# def imprimir_preguntas(respuestas):
#     for categoria, niveles in respuestas.items():
#         print(f"Categoría: {categoria}")
#         for nivel, preguntas in niveles.items():
#             print(f"Nivel: {nivel}")
#             for index,  pregunta in enumerate(preguntas, start=1):
#                     print(f"Pregunta {index}:")
#                     print(f"Pregunta: {pregunta['pregunta']}")
#                     print(f"Respuesta correcta: {pregunta['respuestas']['correcta']}")
#                     print("Respuestas incorrectas:")
#                     for opcion in pregunta['respuestas']['opciones']:
#                         print(f"- {pregunta["respuestas"]["opciones"]}")
#                     print()

def imprimir_preguntas(json_data):
    for pregunta in json_data['videojuegos']:
        print(f"Pregunta:{pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print("-", opcion)
        print(f"Respuesta correcta: {pregunta['correcta']}")
        print(f"Dificultad: {pregunta['dificultad']}\n") # Salto de línea entre preguntas
