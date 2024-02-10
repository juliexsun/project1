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
from game_data import Location, Item, Player, World, Book


# Note: You may add helper functions, classes, etc. here as needed
def print_location_description(the_location: Location) -> None:
    """
    TODO:
    """
    print(f"LOCATION {the_location.location_num}\n")
    if the_location.available_score > 0:
        print(the_location.long_description)
    else:
        print(the_location.short_description)


def prompt_direction(the_location: Location, the_map_list: list[list[int]], x: int, y: int) -> None:
    """ Prompts the player to choose an action and prints out available directions to move in
    current location.
    """
    if any(isinstance(the_item, Book) for the_item in location.items):
        print("!!!Please enter read actions exactly as formatted.")
    print("What do you want to do? \n")
    print("menu")
    for direction in the_location.available_directions(the_map_list, x, y):
        print(direction)


def prompt_action(the_location: Location, items_lst: list[Item], inventory: list[Item]) -> str:
    """ Prompts the player to choose an action and prints out available actions other than direction
    in current location.
    """
    for action in the_location.available_actions(items_lst, inventory):
        print(action)
    the_choice = input("\nEnter action: ")
    return the_choice


def prompt_menu(the_menu: list[str]) -> str:
    """ Prompts the player to choose a menu action and prints out available menu actions.
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

        # location_object = w.get_location(0, 0)
        # print(location_object.location_num, location_object.num)
        # print(location_object.short_description)
        # print(location_object.long_description)

        # location_object.items = location_object.available_items(items_list)
        # for item in location_object.items:
        #     print(item.start, item.target, item.target_points, item.name)

        # map_object = Map(2, 10, 1, 'Bob')
        # print(map_object.start, map_object.target, map_object.target_points, map_object.name)
        # map_object.print_map(map_list)

    p = Player(0, 0, w)  # set starting location of player; you may change the x, y coordinates here as appropriate
    # p.use_item('map', Map(1, 1, 1, 'map'), map_list)
    menu = ["look", "inventory", "score", "quit", "resume"]
    max_moves = 10
    current_moves = 0
    score = 0

    while not p.victory:
        location = w.get_location(p.x, p.y)
        location_available_actions = location.available_actions(items_list, p.inventory)
        location_available_directions = location.available_directions(map_list, p.x, p.y)
        location.actions = location_available_actions + location_available_directions
        location.items = location.available_items(items_list)
        score += locations_list[location.location_num].available_score

        if current_moves == max_moves - 1:
            print("!Warning: You have only one move left!")
        if current_moves > max_moves:
            print("The maximum number of moves is reached. You missed your exam! Try again :)")
            exit()

        print("moves: ", current_moves, "/", max_moves)

        # TESTING AVAILABLE ITEMS
        # location.items = location.available_items(items_list)
        # print("AVAILABLE ITEMS")
        # for item in location.items:
        #     print(item.start, item.target, item.target_points, item.name)
        # print()

        # print("ALL ITEMS")
        # for item in items_list:
        #     print(item.start, item.target, item.target_points, item.name)
        # print()

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)
        print_location_description(location)
        locations_list[location.location_num].available_score = 0
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
        prompt_direction(location, map_list, p.x, p.y)
        choice = prompt_action(location, items_list, p.inventory)
        while choice.lower() not in location.actions and choice not in location.actions and choice != 'menu':
            print("You can't do that. Check your spelling... or maybe your logic?")
            prompt_direction(location, map_list, p.x, p.y)
            choice = prompt_action(location, items_list, p.inventory)

        if choice.lower() == 'go south':
            p.go_south()
            current_moves += 1
        elif choice.lower() == 'go north':
            p.go_north()
            current_moves += 1
        elif choice.lower() == 'go east':
            p.go_east()
            current_moves += 1
        elif choice.lower() == 'go west':
            p.go_west()
            current_moves += 1
        if choice.lower() == 'pick up item':
            print("Available items to pick up: ")
            for item in location.items:
                print(item.name)
            print()
            item_name = input("Enter the name of the item to pick up: ")
            if p.pick_up_item(item_name, location, items_list):
                for item in p.inventory:
                    score += item.target_points
                    item.target_points = 0
                current_moves += 1
        if choice.lower() == 'drop item':
            print("Available items to drop: ")
            for item in p.inventory:
                print(item.name)
            print()
            item_name = input("Enter the name of the item to drop: ")
            location = w.get_location(p.x, p.y)
            if p.drop_item(item_name, location, items_list):
                current_moves += 1
        if choice.lower() == 'use map':
            for item in p.inventory:
                if item.name == 'Map':
                    p.use_item('Map', item, map_list)
        if 'read "How to' in choice:
            for item in items_list:
                if item.name == choice[5:]:
                    item.read_book(choice)
                    score += item.target_points
                    item.target_points = 0
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
            if choice.lower() == 'score':
                print("score:", score)

        location = w.get_location(p.x, p.y)
        p.player_victory(location, score)

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
