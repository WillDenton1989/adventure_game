import yaml

from managers.manager_base import ManagerBase
from managers.monster_manager import MonsterManager
from managers.npc_manager import NpcManager
from managers.player_manager import PlayerManager

from models.entities.exit import Exit
from models.entities.treasure import Treasure
from models.events.entity_event import EntityEvent

class EntityManager(ManagerBase):
    """This manages all entities in the game and entity sub managers."""

    def __init__(self, event_dispatcher):
        ManagerBase.__init__(self, event_dispatcher)
        self._entities = []

        self._load_entity_templates()
        self._player_template = self._load_player_template()

        self._initialize_sub_managers()

    def start(self):
        self._register_manager_starts()

    def process(self):
        self._run_manager_processes()

    # attribute accessors

    @property
    def player_manager(self):
        return self._player_manager

    @property
    def player(self):
        return self._player_manager.player

    # public methods

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(EntityEvent.CREATE_ENTITY_EVENT, self._create_entity_event_handler)

    def _unregister_receivers(self):
        pass

    def _initialize_sub_managers(self):
        self._monster_manager = MonsterManager(self.event_dispatcher)
        self._npc_manager = NpcManager(self.event_dispatcher)
        self._player_manager = PlayerManager(self.event_dispatcher, self._player_template)

        self._add_entity(self._player_manager.player)

    def _register_manager_starts(self):
        self._monster_manager.start()
        self._npc_manager.start()
        self._player_manager.start()

    def _run_manager_processes(self):
        self._player_manager.process()
        self._monster_manager.process()
        self._npc_manager.process()

    def _load_player_template(self): # hardcoded filename no bueno, manager config refactor DEBUG
        with open("data/player_data.yaml") as f:
            player_template = yaml.safe_load(f)

        return player_template

    def _load_entity_templates(self):
        with open("data/npc_data.yaml") as f: # hardcoded filename no bueno, manager config refactor DEBUG
            self._entity_templates = yaml.safe_load(f)

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
        self.event_dispatcher.dispatch(EntityEvent(EntityEvent.ENTITIES_UPDATED_EVENT, { "updated_entities": updated_entities }))

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _create_entity_event_handler(self, event):
        self._create_entity(event.entity_data)
