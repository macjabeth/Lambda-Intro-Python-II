# Implement a class to hold room information. This should have name and
# description attributes.

from colorama import Fore
from replica import *


class Room():
    instances = {}

    def __init__(self, **args):
        self.replica = args['replica']
        self.name = args['name']
        self.description = args['description']
        self.items = args.get('items') or []
        self.exits = args.get('exits') or {}
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
            print(f'You see exits leading {", ".join(exits[:-1])} and {exits[-1]}.')
        else:
            print('You see no exit.')

    def get_exits(self):
        return [move_to_long[x] for x in self.exits.keys()]

    def find_item(self, thing):
        return Object.contains(self.items, thing)

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
    exits={ 'n': 'foyer' },
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
    description='''Dim light filters in from the exits. Dusty passages surround you.''',
    exits = { 's': 'outside', 'n': 'overlook', 'e': 'narrow' }
)

Room(
    replica='overlook',
    name='Grand Overlook',
    description='''A steep cliff appears before you, falling into the darkness. Ahead in the distance, a light flickers invitingly, but there is no way across the chasm.''',
    exits = { 's': 'foyer' }
)

Room(
    replica='narrow',
    name='Narrow Passage',
    description='''The narrow passage bends here from corner to corner. The smell of gold permeates the air.''',
    exits = { 'w': 'foyer', 'n': 'treasure' }
)

Room(
    replica='treasure',
    name='Treasure Chamber',
    description='''You've found the long-lost treasure chamber!''',
    exits={ 's': 'narrow' },
    items=[
        Item(
            replica='chest',
            name='a gold-encrusted chest',
            description='''It is locked shut.''',
            room_desc='''A large gold-encrusted chest rests in the center of the room.''',
            weight='huge',
            aliases=('trunk',)
        ),
        CCC(
            replica='fukumoto',
            name='Brady Fukumoto',
            description='''The renowned Computer Science teacher stands before you.''',
            room_desc='''Brady Fukumoto stands nearby looking rather perturbed.''',
            aliases=('brady',)
        )
    ]
)

# room directional mappings

valid_movements = ('n', 'north', 's', 'south', 'e', 'east', 'w', 'west')

move_to_long = {
    'n': 'north',
    's': 'south',
    'e': 'east',
    'w': 'west'
}

move_to_short = {
    'north': 'n',
    'south': 's',
    'east': 'e',
    'west': 'w',
}
