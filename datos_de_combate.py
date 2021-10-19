from random import randint
import requests

# TODO 
# - Ver como subir el nivel "n"

class Dato_combate:
    def __init__(self, aleatorio):
        self.aleatorio = aleatorio

    # vi --> valor individual de salud
    # eb --> Estadistica base de salud
    # n --> Nivel actual de pokemon.
    def puntos_de_salud(self):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.aleatorio}/").json()
        eb = pokemon['stats'][0]['base_stat']
        n = 5  # falta ver como aumentar y en que aspectos aumenta
        vi = randint(1, eb)

        resultado = vi + (2 * eb)
        resultado = resultado * (n/100)
        resultado = resultado + 10 + n
        return resultado
    

    # viA --> valor individual de ataque
    # ebA --> Estadistica base de ataque
    # n --> Nivel actual de pokemon.
    def ataque(self):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.aleatorio}/").json()
        ebA = pokemon['stats'][1]['base_stat']
        n = 5 # falta ver como aumentar y en que aspectos aumenta
        viA = randint(1, ebA)

        resultado = viA + (2 * ebA)
        resultado = resultado * (n/100)
        resultado = resultado + 5
        return resultado

    # viD --> valor individual de defensa
    # ebD --> Estadistica base de defensa
    # n --> Nivel actual de pokemon.
    def defensa(self):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.aleatorio}/").json()
        ebD = pokemon['stats'][2]['base_stat']
        n = 5 # falta ver como aumentar y en que aspectos aumenta
        vid = randint(1, ebD)

        resultado = vid + (2 * ebD)
        resultado = resultado * (n/100)
        resultado = resultado + 5
        return resultado

    # viAE --> valor individual de ataque especial
    # ebAE --> Estadistica base de ataque especial
    # n --> Nivel actual de pokemon.
    def ataque_especial(self):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.aleatorio}/").json()
        ebAE = pokemon['stats'][3]['base_stat']
        n = 5 # falta ver como aumentar y en que aspectos aumenta
        viAE = randint(1, ebAE)

        resultado = viAE + (2 * ebAE)
        resultado = resultado * (n/100)
        resultado = resultado + 5
        return resultado


    # viDE --> valor individual de defensa especial
    # ebDE --> Estadistica base de defensa especial
    # N --> Nivel actual de pokemon.
    def defensa_especial(self):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.aleatorio}/").json()
        ebDE = pokemon['stats'][4]['base_stat']
        n = 5 # falta ver como aumentar y en que aspectos aumenta
        viDE = randint(1, ebDE)

        resultado = viDE + (2 * ebDE)
        resultado = resultado * (n/100)
        resultado = resultado + 5
        return resultado


    # viv --> valor individual de velocidad
    # ebv --> Estadistica base de velocidad
    # n --> Nivel actual de pokemon.
    def velocidad(self):
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.aleatorio}/").json()
        ebV = pokemon['stats'][5]['base_stat']
        n = 5 # falta ver como aumentar y en que aspectos aumenta
        viV = randint(1, ebV)

        resultado = viV + (2 * ebV)
        resultado = resultado * (n/100)
        resultado = resultado + 5
        return resultado