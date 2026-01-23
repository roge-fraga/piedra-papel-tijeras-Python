# TODO: Lo ingresado por el usuario deberia ser lowercase
# TODO: Replay con bucle while
# TODO: Manejo de errores por si ingresan un numero o algo distinto a string

nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

jugador1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ")
jugador2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print(f"Ha ganado {nombre1}")
else:
    print(f"Ha ganado el {nombre2}")