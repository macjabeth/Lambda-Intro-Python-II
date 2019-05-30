import re
from colorama import init
from command import Command
from player import *
from room import rooms, valid_movements

# initialise coloured output
init()

# make a new player object that is currently in the 'outside' room.

print('-' * 80)

player_name = None
while not player_name:
    player_name = str(input('Greetings adventurer! What is your name? '))

print(f'Welcome, {player_name}! May the odds be ever in your favour...')
print('-' * 80)

player = Player(
    name=player_name,
    room=rooms['outside'],
    health=100, max_health=100
)

# display initial room
player.current_room.display()

#
# main loop
#


def main():
    while True:
        cmd = str(input(f'{player.health}/{player.max_health}h > '))

        if not cmd:
            continue

        m = re.match(r'^(\S+)(?: (.+))?$', cmd.lower())
        verb, args = m.group(1, 2)

        if verb in ('q', 'quit'):
            print('You kneel and pray for salvation...')
            # I'd like to put this on a timer...
            print('\nThe gods answer your prayer and your soul is lifted to the heavens.')
            break
        elif verb in valid_movements:
            player.move(verb)
        else:
            method = Command.parse(verb)

            if method:
                method(persona=player, next=args)
            else:
                print('Huh?')


if __name__ == "__main__":
    main()
