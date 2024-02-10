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


class Item:
    """A general item in our text adventure game world.

    Instance Attributes:
        - start: the starting location number of the item (is updated when moved)
        - target: the target location number of the item (-2 if none)
        - target_points: the points given for picking up this item
        - name: the name of the item

    Representation Invariants:
        - 1 <= start <= 20
        - -2 <= target <= 20
        - name != ''
    """
    start: int
    target: int
    target_points: int
    name: str

    def __init__(self, start: int, target: int, target_points: int, name: str) -> None:
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

        self.start = start
        self.target = target
        self.target_points = target_points
        self.name = name

    def read_book(self, book_name: str) -> None:
        """ Method to be overriden by child class Book
        """


class Map(Item):
    """A Map item in our text adventure game world.

    Instance Attributes:
        - start: the starting location number of the item (is updated when moved)
        - target: the target location number of the item (-2 if none)
        - target_points: the points given for picking up this item
        - name: the name of the item

    Representation Invariants:
        - 1 <= start <= 20
        - -2 <= target <= 20
        - name != ''
    """
    start: int
    target: int
    target_points: int
    name: str

    def __init__(self, start: int, target: int, target_points: int, name: str) -> None:
        """Initialize a new Map item.
        Source: https://www.w3schools.com/python/python_inheritance.asp
        """
        super().__init__(start, target, target_points, name)

    def print_map(self, map_list: list[list[int]]) -> None:
        """
        Prints out the 2D representation of the map with □ representing a blocked space.
        """
        print("□ represents a blocked space.\n")
        for row in map_list:
            for item in row:
                if item == -1:
                    print('□', end=" ")
                else:
                    print(item, end=" ")
            print()


