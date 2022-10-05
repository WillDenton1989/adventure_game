from random import randint

class NameGenerator:
    """the basics of name genrator"""

    def __init__(self):
        pass

    # public methods

    def new_name(self, character_class):
        y = 0# randint(0, 3)
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
        elif(character_class == "dwarf"):
            generated_name = dwarf_names[y]
        else:
            generated_name = names[x]

        return generated_name + " the " + character_class
