
# Juego del ahorcado


import random

# Lista de palbras que se van a jugar 

lista_palabras = ["monitor", "teclado", "mouse", "computadora", "impresora", "pantalla"]

# Aqui elije una palabra aleatoria

palabra = random.choice(lista_palabras)

# Aqui muestran los guiones de la palabra elegida 

guiones = []

for letra in palabra:
    
    
    guiones.append("_")
    
# Aqui empieza con el juego (6 intentos)
    
intentos = 6

while intentos > 0: 
    print(" ".join(guiones))
    letra_jugador = input("Por favor, ingrese una letra: ")
    
# Aqui verifico que la letra ingresada sea correcta, y se muestra en su respectivo guion si es correcta

    if letra_jugador in palabra:
        print("Correcto")
        for i, letra in enumerate(palabra):
            if letra_jugador == letra:
                guiones[i] = letra_jugador
                
#Si no lo es, pierde una vida y se vuelve a jugar, hasta que se acabe el juego o se quede sin intentos
       
    else:
        print("Incorrecto")
        intentos -= 1 
        print ("Intentos restantes", intentos)

#Si acierta todas las letras, se muestra la palabra y se sale del juego

    if "_" not in guiones:
        print("¡Enhorabuena! ¡Has acertado¡")
        print("La palabra fue", palabra)
        break
    
# Caso contrario si se quedo sin intentos se muestra la palabra y se sale del juego.
    
else:
    print("Lo siento, has perdido el juego, la palabra era: ", palabra) 