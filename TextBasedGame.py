# Brianna Lee
# call to function
def main():
    rooms = {
        'Dining Room': {'North': 'Kitchen', 'East': 'Bedroom', 'South': 'Office', 'West': 'Garage'},
        'Kitchen': {'South': 'Dining Room', 'item': 'Flashlight'},
        'Bedroom': {'South': 'Living Room', 'West': 'Dining Room', 'item': 'Rope'},
        'Living Room': {'North': 'Bedroom', 'South': 'Foyer', 'West': 'Office', 'item': 'Screwdriver'},
        'Foyer': {'North': 'Living Room', 'item': 'Basement Key'},
        'Garage': {'East': 'Dining Room', 'item': 'Wire-cutters'},
        'Office': {'North': 'Dining Room', 'East': 'Living Room', 'South': 'Basement',
                   'item': 'AI Robot Instruction Manual'},
        'Basement': {'North': 'Office', 'item': 'Annie the AI Robot!'}  # villain room
    }

    def show_instructions():  # game backstory and instructions
        print('AI Robot Meltdown')
        print('Your helpful, in-home A.I. Robot, Annie, has short-circuited and triggered her self-destruct feature. '
              '\nIt’s up to you to save your home by properly shutting down the A.I. Robot Annie before her detonation '
              '\ntimer runs out. Last you checked, she was located in the basement, but you need to gather a few items '
              '\nbefore you can shut her down. You are going to need the A.I. Robot Instruction Manual from the office '
              '\nto know how to shut her down properly, the rope from the bedroom to tie her up to keep her still, '
              '\nthe screwdriver from the living room to expose her wiring, the wire-cutters from the garage to cut '
              'the '
              '\ncorrect wires, the flashlight from the kitchen to see what you are doing, and the basement key. The '
              '\nbasement automatically locks behind you, so if you run into the basement before gathering all the '
              '\nitems first, you will be locked in there until Annie detonates. It is important to gather ALL items '
              '\nfirst to save your house and yourself! Good Luck!')
        print(
            'Collect all 6 items before facing Annie the AI Robot, or get locked in the basement while Annie '
            'self-destructs')
        print('Move commands to move directions through the house: South, North, East, West')
        print('Command to add item to Inventory: Get item')

    show_instructions()
    currentRoom = 'Dining Room'  # starting location for player
    inventory = []  # what items the player already has

    print('You are in the', currentRoom)
    print('Inventory:', inventory)

    while True:
        move = input("What is your move?")
        if (move == 'North') or (move == 'South') or (move == 'East') or (move == 'West'):
            if move in rooms[currentRoom]:
                print("You are in the " + rooms[currentRoom][move])
                currentRoom = rooms[currentRoom][move]  # changes to show what room player is in
                print('Inventory:', inventory)
            else:
                print("\nSorry, no path in that direction!")
            if 'item' in rooms[currentRoom]:
                item = rooms[currentRoom]['item']
                if item not in inventory:  # to prevent multiples of the same item being added
                    print("You see a " + rooms[currentRoom]['item'])
                if item == 'Annie the AI Robot!':  # villain
                    if len(inventory) == 6:  # required number of items to win
                        print(
                            'Congratulations! You have collected all items and successfully shut off Annie before she '
                            'self-destructed! '
                            '\nThanks for playing the game! Hope you enjoyed it')
                        break
                    else:
                        print("GAME OVER. You were missing an important item to successfully shut down Annie's"
                              "\nself-destruct feature! Unfortunately, you got locked in the basement and Annie"
                              "\nself-destructed, destroying your home and everything in it. Better luck next time. "
                              "Hope you enjoyed the game!")
                        break
        elif (move == 'Get item') and ('item' != 'Annie the AI Robot!'):
            item = rooms[currentRoom]['item']
            if item not in inventory:
                inventory.append(rooms[currentRoom]['item'])
                print('Inventory:', inventory)
            else:
                print('There are no items here!')
        else:
            print("\nPlease enter a valid move")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
