
class CatchphraseGenerator:
    """makes soup"""

    def __init__(self):
        pass

    def new_phrase(self, name):
        intro = "\nAs your foe engages you in glorious combat they cry out...\n"

        return intro + self._phrase_for_name(name)

    def _phrase_for_name(self, name):
        if("Mike" in name):
            return "Why am I even in here, man? Making this was a waste of your time..."
        elif("Scott" in name):
            return "Is that 'THE' father linux?"
        elif("Gary" in name):
            return "It's Gary UwU XD"
        elif("Theo" in name):
            return "It me, Thed the smooth brain"
        elif("Dan" in name):
            return "Reeeeeeeee"
        elif("Biggie" in name):
            return "It was all a dream..."
        elif("Bren" in name):
            return "Gimme your pre workout! I neeeeeeed it!"
        elif("Jim Bob" in name):
            return "Its Jesus' lesser known brother, Jim Bob the son of god!"
        else:
            return "We battle to the death!!"
