#!python3
"""Describes the actions a player can make in the game"""

from player import Player


class Action():
    """The base class for all actions"""
    def __init__(self, method, name, hotkey, ends_turn, **kwargs):
        """Creates a new action
        :param method: the function object to execute
        :param name: the name of the action
        :param ends_turn: True if the player is expected to move after this action else False
        :param hotkey: The keyboard key the player should use to initiate this action
        """
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
        self.ends_turn = ends_turn

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n', ends_turn=True)


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s', ends_turn=True)


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e', ends_turn=True)


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w', ends_turn=True)


class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i', ends_turn=False)

class CheckStats(Action):
    """Prints the player's relavant stats"""
    def __init__(self):
        super().__init__(method=Player.check_stats, name='Stats', hotkey='p', ends_turn=False)

class CheckMap(Action):
    """Outputs the player's map"""
    def __init__(self):
        super().__init__(method=Player.check_map, name='Check Map', hotkey='m', ends_turn=False)

class Heal(Action):	
    """Heals the player"""
    def __init__(self):
        super().__init__(method=Player.use_potion, name='Heal', hotkey='h', ends_turn=True)
        
class Attack(Action):
    """Attacks enemy"""
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy, ends_turn=True)

class Flee(Action):
    """flee from battle into a random near by room"""
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile, ends_turn=True)
