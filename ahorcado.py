

import random

lista_palabras = ["monitor", "teclado", "mouse", "computadora", "impresora", "pantalla"]

palabra = random.choice(lista_palabras)

guiones = []

for letra in palabra:
    
    
    guiones.append("_")
intentos = 6

while intentos > 0: 
    print(" ".join(guiones))
    letra_jugador = input("Por favor, inngrese una letra: ")

    if letra_jugador in palabra:
        print("Correcto")
        for i, letra in enumerate(palabra):
            if letra_jugador == letra:
                guiones[i] = letra_jugador
       
    else:
        print("Incorrecto")
        intentos -= 1 
        print ("Intentos restantes", intentos)

    if "_" not in guiones:
        print("¡Enhorabuena! ¡Has acertado¡")
        print("La palabra fue", palabra)
        break
    
else:
    print("Lo siento, has perdido el juego, la palabra era: ", palabra) 