#!python3
"""Describes the tiles in the world space."""
import items, enemies, actions, world, random
from player import Player


class MapTile:
	"""The base class for a tile within the world space"""
	def __init__(self, x, y):
		"""Creates a new tile.
		:param x: the x-coordinate of the tile
		:param y: the y-coordinate of the tile
		"""
		self.x = x
		self.y = y

	def enter_room(self):
		#A few checks are made to decide what information is displayed
		raise NotImplementedError()

	def modify_player(self, the_player):
		"""Process actions that change the state of the player."""
		raise NotImplementedError()

	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles."""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		return moves
		
	def available_actions(self):
		"""Returns all of the available actions in this room."""
		moves = self.adjacent_moves()
		moves.append (actions.Heal())
		moves.append (actions.CheckStats())
		moves.append(actions.ViewInventory())
		moves.append(actions.CheckMap())
		return moves

#starting room
class StR(MapTile):

	def enter_room(self):
		return """
		You feel like you've been here before
		"""

	def modify_player(self, the_player):
		#Room has no action on player
		pass
#Leave Cave Room (end game)
class END(MapTile):

	def enter_room(self):
		return """
		You see a bright light in the distance...
		... it grows as you get closer! It's sunlight!
		Victory is yours!
		"""

	def modify_player(self, player):
		input("Press Enter to Exit")
		player.victory = True        

#EmptyCavePath 
class ECP(MapTile):

	def enter_room(self):
		x = random.randrange(0,3)
		message_list = [
			"""
			Another unremarkable part of the cave. You must forge onwards.
			""" 
			, 
			"""
			Just a dark cave
			"""
			,
			"""
			You don't notice anything special in this part of the cave
			"""        ]
		return message_list[x]
			
	def modify_player(self, the_player):
		#Room has no action on player
		pass

class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, the_player):
		chance = random.randrange(0,100,2)
		if self.enemy.is_alive():
			if chance < self.enemy.aim:
				the_player.hp = the_player.hp - self.enemy.damage
				print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
			else:
				print ('Enemy Missed!')
	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
		else:
			return self.adjacent_moves()
			
class LootRoom(MapTile):
	"""A room that adds something to the player's inventory"""
	def __init__(self, x, y, item):
		self.item = item
		self.x = x
		self.y = y
		super().__init__(x, y)

	def add_loot(self, the_player):
		#Keeps from adding the same weapon
		HaveWeapon = 0
		HaveItem = 0
		for item in Player.inventory:
			if isinstance(item, items.Weapon):
				if item.name == self.item.name:
					Haveweapon = 1
			elif isinstance(item, items.Essential):
				if item.name == self.item.name:
					if item.x == self.item.x and item.y == self.item.y:
						HaveItem =1
		if HaveWeapon == 1:
			pass
		if HaveItem == 1:
			pass
		else:
			the_player.inventory.append(self.item)

	def modify_player(self, the_player):
			self.add_loot(the_player)

#room with a dagger
class DgR(LootRoom):

	def __init__(self, x, y):
		super().__init__(x, y, items.Dagger())

	def enter_room(self):
		HaveWeapon = 0
		for item in Player.inventory:
			if isinstance(item, items.Weapon):
				if item.name == 'Dagger':
					HaveWeapon = 1
		if HaveWeapon == 1: 
			return"""
			Nothing special about this part of the cave.
			"""
		else:
			return """
		You notice something shiny in the corner.
		It's a dagger! You pick it up.
		"""
#sword room
class SdR(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Sword())

	def enter_room(self):
		HaveWeapon = 0
		for item in Player.inventory:
			if isinstance(item, items.Weapon):
				if item.name == 'Sword':
					HaveWeapon = 1
		if HaveWeapon == 1: 
			return"""
			Nothing special about this part of the cave.
			"""
		else:
			return """
		You see a Sword lying next to the corpse of a dead warrior.
		The poor fool.
		You take the Sword
		"""        
#Axe room	
class AxR(LootRoom):
	def __init__(self, x, y):   
		super().__init__(x, y, items.Axe())

	def enter_room(self):
		HaveWeapon = 0
		for item in Player.inventory:
			if isinstance(item, items.Weapon):
				if item.name == 'Axe':
					HaveWeapon = 1
		if HaveWeapon == 1: 
			return"""
			Nothing special about this part of the cave.
			"""   
		else:
			return """
		You find an Axe wedged in the skull of an Ogre.
		You take the Axe.
		"""
#battle axe room		
class BAR(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.BattleAxe())

	def enter_room(self):
		HaveWeapon = 0
		for item in Player.inventory:
			if isinstance(item, items.Weapon):
				if item.name == 'Battle Axe':
					HaveWeapon = 1
		if HaveWeapon == 1: 
			return"""
			Nothing special about this part of the cave.
			"""
		else:
			return """
		You see the handle of an object sticking out from some rubble.
		You pull out the object to find that it's a Battle Axe!
		"""

#Gold room
class GdR(LootRoom):
	def __init__(self, x, y):
		amount = random.randrange(1,30)
		super().__init__(x, y, items.Gold(amount,x,y))

	def enter_room(self):
		return """
		You find a bag of gold!
		"""       
#potion room
class PtR(LootRoom):
	def __init__(self, x, y):
		amount = random.randrange(20,65,5)
		super().__init__(x, y, items.Potion(amount,x,y))

	def enter_room(self):
		havepotion = 0
		for item in Player.inventory:
			if isinstance(item, items.Essential):
				if item.x == self.item.x and item.y == self.item.y:
					havepotion = 1
					break
		if havepotion == 1:        
			return """
			Doesn't seem to be anyhting here"""
		else:
			return """
			You find a Potion on the ground!
			"""        
		 
#giant spider
class GSR(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.GiantSpider())

	def enter_room(self):
		if self.enemy.is_alive():
		
			return """
			A giant spider jumps down from its web in front of you!
			"""
		else:
			return """
			The corpse of a dead spider rots on the ground.
			"""
#giant rat
class GRR(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.GiantRat())

	def enter_room(self):
		if self.enemy.is_alive():
			return """
			A giant rat starts running towards you!
			"""
		else:
			return """
			A decapitated rat lay at your feet.
			"""
#ogre room
class OgR(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Ogre())

	def enter_room(self):
		if self.enemy.is_alive():
			return """
			An ugly looking ogre is blocking your path!
			"""
		else:
			return """
			A dead ogre reminds you of your triumph.
			"""

#man bear pig
class MBP(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.ManBearPig())

	def enter_room(self):
		if self.enemy.is_alive():
			return """
			You see a disgusting creating eating a corpse.
			It looks up at you.
			It seems to be part human,bear,and pig.
			those bear arms look strong.
			"""
		else:
			return """
			Man Bear Pig is dead! Rejoice!
			"""
#Giant Cave Beetle
class CbR(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.GiantCaveBeetle())

	def enter_room(self):
		if self.enemy.is_alive():
			return """
			A Giant Cave Beetle comes out of a hole in the ground 
			a few feet from where you stand.
			"""
		else:
			return """
			The disgusting bug lies dead in front of you.
			"""

#skeleton room
class SkR(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Skeleton())

	def enter_room(self):
		if self.enemy.is_alive():
			return """
			Ahh fuck the Skeleton is alive!
			"""
		else:
			return """
			The skeleton lays in pieces.
			Funny that it doesn't put itself back together huh?
			"""
