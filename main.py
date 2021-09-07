import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

entrenador = (input('¿Cuál es tu nombre?: '))
print(f"Bienvenido entrenador(a) {entrenador}")
print('--------------------------------------')
print('Seleccion de pokemon')
print('1. Bulbasaur')
print('2. Charmander')
print('3. Squirtle')
pokemon_inicial = int(input('Por favor, selecciona un pokemon: '))
if pokemon_inicial == 1: 
    print(f"Genial entrenador(a) {entrenador}, has seleccionado a Bulbasaur para acompañarte en tu aventura!!!")
    apodo = input('¿Cómo deseas llamar a tu pokemon?: ')
    pause()
    clear()
elif pokemon_inicial == 2:
    print(f"Genial entrenador(a) {entrenador}, has seleccionado a Charmander para acompañarte en tu aventura!!!")
    apodo = input('¿Cómo deseas llamar a tu pokemon?: ')
    print(f"{apodo} ahora es parte de tu equipo pokémon!!!")
    pause()
    clear()
elif pokemon_inicial == 3:
    print(f"Genial entrenador(a) {entrenador}, has seleccionado a Squirtle para acompañarte en tu aventura!!!")
    apodo = input('¿Cómo deseas llamar a tu pokemon?: ')
    print(f"{apodo} ahora es parte de tu equipo pokémon!!!")
    pause()
    clear()
else:
    print(f"Entrenador(a) {entrenador} debes seleccionar una opcion valida!")
    apodo = input('¿Cómo deseas llamar a tu pokemon?: ')
    print(f"{apodo} ahora es parte de tu equipo pokémon!!!")
    pause()
    clear()

print('Menú principal')
print('1. Equipo Pokemón')
print('2. Batallas contra Pokémon salvajes')
print('3. Pokédex')
print('4. Tienda')
print('5. Salir del videojuego')
opcion = int(input('Selecciona un a opción: '))

while True:
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        break
    else:
        continue