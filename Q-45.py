'''
A certain childrens game involves starting with a word in a particular
category. Each participant in turn says a word, but that word must begin with
the final letter of the previous word. Once a word has been given, it cannot
be repeated. If an opponent cannot give a word in the category, they fall out
of the game.
For example, with "animals" as the category,

Child 1: dog 
Child 2: goldfish
Child 1: hippopotamus
Child 2: snake
...
Your task in this exercise is as follows: Take the following selection of 70
English Pokemon names (extracted from Wikipedia's list of Pokemon) and
generate the/a sequence with the highest possible number of Pokemon names
where the subsequent name starts with the final letter of the preceding name.
No Pokemon name is to be repeated.
'''

import random

def pokemon():
    output_list = []

    pokemon_names = """audino bagon baltoy banette bidoof braviary bronzor carracosta
    charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite
    girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan
    kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine
    nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2
    porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking
    sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko
    tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"""

    pokemon_names_list = pokemon_names.rstrip().split()
    #print(pokemon_names_list)
    start = random.choice(pokemon_names_list)
    output_list.append(start)
    
    for element in pokemon_names_list:
        if element.startswith(start[-1]) and element not in output_list:
            output_list.append(element)
            start=element
    print(output_list)
pokemon()



