import yaml
import event_manager

from managers.manager_base import ManagerBase
from managers.monster_manager import MonsterManager
from managers.npc_manager import NpcManager
from managers.player_manager import PlayerManager
from models.entities.exit import Exit
from models.entities.treasure import Treasure

class EntityManager(ManagerBase):
    """the basics of the entity manager"""

    def __init__(self):
        ManagerBase.__init__(self)

        self._entities = []

        self._load_entity_templates()
        self._create_sub_managers()

    # attribute accessors

    @property
    def player_manager(self):
        return self._player_manager

    @property
    def player(self):
        return self._player_manager.player

    # public methods

    def create_player(self):
        self._player_manager.create_player()

    # private methods

    def _register_listeners(self):
        event_manager.listen(event_manager.CREATE_ENTITY_EVENT, self._create_entity_event_handler)

    def _unregister_listeners(self):
        pass

    def _load_entity_templates(self):
        with open("data/npc_data.yaml") as f: # hardcoded filename no bueno
            self._entity_templates = yaml.safe_load(f)

    def _create_sub_managers(self):
        self._monster_manager = MonsterManager()
        self._npc_manager = NpcManager()
        self._player_manager = PlayerManager()

        self._add_entity(self._player_manager.player)

    def _create_entity(self, entity_data):
        template = self._entity_templates[entity_data["key"]]
        create_data = self._create_new_entity_data(template, entity_data)
        new_entity = None

        if(template["entity_type"] == "monster"):
            new_entity = self._monster_manager.create_monster(create_data)
        elif(template["entity_type"] == "exit"):
            new_entity = Exit(create_data)
        elif(template["entity_type"] == "treasure"):
            new_entity = Treasure(create_data)
        elif(template["entity_type"] == "npc"):
            new_entity = self._npc_manager.create_npc(create_data)
        else:
            pass

        if(new_entity != None): self._add_entity(new_entity)

    def _create_new_entity_data(self, template, original_data):
        new_data = template.copy()
        entity_copy = original_data.copy()

        new_data.update(entity_copy["location"])
        new_data.update({ "events": entity_copy["events"] })

        return new_data

    def _add_entity(self, entity):
        self._entities.append(entity)
        updated_entities = self._entities.copy()
        event_manager.trigger_event(event_manager.ENTITIES_UPDATED_EVENT, { "updated_entities": updated_entities })

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _create_entity_event_handler(self, event_name, data):
        self._create_entity(data["entity_data"])
