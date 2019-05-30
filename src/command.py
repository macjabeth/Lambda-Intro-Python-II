import re


class Command():
    instances = {}

    def __init__(self, **args):
        method = args['method']
        for cmd in args['cmds']:
            self.cmd = cmd
            self.method = method
            Command.instances[cmd] = method

    @staticmethod
    def parse(verb):
        for cmd, method in Command.instances.items():
            # maybe use regex in case it's necessary at some point?
            # if re.match(cmd, verb):
            if cmd == verb:
                return method


def look(**args):
    args['persona'].current_room.display()


def examine(**args):
    target = args.get('next')
    if not target:
        print('You reach down and pat your rotund belly flab with a sigh, all the while examining your life choices.')
    else:
        persona = args['persona']
        item = persona.find_item(target) or persona.current_room.find_item(target)
        if item:
            print(item.description)
        else:
            print(f'There is no "{target}" for you to examine.')


def get(**args):
    target = args.get('next')
    if not target:
        print("You reach out and grab at thin air. Nice.")
    else:
        persona = args['persona']
        item = persona.current_room.find_item(target)
        if item:
            persona.current_room.remove_item(item)
            persona.add_item(item)
            print(f'You pick up {item.name}.')
        else:
            print(f'Are you blind? I see no "{target}" here.')


def drop(**args):
    target = args.get('next')
    if not target:
        print('You drop it real low and wiggle them cheeks.')
    else:
        persona = args['persona']
        item = persona.find_item(target)
        if item:
            persona.current_room.add_item(item)
            persona.remove_item(item)
            print(f'You drop {item.name}.')
        else:
            print(f'You hold no "{target}" on your persona.')


def inventory(**args):
    target = args.get('next')
    if not target:
        inventory = args['persona'].inventory
        if len(inventory) == 0:
            print('You have nothing in your inventory.')
        else:
            print('You are holding:')
            for item in inventory:
                print(item.name)


Command(cmds=('look', 'l'), method=look)
Command(cmds=('examine', 'ex'), method=examine)
Command(cmds=('get', 'take'), method=get)
Command(cmds=('drop',), method=drop)
Command(cmds=('inventory', 'inv'), method=inventory)
