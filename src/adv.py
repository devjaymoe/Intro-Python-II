from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all items
items = {
    'key': Item('Key', 'A small key, wonder what it unlocks...'),
    'sword': Item('Sword', 'A sharp sword, good for cutting.'),
    'chest': Item('Chest', 'A small chest, it seems to be locked.'),
    'glasses': Item('Glasses', 'A pair of glasses, might be useful'),
    'hat': Item('Hat', 'Fancy hat, so stylish'),
    'wine': Item('Wine Bottle', 'Wine, good for getting drunk!')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Placing items in rooms

room['outside'].place_items(items['hat'])
room['foyer'].place_items(items['sword'], items['glasses'])
room['overlook'].place_items(items['key'])
room['treasure'].place_items(items['chest'], items['wine'])

# print(room['outside'])
#
# Main
#

# print(items['hat'] == room['outside'].room_items[0])

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

def pickup_item(itemName, roomName):
    for index, value in enumerate(room[roomName].room_items):
        if value == items[itemName]:
            room[roomName].room_items.pop(index)
            player.inventory.append(items[itemName])
            print(f'{items[itemName].name} has been added to your inventory!')
        else:
            print('Item not found in room.')

pickup_item('hat', 'outside')

def drop_item(itemName):
    for index, value in enumerate(player.inventory):
        if value == items[itemName]:
            player.inventory.pop(index)
            player.room.room_items.append(items[itemName])
            print(f'You dropped the {items[itemName].name} at the {player.room.name}')
        else:
            print('Item not found in inventory.')    

drop_item('hat')

# player.check_room()
# player.pickup_item('hat')
# player.check_room()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# game_on = True

# while game_on:

#     print(player.room)

#     player_action = input('Which Direction should I go?')

#     player_action = player_action.lower()

#     player_action = player_action[0]

#     if player_action == 'n':
#         player.move('n')
#     elif player_action == 's':
#         player.move('s')
#     elif player_action == 'e':
#         player.move('e')
#     elif player_action == 'w':
#         player.move('w')
#     elif player_action == 'q':
#         game_on = False
#     else:
#         print('I dont understand...')