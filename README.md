# Juego del Ahorcado

**Proyecto Final — Fundamentos de Programacion**  
**Fecha:** Junio 2026

---

##  Objetivo

Desarrollar una version digital e interactiva del clasico juego del ahorcado utilizando Python, aplicando los conceptos aprendidos a lo largo del curso: entorno de programacion, manejo de datos, algoritmos, condicionales, bucles, funciones y estructuras de datos como diccionarios y listas.

El proyecto busca demostrar como la tecnologia puede transformar una actividad recreativa tradicional en una herramienta educativa moderna, accesible e interactiva.

---

##  Descripcion de funcionalidades

### 1. Seleccion de categoria
El jugador elige entre tres categorias de palabras, todas relacionadas con tecnologia e informatica:
- **Tecnologia** — monitor, teclado, mouse, computadora, impresora
- **Programacion** — variable, funcion, bucle, diccionario, algoritmo
- **Redes** — router, servidor, protocolo, firewall, ethernet

### 2. Palabra aleatoria
Una vez elegida la categoria, el sistema selecciona automaticamente una palabra al azar usando `random.choice`.

### 3. Dibujo ASCII del ahorcado
El estado del ahorcado se actualiza visualmente en cada turno. Hay 7 etapas posibles, desde el tablero vacio hasta el ahorcado completo, segun los intentos restantes.

### 4. Sistema de intentos
El jugador tiene **6 intentos** para adivinar la palabra. Por cada letra incorrecta, se pierde un intento y el dibujo avanza una etapa.

### 5. Control de letras usadas
El sistema registra las letras ya ingresadas y avisa al jugador si intenta repetir una, sin penalizarlo con un intento.

### 6. Mensajes motivacionales
En cada turno se muestra un mensaje personalizado segun los intentos restantes, para mantener al jugador motivado durante la partida.

### 7. Sistema de puntuacion
- **+10 puntos** por cada letra correcta adivinada.
- **Bonus** al ganar: se suman 5 puntos por cada intento que sobro.
- Al finalizar cada partida se muestra el puntaje acumulado con un mensaje segun el desempeno.

### 8. Opcion de repetir
Al terminar una partida, el jugador puede elegir jugar otra vez. El puntaje se acumula entre partidas.

---

##  Estructura del codigo

El programa esta organizado en las siguientes funciones:

| Funcion | Descripcion |
|---|---|
| `elegir_categoria()` | Muestra el menu de categorias y valida la eleccion del usuario |
| `elegir_palabra(categoria)` | Selecciona una palabra aleatoria de la categoria elegida |
| `crear_guiones(palabra)` | Genera la lista de guiones segun la longitud de la palabra |
| `mostrar_ahorcado(intentos)` | Muestra el dibujo ASCII correspondiente al estado actual |
| `verificar_letra(letra, palabra, guiones)` | Verifica si la letra esta en la palabra y actualiza los guiones |
| `jugar(palabra, categoria)` | Controla el bucle principal del juego y retorna el puntaje |
| `mostrar_puntaje(puntaje_total)` | Imprime el puntaje final con mensaje de desempeno |
| `main()` | Funcion principal que coordina el flujo completo del programa |

---

##  Tecnologias utilizadas

- **Lenguaje:** Python 
- **Libreria:** `random` (incluida en Python, no requiere instalacion)

---

## ▶ Como ejecutar el programa

1. Asegurate de tener Python  instalado en tu computadora o dispostivo movil.
2. Descarga o clona este repositorio.
3. Abre una terminal en la carpeta del proyecto.
4. Ejecuta el siguiente comando:

```bash
python ahorcado.py
```

5. Sigue las instrucciones en pantalla para jugar.

---

##  Archivos del repositorio

```
 proyecto-ahorcado
 ┣ 📄 ahorcado.py       # Codigo fuente del juego
 ┣ 📄 README.md         # Este archivo
 ┣ 📄 Flujo_Final.png   # Diagrama de flujo del juego
```

---

##  Autor

Proyecto desarrollado de forma individual como entrega final del curso de **Fundamentos de Programacion**.
