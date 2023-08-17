import yaml

class GameParser:
    def __inti__(self):
        pass

    # attribute accessors

    # public methods

    def load_player_template(self, player_template):
        with open(player_template) as f:
            player_template = yaml.safe_load(f)

        return player_template

    def load_entity_templates(self, entity_template):
        with open(entity_template) as f:
            self._entity_templates = yaml.safe_load(f)

    def load_item_templates(self, filename):
        item_templates = None
        with open(filename) as f:
            item_templates = yaml.safe_load(f)["item_data"]

        return item_templates

    def load_txt_file(self):
        # "data/dwarf_name.txt", "data/battle_display.txt"
        with open("data/dwarf_name.txt") as name: # DEBUG FILE
            list = []
            for line in name:
                print(line, end="")

    # private methods
