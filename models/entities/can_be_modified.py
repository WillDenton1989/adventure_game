class CanBeModified:
    def __init__(self, data):
        self._modifiers = {}

    def add_modifier(self, source_id, stat, modifier):
        if self._modifiers.get(stat) == None: self._modifiers[stat] = []

        self._modifiers[stat].append({ "source_id": source_id, "modifier": modifier })

    def remove_modifier(self, source_id):
        for modifier in self._modifiers:
            modifier_list = self._modifiers.get(modifier)

            if(source_id == modifier_list[0].get("source_id")):
                correct_modifier = modifier

        self._modifiers.pop(correct_modifier)

    @classmethod
    def modifiable_attribute(self, decorated):
        def wrapper(self):
            stat = decorated.__name__
            modifier = self.modifier_for(stat)

            return decorated(self) + modifier

        return wrapper

    def modifier_for(self, stat):
        sum = 0
        modifiers = self._modifiers.get(stat)
        if modifiers == None: return sum

        for modifier in modifiers:
            sum += modifier["modifier"]

        return sum