class Book(Item):
    """A Book item in our text adventure game world.

    Instance Attributes:
        - start: the starting location number of the item (is updated when moved)
        - target: the target location number of the item (-2 if none)
        - target_points: the points given for picking up this item
        - name: the name of the item

    Representation Invariants:
        - 1 <= start <= 20
        - -2 <= target <= 20
        - name != ''
    """""
    start: int
    target: int
    target_points: int
    name: str

    def __init__(self, start: int, target: int, target_points: int, name: str) -> None:
        """Initialize a new item.
        Source: https://www.w3schools.com/python/python_inheritance.asp
        """
        super().__init__(start, target, target_points, name)

    def read_book(self, book_name: str) -> None:
        """ Print corresponding results for reading any book.
        """
        if book_name == '"How to Manage Your Time"':
            print("Woah! A ragged piece of paper falls out from the book. It says,")
            print("Head over to a certain mysterious room. Location number [REDACTED]. Bring the book for a")
            print("surprise. UGH! What location number! Where! There may be another clue or a map somewhere...")
        elif book_name == '"How to Determine The Best Number"':
            print("Wow, this book only has one page, one sentence. It reads, \"The best number is 5.\"")
        elif book_name in {'How to Pull All Nighters Gaming', 'How to Procrastinate'}:
            print("Uh-oh. You feel not-so-knowledgeable. Your score seems to be getting lower.")
            print("Maybe pick more helpful books to read.")
        elif book_name == '"How to Make a TA Love You"':
            print("Hmm... perhaps the TA will be less grumpy when marking your test now.")
        else:
            print(f"You read {book_name}. You are now more knowledgeable.")


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        location_num: the location number
        available_score: the score received for visiting this location
        short_description: short description of this location
        long_description: long description of this location
        items: list of items available at this location
        actions: list of actions available at this location

    Representation Invariants:
        - location_num == -1 or 1 <= location_num <= 20
        - long_description != ''
        - short_description != ''
    """
    location_num: int
    available_score: int
    short_description: str
    long_description: str
    items: list[Item]
    actions: list[str]

    def __init__(self, location_num: int, available_score: int, short_description: str, long_description: str) -> None:
        """Initialize a new location without items and actions (to be initialized when creating an instance
        using available_items and available_directions and available_actions methods)
        """
        self.location_num = location_num
        self.available_score = available_score
        self.long_description = long_description
        self.short_description = short_description
        self.items = []
        self.actions = []

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

    def available_items(self, items_list: list[Item]) -> list[Item]:
        """ Returns a list of items available to pick up at this location
        """
        items = []
        for item in items_list:
            if item.start == self.location_num:
                items.append(item)
        return items

    def available_directions(self, map_list: list[list[int]], x: int, y: int) -> list[str]:
        """
        Return the list of available directions in this location depending
        on the x,y position of this location on the world map.
        """
        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        # implemented for movement
        directions = []
        if y + 1 < len(map_list[x]) and map_list[x][y + 1] != -1:
            directions.append('go east')
        if y - 1 >= 0 and map_list[x][y - 1] != -1:
            directions.append('go west')
        if x + 1 < len(map_list) and map_list[x + 1][y] != -1:
            directions.append('go south')
        if x - 1 >= 0 and map_list[x - 1][y] != -1:
            directions.append('go north')
        return directions

    def available_actions(self, items_list: list[Item], inventory: list[Item]) -> list[str]:
        """
        Return the list of available actions at this location including pick up, drop, map, and read.
        """
        actions = []
        if len(self.available_items(items_list)) > 0:
            actions.append('pick up item')
        if len(inventory) > 0:
            actions.append('drop item')
        for item in inventory:
            if item.name == 'Map':
                actions.append('use map')
                break
        for item in self.available_items(items_list):
            if isinstance(item, Book):
                read_book = 'read ' + item.name
                actions.append(read_book)
        return actions


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - locations: a nested list representation of the locations in the world
        - items: a nested list representation of the items in the world

    Representation Invariants:
        - len(map) > 0
        - len(locations) > 0
        - len(items) > 0
    """
    map: list[list[int]]
    locations: list[Location]
    items: list[Item]

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
        the_map = []
        file = map_data.readlines()
        for line in file:
            row = [int(num) for num in line.split()]
            the_map.append(row)
        return the_map

    def load_locations(self, location_data: TextIO) -> list[Location]:
        """
        Store locations from open file location_data as the locations attribute of this object, as a list
        of Location objects of length 4, containing the location number, number of points earned for
        visiting this location for the first time, short description, long description attributes, in that order.
        """
        locations = []
        while True:
            location_num = location_data.readline().strip()
            if location_num == '':
                break
            location_num = int(location_num)
            number1 = int(location_data.readline().strip())

            short_description = location_data.readline().strip()

            long_description = ''
            while True:
                line = location_data.readline()
                if line == 'END\n':
                    break
                long_description += line

            locations.append(Location(location_num, number1, short_description, long_description))
            # to skip the ''
            location_data.readline()
        return locations

    def load_items(self, items_data: TextIO) -> list[Item]:
        """
        Store items from open file location_data as the items attribute of this object, as a list of
        Item objects or its child class objects with starting location, target location, points granted
        for picking up the item, and item name attributes, in that order.
        """
        items = []
        file = items_data.readlines()
        for line in file:
            elements = line.split()
            item_name = ' '.join(elements[3:])
            if 'How to' in item_name:
                item = Book(int(elements[0]), int(elements[1]), int(elements[2]), item_name)
            elif item_name == 'Map':
                item = Map(int(elements[0]), int(elements[1]), int(elements[2]), item_name)
            else:
                item = Item(int(elements[0]), int(elements[1]), int(elements[2]), item_name)
            items.append(item)
        return items

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        location_num = self.map[x][y]
        if location_num == -1:
            return None
        for location in self.locations:
            if location.location_num == location_num:
                return location
        return None


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
    x: int
    y: int
    victory: bool
    inventory: list
    world: World
    inventory_size: int

    def __init__(self, x: int, y: int, world: World) -> None:
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
        self.inventory_size = 2

    # MOVEMENT FUNCTIONS here:
    def move(self, dx: int, dy: int) -> None:
        """
        The player's movement
        """
        new_x = self.x + dx
        new_y = self.y + dy
        self.x = new_x
        self.y = new_y

    def go_north(self) -> None:
        """
        The player chooses to go north by one step
        """
        self.move(-1, 0)

    def go_south(self) -> None:
        """
        The player chooses to go south by one step
        """
        self.move(1, 0)

    def go_west(self) -> None:
        """
        The player chooses to go west by one step
        """
        self.move(0, -1)

    def go_east(self) -> None:
        """
        The player chooses to go east by one step
        """
        self.move(0, 1)

    # INVENTORY FUNCTIONS here:
    def remove_from_location(self, item_to_pick_up: Item, items_list: list[Item]) -> None:
        """
        Remove picked up item from its location
        """
        for item_in_list in items_list:
            if item_in_list.name == item_to_pick_up.name:
                item_in_list.start = -2

    def pick_up_item(self, item_name: str, location: Location, items_list: list[Item]) -> bool:
        """
        Add an item to the player's inventory.
        """
        item_to_pick_up = None

        for item in location.items:
            if item.name == item_name:
                item_to_pick_up = item
                break

        if item_to_pick_up:
            if item_name == "Bag":
                self.inventory_size = 3
                location.items.remove(item_to_pick_up)
                print(f"Picked up {item_name}.")
                print("WOW You found DORA's bag! Now your inventory size increase to 3 :)")
                self.remove_from_location(item_to_pick_up, items_list)
                return True
            elif len(self.inventory) <= self.inventory_size:
                self.inventory.append(item_to_pick_up)
                location.items.remove(item_to_pick_up)
                print(f"Picked up {item_name}.")
                self.remove_from_location(item_to_pick_up, items_list)
                return True
            else:
                print("Sorry, your bag is full :( You can't pick up ", item_name)
        else:
            print("Item not found in this location.")
        return False

    def drop_item(self, item_name: str, location: Location, items_list: list[Item]) -> bool:
        """
        Drop the specified item from the player's inventory
        (plus: adding it to the current location).
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
            location.items.append(item_to_drop)
            print(f"Dropped {item_name}.")
            for item_in_list in items_list:
                if item_in_list.name == item_to_drop.name:
                    item_in_list.start = location.location_num
                    break
            return True
        else:
            print(f"You do not have {item_name} in your inventory.")
            return False

    def view_inventory(self) -> None:
        """
        Display a list of current items in the inventory.
        """
        if self.inventory:
            inventory_names = [item.name for item in self.inventory]
            print("Inventory:", ", ".join(inventory_names))

        else:
            print("Your inventory is empty.")

    def player_victory(self, location: Location, score: int) -> None:
        """
        Player achieve victory with specific condition.
        """
        inventory_items = [item.name for item in self.inventory]

        correct_items = {item.name for item in location.items if location.location_num == item.target}
        if correct_items == {'Cheat Sheet', 'T-Card', 'Lucky Pen'}:
            if score >= 35:
                self.victory = True
                print("Congratulations! You scored great on the exam!")
            else:
                print("You successfully took the exam, but you failed :(")
                print("Next time, try exploring the campus more and look for items that will")
                print("help you score better on the exam!")
                exit()
        elif location.location_num == 5 and '"How to Manage Your Time"' in inventory_items:
            self.victory = True
            print("The time machine turns on. It makes some funky noises and turns off again.")
            print("Unconvinced, you check the time. It's the day after the exam!")
            print("You brought the correct book to the time machine! That's its key!")
            print("You receive an email from CrowdMark that your exam was graded. You check and... you")
            print("scored amazing! Maybe it's some butterfly effect from time travel.")
