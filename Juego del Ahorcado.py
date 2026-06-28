import random


# ESTRUCTURAS DE DATOS


# Diccionario con categorías de palabras (todas tecnológicas)
categorias = {
    "Tecnologia":            ["monitor", "teclado", "mouse", "computadora", "impresora"],
    "Programacion":          ["variable", "funcion", "bucle", "diccionario", "algoritmo"],
    "Redes":                 ["router", "servidor", "protocolo", "firewall", "ethernet"]
}
# Etapas del ahorcado
# Lista con los dibujos del ahorcado (de 6 intentos a 0)
etapas_ahorcado = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

# Diccionario de mensajes motivacionales según intentos restantes
mensajes = {
    6: "Empecemos!",
    5: "Buen comienzo, sigue asi!",
    4: "Vas bien, no te rindas!",
    3: "Cuidado, estas a la mitad.",
    2: "Solo 2 intentos, piensa bien!",
    1: "ULTIMO INTENTO! Tu puedes!",
    0: "Has perdido... pero sigue intentando."
}


# FUNCIONES DE LAS CATEGORIAS


# FUNCIÓN 1: Muestra las categorías y el jugador elige una
def elegir_categoria():
    print("\n=== ELIGE UNA CATEGORIA ===")
    lista = list(categorias.keys())           # Convierte las claves del diccionario en lista
    for i in range(len(lista)):
        print(i + 1, "-", lista[i])           # Muestra: 1 - tecnologia, 2 - lenguajes...

    opcion = int(input("Ingresa el numero de la categoria: "))
    return lista[opcion - 1]                  # Retorna el nombre de la categoría elegida


# FUNCIÓN 2: Elige una palabra aleatoria de la categoría
def elegir_palabra(categoria):
    return random.choice(categorias[categoria])


# FUNCIÓN 3: Crea la lista de guiones según el largo de la palabra
def crear_guiones(palabra):
    guiones = []
    for letra in palabra:
        guiones.append("_")                   # Un guión por cada letra
    return guiones


# FUNCIÓN 4: Dibuja el ahorcado según los intentos que quedan
def mostrar_ahorcado(intentos):
    indice = 6 - intentos                     # 6 intentos = índice 0, 0 intentos = índice 6
    print(etapas_ahorcado[indice])


# FUNCIÓN 5: Verifica si la letra está en la palabra y actualiza los guiones
def verificar_letra(letra, palabra, guiones):
    encontrada = False
    for i in range(len(palabra)):
        if palabra[i] == letra:
            guiones[i] = letra                # Reemplaza el guión con la letra correcta
            encontrada = True
    return encontrada                         # Retorna True si estaba, False si no


# FUNCIÓN 6: Lógica principal de una partida
def jugar(palabra, categoria):
    guiones  = crear_guiones(palabra)
    intentos = 6
    puntos   = 0
    letras_usadas = []                        # Lista simple para guardar letras ya ingresadas

    print("\nCategoria:", categoria)
    print("La palabra tiene", len(palabra), "letras.")

    # Bucle principal: mientras queden intentos
    while intentos > 0:

        mostrar_ahorcado(intentos)
        print("\n", " ".join(guiones))        # Muestra los guiones: _ _ _ _ _
        print("Letras usadas:", letras_usadas)
        print("Intentos restantes:", intentos)
        print(mensajes[intentos])             # Muestra mensaje motivacional

        letra = input("Ingresa una letra: ").lower()

        # Verifica si ya usó esa letra
        if letra in letras_usadas:
            print("Ya usaste esa letra, intenta con otra.")
            continue                          # Vuelve al inicio del bucle sin perder intento

        letras_usadas.append(letra)           # Guarda la letra usada

        # Verifica si la letra es correcta o no
        if verificar_letra(letra, palabra, guiones):
            print("Correcto!")
            puntos = puntos + 10              # Suma 10 puntos por letra correcta
        else:
            print("Incorrecto.")
            intentos = intentos - 1           # Resta un intento

        # Revisa si ya completó la palabra
        if "_" not in guiones:
            mostrar_ahorcado(intentos)
            print("\nFelicitaciones! Adivinaste la palabra:", palabra)
            puntos = puntos + (intentos * 5)  # Bonus por intentos sobrantes
            print("Puntos obtenidos:", puntos)
            return puntos                     # Sale de la función con los puntos ganados

    # Si se acaban los intentos (llega aquí solo si el while terminó sin adivinar)
    mostrar_ahorcado(0)
    print(mensajes[0])
    print("La palabra era:", palabra)
    print("Puntos obtenidos:", puntos)
    return puntos


# FUNCIÓN 7: Muestra el puntaje final con mensaje según desempeño
def mostrar_puntaje(puntaje_total):
    print("\n=============================")
    print("  PUNTAJE FINAL:", puntaje_total, "pts")
    if puntaje_total >= 80:
        print("  Excelente desempeno!")
    elif puntaje_total >= 40:
        print("  Buen trabajo!")
    else:
        print("  Sigue practicando!")
    print("=============================")



# PROGRAMA PRINCIPAL 


def main():
    print("============================")
    print("   JUEGO DEL AHORCADO")
    print("============================")

    puntaje_total = 0

    # Bucle para jugar varias veces
    while True:
        categoria     = elegir_categoria()          # Paso 1: elegir categoría
        palabra       = elegir_palabra(categoria)   # Paso 2: elegir palabra
        puntaje_total = puntaje_total + jugar(palabra, categoria)  # Paso 3: jugar y sumar puntos

        mostrar_puntaje(puntaje_total)              # Paso 4: mostrar puntaje

        otra = input("Quieres jugar otra vez? (s/n): ").lower()
        if otra != "s":
            print("Hasta luego!")
            break                                   # Sale del bucle y termina el programa

main()
