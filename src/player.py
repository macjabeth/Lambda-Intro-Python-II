# Write a class to hold player information, e.g. what room they are in
# currently.

from room import move_to_long
from item import Item

class CharacterStats():
    def __init__(self, args):
        self.health = args['health']
        self.max_health = args['max_health']

class Player(CharacterStats):
    def __init__(self, **args):
        super().__init__(args)
        self.name = args['name']
        self.current_room = args['room']
        self.inventory = args.get('inventory') or []

    def move(self, direction):
        room = vars(self.current_room)
        if direction in room:
            self.current_room = room[direction]
            print(f'You move {move_to_long[direction]}')
            self.current_room.display()
        else:
            print('You cannot go that way!')

    def find_item(self, thing):
        # last word is most likely the item we need
        # this way we handle cases like `get silver knife`
        return Item.contains(self.inventory, thing)

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        for obj in self.inventory:
            if obj == item:
                self.inventory.remove(obj)
                break
