from random import randint

class NameGenerator:
    """Class to generate random names for npcs."""

    def __init__(self):
        pass

    # attribute accessors

    # public methods

    def new_name(self, character_class): # DEBUG
        y = 0
        x = randint(0, 16)
        names = [
            "Bob",
            "Joe",
            "Jeff",
            "Bren",
            "Mike",
            "Dennis",
            "Tupok",
            "Biggie",
            "Huell",
            "Jerry",
            "Scott",
            "Clarence",
            "Dan",
            "Gary",
            "Kyle",
            "Theo",
            "Jim Bob"
        ]

        dwarf_names = [
            "Dain",
            "Gimli",
            "Kirk",
            "Scotty"
        ]

        generated_name = None

        if("goblin" in character_class):
            generated_name = names[x]
        elif("dwarf" in character_class):
            generated_name = dwarf_names[y]
        else:
            generated_name = names[x]

        return generated_name + " the " + character_class

    # private methods
