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
from game_data import Location, Item, Player, World


# Note: You may add helper functions, classes, etc. here as needed
def print_location_description(the_location: Location) -> None:
    """
    TODO:
    """
    if the_location.num > 0:
        print(the_location.long_description)
    else:
        print(the_location.short_description)


def prompt_action(the_location: Location, the_map_list: list[list[int]], x: int, y: int, items_lst: list[Item]) -> str:
    """
    # TODO: CHANGE THE VAR NAMES
    """
    print("What do you want to do? \n")
    print("menu")
    for action in the_location.available_directions(the_map_list, x, y):
        print(action)
    for action in the_location.available_actions(items_lst):
        print(action)
    the_choice = input("\nEnter action: ")
    return the_choice


def prompt_menu(the_menu: list[str]) -> str:
    """
    # TODO:
    """
    print("Menu Options: \n")
    for option in the_menu:
        print(option)
    the_choice = input("\nChoose action: ")
    return the_choice


# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    # GIVEN CODE
    # w = World(open("map.txt"), open("locations.txt"), open("items.txt"))

    # testing loading methods
    with open('map.txt') as map_file, open('locations.txt') as location_file, open('items.txt') as item_file:
        w = World(map_file, location_file, item_file)
        # print(w.map)
        # for item in w.items:
        #     print(item.start, item.target, item.target_points, item.name)
        map_list = w.map
        locations_list = w.locations
        items_list = w.items

        location_object = w.get_location(0, 0)
        # print(location_object.location_num, location_object.num)
        # print(location_object.short_description)
        # print(location_object.long_description)

        location_object.items = location_object.available_items(items_list)
        for item in location_object.items:
            print(item.start, item.target, item.target_points, item.name)


    p = Player(0, 0, w)  # set starting location of player; you may change the x, y coordinates here as appropriate
    p.pick_up_item("Cheat Sheet", location_object, items_list)
    # p.go_south()
    # print(f"{p.x}{p.y}")
    # print(w.map[p.x][p.y])
    # p.go_east()
    # print(f"{p.x}{p.y}")
    # print(w.map[p.x][p.y])
    # p.go_north()
    # print(f"{p.x}{p.y}")
    # print(w.map[p.x][p.y])
    # p.go_west()
    # print(f"{p.x}{p.y}")
    # print(w.map[p.x][p.y])
    # location = w.get_location(p.x, p.y)
    # location.items = location.available_items(items_list)
    #
    # print("Items at the starting location:", location.items)
    # p.pick_up_item('Cheat Sheet', location, items_list)
    # print(items_list)
    # location1 = w.get_location(0, 0)
    # p.go_south()
    # print(location.location_num)
    # print("Player's inventory after picking up:", p.inventory)
    # p.drop_item('Cheat Sheet', location, items_list)
    # print(items_list)
    # print(location1.available_items(items_list))
    # print("Player's inventory after dropping:", p.inventory)
    # print("Items at this location:", location.items)

    exit()  # REMOVE THIS LINE for the program to continue executing

    menu = ["look", "inventory", "score", "quit", "resume"]

    while not p.victory:
        location = w.get_location(p.x, p.y)
        location.actions = location.available_directions(map_list, p.x, p.y) + location.available_actions(items_list)
        location.items = location.available_items(items_list)

        print(location.actions)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        print_location_description(location)
        locations_list[location.location_num].num = 0
        #
        # print("Items at the starting location:", location.items)
        # p.pick_up_item('Cheat Sheet', location, items_list)
        # print(items_list)
        # location1 = w.get_location(0, 0)
        # p.go_south()
        # location = w.get_location(p.x, p.y)
        # print(location.location_num)
        # print("Player's inventory after picking up:", p.inventory)
        # p.drop_item('Cheat Sheet', location, items_list)
        # print(items_list)
        # print(location1.available_items(items_list))
        # print("Player's inventory after dropping:", p.inventory)
        # print("Items at this location:", location.items)

        choice = prompt_action(location, map_list, p.x, p.y, items_list)
        while choice.lower() not in location.actions and choice != 'menu':
            print("You can't do that. Check your spelling... or maybe your logic?")
            choice = prompt_action(location, map_list, p.x, p.y, items_list)

        if choice.lower() == 'go south':
            p.go_south()
        elif choice.lower() == 'go north':
            p.go_north()
        elif choice.lower() == 'go east':
            p.go_east()
        elif choice.lower() == 'go west':
            p.go_west()
        if choice.lower() == 'pick up item':
            item_name = input("Enter the name of the item to pick up: ")
            p.pick_up_item(item_name, location, items_list)
        if choice.lower() == 'drop item':
            item_name = input("Enter the name of the item to drop: ")
            location = w.get_location(p.x, p.y)
            p.drop_item(item_name, location, items_list)

        if choice.lower() == "menu":
            choice = prompt_menu(menu)
            while choice.lower() not in menu:
                print("You can't do that. Check your spelling... or maybe your logic?")
                choice = prompt_menu(menu)
            if choice.lower() == 'look':
                print(location.long_description)
            if choice.lower() == 'quit':
                exit()
            if choice.lower() == 'inventory':
                p.view_inventory()

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
