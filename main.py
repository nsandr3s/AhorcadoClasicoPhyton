
import random
from palabras import obtener_palabra

def mostrar_tablero(palabra_oculta, intentos):
    print("Palabra: " + " ".join(palabra_oculta))
    print("Intentos restantes: " + str(intentos))
    print()

def obtener_letra_usada(letras_usadas):
    while True:
        letra = input("Adivina una letra: ").upper()
        if len(letra) == 1 and letra.isalpha() and letra not in letras_usadas:
            letras_usadas.append(letra)
            return letra
        else:
            print("Letra no válida o ya usada. Intenta de nuevo.")

def ahorcado():
    palabra = obtener_palabra()
    palabra_oculta = ["_" for _ in palabra]
    intentos = 6
    letras_usadas = []

    while intentos > 0 and "_" in palabra_oculta:
        mostrar_tablero(palabra_oculta, intentos)
        letra = obtener_letra_usada(letras_usadas)

        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    palabra_oculta[i] = letra
        else:
            intentos -= 1

        print("Letras usadas: " + ", ".join(letras_usadas))

    if "_" not in palabra_oculta:
        print("¡Felicidades! Adivinaste la palabra: " + palabra)
    else:
        print("¡Lo siento! Te quedaste sin intentos. La palabra era: " + palabra)

if __name__ == "__main__":
    ahorcado()
