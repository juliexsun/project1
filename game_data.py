"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - long_description
        - short_description
        - location_num: the numerical representation of the location
        - num: RANDOM NUMBER CHANGE LATER
        - items:
        - BALABALA DO THIS

    Representation Invariants:
        - location_num == -1 or location_num > 0
        - long_description != ''
        - short_description != ''
    """
    location_num: int
    num: int
    short_description: str
    long_description: str
    _items: list[str]
    actions: list[str]
    x: int
    y: int

    # does not initialize _items when using get_locations() from World class
    # must initialize separately
    def __init__(self, location_num: int, num: int, short_description: str, long_description: str,
                 x: int, y: int, items_list: list[list[str]] = None, map_list: list[list[int]] = None) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """
        self.location_num = location_num
        self.num = num
        self.long_description = long_description
        self.short_description = short_description
        self.x = x
        self.y = y
        if items_list is not None:
            self._items = self.available_items(items_list)
        if map_list is not None:
            self.actions = self.available_actions(map_list)

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        # TODO: Complete this method

    def available_items(self, items_list: list[list[str]]) -> list[str]:
        """
        WRITE DOCSTRING
        """
        items = []
        for item in items_list:
            if int(item[0]) == self.location_num:
                items.append(item[3])
        return items

    def available_actions(self, map_list: list[list[int]]) -> list[str]:
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        # TODO: Complete this method, if you'd like or remove/replace it if you're not using it
        # implemented for movement
        actions = []
        try:
            if map_list[self.x + 1][self.y] != -1:
                actions.append('South')
        except IndexError:
            pass
        try:
            if map_list[self.x - 1][self.y] != -1:
                actions.append('North')
        except IndexError:
            pass
        try:
            if map_list[self.x][self.y + 1] != -1:
                actions.append('North')
        except IndexError:
            pass
        try:
            if map_list[self.x][self.y - 1] != -1:
                actions.append('North')
        except IndexError:
            pass
        return actions


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: the name of the item
        - start: the start lacation
        - target: the target location
        - target_points: the points player can get

    Representation Invariants:
        - name!= ''

    """
    name: str
    start: int
    target: int
    target_points: int

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: The x-coordinate of the player's current position in the game world.
        - y: The y-coordinate of the player's current position in the game world.
        - inventory: A list that stores items that the player has collected during the game.
        - victory: Set to be False, and Ture if the player wins.

    Representation Invariants:
        - x >= 0
        - y >= 0
    """

    def __init__(self, x: int, y: int, world) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.world = world

    # MOVEMENT FUNCTIONS here:
    def move(self, dx, dy):
        """
        The player's movement
        """
        new_x = self.x + dx
        new_y = self.y + dy
        if self.world.valid_location(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            print("That way is blocked")

    def go_north(self):
        """
        The player chooses to go north by one step
        """
        self.move(-1, 0)

    def go_south(self):
        """
        The player chooses to go south by one step
        """
        self.move(1, 0)

    def go_west(self):
        """
        The player chooses to go west by one step
        """
        self.move(0, -1)

    def go_east(self):
        """
        The player chooses to go east by one step
        """
        self.move(0, 1)

    # INVENTORY FUNCTIONS here:
    def pick_up_item(self, item_name):
        """
        Add an item to the player's inventory.
        """
        current_location = self.world.get_location(self.x, self.y)
        item_to_pick_up = None

        for item in current_location.items:
            if item.name == item_name:
                item_to_pick_up = item
                break

        if item_to_pick_up:
            self.inventory.append(item_to_pick_up)
            current_location.items.remove(item_to_pick_up)
            print(f"Picked up {item_name}.")
        else:
            print("Item not found in this location.")

    def drop_item(self, item_name):
        """
        Drop the specified item from the player's inventory
        (plus: adding it back to the current location).
        """
        item_to_drop = None
        for item in self.inventory:
            if item.name == item_name:
                item_to_drop = item
                break

        if item_to_drop:
            # Remove the item from the inventory
            self.inventory.remove(item_to_drop)

            # Add the item back to the current location
            current_location = self.world.get_location(self.x, self.y)
            current_location.items.append(item_to_drop)

            print(f"Dropped {item_name}.")
        else:
            print(f"You do not have {item_name} in your inventory.")

    def use_item(self, item_name):
        """
        Use the item in the inventory
        """
        if item_name in self.inventory:
            # Implement the logic for using the item
            print(f"Used {item_name}.")
        else:
            print("You don't have this item in your inventory.")

    def view_inventory(self):
        """
        Display a list of current items in the inventory.
        """
        if self.inventory:
            print("Inventory:", ", ".join(self.inventory))
        else:
            print("Your inventory is empty.")


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - # TODO add more instance attributes as needed; do NOT remove the map attribute
        - locations: a nested list representation of the locations in the world
        - items: a nested list representation of the items in the world

    Representation Invariants:
        - # TODO
    """

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.locations = self.load_locations(location_data)
        self.items = self.load_items(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        # TODO: Complete this method as specified. Do not modify any of this function's specifications.
        the_map = []
        file = map_data.readlines()
        for line in file:
            row = [int(num) for num in line.split()]
            the_map.append(row)
        return the_map

    # TODO: Add methods for loading location data and item data (see note above).
    def load_locations(self, location_data) -> list[list[str]]:
        """
        WRITE THE DOCSTRING BUT LIKE IT PUTS THE LOCATIONS INTO A NESTED LIST
        AND WE CAN ACCESS SPECIFIC ATRRIBUTES WITH SPECIFIC INDEXES RAHHHHHH
        """
        locations = []
        while True:
            location_num = location_data.readline().strip()
            if location_num == '':
                break
            number1 = location_data.readline().strip  # must change to int to use

            short_description = location_data.readline().strip()

            long_description = ''
            while True:
                line = location_data.readline()
                if line == 'END\n':
                    break
                long_description += line

            locations.append([location_num, number1, short_description, long_description])
            # to skip the ''
            location_data.readline()
        return locations

    def load_items(self, items_data) -> list[list[str]]:
        """
        WRITE DOCSTRING. CHANGES ITEMS.TXT INTO NESTED LIST
        """
        items = []
        file = items_data.readlines()
        for line in file:
            elements = line.split()
            first_three_elements = [element for element in elements[:3]]
            row = first_three_elements + [' '.join(elements[3:])]
            items.append(row)
        return items

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """

        # TODO: Complete this method as specified. Do not modify any of this function's specifications.
        try:
            location_num = self.map[x][y]
            if location_num == -1:
                return None
            for location in self.locations:
                if int(location[0]) == location_num:
                    return Location(int(location[0]), int(location[1]), location[2], location[3], x, y)
        except IndexError:
            return None

    def valid_location(self, x: int, y: int) -> bool:
        """Return True if the location at (x, y) is valid and within the map boundaries.
        """
        if 0 <= x < len(self.map) and 0 <= y < len(self.map[0]):
            return self.map[x][y] != -1
        else:
            return False
