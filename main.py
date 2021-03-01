import math
import pandas as pd

fish_names = ['Angler', 'Crimsonfish', 'Glacierfish', 'Glacierfish Jr.', 'Legend', 'Legend II', 'Ms. Angler', 'Mutant Carp', 'Radioactive Carp', 'Son of Crimsonfish', 'Albacore', 'Anchovy', 'Clam', 'Cockle', 'Eel', 'Flounder', 'Halibut', 'Herring', 'Mussel', 'Octopus', 'Oyster', 'Pufferfish', 'Red Mullet', 'Red Snapper', 'Sardine', 'Sea Cucumber', 'Squid', 'Super Cucumber', 'Tilapia', 'Tuna', 'Bream', 'Catfish', 'Chub', 'Dorado', 'Lingcod', 'Perch', 'Pike', 'Rainbow Trout', 'Salmon', 'Shad', 'Smallmouth Bass', 'Sunfish', 'Tiger Trout', 'Walleye', 'Bullhead', 'Carp', 'Largemouth Bass', 'Midnight Carp', 'Sturgeon', 'Woodskip', 'Mines', 'Ghostfish', 'Ice Pip', 'Lava Eel', 'Stonefish', 'Sandfish', 'Scorpion Carp', 'Slimejack', 'Void Salmon', 'Blobfish', 'Midnight Squid', 'Spook Fish', 'Crab', 'Crayfish', 'Lobster', 'Periwinkle', 'Shrimp', 'Snail', 'Blue Discus', 'Lionfish', 'Stingray']

data = pd.read_excel('Stardew Valley - FishGuide (1.5.3).xlsx')[['Name', 'normal', 'silver', 'gold', 'iridium']]

inventory = []

FISHER_LEVEL = 0

# Insert fishing level
def fisher_level():
    global FISHER_LEVEL
    fisher = int(input("Which bonus of fisherman? 0, 1 or 2: "))
    try:
        if fisher < 0 or fisher > 2:
            print("This is not a valid input.")
            fisher_level()
    except ValueError:
        print("Numbers only.")
        fisher_level()
    else:
        FISHER_LEVEL = int(fisher)
        fish_name()

# Insert fish name
def fish_name():
    """Define o peixe a ser usado no cálculo."""
    name = input("Which fish do you have? ").title()
    if name not in fish_names:
        print("This is not a valid fish. Type 'final' to get your total and quit.\n")
        fish_name()
    else:
        fish_rarity(name)

# Insert fish quality and quantity, add them to inventory
def fish_rarity(name):
    """Define a raridade do peixe e a quantidade a serem usadas no cálculo."""
    rarity_dict = {1: 'normal', 2: 'silver', 3: 'gold', 4: 'iridium'}
    rarity_input = int(input(f"Which rarity of '{name}' to add?\n 1 for 'normal', 2 for 'silver', 3 for 'gold', 4 for 'iridium': "))

    if rarity_input in rarity_dict:
        data_name = data[data['Name'] == name]
        rarity_word = rarity_dict[rarity_input]
        price = int(data_name[rarity_word])
        print(f"The {name}'s {rarity_word} value is {price}g.\n")

        qtde = int(input(f"How many of '{name}' will you sell? "))

        if fisher_level == 1:
            price += price * 0.25
        elif fisher_level == 2:
            price += price * 0.5

        price = math.floor(price) * qtde
        inventory.append(price)
        end(name)

    else:
        print("This is not a valid input.")
        fish_rarity(name)

# Ending options
def end(name):
    """Entrega opções de finalização: nova raridade, novo peixe, saber o total, ou sair."""
    print("------------------------------")
    call = input(f"Would you like to add another rarity of '{name}' ('y'),\n add another fish ('other') "
                 f"or know your total ('total')? ")
    if call == "y":
      fish_rarity(name)

    elif call == "other":
      fish_name()

    elif call == "total":
        print("------------------------------")
        total = sum(inventory)
        print(f"You'll get ${total} by selling those fish.")
        now_what = input("Type 'end' to exit, 'new' to start over, or anything else to keep adding: ")
        if now_what == "end":
            print("------------------------------")
            print("\nGoodbye!")

        elif now_what == "new":
            fisher_level()

        else:
           fish_name()

fisher_level()