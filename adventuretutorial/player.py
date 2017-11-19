#!python3
import random
import items, world

class Player():
	inventory = [items.Rock()]
	hp = 100
	location_x, location_y = (12, 20)
	victory = False
	pmap = [[12, 20]] 

	def is_alive(self):
		return self.hp > 0
		
	def dead(self):
		return self.hp <= 0

	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)

	def print_inventory(self):
		#creates a fresh list and checks inventory for potions
		#and adds Heal amount of each potion to the list
		potionlist = list()        
		for item in self.inventory:
			if isinstance(item, items.Potion):
				potionlist.append(item.value)
		Total_Gold = 0
		for item in self.inventory:
			if item.name != "Gold":
				print("--------------------")
				if item.name != "Potion":
					print(item, '\n')  
			if item.name == "Gold":
				Total_Gold = Total_Gold + item.value
		print("--------------------")
		print("Gold:",Total_Gold)
		print("Potions:",potionlist)
		print("--------------------")
		
	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(world.tile_exists(self.location_x, self.location_y).enter_room())

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)

	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0
		max_aim = 0
		chance = random.randrange(0,101)
		for i in self.inventory:
			if isinstance(i, items.Weapon):
				if i.IsEquiped:
					max_dmg = i.damage
					best_weapon = i
					if i.aim > max_aim:
						max_aim = i.aim
					print("You use {} against {}!".format(best_weapon.name, enemy.name))
					if chance <= max_aim:
						enemy.hp -= best_weapon.damage
						if not enemy.is_alive():
							print("You killed the {}!".format(enemy.name))
							print("==========================")
						else:
							print("you hit {} dealing {} damage, enemy HP is {}.".format(enemy.name, max_dmg, enemy.hp))
							print("==========================")
					elif chance > max_aim:
						print("You miss, {}'s health is still {}.".format(enemy.name, enemy.hp))
						print("==========================")
	def use_potion(self):
		#creates a fresh list and checks inventory for potions
		#and adds Heal amount of each potion to the list
		potionlist = list()    
		for item in self.inventory:
			if isinstance(item, items.Potion):
				potionlist.append(item.value)
				
		#keeps you from healing while having full health
		if self.hp == 100:
			print("")
			print("Health already full")
			print("") 
   
		#checks if the potion list is still empty after checking inventory for them
		elif potionlist == []:
			print("")
			print("No Potions")
			print("")
		
		#This is if the Potion has potions in it
		elif potionlist != []:
			print("")
			print("Health is:",self.hp)            
			print("Potions Strengths Available:",potionlist ) 
			#Keeps people from being an ass and crashing the game with invalid entries
			try:
				healamt = int(input("""Enter potion's heal strength  to heal or enter 0 to exit: """))
			except:
				healamt = 0
			#This checks if the heal amount you entered matches a heal amount of a potion in your inventory
			for i in potionlist:       
				if i == healamt:
					self.hp = self.hp + healamt
					if self.hp > 100:
						self.hp = 100
					print("Health Restored by:",healamt)
					print("Health is now:",self.hp)
					print("")
					break
				#This break the healing action if you enter 0,leave blank, or enter invalid character for 'healamt'
				elif i == 0:
					print("")
					break
			#removes potion used
			index = -1
			for item in self.inventory:
				index +=1
				if isinstance(item, items.Potion):
					if item.value == healamt:
						self.inventory.pop(index)
						
		
			 
	def flee(self, tile):
		"""Moves the player randomly to an adjacent tile"""
		available_moves = tile.adjacent_moves()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])

	def check_stats(self):	       
		for item in self.inventory:
			if item.IsEquiped:
				current_weapon = item.name
				current_aim = item.aim
				current_dmg = item.damage
		total_potions = 0
		potionlist = list()    
		for item in self.inventory:
			if isinstance(item, items.Potion):
				total_potions += 1
		print("--------------------")
		print("Health: {}".format(self.hp))
		print("Potions: {}".format(total_potions))
		print("Equiped:",current_weapon)
		print("Damage: {}".format(current_dmg))
		print("Hit chance: {}%".format(current_aim))
		print("--------------------")

	def check_map(self):
		with open('resources/newmap.txt', 'r') as f:
			rows = f.readlines()
		x_max = len(rows[0].split('\t'))
		map_lay = "X"
		for x in range(x_max):
			map_lay = map_lay + " " + str(x)
		for y in range(len(rows)):
			map_lay = map_lay + "\n" + str(y) + " "
			for x in range(x_max):
				room_disc = False
				current_room = False
				for room in self.pmap:
					if (y == room[1] and x == room[0]):
						room_disc = True
					if (y == self.location_y and x == self.location_x):
						current_room = True
				if ( current_room == True ):
					map_lay = map_lay + "x "
				elif (room_disc == True):
					map_lay = map_lay + "O "
				else:
					map_lay = map_lay + ". "		
		print(map_lay)

	def update_map(self):
		discovered = False
		for room in self.pmap:
			if (room[1] == self.location_y and room[0] == self.location_x):
				discovered = True
		if (discovered == False):
			self.pmap.append([self.location_x, self.location_y])
