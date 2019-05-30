# Implement a class to hold room information. This should have name and
# description attributes.

from colorama import Fore
from item import Item


class Room():
    instances = {}

    def __init__(self, **args):
        self.replica = args['replica']
        self.name = args['name']
        self.description = args['description']
        self.items = args.get('items') or []
        Room.instances[self.replica] = self

    def display(self,):
        # display room name and description
        print(Fore.YELLOW + self.name + Fore.RESET)
        print(self.description)

        # display room items
        if len(self.items) > 0:
            print(Fore.MAGENTA, end='')
            for index, item in enumerate(self.items):
                if index == len(self.items) - 1:
                    print(item.room_desc)
                else:
                    print(item.room_desc,  end=' ')

        # display possible exits
        exits = self.get_exits()

        print(Fore.RESET, end='')

        if len(exits) == 1:
            print(f'You see a single exit leading {exits[0]}.')
        elif len(exits) > 1:
            print(
                f"You see exits leading {', '.join(exits[:-1])} and {exits[-1]}")
        else:
            print('You see no exit.')

    def get_exits(self):
        exits = []
        for key in vars(self):
            xdir = move_to_long.get(key)
            if xdir:
                exits.append(xdir)
        return exits

    def find_item(self, thing):
        return Item.contains(self.items, thing)

    def list_items(self):
        for item in self.items:
            print(item)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        for obj in self.items:
            if obj == item:
                self.items.remove(obj)
                break


# Declare all the rooms
Room(
    replica='outside',
    name='Outside Cave Entrance',
    description='''Ahead of you, the cave mount beckons.''',
    items=[
        Item(
            replica='knife',
            name='a silver knife',
            description='''It's covered in blood!''',
            room_desc='''A silver knife lies here.''',
            aliases=('blade', 'dagger')
        )
    ]
)

Room(
    replica='foyer',
    name='Foyer',
    description='''Dim light filters in from the exits. Dusty passages surround you.'''
)

Room(
    replica='overlook',
    name='Grand Overlook',
    description='''A steep cliff appears before you, falling into the darkness. Ahead in the distance, a light flickers invitingly, but there is no way across the chasm.'''
)

Room(
    replica='narrow',
    name='Narrow Passage',
    description='''The narrow passage bends here from corner to corner. The smell of gold permeates the air.'''
)

Room(
    replica='treasure',
    name='Treasure Chamber',
    description='''You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers.'''
)

# Link rooms together

rooms = Room.instances

rooms['outside'].n = rooms['foyer']

rooms['foyer'].s = rooms['outside']
rooms['foyer'].n = rooms['overlook']
rooms['foyer'].e = rooms['narrow']

rooms['overlook'].s = rooms['foyer']

rooms['narrow'].w = rooms['foyer']
rooms['narrow'].n = rooms['treasure']

rooms['treasure'].s = rooms['narrow']

# room directional mappings

valid_movements = ('n', 's', 'e', 'w')

move_to_long = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west'
}
