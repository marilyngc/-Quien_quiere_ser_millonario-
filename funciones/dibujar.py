from .funciones import dibujar_imagen, dibujar_titulo, renderizar_texto

# esta funcion funciona
# def mostrar_boton(ventana, orientacion, posicion, lista_texto, imagen, tamaño_fuente, color_texto, color_fondo):
#     posicion_x_inicial = posicion[0]
#     posicion_y_inicial = posicion[1]

#     if orientacion == "Vertical":
#         # Reiniciar la posición Y para las opciones
#         posicion_y = posicion_y_inicial
#         for texto in lista_texto:
#             if imagen:
#                 dibujar_imagen(ventana, imagen, (posicion_x_inicial, posicion_y))
#             dibujar_titulo(ventana, texto, tamaño_fuente, color_texto, color_fondo, (posicion_x_inicial, posicion_y))
#             posicion_y += 100
#     elif orientacion == "Horizontal":
#         # Reiniciar la posición X para las opciones
#         posicion_x = posicion_x_inicial
#         for texto in lista_texto:
#             if imagen:
#                 dibujar_imagen(ventana, imagen, (posicion_x, posicion_y_inicial))
#             dibujar_titulo(ventana, texto, tamaño_fuente, color_texto, color_fondo, (posicion_x, posicion_y_inicial))
#             posicion_x += 150

# # def mostrar_boton(ventana, orientacion, posicion,lista_texto, imagen, tamaño_fuente, color_texto, color_fondo):
# #     # dibuja de manera vertical
# #     posicion_x_inicial = posicion[0]
# #     posicion_y_inicial = posicion[1]
# #     if orientacion == "Vertical":
# #         # Reiniciar la posición Y para las opciones
# #         posicion_y = posicion_y_inicial
# #     else:    
# #         posicion_x = posicion_x_inicial
# #         for texto in lista_texto:
# #             if imagen:
# #                 dibujar_imagen(ventana,imagen,(posicion_x, posicion_y))
              
# #             dibujar_titulo(ventana, texto,tamaño_fuente, color_texto, color_fondo, (posicion_x, posicion_y)) 
 
# #     if orientacion == "Vertical":    
# #         posicion_y += 100     
# #     elif orientacion == "Horizontal":   
# #         posicion_x += 150        

# def mouse_movimiento_boton(mouse_posicion, orientacion, posicion, lista_texto):
   
#         posicion_x_inicial = posicion[0]
#         posicion_y_inicial = posicion[1]
#         retorno = None
#         if orientacion == "Vertical":
#             posicion_y = posicion_y_inicial   
#         else:
#             sposicion_x = posicion_x_inicial
#             # compara las posiciones 
#             for texto in lista_texto:
                
#                 texto_recta = renderizar_texto(texto)
#                 if texto_recta.collidepoint(mouse_posicion):
#                     retorno = texto 
                  
#                 if orientacion == "Vertical":
#                     posicion_y += 100  
#                 elif orientacion == "Horizontal":  
#                     posicion_x += 150     
                     
#         return retorno    
       
            
# def mostrar_preguntas(ventana,pregunta,posicion,lista_opcion, color_texto): #PASAR A OTRA CLASE
#     posicion_x_inicial = posicion[0]
#     posicion_y_inicial = posicion[1]
#     dibujar_titulo(ventana, pregunta, 10, color_texto,None,(550,150))
#       # Reiniciar la posición Y para las opciones
#   # Reiniciar la posición Y para las opciones
#     contador = 0
#       # Recorrer las opciones
#     for opcion in lista_opcion:
#         if contador < 2:
#             dibujar_titulo(ventana, opcion, 10, color_texto, None, (posicion_x, posicion_y))
#             posicion_y += 100
#         else:
#             # Cambiar a la segunda columna
#             posicion_x += 300
#             posicion_y = 200  # Resetear Y para la nueva columna
#             dibujar_titulo(ventana, opcion, 10, color_texto, None, (posicion_x,posicion_y))
#             posicion_y += 100
#             contador = 0
#         contador += 1
        
def mostrar_porcentajes(lista_porcentajes:list, ventana, color_texto, coordenadas):
    coordenada_x = coordenadas[0]
    coordenada_y = coordenadas[1]
    for i in range(len(lista_porcentajes)): #IMAGEN DINAMICA
        porcentaje = f"{lista_porcentajes[i]}"
        dibujar_titulo(ventana, str(porcentaje),20, color_texto,None, (coordenada_x, coordenada_y))
        coordenada_x +=50 
        print(lista_porcentajes[i])

def mostrar_ganancias(matriz_ganancias:list, ventana):
    
    posicion_x = 1000
    posicion_y = 100
    
    for i in range(len(matriz_ganancias) -1, -1, -1): 
            for j in range(len(matriz_ganancias[i])):
                dibujar_titulo(ventana,f"${matriz_ganancias[i][j]:3}", 20, (255,255,255), (0,0,0), (posicion_x, posicion_y))   
                posicion_y += 50
                
def mostrar_ultima_ganancia(ganancia:int, ventana, posicion): 
    
    dibujar_titulo(ventana, str(ganancia), 20, (255,255,255), None, posicion)