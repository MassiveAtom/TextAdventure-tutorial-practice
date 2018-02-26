#!python3
import os
"""
A simple text adventure designed as a learning experience for new programmers.
"""
import world
import messages
from player import Player

def play():
	os.system('cls')
	os.system('color 0f')

	world.load_tiles()
	player = Player()
	messages.output('prelude')

	while player.is_alive() and not player.victory:
		room = world.tile_exists(player.location_x, player.location_y)
		room.modify_player(player)
		# Check again since the room could have changed the player's state
		if player.is_alive() and not player.victory:
			ends_turn = False
			while ends_turn == False:
				print("\nChoose an action:")
				available_actions = room.available_actions()
				for action in available_actions:
					print(action)
				action_input = input('Action: ')
				player.update_map()
				invalid_input = True
				for action in available_actions:
					if action_input == action.hotkey:
						invalid_input = False
						player.do_action(action, **action.kwargs)
						ends_turn = action.ends_turn
				if invalid_input:
					print("\n***********Action Not Allowed***********\n")

	if player.dead:
		print ("You have died! care to try again?")
		print ("")
		input('''
		Press enter to quit''')

if __name__ == "__main__":
	play()
