import random

def obtener_palabra():
    palabras = ["python", "desarrollo", "backend", "programacion", "ahorcado"]
    return random.choice(palabras).upper()
