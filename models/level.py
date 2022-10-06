import copy

class Level:
    PASSABLE_SPACE = "EE"

    def __init__(self, raw_map, symbols):
        self._map = self._build_map(raw_map, symbols)
        self._symbols = symbols
        self._entities = []
        self._events = []

        self._check_map(self._map)

    # attribute accessors

    # public methods

    def update_entities(self, updated_entities):
        self._entities = updated_entities
        self._events = []

        for entity in self._entities:
            if(entity.events == None): continue

            for event_name in entity.events:
                self._add_event(event_name, entity)

    def drawable_map(self):
        drawable = []
        column_index, row_index = 0, 0

        for row in self._map:
            new_row = []
            for column in row:
                new_column = self._symbol_for(column_index, row_index, column)
                new_row.append(new_column)
                column_index += 1
            row_index += 1
            column_index = 0
            drawable.append(new_row)

        return drawable

    def events_for(self, column, row):
        triggered_events = []

        for event in self._events:
            if(event["location"]["column"] == column and event["location"]["row"] == row):
                triggered_events.append(event)

        return triggered_events

    def can_move_to(self, column, row):
        if(self._is_coordinate_on_map(self._map, column, row) == False): return False
        if(self._is_coordinate_passable(self._map, column, row) == False): return False

        return True

    # private methods

    def _build_map(self, raw_map, symbols):
        map = []

        for row in raw_map:
            new_row = []
            for column in row:
                new_column = copy.copy(column)
                new_row.append(new_column)
            map.append(new_row)

        return map

    def _check_map(self, map):
        if(self._is_it_square(map) == False):
            raise Exception("Map was not sqaure")

    def _is_it_square(self, map):
        if(len(map) != len(map[0])):
            return False
        else:
            return True

    def _add_event(self, event_name, entity):
        location = { "row": entity.row, "column": entity.column }
        self._events.append({ "event_name": event_name, "data": { "entity": entity }, "location": location })

    def _symbol_for(self, column_index, row_index, column):
        entity = self._entity_for(column_index, row_index)

        if(entity == None):
            return self._symbols.get(column)
        else:
            return self._symbols.get(entity.symbol)

    def _entity_for(self, column_index, row_index):
        entities_at_location = []
        for entity in self._entities:
            if(entity.column == column_index and entity.row == row_index):
                entities_at_location.append(entity)

        if(len(entities_at_location) == 0):
            return None
        else:
            entities_at_location.sort()
            return entities_at_location[0]

    def _is_coordinate_on_map(self, map, column, row):
        num_rows = len(map)
        num_columns = len(map[0])

        if(column < 0):
            return False
        if(column >= num_columns):
            return False
        if(row < 0):
            return False
        if(row >= num_rows):
            return False
        return True

    def _is_coordinate_passable(self, map, column, row):
        if(map[row][column] == self.PASSABLE_SPACE):
            return True
        else:
            return False
