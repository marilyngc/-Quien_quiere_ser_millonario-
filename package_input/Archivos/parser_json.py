import json

# Cargar el archivo JSON
def parsear_json(path:str) -> list:
    with open('package_input\Archivos\documentos\preguntas_respuestas.json', 'r', encoding='utf-8') as file:
        preguntas_respuestas = json.load(file)
    return preguntas_respuestas    


# Función para imprimir las preguntas y respuestas
def imprimir_preguntas(respuestas):
    for categoria, niveles in respuestas.items():
        print(f"Categoría: {categoria}")
        for nivel, preguntas in niveles.items():
            print(f"Nivel: {nivel}")
            for index, pregunta in enumerate(preguntas, start=1):
                print(f"Pregunta {index}:")
                print(f"Pregunta: {pregunta['pregunta']}")
                print(f"Respuesta correcta: {pregunta['respuestas']['correcta']}")
                print("Respuestas incorrectas:")
                for incorrecta in pregunta['respuestas']['incorrectas']:
                    print(f"- {incorrecta}")
                print()

