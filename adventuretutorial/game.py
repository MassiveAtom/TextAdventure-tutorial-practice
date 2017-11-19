#!python3
import os
"""
A simple text adventure designed as a learning experience for new programmers.
"""
import world
from player import Player


def play():
    os.system('cls')
    os.system('color 0f')
    world.load_tiles()
    player = Player()
    input("""
    TIP:
    Get some paper(preferably Grid), draw a Compass Rose(N,S,E,W) 
    pick a starting point on the paper, keep track of which direction you go.
    So you can remember where you've been. YOU WILL GET LOST! (^_^) 
    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    If you beat the map and wish for another one 
    or wish for a less impossible one, just let me know. 
    Email: blueburritosuit@gmail.com
   
    Can you make it out alive?
    we shall see!
    
    Press Enter to start""")
    os.system('cls')
    print("""
    You awaken in a damp and dark cave. 
    The last thing you remember was wandering through the woods near town 
    when a sharp pain burst from the back of your head.
    In your last moments of consciousness 
    you recall hearing the deep bellowing laughter of an Ogre!
    You stand up, brush the dirt off your clothes, grab the nearest rock,
    and swear to escape this dreadful place alive!
    
    You see two paths before you. 'Which one is the way out?', you wonder.
    """)
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("""
Choose an action:""")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            cls_excluded_hotkeys = ["a", "n", "e", "s", "w"]
            clearscreen = True;
            for act_hotkey in cls_excluded_hotkeys:
                if action_input == act_hotkey:
                    clearscreen = False;
            if clearscreen == True: os.system('cls')
            player.update_map()
            if action_input == "a": 
                print("")
                print("==========================")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    if player.dead:
        print ("You have died! care to try again?")
        print ("")
        input('''
        Press enter to quit''')
if __name__ == "__main__":
    play()