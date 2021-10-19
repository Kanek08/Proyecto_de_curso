from pokemonInicial import SeleccionarPokeInicial
from datos_de_combate import Dato_combate
datoP = Dato_combate()
pokemon = SeleccionarPokeInicial()
print ("Equipo Pokemon")

print("1- Combate")
print("pokemon seleccionado")
print("2- Objetos")
print("3- Pokemon")
print("4- Escapar")
opcion = int(input("¿Qué deberia hacer {pokemon}? "))
if opcion == 1:
    print(f"Puntos de salud{datoP.puntos_de_salud}")
    print(f"Ataque 1")
    print("ataque 2")
    print("ataque 4")
    print("ataque 3")
elif opcion == 2:
    print("Mochila")
    print("1-Objetos curativos")
    print("2-Objetos de combate")
    print("3-Pokebolas")
elif opcion == 3:
    print("pokemon 1")
    print("Pokemon 2")
    pok = int(input("Que pokemon desea sacar: "))
    if pok == 1:
        print("1-sacar")
        print("2-stats")
        opcion = int(input("Eliga una opcion"))
        if opcion == 1:
            print("saca el pokemon")
        elif opcion == 2:
            print(f"Puntos de salud: {datoP.puntos_de_salud()}")
            print(f"Ataque: {datoP.ataque()}")
            print(f"Ataque especial: {datoP.ataque_especial()}")
            print(f"Defensa: {datoP.defensa()}")
            print(f"Defensa especial: {datoP.defensa_especial()}")
            print(f"Velocidad: {datoP.velocidad()}")
    elif pok == 2:
        pass
elif opcion == 4:
    print("Ha escado del combate")    

