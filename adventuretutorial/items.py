#!python3
"""Describes the items in the game."""


class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage, aim, IsEquiped):
        self.damage = damage
        self.aim = aim
        self.IsEquiped = IsEquiped
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Essential(Item):
    #This Class is only used to allow "isinstance" to affect how they are picked up
    def __init__(self, name, description, value,x,y):
        self.x = x
        self.y = y
        self.name = name
        self.description = description
        self.value = value
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
 
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5,
                         aim=100,
                         IsEquiped=True)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10,
                         aim=60,
                         IsEquiped=False)
                                        
class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A sword with some blood on it.",
                         value=20,
                         damage=20,
                         aim=55,
                         IsEquiped=False)

class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                         description="Nicely sharpened Axe.",
                         value=23,
                         damage=30,
                         aim=40,
                         IsEquiped=False)

class BattleAxe(Weapon):
    def __init__(self):
        super().__init__(name="Battle Axe",
                         description="A heavy Battle Axe.",
                         value=30,
                         damage=37,
                         aim=35,
                         IsEquiped=False)
           
class Gold(Essential):
    def __init__(self, amt,x,y):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt,
                         x = x,
                         y = y)
                         
class Potion(Essential):
    def __init__(self, HitPoints,x,y):
        self.amt = HitPoints
        super().__init__(name="Potion",
                         description="A Potion that restores {} HP.".format(str(self.amt)),
                         value=self.amt,
                         x = x,
                         y = y)
