"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import World, Item, Location, Player

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    # GIVEN CODE
    # w = World(open("map.txt"), open("locations.txt"), open("items.txt"))

    # testing loading methods
    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        w = World(map_file, location_file, item_file)
        # print(w.map)
        # print(w.locations)
        # print(w.items)
        map_list = w.map
        locations_list = w.locations
        items_list = w.items

        location_object = w.get_location(1, 0)
        print(location_object.short_description)

        location_object.actions = location_object.available_actions(map_list)
        print(location_object.actions)

        location_object._items = location_object.available_items(items_list)
        print(location_object._items)

    p = Player(0, 0, w)  # set starting location of player; you may change the x, y coordinates here as appropriate
    p.go_south()
    print(f"{p.x}{p.y}")
    print(w.map[p.x][p.y])
    p.go_east()
    print(f"{p.x}{p.y}")
    print(w.map[p.x][p.y])
    p.go_north()
    print(f"{p.x}{p.y}")
    print(w.map[p.x][p.y])
    p.go_west()
    print(f"{p.x}{p.y}")
    print(w.map[p.x][p.y])

    exit()  # REMOVE THIS LINE for the program to continue executing

    menu = ["look", "inventory", "score", "quit", "back"]

    while not p.victory:
        location = w.get_location(p.x, p.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)

        print("What to do? \n")
        print("[menu]")
        for action in location.available_actions():
            print(action)
        choice = input("\nEnter action: ")

        if choice == "[menu]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
