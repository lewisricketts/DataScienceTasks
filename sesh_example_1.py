# Function

global_poke = "MewTwo" #declared before defining the function and is in a global position - global scope

def poke_in_bag(poke1, poke2):
    print(f"Pokemon 1: {poke1}\nPokemon2: {poke2}")
    print(f"You have an additional pokemon called {global_poke}")


poke_in_bag("slowpoke", "gengar")