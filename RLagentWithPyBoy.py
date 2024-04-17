#'C:/Users/henri/PyBoy/PokemonRed.gb'
#pyboy.plugins.game_wrapper_pokemon_gen1

from pyboy import PyBoy
from pyboy.plugins.game_wrapper_pokemon_gen1 import GameWrapperPokemonGen1


gamerom = 'C:/Users/henri/PyBoy/PokemonRed.gb'
savefile = 'C:/Users/henri/PyBoy/PokemonRed.gb.state'
gameboy = PyBoy(gamerom)
gameboy.tick()

wrapper = GameWrapperPokemonGen1(gameboy, gameboy.mb, {})


def innitiate_game ():
    for _ in range(4):
        gameboy.button('a')
        gameboy.tick()
    return

while gameboy.tick():
    innitiate_game()
    gameboy.button('down')
    gameboy.tick()
    #print(wrapper)
    gameboy.button('up')
    gameboy.tick()
    
    pass
gameboy.stop()
