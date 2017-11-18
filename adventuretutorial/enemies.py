#!python3
"""Defines the enemies in the game"""


class Enemy:
    """A base class for all enemies"""
    def __init__(self, name, hp, damage, aim):
        """Creates a new enemy
        :param name: the name of the enemy
        :param hp: the hit points of the enemy
        :param damage: the damage the enemy does with each attack
        """
        self.name = name
        self.hp = hp
        self.damage = damage
        self.aim = aim

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=40, damage=6, aim=65)
        
class GiantRat(Enemy):
    def __init__(self):
        super().__init__(name="Giant Rat", hp=35, damage=10, aim=60)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=55, damage=25, aim=56)

class ManBearPig(Enemy):
    def __init__(self):
        super().__init__(name="Man Bear Pig", hp=65, damage=40, aim=35)

class GiantCaveBeetle(Enemy):
    def __init__(self):
        super().__init__(name="Giant Cave Beetle", hp=50, damage=25, aim=59)

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp=45, damage=30, aim=60)