from funciones.pregunta_class import *
from funciones.funciones import *
from Archivos.parser_json import *
from funciones.comodines import *
path_preguntas ="Archivos\documentos\preguntas_respuestas.json"
preguntas_respuestas = parsear_json(path_preguntas)

videojuegos = [ {
    "pregunta": "¿Cuál es el nombre del personaje principal que el jugador puede elegir al inicio del juego en Genshin Impact?",
    "correcta": "El Viajero (Aether o Lumine)",
    "opciones": ["Diluc", "Mona", "Kaeya","El Viajero (Aether o Lumine)"],
    "dificultad": "facil"
},
{
    "pregunta": "¿Cuántos personajes principales se pueden controlar en GTA V?",
    "correcta": "Tres",
    "opciones": ["Uno", "Cuatro", "Cinco","Tres"],
    "dificultad": "facil"
},
{
    "pregunta": "¿Cuál es el nombre del modo de juego en Fortnite donde los jugadores compiten para ser el último en pie?",
    "correcta": "Battle Royale",
    "opciones": ["Save the World", "Creative Mode", "Arena Mode","Battle Royale"],
    "dificultad": "facil"
},
{
    "pregunta": "¿Cuál es el nombre de la región inspirada en China dentro del juego Genshin Impact?",
    "correcta": "Liyue",
    "opciones": ["Mondstadt", "Inazuma", "Sumeru","Liyue"],
    "dificultad": "medio"
},
{
    "pregunta": "¿Cuál es el nombre del banco que Michael y Trevor roban al inicio de la historia en GTA V?",
    "correcta": "Banco de Ludendorff",
    "opciones": ["Fleeca Bank", "Pacific Standard Public Deposit Bank", "Union Depository","Banco de Ludendorff"],
    "dificultad": "medio"
},
{
    "pregunta": "¿Qué temporada introdujo el evento de colaboración con Marvel que incluía a personajes como Iron Man y Thor en Fortnite?",
    "correcta": "Temporada 4, Capítulo 2",
    "opciones": ["Temporada 5, Capítulo 2", "Temporada 3, Capítulo 1", "Temporada 2, Capítulo 2", "Temporada 4, Capítulo 2"],
    "dificultad": "medio"
},
{
    "pregunta": "¿Qué material necesitas para construir un portal al Nether en Minecraft?",
    "correcta": "Obsidiana",
    "opciones": ["Diamante", "Piedra", "Arena","Obsidiana"],
    "dificultad": "dificil"
    
},
{
    "pregunta": "¿Qué dispositivos se usan comúnmente para jugar Osu?",
    "correcta": "Tableta gráfica y ratón",
    "opciones": ["Teclado y monitor", "Joystick y pantalla táctil", "Gamepad y auriculares","Tableta gráfica y ratón"],
    "dificultad": "dificil"
},
{
    "pregunta": "¿Qué mod en Osu! aumenta la velocidad de la canción y las notas?",
    "correcta": "Double Time (DT)",
    "opciones": ["Hard Rock (HR)", "Hidden (HD)", "Flashlight (FL)","Double Time (DT)"],
    "dificultad": "dificil"
}
  ] 

def establecer_matriz(videojuegos):
    N = 2
    M = 9

    matriz = [[0]*N for _ in range(M)]
    
    print(matriz)
    ganancia_facil = 1
    ganancia_media = 2
    ganancia_dificil = 3
    
    for diccionario in videojuegos:
        for i in range(M): 
            for j in range(N):
                if diccionario["dificultad"] == "facil":
                    matriz[i][0] = diccionario["dificultad"]
                    matriz[i][1] = ganancia_facil
                    

    return matriz
matriz = establecer_matriz(videojuegos)

def mostrar_matriz(matriz:list) -> list: 
    """Mostrar una matriz

    Args:
        matriz (list): matriz proporcionada

    Returns:
        list: muestra la matriz proporcionada
    """
    M = len(matriz)
    N = len(matriz[0])

    for i in range(M): 
        for j in range(N):   
            print(f"{matriz[i][j]:3}", end = " ")
        print("")
        
mostrar_matriz(matriz)