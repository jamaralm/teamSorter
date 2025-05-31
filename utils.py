from models import Player

'''
PLAYER FUNCTIONS
'''

def createPlayer():
    name = input("Nome do jogador: ")
    position = input("Posição (Goleiro/Linha): ").capitalize()

    attributes = {}
    for atr in ["skill", "speed", "strength", "vision", "defense", "attack", "teamplay"]:
        atrValue = int(input(f"{atr.capitalize()} (0 a 10): "))
        attributes[atr] = atrValue

    return Player(name, position, attributes)

'''
JSON FUNCTIONS
'''