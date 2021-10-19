  
from random import randint
import os

clear = lambda: os.system('cls')
pause = lambda: os.system('pause')

class SeleccionarPokeInicial:
    # TODO 
    # -Ver como cambia "n" con respecto al paso del juego.

    def __init__(self, pokemon_inicial):
        self.pokemon_inicial = pokemon_inicial
    
    # POKEMON 1 --> Bulbasaur
    def salud_pokemon1(self):
        # PUNTOS DE SALUD
        #  -viS valor individual de salud.
        #  -ebS estadistica base en salud
        #  -n es nivel actual del pokemon
        n = 5 
        ebS = 45
        viS = randint(1, ebS)
        puntos_salud = viS + (2 * ebS)
        puntos_salud = puntos_salud * (n/100)
        puntos_salud = puntos_salud + 10 + n
        return puntos_salud
    
    def ataque_pokemon1(self):
        #PUNTOS DE ATAQUE
        #  -viA valor individual de ataque.
        #  -ebA estadistica base en ataque.
        #  -n es nivel actual del pokemon
        n = 5
        ebA = 49
        viA = randint(1, ebA)
        puntos_ataque = viA + (2 * ebA)
        puntos_ataque = puntos_ataque * (n/100)
        puntos_ataque = puntos_ataque + 5
        return puntos_ataque
    
    def defensa_pokemon1(self):
        #PUNTOS DE DEFENSA
        #  -vid valor individual de defensa.
        #  -ebd estadistica base en defensa.
        #  -n es nivel actual del pokemon

        n = 5
        ebD = 49
        viD = randint(1, ebD)
        puntos_defensa = viD + (2 * ebD)
        puntos_defensa = puntos_defensa * (n/100)
        puntos_defensa = puntos_defensa + 5
        return puntos_defensa
    
    def ataque_especial_pokemon1(self):
        #PUNTOS DE ATAQUE ESPECIAL
        #  -viAE valor individual de ataque especial.
        #  -ebAE estadistica base en ataque especial.
        #  -n es nivel actual del pokemon
        n = 5
        ebAE = 65
        viAE = randint(1, ebAE)
        ataque_especial = viAE + (2 * ebAE)
        ataque_especial = ataque_especial * (n/100)
        ataque_especial = ataque_especial + 5
        return ataque_especial
    
    def defensa_especial_pokemon1(self):
        #PUNTOS DEFENSA ESPECIAL
        #  -viDE valor individual de defensa especial.
        #  -ebDE estadistica base en defensa especial.
        #  -n es nivel actual del pokemon
        n = 5
        ebDE = 65
        viDE = randint(1, ebDE)
        defensa_especial = viDE + (2 * ebDE)
        defensa_especial = defensa_especial * (n/100)
        defensa_especial = defensa_especial + 5
        return defensa_especial
    
    def velocidad_pokemon1(self):
        #PUNTOS VELOCIDAD
        #  -viDE valor individual de velocidad.
        #  -ebDE estadistica base en velocidad.
        #  -n es nivel actual del pokemon
        n = 5
        ebV = 45
        viV = randint(1, ebV)
        puntos_velocidad = viV + (2 * ebV)
        puntos_velocidad = puntos_velocidad * (n/100)
        puntos_velocidad = puntos_velocidad + 5
        return puntos_velocidad


# POKEMON 2 --> Charmander
    def salud_pokemon2(self):
        n = 5 
        ebS = 45
        viS = randint(1, ebS)
        puntos_salud = viS + (2 * ebS)
        puntos_salud = puntos_salud * (n/100)
        puntos_salud = puntos_salud + 10 + n
        return puntos_salud
    
    def ataque_pokemon2(self):
        n = 5
        ebA = 49
        viA = randint(1, ebA)
        puntos_ataque = viA + (2 * ebA)
        puntos_ataque = puntos_ataque * (n/100)
        puntos_ataque = puntos_ataque + 5
        return puntos_ataque
    
    def defensa_pokemon2(self):
        n = 5
        ebD = 49
        viD = randint(1, ebD)
        puntos_defensa = viD + (2 * ebD)
        puntos_defensa = puntos_defensa * (n/100)
        puntos_defensa = puntos_defensa + 5
        return puntos_defensa
    
    def ataque_especial_pokemon2(self):
        n = 5
        ebAE = 65
        viAE = randint(1, ebAE)
        ataque_especial = viAE + (2 * ebAE)
        ataque_especial = ataque_especial * (n/100)
        ataque_especial = ataque_especial + 5
        return ataque_especial
    
    def defensa_especial_pokemon2(self):
        n = 5
        ebDE = 65
        viDE = randint(1, ebDE)
        defensa_especial = viDE + (2 * ebDE)
        defensa_especial = defensa_especial * (n/100)
        defensa_especial = defensa_especial + 5
        return defensa_especial
    
    def velocidad_pokemon2(self):
        n = 5
        ebV = 45
        viV = randint(1, ebV)
        puntos_velocidad = viV + (2 * ebV)
        puntos_velocidad = puntos_velocidad * (n/100)
        puntos_velocidad = puntos_velocidad + 5
        return puntos_velocidad


# POKEMON 3 --> Squirtle
    def salud_pokemon3(self):
        n = 5 
        ebS = 45
        viS = randint(1, ebS)
        puntos_salud = viS + (2 * ebS)
        puntos_salud = puntos_salud * (n/100)
        puntos_salud = puntos_salud + 10 + n
        return puntos_salud
    
    def ataque_pokemon3(self):
        n = 5
        ebA = 49
        viA = randint(1, ebA)
        puntos_ataque = viA + (2 * ebA)
        puntos_ataque = puntos_ataque * (n/100)
        puntos_ataque = puntos_ataque + 5
        return puntos_ataque
    
    def defensa_pokemon3(self):
        n = 5
        ebD = 49
        viD = randint(1, ebD)
        puntos_defensa = viD + (2 * ebD)
        puntos_defensa = puntos_defensa * (n/100)
        puntos_defensa = puntos_defensa + 5
        return puntos_defensa
    
    def ataque_especial_pokemon3(self):
        n = 5
        ebAE = 65
        viAE = randint(1, ebAE)
        ataque_especial = viAE + (2 * ebAE)
        ataque_especial = ataque_especial * (n/100)
        ataque_especial = ataque_especial + 5
        return ataque_especial
    
    def defensa_especial_pokemon3(self):
        n = 5
        ebDE = 65
        viDE = randint(1, ebDE)
        defensa_especial = viDE + (2 * ebDE)
        defensa_especial = defensa_especial * (n/100)
        defensa_especial = defensa_especial + 5
        return defensa_especial
    
    def velocidad_pokemon3(self):
        n = 5
        ebV = 45
        viV = randint(1, ebV)
        puntos_velocidad = viV + (2 * ebV)
        puntos_velocidad = puntos_velocidad * (n/100)
        puntos_velocidad = puntos_velocidad + 5
        return puntos_velocidad