from package_input.pregunta_class import *
from package_input.Archivos.parser_json import *
path_preguntas ="package_input\Archivos\documentos\preguntas_respuestas.json"
preguntas_respuestas = parsear_json(path_preguntas)

Pregunta.es_correcta(preguntas_respuestas)

#GUARDAMOS LOS VALORES EN UNA MATRIZ
