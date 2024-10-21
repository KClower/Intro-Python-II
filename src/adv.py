from room import Room
from player import Player
from item import Item
import sys
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", [Item("Sword", "Double edged blade")]),
                   
                    

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


# Link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

def main():
    cardinalDirections = ["n", "s", "e", "w"]
    player = Player(room['outside'])
    while (True):
        print(player.room.name)
        print(player.room.desc)
        for item in player.room.items:
            print(f'There is a {item.name} on the ground that is a {item.desc}')
           
        command = input("Choose n, s, e, w, to move. Or q to quit: ")

        if command == "q":
            break

        if command not in cardinalDirections:
            print("Invalid Command.")
            continue

        roomExits = player.room.getPossibleExits()
        if command not in roomExits:
            print("Can't go that direction")
            continue
            
        if command == "n":
            player.room = player.room.n_to
          
        if command == "s":
            player.room = player.room.s_to

        if command == "e":
            player.room = player.room.e_to

        if command == "w":
            player.room = player.room.w_to

    
          
    sys.exit()


    
if __name__ == "__main__":
    main()

