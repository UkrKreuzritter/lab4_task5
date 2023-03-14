"""
Game module
"""
killed_enemies = 0
class Room:
    """
    Class Room
    """
    def __init__(self, name):
        self.name = name
        self.rooms=dict()
        self.__description__ = None
        self.character = None
        self.__item__ = None

    def set_description(self, description):
        self.__description__ = description

    def link_room(self, another_room, direction):
        self.rooms[direction] = another_room

    def move(self, command):
        return self.rooms[command]

    def get_details(self):
        print(f'{self.name}\n--------------------\n{self.__description__}')
        for i in self.rooms:
            print(f'{self.rooms[i].name} is {i}')

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def set_item(self, item):
        self.__item__ = item

    def get_item(self):
        return self.__item__

class Enemy:
    """
    Class Enemy
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_weakness(self, weakness):
        self.weakness = weakness

    def set_conversation(self, replica):
        self.replica = replica

    def describe(self):
        print(f'{self.name} is here!\n{self.description}')

    def talk(self):
        print(f'[{self.name} says]: {self.replica}')

    def fight(self, fight_with):
        return self.weakness == fight_with

    def get_defeated(self):
        global killed_enemies
        killed_enemies+=1
        return killed_enemies

class Item:
    """
    Class Item
    """
    def __init__(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        return self.name
