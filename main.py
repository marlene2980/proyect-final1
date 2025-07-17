import random
import string



                              
"""importacion del archivo de palabras"""
from palabras import palabras
from mono import vidas
def obtener_palabra_valida(palabras):
    palabra =random . choice(palabras) # seleccionar una palabra al azar de la lista
    
    # si la palabra contiene un guion o un espacio,
    # seguir seleccionado una palabra al azar.
    while '_'  in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()
def muñequito():

    print("============================")
    print(" ¡bienvenido(a) al juego del ahorcado! ")
    print("============================")

    palabra = obtener_palabra_valida(palabras)
    letras_por_adivinar = set (palabra) # conjunto de letras de la palabra que deven ser adivinadas
    abecedario = set(string.ascii_uppercase) #conjunto deen le abcdario.
    letras_adivinadas = set( ) # letras que el usuario ha adivinando duramte el juego.

    vidas = 7

    # obtener respuestas del usuario mientras existan
    # letras pendientes y al jugador le queden vidas.
    while len (letras_por_adivinar) > 0 and vidas > 0:
        # letras adivinadas:
        # ' '. join(['a','b','c'])  --> 'a b c'
        print(f"te quedan {vidas}vidas y has usado estas letras: {' '. join(letras_adivinadas)}")

        #estado actual de la palabra que el jugador debe adivinar (por ejemplo: h - l a)
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) # mostrar estado del ahorcado.
        print(f"palabra: {' '.join(palabra_lista)}")

        # el usuario escoge una letra nueva
        letra_usuario = input('escoge una letra: ').upper()

        # si la letra escogida por el usuario esta en el abcdario
        # y no esta en el conjunto de letras quw ya se han ingresado,
        # se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            # si la letra esta en la palabra, quitarla letra
            # del conjunto de lettras pendientes por adivinar
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print(' ')
            # si la letra no esta en la palabras, quitar una vida.
            else:
                vidas = vidas - 1
                print(F"\nTu letra, {letra_usuario}no esta en la palabra.")
        # si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. por favor escoge una letra nueva. ")
        else:
            print("\nEsta letra no es valida.")


    # el juego llega a esta linea cuando se agotan las vida del jugador
    # o cuando se adivinan todas las letras de la palabras.
    if vidas == 0:
        print(vidas_diccionario_visul[vidas])
        print(f"¡Ahorcado! perdiste. lo lamento mucho. la palabra era:{palabra}")
    else:
        print(f'¡excelente! ¡adivinaste la palabra {palabra}!')
