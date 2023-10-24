  # pedir al jugar ingresar el nombre
nombre_jugador = input("Ingrese su nombre: ")


# Definir el laberinto como una lista de cadenas
laberinto = [
    "#######################",
    "#P....................#",
    "#.###################.#",
    "#.#.................#.#",
    "#.#.###############.#.#",
    "#.#.#...............#.#",
    "#.#.#.###############.#",
    "#.#.#.#...............#",
    "#.#.#.#################",
    "#.#.#.................#",
    "#.#.###################",
    "#.#...................#",
    "#.#####################",
    "#.....................#",
    "#######################"
]

# Función para imprimir el laberinto en la pantalla
def imprimir_laberinto():
    for fila in laberinto:
        print(fila)

# Función para mover al personaje en el laberinto
def mover_personaje(direccion):
    global laberinto
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'P':
                if direccion == '↑' and laberinto[i - 1][j] == '.':
                    laberinto[i - 1] = laberinto[i - 1][:j] + 'P' + laberinto[i - 1][j + 1:]
                    laberinto[i] = laberinto[i][:j] + '.' + laberinto[i][j + 1:]
                elif direccion == '↓' and laberinto[i + 1][j] == '.':
                    laberinto[i + 1] = laberinto[i + 1][:j] + 'P' + laberinto[i + 1][j + 1:]
                    laberinto[i] = laberinto[i][:j] + '.' + laberinto[i][j + 1:]
                elif direccion == '←' and laberinto[i][j - 1] == '.':
                    laberinto[i] = laberinto[i][:j - 1] + 'P' + laberinto[i][j] + laberinto[i][j + 1:]
                elif direccion == '→' and laberinto[i][j + 1] == '.':
                    laberinto[i] = laberinto[i][:j] + laberinto[i][j + 1] + 'P' + laberinto[i][j + 2:]

# dar un mensaje de bienvenida
print(f"Bienvenido, {nombre_jugador}! Comienza a explorar el laberinto.")

# Bucle principal del juego
while True:
    imprimir_laberinto()
    movimiento = input("Mueve al personaje (↑ ↓ ← → o Q para salir): ")
    if movimiento == 'Q':
        break
    if movimiento in ['↑', '↓', '←', '→']:
        mover_personaje(movimiento)
    else:
        print("Movimiento no válido. Usa ↑ ↓ ← → o Q para salir.")
