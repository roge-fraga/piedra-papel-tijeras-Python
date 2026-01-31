# TODO: 

def pedir_jugada(nombre):
    opciones = ["piedra", "papel", "tijeras"]

    while True:
        jugada = input(f"¡Hola {nombre}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ").lower().strip()
        if jugada in opciones:
            return jugada
        else:
            print(f"❌ {nombre}, opción inválida. Intenta nuevamente.")

logica_ganadora = {
    "piedra" : "tijeras",
    "papel" : "piedra",
    "tijeras" : "papel"
}

emojis = {
    "piedra": "🪨",
    "papel": "📄",
    "tijeras": "✂️"
}

nombre1 = input("¿Cómo se llamará el jugador 1?: ").capitalize()
nombre2 = input("¿Cómo se llamará el jugador 2?: ").capitalize()

jugador1 = pedir_jugada(nombre1)
jugador2 = pedir_jugada(nombre2)

print(f"\n{nombre1} eligió {emojis[jugador1]} {jugador1.capitalize()}")
print(f"{nombre2} eligió {emojis[jugador2]} {jugador2.capitalize()}")

if jugador1 == jugador2:
    print(f"🤝 ¡Ha sido un empate! Ambos jugadores eligieron {jugador1.capitalize()}.")
elif logica_ganadora[jugador1] == jugador2:
    print(f"🏆 Ha ganado {nombre1}.")
else:
    print(f"🏆 Ha ganado {nombre2}.")