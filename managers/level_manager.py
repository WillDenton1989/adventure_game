from managers.input_manager import InputManager
from managers.manager_base import ManagerBase

from models.events.entity_event import EntityEvent
# from models.events.input_event import InputEvent
from models.events.level_event import LevelEvent
from models.level_parser import LevelParser

class LevelManager(ManagerBase):
    def __init__(self, event_dispatcher, game_manager):
        ManagerBase.__init__(self, event_dispatcher)
        self._game_manager = game_manager
        self._level_parser = LevelParser()
        self._level = None

    def start(self):
        pass

    def process(self):
        # while(self.game_state != "state_game_end"):
        if(self.game_state == "state_movement"):
            self._draw_level()
        else:
            pass

    # public methods

    def set_level(self, level_name, symbol_dict):
        self._level = self._level_parser.build_the_level(level_name, symbol_dict)
        self._add_entities()

    # private methods

    def _register_receivers(self):
        self.event_dispatcher.receive(LevelEvent.MOVEMENT_EVENT, self._movement_event_handler)
        self.event_dispatcher.receive(EntityEvent.ENTITIES_UPDATED_EVENT, self._entities_updated_event_handler)
        self.event_dispatcher.receive(LevelEvent.DRAW_LEVEL_EVENT, self._draw_level_event_handler)

    def _unregister_receivers(self):
        pass

    def _draw_level(self):
        map = self._level.drawable_map()
        print("------------------------------------------------------------------------")

        for row in map:
            for column in row:
                print(chr(column), end = "")
            print("\r")

    def _trigger_level_events(self, column, row):
        triggered_events = self._level.events_for(column, row)
        for event in triggered_events:
            event_manager.trigger_event(event["event_name"], event["data"])

    def _move(self, direction):
        player = self._game_manager.player
        new_column, new_row = self._determine_new_coordinates(direction, player.column, player.row)

        if(self._level.can_move_to(new_column, new_row) == True):
            data = { "location": { "column": new_column, "row": new_row } }
            self.event_dispatcher.dispatch(LevelEvent(LevelEvent.UPDATE_PLAYER_LOCATION_EVENT, data))
            self._trigger_level_events(new_column, new_row)
        else:
            print("That is not passable terrain my friend.")

    def _trigger_level_events(self, column, row):
        triggered_events = self._level.events_for(column, row)
        for event_data in triggered_events:
            event_name = event_data["event_name"]
            data = event_data["data"]

            event = self.event_dispatcher.event_from_string(event_name, data)
            self.event_dispatcher.dispatch(event)

    def _determine_new_coordinates(self, direction, column, row):
        if(direction == "right"):
            return column + 1, row
        elif(direction == "left"):
            return column - 1, row
        elif(direction == "up"):
            return column, row - 1
        elif(direction == "down"):
            return column, row + 1
        else:
            pass

    def _update_entities(self, updated_entities):
        self._level.update_entities(updated_entities)

    def _add_entities(self):
        entity_templates = self._level.entity_templates

        for entity_template in entity_templates["templates"]:
            if(entity_template["template_name"] == "player_start"):
                self._add_player(entity_template)
            else:
                self._add_entity(entity_template)

    def _add_player(self, template):
        data = { "location": template["location"] }
        self._event_dispatcher.dispatch(LevelEvent(LevelEvent.UPDATE_PLAYER_LOCATION_EVENT, data))

    def _add_entity(self, entity_data):
        data = { "entity_data": entity_data }
        self._event_dispatcher.dispatch(EntityEvent(EntityEvent.CREATE_ENTITY_EVENT, data))

    def _handle_game_state_change(self, previous_state, new_state, data):
        pass

    # event handlers

    def _movement_event_handler(self, event):
        self._move(event.direction)

    def _entities_updated_event_handler(self, event):
        self._update_entities(event.updated_entities)

    def _draw_level_event_handler(self, _event):
        self._draw_level()
