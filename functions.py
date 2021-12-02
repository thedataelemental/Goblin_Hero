# functions.py
# Author: Jackie P / TheDataElemental


# Import built-in modules
import sys
import random
import threading
import time
import math
import os

# Import pygame, classes and data
sys.path.append('C:/Users/elimu/Desktop/Goblin Hero/Data')
from instances import *

# Import other functions
from universal_functions import *
from overworld_functions import *
from battle_functions import *


# Player is prompted to save at a Golden Flower (save point)
# def save_game():
#	save_game_text = text_font.render\
#		("Step outside of time?", True, WHITE)
#	scroll_text(save_game_text, 
#	yes_or_no()


# Player interacts with a Heal Point (Golden Flower) on the overworld
def use_heal_point():
	# Restore all party members' hp to max
	for party_member in living_party_members:
		party_member.hp = party_member.max_hp
		
	# Display "health restored" message
	health_restored_text = "Health restored."
	scroll_text(health_restored_text, False, None, False)
	pygame.time.delay(300)


# Display all elements on the screen
def update_screen():
	for entity in current_entities:
			if entity.render_type == True:
				# Display 2-tile-tall entities one tile above normal
				if (entity.race == 'Troll') or \
					(entity.type == 'Heal Point'):
						screen.blit(entity.current_image,\
							(entity.position_x,entity.position_y - 32))
				# Display one-tile-tall entities
				else:
					screen.blit(entity.current_image,\
						(entity.position_x,entity.position_y))


# Play party chat conversation
def play_conversation(conversation):
	if conversation.played == False:
		for i in range(len(conversation.speaker_list)):
			scroll_text\
				(conversation.speech_list[i], True, \
				conversation.speaker_list[i], True)
	
		conversation.played = True


# Player selects and buys an item from the shop
def buy_an_item(shopcounter):
	# Player uses cursor to select an item. Returns coordinate pair
	# of cursor location.
	item_selection = str(cursor_system(64, 108, 1, 6, 0, 40))
	if item_selection == 'BACK':
		shop(shopcounter.owner, shopcounter.inventory, shopcounter.prices)
	
	# Fetch the number of the selected item from cursor's y coord.
	item_number = item_selection[4]
	
	# Remove (skip over) negative sign in item number
	if item_number == "-":
		item_number = item_selection[5]
		
	# Generate and display confirmation message
	confirm_prompt = "The " + shopcounter.inventory[int(item_number)] + \
		"? That'll be " + shopcounter.prices[int(item_number)] + \
		" Teeth. Okay?"
	scroll_text(confirm_prompt, True, shopcounter.owner, False)
	
	# Display yes or no prompt and return player selection
	yes_or_no_choice = str(yes_or_no())[4]
	
	if yes_or_no_choice == '0':
		# Check if player has enough gold (Teeth) to buy item
		if player.gold >= int(shopcounter.prices[int(item_number)]):
			# Add selected item to player's inventory from shop's
			player.inventory.append(shopcounter.inventory[int(item_number)])
			scroll_text(gee_thanks, True, shopcounter.owner, False)
			
			# Take money from player and update money display
			player.gold -= int(shopcounter.prices[int(item_number)])
			show_teeth()
			
		else:
			scroll_text(not_enough_teeth, True, shopcounter.owner, False)
	
	# "Anything else?"
	scroll_text(anything_else, True, shopcounter.owner, False)
	yes_or_no_choice = str(yes_or_no())[4]
	
	if yes_or_no_choice == '0':
		# Restart shop function
		self.shop(shopcounter.owner, shopcounter.inventory, shopcounter.prices)
		
	else:
		# End shop
		scroll_text(dont_lose_your_head, True, shopcounter.owner, False)
		pygame.time.delay(500)


# Player shops at shop counter (begin shop)
def shop(shopcounter):
	# "Buy somethin will ya?"
	scroll_text(item_vendor_script, True, shopcounter.owner, False)
	pygame.time.delay(300)
	
	# Display player's Gold (Teeth) counter
	show_teeth()	
	
	# Generate and display names of items for sale in shop
	screen.blit(shop_buy_frame,(32,78))
	n = 0
	for item in shopcounter.inventory:
		item_name = menu_font.render(item, True, WHITE)
		# T stands for Teeth (Goblin Hero's version of Gold)
		item_price = \
			menu_font.render(shopcounter.prices[n] + " T.", True, WHITE)
		screen.blit(item_name, (90, (108 + (40 * n))))
		screen.blit(item_price, (330, (108 + (40 * n))))
		n += 1	
	
	pygame.display.flip()
	
	# Call function for buying an item
	buy_an_item(shopcounter)


# Teleport player to portal's destination
def teleport(portal):
		global world_map
		global world_x
		global world_y
		global current_level
		global current_entities
		global current_walls
		global steps_taken_into_level
		global current_zone
		global battle_step_counter
		
		# Reset NPC talk counters
		for entity in current_entities:
			if entity.type == 'NPC':
				entity.talk_counter = 0
				
		# Reset steps taken before battle check
		battle_step_counter = 0
		
		# Make party members face correct direction while
		# exiting portal
		if portal.destination_object.portal_facing == 'South':
			player_2.position_x = 224
			player_2.position_y = 192
			player_3.position_x = 224
			player_3.position_y = 160
			player_4.position_x = 224
			player_4.position_y = 128
			for party_member in party_members:
				party_member.current_facing = 'Front'
			player.current_idle_images = player.front_idles
				
		elif portal.destination_object.portal_facing == 'North':
			player_2.position_x = 224
			player_2.position_y = 256
			player_3.position_x = 224
			player_3.position_y = 288
			player_4.position_x = 224
			player_4.position_y = 320
			for party_member in party_members:
				party_member.current_facing = 'Back'
				player.current_idle_images = player.back_idles
				
		elif portal.destination_object.portal_facing == 'East':
			player_2.position_x = 192
			player_2.position_y = 224
			player_3.position_x = 160
			player_3.position_y = 224
			player_4.position_x = 128
			player_4.position_y = 224
			for party_member in party_members:
				party_member.current_facing = 'Right'
			player.current_idle_images = player.right_idles
				
		elif portal.destination_object.portal_facing == 'West':
			player_2.position_x = 256
			player_2.position_y = 224
			player_3.position_x = 288
			player_3.position_y = 224
			player_4.position_x = 320
			player_4.position_y = 224
			for party_member in party_members:
				party_member.current_facing = 'Left'
			player.current_idle_images = player.left_idles
		
		# Black out screen
		screen.blit(black_screen,(0,0))
		pygame.display.flip()
		pygame.time.delay(250)
		
		# Remove non-player party members from current level
		for party_member in [player_2, player_3, player_4]:
			if party_member in current_level.entities:
				current_level.entities.remove(party_member)
		
		# Replace current level with destination level
		portal.destination_level.current_entrance = portal
		current_level = portal.destination_level
		
		world_map = portal.destination_level.image_1
		(world_x, world_y) = (portal.destination_object.set_world_x, \
			portal.destination_object.set_world_y)
			
		current_walls = portal.destination_level.walls
		current_entities = portal.destination_level.entities
		
		steps_taken_into_level = 0
		
		current_zone = portal.destination_zone


# Display window with gold / teeth count
def show_teeth():
	screen.blit(teeth_display_frame,(96, 0))
	teeth_text = menu_font.render('Teeth:', True, WHITE)
	teeth_number = menu_font.render(str(player.gold), True, WHITE)
	screen.blit(teeth_text, (118, 24))
	screen.blit(teeth_number, (218, 24))
	pygame.display.flip()
	
	
# Open a treasure chest.
def open_chest(chest, opener):
	global current_entities
	
	if chest.state == 'Closed':
		chest.state = 'Open'
		chest.current_image = chest.open_image
		
		
#		screen.blit(chest.current_image,\
#			(chest.position_x, chest.position_y))
		
		# Update chest image to 'open' image.
		screen.blit(world_map, (world_x, world_y))
		screen.blit(player.current_image, \
			(player.position_x, player.position_y))
		update_screen()	
		
		# Generate chest-opening text.
		chest_open_text = opener.name + " opened the chest!"
		obtain_item_text = \
			opener.name + " found the " + chest.contents + "!"
		
		# Put chest conents in opener's inventory.
		opener.inventory.append(chest.contents)
	
		# Display chest-opening text messages on screen.
		screen.blit(text_box,(0,352))
		scroll_text(chest_open_text, False, None, False)
		scroll_text(obtain_item_text, False, None, False)
		pygame.time.delay(300)
		
		# Special case - display Prototype ending sequence
		if 'Ancient Key' in opener.inventory:	
			scroll_text(helena_prototype_speech, \
				True, player_3, True)
			scroll_text(bolder_prototype_speech, \
				True, player_4, True)
			scroll_text(skratch_prototype_speech, \
				True, player_2, True)
			scroll_text(ivy_prototype_speech, \
				True, player, True)

			# Display prototype end screens
			screen.blit(the_end, (0,0))
			pygame.display.flip()
			
			# Start fading out music
			for i in range(10):
				pygame.mixer.music.set_volume(0.25 - (i / 200))
				pygame.time.delay(250)
			
			screen.blit(prototype_end_screen, (0,0))
			pygame.display.flip()
			
			# Finish music fade
			for i in range(40):
				pygame.mixer.music.set_volume(0.20 - (i / 200))
				pygame.time.delay(250)
			pygame.mixer.music.stop()
			
			quit()


# Choose possible monsters based on area
# note - starting world map position:
# world_x = -268
# world_y = -6056
def check_map_location():
	global world_x
	global world_y
	global monster_list
	global current_map
	global current_zone
	
	if current_level == 'overworld':
		# Forest Zone 1, Block 1
		if (-592 <= world_x <= 48) and (-6432 <= world_y <= -5632):
			current_zone = 'Forest Zone 1'
			monster_list = forest_zone_1_monsters
		# Forest Zone 1, Block 2
		elif (-2000 <= world_x <= -624) and (-6816 <= world_y <= -6048):
			current_zone = 'Forest Zone 1'
			monster_list = forest_zone_1_monsters
		# Forest Zone 2, Block 1
		elif (-1968 <= world_x <= -720) and (-5984 <= world_y <= -5632):
			current_zone = 'Forest Zone 2'
			monster_list = forest_zone_2_monsters
		# Forest Zone 2, Block 2
		elif (-4048 <= world_x <= -2000) and (-5920 <= world_y <= -4928):
			current_zone = 'Forest Zone 2'
			monster_list = forest_zone_2_monsters
			
	# Catch-all for player outside of defined monster zones
		else:
			current_zone = "Unknown"
			monster_list = forest_zone_1_monsters
			
#	elif current_level == 'forest_shrine':
#		monster_list = forest_shrine_monsters
		
	elif current_level == prototype_basement:
		monster_list = prototype_basement_monsters
	
	elif current_level == prototype_basement_level_2:
		monster_list = prototype_basement_monsters


# Player chooses actions for each party member during battle
def choose_actions():
	global active_party_member
	
	active_party_member = 0
	
	# Give player option to fight battle or run away
	fight_or_run_choice = 'BACK'
		
	while fight_or_run_choice == 'BACK':
		fight_or_run_choice = fight_or_run()
			
	if fight_or_run_choice[1] == 0:
		# Give each party member option to attack, 
		# use an item, use a spell or guard
		while active_party_member != len(living_party_members):
			if active_party_member == -1:
				active_party_member = 0
				choose_actions()
				
			else:
				battle_cursor()
				active_party_member += 1
	
		# Player chooses to run away
	elif fight_or_run_choice[1] == -1:
		print('Running away!')
		run_away()
		overworld()


# High-level state manager of battle system function calls
def battle_manager():
	global active_party_member
	
	# Start battle. Select enemy monsters, generate relevant data
	battle_start()
	
	# Main battle loop
	while len(living_party_members) != 0:
		
		# Choose party member actions
		choose_actions()

		# Party members take their chosen actions
		for party_member in living_party_members:
			
			# This line exists entirely to prevent freezing
			pygame.event.pump()
			
			if party_member.next_action == 'Attack':
				player_attack\
					(party_member, party_member.attack_target)
				pygame.time.delay(500)
				
#			elif party_member.next_action == 'Item':
#				use_item(party_member, party_member.item_choice, \
#					party_member.item_target)
				
			elif party_member.next_action == 'Spell':
				cast_spell(party_member, party_member.spell_choice, \
					party_member.spell_target)
			
			elif party_member.next_action == 'Guard':
				guard(party_member)
		
		# Check if monsters are dead			
		monster_death_check()
	
		# If all enemies are dead, end battle
		if len(battle_monsters) == 0:
			end_battle()
			overworld()
	
		# Enemy monsters retaliate
		for monster in battle_monsters:
			
			# This line exists entirely to prevent freezing
			pygame.event.pump()
			
			monster_attack(monster)
		
			# Check if any party members have died
			for party_member in living_party_members:
				player_death_check(party_member)
		
			# If all party members are dead, play game over sequence
			if len(living_party_members) == 0:
				game_over()
				
				
# Party member casts selected spell
def cast_spell(spell_caster, spell, target):
	
	clear_battle_screen()
	
	# Display spell-casting text
	cast_spell_text = spell_caster.name + " recites " + spell.name + "!"
	cast_spell_message = text_font.render(cast_spell_text, True, WHITE)
	screen.blit(text_box, (0,352))
	screen.blit(cast_spell_message, (42,380))
	pygame.display.flip()
	
	# Display spell animation
	loop_animation(1, spell.animation, 100, target.img_coords)
	screen.blit(target.img, target.img_coords)
	
	# Flicker target monster's sprite
	flicker_monster_sprite(target.img, target.img_coords)
	
	# Deduct mana points (SP)
	spell_caster.sp -= spell.mana_cost
	if spell_caster.sp < 0:
		spell_caster.sp = 0
	print_stats(0,0)
		
	# Carry out spell's effects
	damage = spell.effect(target)
	print_stats(0, 0)
	pygame.display.flip()
	pygame.time.delay(500)
	
	# Display damage done to monster
	attack_text_1 = text_font.render\
		(target.name + " takes:", True, WHITE)
	damage_text = str(damage) + " damage!"
	attack_text_2 = text_font.render\
		(damage_text, True, WHITE)
	screen.blit(attack_text_1,(42,405))
	pygame.display.flip()
	pygame.time.delay(500)
	screen.blit(attack_text_2,(42,430))
	pygame.display.flip()
	
	pygame.time.delay(1000)


# Party member guards against incoming damage during battle
def guard(party_member):
	global active_party_member
	
	party_member.is_guarding = True
		
	clear_battle_screen()
		
	# Display guarding text
	guarding_text_1 = party_member.name + \
		" assumed a guarded"
	guarding_text_2 = "stance!"
	guarding_display_text_1 = \
		text_font.render(guarding_text_1, True, WHITE)
	guarding_display_text_2 = \
		text_font.render(guarding_text_2, True, WHITE)
	screen.blit(text_box, (0,352))
	screen.blit(guarding_display_text_1, (42,380))
	screen.blit(guarding_display_text_2, (42,405))
	pygame.display.flip()
	pygame.time.delay(500)
	

# Flicker enemy monster sprite when taking damage
def flicker_monster_sprite(image, coordinates):
	monster_take_damage_sound.play()
	
	for i in range(2):
		screen.blit(black_monster_square, coordinates)
		pygame.display.flip()
		pygame.time.delay(50)
	
		screen.blit(image, coordinates)
		pygame.display.flip()
		pygame.time.delay(50)
	
	pygame.time.delay(500)
	
	
# Clear battle screen of extraneous images (player portrait, menus, etc)
def clear_battle_screen():
	screen.blit(black_screen, (0,0))
	screen.blit(battle_frame, (0,0))
	for monster in battle_monsters:
		screen.blit(monster.img, monster.img_coords)
	screen.blit(ui_box_1, (0,0))
	print_stats(0,0)
	screen.blit(text_box, (0,352))
	pygame.display.flip()
	

# Start random battle
def battle_start():
	global player
	global monster_1
	global monster_2
	global monster_3
	global monster_4
	global monster_list
	global battle_step_counter
	global battle_monsters
	global attack_cursor_x_locations
	global attack_cursor_y_locations
	global monster_display_names
	global monster_erase_names
	global monster_shine_names
	global text_x_pos
	global text_y_pos
	
	# Clear lists for "monster appears!" messages
	monster_appearance_messages = []
#	monster_types = [None, None, None, None]
#	monster_type_totals = [0, 0, 0, 0]
	
	# Total duplicate monsters from each available monster type
	group_1_total = 0
	group_2_total = 0
	group_3_total = 0
	
	# Play battle music
	# pygame.mixer.music.load\
	#	("Assets/Exports/Music/Goblin Hero - Battle.wav")
	# pygame.mixer.music.play(-1)
	
	# Reset steps until random battle
	battle_step_counter = 0
	
	# Flash black screen over Overworld
	for i in range(2):
		# Display black screen
		screen.blit(black_screen, (0,0))
		pygame.display.flip()
		pygame.time.delay(200)
		
		# Display overworld
		screen.blit(world_map,(world_x,world_y))
		screen.blit(player.current_image, (player.position_x, player.position_y))
		update_screen()

		pygame.display.flip()
		pygame.time.delay(200)
			
	# Play screen wipe effect for battle transition
	monster_appears_sound.play()
	transition_effect = screen_transitions \
		[random.randint(0, (len(screen_transitions) - 1))]
	for image in transition_effect:
		screen.blit(image, (0,0))
		pygame.display.flip()
		pygame.time.delay(50)
		
#	for i in range(480):
#		screen.blit(battle_wipe_down_1, (0,i))
#		pygame.display.flip()
		
#	for i in range(512):
#		screen.blit(battle_wipe_right_1, (i,0))
#		pygame.display.flip()
	
	# Display battle background
	screen.blit(black_screen, (0,0))
	pygame.display.flip()
	pygame.time.delay(1000)
	screen.blit(battle_frame, (0,0))
	screen.blit(text_box, (0,352))
	screen.blit(ui_box_1,(0,0))
	print_stats(0, 0)
	check_map_location()
	total_monsters = random.randint(1,4)
	
	# List of possible sets of monster portrait coordinates
	monster_coordinate_sets = [[(212,180)],\
		[(152,180),(272,184)],\
		[(92,180),(212,184),(332,180)],\
		[(32,180),(152,184),(272,180),(392,184)]]
		
	battle_monsters = []
	
	# Clear lists for displaying monster names during target selection
	monster_display_names = []
	monster_erase_names = []
	monster_shine_names = []
	
	group_1_total = 0
	group_2_total = 0
	group_3_total = 0
	group_4_total = 0
	group_totals = [group_1_total, group_2_total, \
		group_3_total, group_4_total]
	
	for i in range(total_monsters):
		if i % 2 == 0:
			even_or_odd = 'even'
		else:
			even_or_odd = 'odd'
			
		# Choose random monster from appropriate group
		group_selection = random.randint(0,3)
		monster_group = monster_list[group_selection]
		monster = monster_group[group_totals[group_selection]]
		
#		# Code for displaying "monster appears" message later
#		monster_type_totals[group_selection] += 1
#		if monster.true_name not in monster_types:
#			monster_types[group_selection] = monster.true_name
		
		group_totals[group_selection] += 1
		battle_monsters.append(monster)
		
		# Blit monster to the screen
		monster.img_coords = monster_coordinate_sets\
			[total_monsters - 1][i]
		screen.blit(monster.img,monster.img_coords)
		screen.blit(text_box,(0,352))
		
		monster_text = text_font.render\
			("A " + monster.name + " appears!", True, WHITE)	
			
		# Colorize & capitalize monster name
		name_color = element_colors[monster.element]
		upper_name = monster.name.upper()
				
		# Add spaces to center name if shorter than max length
		if len(upper_name) < 20:
			name_length = len(upper_name)
			spaces_to_center = round((20 - name_length) / 2) + 1
			for i in range(spaces_to_center):
				upper_name = ' ' + upper_name[:]
				
		# Make white text characters for "shine" name effect
		shine_name = []
		for i in range(len(upper_name)):
			spaced_char = \
				(' ' * i) + upper_name[i]
			shine_char = menu_font.render(spaced_char, True, WHITE)
			shine_name.append(shine_char)
		monster_shine_names.append(shine_name)
		
		# Generate monster name for display and erasure
		color_name = \
			menu_font.render(upper_name, True, name_color)
		erase_name = \
			menu_font.render(upper_name, True, BLACK)
			
		# Make list of display and erase names for attack cursor
		monster_display_names.append(color_name)
		monster_erase_names.append(erase_name)
			
	# Generate monster appearance message (new method)
	for i in range(len(battle_monsters)):
#		if group_totals[i] > 1:
#			appearance_text = str(group_totals[i]) + " " + \
#				monster_list[i][0].true_name + "s appear!"
#			appearance_message = text_font.render\
#				(appearance_text, True, WHITE)
#			monster_appearance_messages.append(appearance_message)
			
		appearance_text = "A " + battle_monsters[i].true_name \
			+ " approaches!"
		appearance_message = text_font.render\
			(appearance_text, True, WHITE)
		monster_appearance_messages.append(appearance_message)
			
	# Display monster appearance message
	for i in range(len(monster_appearance_messages)):
		screen.blit(monster_appearance_messages[i],(42,370 + (25 * i)))
		
	pygame.display.flip()
	
	text_x_pos = len(appearance_text) * 16
	text_y_pos = 370 + (25 * (len(battle_monsters) - 1))
	get_enter()
	
	
	# TODO:
	# Create opening "x number of y monsters appear!" message:
	# Use a dictionary of battle monster's true_names and their totals.
	# Test first by printing, then work out screen text formatting.
	# Other idea:
	# Create list of totals while monsters are being selected.
		
	
	# Generate lists of possible x and y locations for attack cursor
	attack_cursor_x_locations = []
	attack_cursor_y_locations = []
	for monster in battle_monsters:
		attack_cursor_x_locations.append(monster.img_coords[0] + 38)
		attack_cursor_y_locations.append(monster.img_coords[1] + 100)
	
	# Debug code
	print("Battle start!")
	print("Monsters in battle:")
	for monster in battle_monsters:
		print(monster.name)
	print()
	
	
# Check if monsters or player are dead. If not, monsters attack.
def monster_death_check():
	global monster_1
	global monster_2
	global monster_3
	global monster_4
	global battle_monsters
	global dead_monsters
	global earned_exp
	global earned_gold
	global text_x_pos
	
	screen.blit(text_box,(0,352))
	
	# Monster death check
	monster_index = 0
	for monster in battle_monsters:
		if monster.hp <= 0:
			monster.hp = 0
		if monster.hp == 0:
			
			# Remove monster from battle
			monster_die_text = monster.name + " is slain!"
			monster_die_display_text = text_font.render\
				(monster_die_text, True, WHITE)
			print(monster.name, "died!")
			battle_monsters.remove(monster)
			dead_monsters.append(monster)
			screen.blit(monster_die_display_text,(42,380))
			screen.blit(battle_frame,(0,0))
			print("Monsters still alive:")
			for monster in battle_monsters:
				print(monster.name)
			print()
			print("Dead monsters:")
			for monster in dead_monsters:
				print(monster.name)
			print()
			screen.blit(ui_box_1,(0,0))
			print_stats(0, 0)
			
			# Remove display names and cursor locations of dead monster
			del monster_display_names[monster_index]
			del monster_erase_names[monster_index]
			del attack_cursor_x_locations[monster_index]
			del attack_cursor_y_locations[monster_index]
			
			# Show remaining monster portraits on screen
			for monster in battle_monsters:
				screen.blit(monster.img, monster.img_coords)
			pygame.display.flip()
			
			# Put cursor at end of line to be displayed
			text_x_pos = ((len(monster_die_text) - 1) * 16) + 20
			get_enter()
			
		else:
			monster_index += 1
		

# Play end-of-battle sequence
def end_battle():
	global dead_monsters
	
	earned_exp = 0
	earned_gold = 0
	
	# pygame.mixer.music.stop()
	battle_win_sound.play()
	# Give player experience and gold
	for monster in dead_monsters:
		earned_exp += monster.exp
		earned_gold += monster.gold
	player.exp += earned_exp
	player.gold += earned_gold
	exp_text = "Gained " + str(earned_exp) + " Experience!"
	gold_text = "Found " + str(earned_gold) + " Gold!"
	# "False, None, False" = not dialogue, no speaker, no portrait
	scroll_text(exp_text, False, None, False)
	scroll_text(gold_text, False, None, False)
	# Level up player, if appropriate
	if player.exp >= LEVEL_CAPS[player.level - 1]:
		level_up()
	# Clear list of dead monsters and other variables
	battle_monsters = []
	for monster in dead_monsters:
		monster.hp = monster.max_hp
	dead_monsters = []
	earned_exp = 0
	earned_gold = 0
	screen.blit(black_screen,(0,0))
	pygame.display.flip()
	pygame.time.delay(1000)


# Check for and carry out party member death
def player_death_check(party_member):
	global text_x_pos
	global text_y_pos
	
	# If party_member dies, show text & remove them from the battle.
	if party_member.hp == 0:
		pygame.mixer.music.stop()
		death_sound.play()
		death_text = party_member.name + " died!"
		death_prompt = text_font.render(death_text, True, WHITE)
		screen.blit(death_prompt, (42, 380))
		pygame.display.flip()
		
		# Set location of blinking cursor
		text_x_pos = 30 + (len(death_text) * 16)
		text_y_pos = 380
		
		# Kill party member
		living_party_members.remove(party_member)
		dead_party_members.append(party_member)
		
		print(living_party_members)
		print(dead_party_members)
		
		# Replace party member overworld sprites with ghost sprites
		party_member.assume_ghost_form()
		
		get_enter()


# Play animation for given number of loops, list of images, etc
def loop_animation(number_of_loops, list_of_images, delay, location):
	for i in range(number_of_loops):
		for image in list_of_images:
			screen.blit(image, location)
			pygame.display.flip()
			pygame.time.delay(delay)			
			
			
# Game Over / Death Angel sequence
def game_over():
	screen.blit(text_box, (0,352))
	all_dead_text = "All party members have died!"
	all_dead_display_text = text_font.render(all_dead_text, True, WHITE)
	screen.blit(all_dead_display_text, (42,380))
	pygame.display.flip()
	text_x_pos = 30 + (len(all_dead_text) * 16)
	text_y_pos = 380
	get_enter()
	
	screen.blit(text_box, (0,352))
	scroll_text("Darkness closes in...", False, None, False)
	screen.blit(black_screen, (0,0))
	pygame.display.flip()
	pygame.time.delay(1000)
	
	# Choose and display Angel dialogue image
	angel_dialogue_index = random.randint(0, (len(angel_dialogues) - 1))
	angel_dialogue_image = angel_dialogues[angel_dialogue_index]
	screen.blit(angel_dialogue_image, (60,285))
	
	# Angel blinks twice, then ring continues spinning, then speeds up
	loop_animation(2, angel_blink_images, 100, (192,160))
	loop_animation(4, angel_ring_images, 100, (192,160))
	loop_animation(10, angel_ring_images, 50, (192,160))
			
	# Game Over screen
	screen.blit(game_over_image, (0,0))
	pygame.display.flip()
	pygame.time.delay(3000)
	quit()


# Player attack monster
def player_attack(attacking_player, player_target):
	global battle_monsters
	global text_x_pos
	global text_y_pos
	
	# Erase player portrait
	clear_battle_screen()
	
	# Debug code
	print("Monster HPs before player attack:")
	for monster in battle_monsters:
		print(monster.name + " HP:", monster.hp)
	print()
		
	# Display player attack text and play sound
	player_attack_text_1 = text_font.render\
		(attacking_player.name + " attacks!", True, WHITE)
	screen.blit(text_box, (0,352))
	screen.blit(player_attack_text_1,(42,380))
	attack_sound.play()
	pygame.display.flip()
	pygame.time.delay(500)
	
	# Debug code
	print("Player attacks", player_target)
	
	# Flicker attacked monster's sprite
	flicker_monster_sprite(player_target.img,player_target.img_coords)
	
	# Generate, apply and display damage done to monster
	damage = random.randint\
		(attacking_player.damage_low,attacking_player.damage_high)
	player_target.hp -= damage
	player_attack_text_2 = text_font.render\
		(player_target.name + " takes:", True, WHITE)
	damage_text = str(damage) + " damage!"
	player_attack_text_3 = text_font.render\
		(damage_text, True, WHITE)
	screen.blit(player_attack_text_2,(42,405))
	pygame.display.flip()
	pygame.time.delay(500)
	screen.blit(player_attack_text_3,(42,430))
	pygame.display.flip()
	
	# Debug code
	print("Monster HPs after player attack:")
	for monster in battle_monsters:
		print(monster.name + " HP:", monster.hp)
	print()
	
	# Set location of blinking cursor
	text_x_pos = 30 + (len(damage_text) * 16)
	text_y_pos = 430
	
	
# Enemy monster attacks player during battle
def monster_attack(monster):
	global text_x_pos
	global text_y_pos
	
	# Enemy monster chooses random target to attack
	monster_target = \
		living_party_members\
			[random.randint(0, len(living_party_members) - 1)]
	
	clear_battle_screen()
	
	# Display attack text
	monster_attack_text_1 = text_font.render\
		(monster.name + " attacks!", True, WHITE)
	monster_attack_sound.play()
	screen.blit(monster_attack_text_1,(42,380))
	pygame.display.flip()
	
	# Play monster attack animation
	for i in range(2):
		for image in monster.attack_images:
			screen.blit(image, monster.img_coords)
			pygame.display.flip()
			pygame.time.delay(75)
	screen.blit(monster.attack_images[0], monster.img_coords)
	pygame.display.flip()
	
	pygame.time.delay(200)
	
	# Shake screen and play damage sound
	take_damage_sound.play()
	screen.blit(black_screen, (0,0))
	screen.blit(battle_frame, (-2,2))
	screen.blit(ui_box_1, (-2,2))
	screen.blit(text_box, (-2,354))
	screen.blit(monster_attack_text_1,(40,382))
	print_stats(-2, 2)
	for monster in battle_monsters:
		screen.blit(monster.img, \
			(monster.img_coords[0] - 2, monster.img_coords[1] + 2))
	
	pygame.display.flip()
	pygame.time.delay(50)
	screen.blit(black_screen, (-2,2))
	screen.blit(battle_frame, (2,2))
	screen.blit(ui_box_1, (2,2))
	screen.blit(text_box, (2,354))
	screen.blit(monster_attack_text_1,(44,382))
	print_stats(2, 2)
	for monster in battle_monsters:
		screen.blit(monster.img, \
		(monster.img_coords[0] + 2, monster.img_coords[1] + 2))
	
	pygame.display.flip()
	pygame.time.delay(50)
	screen.blit(black_screen, (2,2))
	screen.blit(battle_frame, (2,-2))
	screen.blit(ui_box_1, (2,-2))
	screen.blit(text_box, (2,350))
	screen.blit(monster_attack_text_1,(44,378))
	print_stats(2, -2)
	for monster in battle_monsters:
		screen.blit(monster.img, \
			(monster.img_coords[0] + 2, monster.img_coords[1] - 2))
	
	pygame.display.flip()
	pygame.time.delay(50)
	screen.blit(black_screen, (2,-2))
	screen.blit(battle_frame, (-2,-2))
	screen.blit(ui_box_1, (-2,-2))
	screen.blit(text_box, (-2,350))
	screen.blit(monster_attack_text_1,(40,378))
	print_stats(-2, -2)
	for monster in battle_monsters:
		screen.blit(monster.img, \
			(monster.img_coords[0] - 2, monster.img_coords[1] - 2))
	
	pygame.display.flip()
	pygame.time.delay(50)
	screen.blit(black_screen, (-2,-2))
	screen.blit(battle_frame, (0,0))
	screen.blit(ui_box_1, (0,0))
	screen.blit(text_box, (0,352))
	screen.blit(monster_attack_text_1,(42,380))
	print_stats(0, 0)
	
	for monster in battle_monsters:
		screen.blit(monster.img, monster.img_coords)
	pygame.display.flip()
		
	# Generate damage monster deals to player
	monster_damage = \
		random.randint(monster.attack_low,monster.attack_high)
	if monster_target.is_guarding == True:
		monster_damage = round(monster_damage / 2)
		if monster_damage <= 0:
			monster_damage = 1
	
	# Display damage-dealt text
	monster_attack_text_2 = text_font.render\
		(monster_target.name + " takes: ", True, WHITE)
	screen.blit(monster_attack_text_2,(42,405))
	pygame.display.flip()
	pygame.time.delay(500)
	damage_text = str(monster_damage) + " damage!"
	monster_damage_text = text_font.render(damage_text, True, WHITE)
	screen.blit(monster_damage_text,(42,430))
	pygame.display.flip()
	
	# Set location of blinking cursor
	text_x_pos = 30 + (len(damage_text) * 16)
	text_y_pos = 430
	
	pygame.time.delay(500)
	screen.blit(text_box,(0,352))
	pygame.display.flip()
	
	# Deal damage to player
	monster_target.hp -= monster_damage
	if monster_target.hp <= 0:
			monster_target.hp = 0
			
	screen.blit(ui_box_1,(0,0))
	print_stats(0, 0)
	

# Print stats (HP, Gold, items, etc) to UI windows. Used during Battle.
# X and Y offsets are used for screen shake effect.
def print_stats(x_offset, y_offset):
	screen.blit(ui_box_erase, (0,0))
	screen.blit(ui_box_1, (0,0))
	
	for i in range(len(party_members_ordered)):
		player_name_text = small_font.render\
			(" " + party_members_ordered[i].name.upper(), True, WHITE)
		screen.blit(player_name_text,\
			((x_offset +  16 + ((128 * (i))), y_offset + 24)))
			
		hp_text = small_font.render\
			(" HP:" + str(party_members_ordered[i].hp), True, WHITE)
		screen.blit(hp_text,\
			((x_offset +  16 + ((128 * (i))), y_offset + 48)))
			
		sp_text = small_font.render\
			(" SP:" + str(party_members_ordered[i].sp), True, WHITE)
		screen.blit(sp_text,\
			((x_offset +  16 + ((128 * (i))), y_offset + 72)))
			
		level_text = small_font.render\
			(" LV:" + str(party_members_ordered[i].level), True, WHITE)
		screen.blit(level_text,\
			((x_offset +  16 + ((128 * (i))), y_offset + 96)))
			
#	pygame.display.flip()


# Level up player
def level_up(player):
	hp_up = random.randint(2,4)
	attack_up = random.randint(1,2)
	player.max_hp += hp_up
	player.damage_low += attack_up
	player.damage_high += attack_up
	player.level += 1
	# Generate levelup messages
	levelup_message = player.name + \
		" reached Level " + str(player.level) + "!*"
	HP_up_message = player.name + \
		"'s Max HP increased by", str(hp_up) + "!"
	attack_up_message = player.name + \
		"'s Attack increased by", str(attack_up) + "!"
	# Display levelup messages
	scroll_text(levelup_message, False, None, False)
	scroll_text(HP_up_message, False, None, False)
	scroll_text(attack_up_message, False, None, False)


# Player chooses to fight or run at start of battle
def fight_or_run():
	global active_party_member
	
	# Start with first party member
	active_party_member = 0
	
	# Display background
	screen.blit(text_box_barred,(0,352))
	screen.blit(empty_frame,(176, 320))
	screen.blit(fight_text,(215, 360))
	screen.blit(run_text,(215, 410))
	pygame.display.flip()
	
	# Call cursor_system for player interaction
	fight_or_run_choice = cursor_system(195, 362, 1, 2, 0, 50)
	
	# Reset Guard status and attack target for each party member
	for party_member in party_members_ordered:
		party_member.is_guarding = False
		party_member.attack_target = None
	
	# Return player choice to battle_manager
	if fight_or_run_choice == 'BACK':
		print('BACK found')
	return fight_or_run_choice


# Player chooses to run from battle
def run_away():
	clear_battle_screen()
	
	# Show run away text
	run_away_text = "Scrambled to safety!"
	run_away_display_text = \
		text_font.render(run_away_text, True, WHITE)
	screen.blit(text_box, (0,352))
	screen.blit(run_away_display_text, (42, 380))
	pygame.display.flip()
	pygame.time.delay(1500)
	screen.blit(black_screen, (0,0))
	pygame.display.flip()
	footsteps_sound.play()
	pygame.time.delay(500)	


# Let currently-active party member select an action while in battle
def battle_cursor():
	global cursor_pos_x
	global current_location
	global active_party_member
	global fight_or_run_choice
	
	# Display battle UI
	screen.blit(text_box,(0,352))
	
	screen.blit(attack_text, (42,380))
	screen.blit(item_text, (382,380))
	screen.blit(spell_text, (42, 430))
	screen.blit(guard_text, (382, 430))
	
	screen.blit(living_party_members\
		[active_party_member].portrait, (176, 320))
	pygame.display.flip()
	
	
	battle_cursor_choice = cursor_system(20, 382, 2, 2, 340, 50)
	
	# Player chooses to attack
	if battle_cursor_choice == (0, 0):
		attack_cursor('Attack')

	# Player chooses to use an Item
	elif battle_cursor_choice == (1, 0):
		item_cursor(living_party_members[active_party_member])
		
	# Player chooses to cast a Spell
	elif battle_cursor_choice == (0, -1):
		spell_sort(living_party_members[active_party_member])
		if spell_cursor(living_party_members[active_party_member]) \
			!= 'BACK':
				attack_cursor('Spell')
		else:
			clear_battle_screen()
		
	# Player chooses to Guard (defend)
	elif battle_cursor_choice == (1, -1):
		living_party_members[active_party_member].next_action = 'Guard'
		
	# Player hits the Back button
	elif battle_cursor_choice == 'BACK':
		print('Going back?')
		fight_or_run_choice = 'BACK'
		active_party_member -= 2
		

# Player chooses which item to use
def item_cursor(item_user):
	screen.blit(item_frame_battle, (0, 320))
	
	# Display list of available items
	item_display_x = 32
	item_display_y = 350
	
#	for item in item_user.inventory:
#		item_display_name = text_font.render(item.name, True, WHITE)
#		screen.blit(item_display_name, (item_display_x, item_display_y)
#		item_display_y += 30
	
	pygame.display.flip()
	get_enter()
		
		
# Sort party member's spells into two lists - column A and column B
def spell_sort(spell_caster):
	global spell_list_A
	global spell_list_B
	
	spell_index = 0
	spell_list_A = []
	spell_list_B = []
	
	for spell in spell_caster.spell_list:
		# Sort every other spell name into alternating columns
		if spell_index == 0:
			spell_list_A.append(spell)
		elif spell_index % 2 != 0:
			spell_list_B.append(spell)
		elif spell_index % 2 == 0:
			spell_list_A.append(spell)	
			
		spell_index += 1
		

# Player chooses which spell to cast		
def spell_cursor(spell_caster):	
	global spell_list_A
	global spell_list_B
	global active_party_member
	
	# Display list of available spells
	screen.blit(spell_frame_battle, (176, 320))
	
	spell_display_x = 226
	spell_display_y = 350
	
	for i in range(len(spell_caster.spell_list)):
		
		# Display spell name from column A
		try:
			spell_display_name = \
				text_font.render(spell_list_A[i], True, WHITE)
		
		except IndexError:
			break
			
		screen.blit(spell_display_name,(spell_display_x,spell_display_y))
		spell_display_x += 144
		
		# Display spell name from column B
		try:
			spell_display_name = \
				text_font.render(spell_list_B[i], True, WHITE)
				
		except IndexError:
			break
			
		screen.blit(spell_display_name,(spell_display_x,spell_display_y))
		spell_display_x -= 144
		spell_display_y += 30		
			
	# Let player choose a spell
	spell_choice_index = cursor_system(204, 350, 2, 4, 144, 30)
	
	# Go back to battle cursor menu
	if spell_choice_index == 'BACK':
		print('Spell selection canceled.')
		active_party_member -= 1
		return('BACK')
		
	else:
		# Fetch chosen spell from master spell dictionary
		if spell_choice_index[0] == 1:
			spell_choice = \
				master_spell_dict[spell_list_B[abs(spell_choice_index[1])]]
			
		elif spell_choice_index[0] == 0:
			spell_choice = \
				master_spell_dict[spell_list_A[abs(spell_choice_index[1])]]
	
		# Assign spell casting action, and chosen spell, to party member
		spell_caster.next_action = 'Spell'	
		spell_caster.spell_choice = spell_choice
	
	# Erase spell menu
	screen.blit(spell_frame_battle_erase, (176, 320))
	screen.blit(battle_frame, (0,0))
	screen.blit(ui_box_1, (0,0))
	print_stats(0,0)
	screen.blit(text_box, (0,352))
	pygame.display.flip()
		
		
# Player chooses which monster to attack
def attack_cursor(attack_type):
	global battle_monsters
	global active_party_member
	
	# Call variable cursor system in 'attack' mode
	target = variable_cursor_system \
		(attack_cursor_x_locations, attack_cursor_y_locations, 'attack')
		
	if target == 'BACK':
		active_party_member -= 1
		return
	
	# Assign party member's target to attack
	if attack_type == 'Attack':
		living_party_members[active_party_member].attack_target = \
		battle_monsters[target[0]]
		
		living_party_members[active_party_member].next_action = 'Attack'
	
	# Assign party member's spell target	
	elif attack_type == 'Spell':
		living_party_members[active_party_member].spell_target = \
		battle_monsters[target[0]]
	
	
# Require player to press Enter to proceed
def get_enter():
	global text_x_pos
	global text_y_pos
	
	pygame.time.delay(250)
	screen.blit(cursor,(text_x_pos,text_y_pos))
	pygame.display.flip()
	enter_prompt = 'on'
	while enter_prompt == 'on':
		# Blink cursor
		if world_anim_state == 0:
			screen.blit(blank_cursor,(text_x_pos,text_y_pos))
		if world_anim_state == 1:
			screen.blit(cursor,(text_x_pos,text_y_pos))
		pygame.display.flip()
		
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					reset_text_coords()
					enter_prompt = 'off'
					pygame.display.flip()
					
			# Close game window
			if event.type == pygame.QUIT:
				sys.exit()
				

# Run in background via thread, toggle animation states				
def idle_animations():
	global sprite_anim_state
	global world_anim_state
	global facing_anim_state
	global toggle_state
	
	toggle_state = 0
	
	while True:
		facing_anim_state = 0
		world_anim_state = 0
		time.sleep(.250)
		time.sleep(.250)
		sprite_anim_state = 1
		time.sleep(.250)
		time.sleep(.250)
		sprite_anim_state = 0
		facing_anim_state = 1
		world_anim_state = 1
		time.sleep(.250)
		time.sleep(.250)
		sprite_anim_state = 1
		time.sleep(.250)
		time.sleep(.250)
		sprite_anim_state = 0
		
		if toggle_state == 0:
			toggle_state = 1
		elif toggle_state == 1:
			toggle_state = 0


# Overworld system
def overworld():
	global world_x
	global world_y
	global world_map
	global player_pose
	global sprite_anim_state
	global world_anim_state
	global toggle_state
	global battle_step_counter
	global current_map
	global current_zone
	global current_entities
	global current_walls
	global walk_frames
	
	# Play overworld music
	# pygame.mixer.music.load\
	#	("Assets/Exports/Music/Goblin Hero - Overworld.wav")
	# pygame.mixer.music.play(-1)
	
	while True:
		# Toggle overworld animations - flowers, etc
		if toggle_state == 0 and world_anim_state == 0:
			world_map = current_level.image_1
		if toggle_state == 0 and world_anim_state == 1:
			world_map = current_level.image_2
		if toggle_state == 1 and world_anim_state == 0:
			world_map = current_level.image_3
		if toggle_state == 1 and world_anim_state == 1:
			world_map = current_level.image_4

		# Display world
		screen.blit(world_map,(world_x,world_y))
		
		# Display entity idle sprites
		for entity in current_entities:
			if entity.type == 'Player' or entity.type == 'NPC':
				entity.current_image = \
					entity.current_idle_images[sprite_anim_state]
				
				# Given NPCs face random directions while idling
				if (entity.type == 'NPC') and \
					(entity.does_idle == True):
					if facing_anim_state == 0:
							entity.has_done_idle = False
					if facing_anim_state == 1:
						if entity.has_done_idle == False:
							random_facing = random.randint(0,3)
							entity.current_idle_images = \
								entity.idle_directions[random_facing]
							entity.has_done_idle = True
			
		update_screen()
		
		# Play idle animations while standing still
		player.current_image = \
			player.current_idle_images[sprite_anim_state]
		screen.blit(player.current_image,(224,224))
		
		pygame.display.flip()
		
		events = pygame.event.get()
		for event in events:
		# Close game window
			if event.type == pygame.QUIT:
				sys.exit()
		
		key = pygame.key.get_pressed()
		
		# Walk left
		if key[pygame.K_LEFT] or key[pygame.K_a]:
			player.current_facing = 'Left'
			player.current_waking_images = player.left_walks
			player.current_idle_images = player.left_idles
			if entity_collision_check(player.current_facing) != True:
				player.current_walking_images = player.left_walks
				# Call walk function to scroll world to the right
				walk(2,0)
				
		# Walk right
		elif key[pygame.K_RIGHT] or key[pygame.K_d]:
			player.current_facing = 'Right'
			player.current_waking_images = player.right_walks
			player.current_idle_images = player.right_idles
			if entity_collision_check(player.current_facing) != True:
				player.current_walking_images = player.right_walks
				# Call walk function to scroll world to the left
				walk(-2,0)
				
		# Walk up
		elif key[pygame.K_UP] or key[pygame.K_w]:
			player.current_facing = 'Back'
			player.current_waking_images = player.back_walks
			player.current_idle_images = player.back_idles
			if entity_collision_check(player.current_facing) != True:
				player.current_walking_images = player.back_walks
				# Call walk function to scroll world down
				walk(0,2)
				
		# Walk down
		elif key[pygame.K_DOWN] or key[pygame.K_s]:
			player.current_facing = 'Front'
			player.current_waking_images = player.front_walks
			player.current_idle_images = player.front_idles
			if entity_collision_check(player.current_facing) != True:
				player.current_walking_images = player.front_walks
				# Call walk function to scroll world up
				walk(0,-2)
				
		# Open command / start / space menu
		elif key[pygame.K_SPACE]:
			# Play open-menu sound
			open_start_menu_sound.play()
			# Display command menu UI
			screen.blit(command_menu_frame,(40,40))
			screen.blit(gear_menu_text, (90, 68))
			screen.blit(magic_menu_text, (90, 108))
			screen.blit(system_menu_text, (90, 148))
			screen.blit(map_menu_text, (250, 68))
			screen.blit(stats_menu_text, (250, 108))
			screen.blit(exit_menu_text, (250, 148))
			# Activate command menu cursor
			command_choice = cursor_system(64, 68, 2, 3, 160, 40)
			if command_choice == ('BACK' or (1, -2)):
				overworld()
			
			
		# Check for adjacent NPC to talk to / object to interact with.
		elif key[pygame.K_RETURN]:
			for entity in current_entities:
				if player.current_facing == 'Right' and \
					(entity.position_x, entity.position_y) == \
						(player_x + 32, player_y):
							if entity.type == 'NPC':
								entity.current_idle_images = entity.left_idles
								entity.current_image = entity.left_idles[0]
								npc_talk(entity)
							elif entity.type == 'Chest':
									open_chest(entity, player)
							elif entity.type == 'Door':
								entity.open(player)
							elif entity.type == 'Shop Counter':
								shop(entity)
							elif entity.type == 'Heal Point':
								use_heal_point()
				elif player.current_facing == 'Back' and \
					(entity.position_x, entity.position_y) == \
						(player_x, player_y - 32):
							if entity.type == 'NPC':
								entity.current_idle_images = entity.front_idles
								entity.current_image = entity.front_idles[0]
								npc_talk(entity)
							elif entity.type == 'Chest':
								open_chest(entity, player)
							elif entity.type == 'Door':
								entity.open(player)
							elif entity.type == 'Shop Counter':
								shop(entity)
							elif entity.type == 'Heal Point':
								use_heal_point()
				elif player.current_facing == 'Left' and \
					(entity.position_x, entity.position_y) == \
						(player_x - 32, player_y):
							if entity.type == 'NPC':
								entity.current_idle_images = entity.right_idles
								entity.current_image = entity.right_idles[0]
								npc_talk(entity)
							elif entity.type == 'Chest':
								open_chest(entity, player)
							elif entity.type == 'Door':
								entity.open(player)
							elif entity.type == 'Shop Counter':
								shop(entity)
							elif entity.type == 'Heal Point':
								use_heal_point()
				elif player.current_facing == 'Front' and \
					(entity.position_x, entity.position_y) == \
						(player_x, player_y + 32):
							if entity.type == 'NPC':
								entity.current_idle_images = entity.back_idles
								entity.current_image = entity.back_idles[0]	
								npc_talk(entity)
							elif entity.type == 'Chest':
								open_chest(entity, player)
							elif entity.type == 'Door':
								entity.open(player)
							elif entity.type == 'Shop Counter':
								shop(entity)
							elif entity.type == 'Heal Point':
								use_heal_point()
								
		clock.tick(FPS)
	

# Check if player will collide with an adjacent entity or wall.
def entity_collision_check(facing):
	# Check for collision with current level's entities.
	for entity in current_entities:
		if facing == 'Right':
			if (entity.position_x, entity.position_y) == \
					(player_x + 32, player_y):
						if entity.collision == True:
							return True
		elif facing == 'Back':
			if (entity.position_x, entity.position_y) == \
					(player_x, player_y - 32):
						if entity.collision == True:
							return True
		elif facing == 'Left':
			if (entity.position_x, entity.position_y) == \
					(player_x - 32, player_y):
						if entity.collision == True:
							return True
		elif facing == 'Front':
			if (entity.position_x, entity.position_y) == \
					(player_x, player_y + 32):
						if entity.collision == True:
							return True

	# Check for collision with current level's walls / background tiles.
	for wall in current_walls:
		if facing == 'Right':
			# "upper" and "lower" refer to tile's location in-game,
			# not numerical value.
			if (wall.upper_x <= player_x + 32 <= wall.lower_x):
				if (wall.upper_y <= player_y <= wall.lower_y):
					return True
		elif facing == 'Back':
			if (wall.upper_x <= player_x <= wall.lower_x):
				if (wall.upper_y <= player_y - 32 <= wall.lower_y):
					return True
		elif facing == 'Left':
			if (wall.upper_x <= player_x - 32 <= wall.lower_x):
				if (wall.upper_y <= player_y <= wall.lower_y):
					return True
		elif facing == 'Front':
			if (wall.upper_x <= player_x <= wall.lower_x):
				if (wall.upper_y <= player_y + 32 <= wall.lower_y):
					return True
			
# NPC talks to Player
def npc_talk(entity):
	screen.blit(entity.current_image, \
		(entity.position_x, entity.position_y))
	pygame.display.flip()
	# Check if NPC has portrait or not
	if entity.NPC_type == 'Minor NPC':
		scroll_text(entity.dialogues[entity.talk_counter], \
			True, entity, False)
	elif entity.NPC_type == 'Major NPC':
		scroll_text(entity.dialogues[entity.talk_counter], \
			True, entity, True)
	if entity.talk_counter != entity.max_talk_counter:
		entity.talk_counter += 1
	pygame.time.delay(300)
	
		
# Scroll the world and objects when the player walks
def walk(x_scroll, y_scroll):
	global world_x
	global world_y
	global world_map
	global battle_step_counter
	global walk_frames
	global steps_taken_into_level
	global current_entities
	
	for i in [2, 1, 0]:
		# Each party member assumes the facing of the one in front of them
		party_members[i].next_facing = party_members[i + 1].current_facing
		
		# Update party member walking and idle animations
		party_members[i].current_idle_images = \
			party_members[i].idles[party_members[i].current_facing]
		party_members[i].current_walking_images = \
			party_members[i].walks[party_members[i].current_facing]
		
		party_members[i].current_image = \
			party_members[i].current_walking_images[sprite_anim_state]
			
	for i in range(0,16):
		# Scroll and display the background image / world
		world_x += x_scroll
		world_y += y_scroll
		screen.blit(world_map,(world_x,world_y))
		
		# Party member sprites follow player sprite
		for i in [2, 1, 0]:
			if party_members[i].current_facing != \
				party_members[3].current_facing:
					party_members[i].position_x += x_scroll
					party_members[i].position_y += y_scroll
					if party_members[i].current_facing == 'Front':
						party_members[i].position_y += 2
					elif party_members[i].current_facing == 'Back':
						party_members[i].position_y -= 2
					elif party_members[i].current_facing == 'Left':
						party_members[i].position_x -= 2
					elif party_members[i].current_facing == 'Right':
						party_members[i].position_x += 2
				
		# Scroll and display sprites
		for entity in current_entities:
			if entity.type != 'Player':
				entity.position_x += x_scroll
				entity.position_y += y_scroll
			
			if entity.render_type == True:
				if (entity.race == 'Troll') or \
					(entity.type == 'Heal Point'):
						screen.blit(entity.current_image,\
							(entity.position_x,entity.position_y - 32))
				else:
					screen.blit(entity.current_image,\
						(entity.position_x,entity.position_y))
		
		for wall in current_walls:
			wall.upper_x += x_scroll
			wall.upper_y += y_scroll
			wall.lower_x += x_scroll
			wall.lower_y += y_scroll
					
		# Display player sprite
		player.current_image = \
			player.current_walking_images[sprite_anim_state]
		screen.blit(player.current_image,(224,224))
		pygame.display.flip()
		clock.tick(FPS)
				
	for i in [0, 1, 2]:
		party_members[i].current_facing = party_members[i].next_facing
	
	# Add non-player party members to current level as player walks in
	if steps_taken_into_level <= 2:	
		current_level.entities.append \
			(non_player_party_members[steps_taken_into_level])
		current_entities = current_level.entities
		steps_taken_into_level += 1
	
	# print("World X =", world_x, " World Y =", world_y)
	check_map_location()
	# print("Current zone:", current_zone)
	
	# Check for random battle
	if current_zone != 'Safe':
		battle_step_counter += 1
		battle_check()

	# Check if player is on stairs or other portals	
	for entity in current_entities:
		if (entity.position_x, entity.position_y) == \
			(player_x, player_y):
				if entity.type == 'Portal':
					teleport(entity)
				if entity.type == 'Conversation':
					play_conversation(entity)
						

# Universal menu cursor with customizable dimensions & step sizes
# Returns simplified cursor coordinates on termination
def cursor_system(cursor_starting_x, cursor_starting_y, \
	total_columns, total_rows, \
	step_distance_x, step_distance_y):
		
		frame_counter = 0
		
		# Assign cursor starting position 
		cursor_x_pos = cursor_starting_x
		cursor_y_pos = cursor_starting_y
		
		# Initialize output value as (0,0)
		cursor_output_pos_x = 0
		cursor_output_pos_y = 0
		
		# Draw cursor at starting position
		screen.blit(cursor, (cursor_x_pos,cursor_y_pos))
		pygame.display.flip()
		
		# Move cursor according to player input
		while True:
			events = pygame.event.get()
			for event in events:
			
				if event.type == pygame.KEYDOWN:
					
					frame_counter = 0
					
					# Erase cursor at current location
					screen.blit(blank_cursor, \
					(cursor_x_pos,cursor_y_pos))
				
					# Move cursor left
					if event.key == pygame.K_LEFT and \
						cursor_x_pos - step_distance_x >= \
						cursor_starting_x:
							cursor_x_pos -= step_distance_x
							cursor_output_pos_x -= 1
						
					# Move cursor right
					if event.key == pygame.K_RIGHT and \
						(cursor_x_pos + step_distance_x) <= \
						(cursor_starting_x + \
						((total_columns - 1) * step_distance_x)):
							cursor_x_pos += step_distance_x
							cursor_output_pos_x += 1
						
					# Move cursor down
					if event.key == pygame.K_DOWN and \
						(cursor_y_pos + step_distance_y) <= \
						(cursor_starting_y + \
						((total_rows - 1) * step_distance_y)):
							cursor_y_pos += step_distance_y
							cursor_output_pos_y -= 1
						
					# Move cursor up
					if event.key == pygame.K_UP and \
						cursor_y_pos - step_distance_y >= \
						cursor_starting_y:
							cursor_y_pos -= step_distance_y
							cursor_output_pos_y += 1
				
					# Draw cursor at new position
					screen.blit(cursor, (cursor_x_pos,cursor_y_pos))
				
					# Update display
					pygame.display.flip()
					
					# Return simplified cursor position as output
					if event.key == pygame.K_RETURN:
						return(cursor_output_pos_x, cursor_output_pos_y)
						
					if event.key == pygame.K_BACKSPACE:
						return('BACK')
			
			frame_counter += 1
			if frame_counter == 30:
				screen.blit(blank_cursor,(cursor_x_pos,cursor_y_pos))
				
			if frame_counter == 60:
				screen.blit(cursor,(cursor_x_pos,cursor_y_pos))
				frame_counter = 0
				
			pygame.display.flip()
			clock.tick(FPS)
						
	
# Cursor system with variable step sizes
# Lists must be same length. Repeated entries are okay
def variable_cursor_system\
	(x_coordinate_list, y_coordinate_list, cursor_type):
		
	frame_counter = 0
		
	# Initialize cursor location
	cursor_x_index = 0
	cursor_y_index = 0
	cursor_location = \
		(x_coordinate_list[cursor_x_index], \
		y_coordinate_list[cursor_y_index])
	if cursor_type == 'attack':
		screen.blit(attack_cursor_img, (cursor_location))
		pygame.display.flip()
	else:	
		screen.blit(cursor, (cursor_location))
		pygame.display.flip()
	
	# If 'attack cursor' type, display first monster's name
	if cursor_type == 'attack':
		screen.blit(monster_display_names\
			[cursor_x_index], (75,150))
		pygame.display.flip()
	
	# Move cursor according to player input
	shine_char_index = 0
	
	while True:
		events = pygame.event.get()
		for event in events:
		
			if event.type == pygame.KEYDOWN:
				frame_counter = 0
				shine_char_index = 0
				
				# Erase cursor at current location
				screen.blit(attack_cursor_blank, \
				(cursor_location))
				
				# If 'attack cursor' type, erase previous monster name
				if cursor_type == 'attack':
					screen.blit(monster_erase_names\
						[cursor_x_index], (75,150))
				
				# Cancel target selection
				if event.key == pygame.K_BACKSPACE:
					return('BACK')
				
				# Try to move cursor left
				elif event.key == pygame.K_LEFT and cursor_x_index > 0:
					cursor_x_index -= 1
				
				# Try to move cursor right
				elif event.key == pygame.K_RIGHT and cursor_x_index < \
					(len(x_coordinate_list) - 1):
						cursor_x_index += 1
				
				# Try to move cursor up
				elif event.key == pygame.K_UP and cursor_y_index < \
					(len(y_coordinate_list) - 1):
						cursor_y_index += 1
						
				# Try to move cursor down
				elif event.key == pygame.K_DOWN and cursor_y_index > 0:
					cursor_y_index -= 1
				
				# Update cusor location
				cursor_location = \
					(x_coordinate_list[cursor_x_index], \
					y_coordinate_list[cursor_y_index])
				screen.blit(attack_cursor_img, (cursor_location))
				
				# If 'attack cursor' type, display current monster name
				if cursor_type == 'attack':
					screen.blit(monster_display_names\
						[cursor_x_index], (75,150))
				pygame.display.flip()
				
				# Return player's selection
				if event.key == pygame.K_RETURN:
					if cursor_type == 'attack':
						screen.blit(monster_erase_names\
							[cursor_x_index], (75,150))
						screen.blit(attack_cursor_blank, cursor_location)
					return (cursor_x_index, cursor_y_index)
		
		frame_counter += 1
		
		# Play shining name and blinking cursor animtions at right time:
		
		# Blink attack cursor at appropriate location
		if frame_counter in [60, 120, 180, 240]:
			screen.blit(attack_cursor_img, cursor_location)
			
			# Move enemy monster sprites up and down
			for monster in battle_monsters:
				screen.blit(black_monster_square, monster.img_coords)
				
				if monster.img_coords[1] == 180:
					monster.img_coords = \
						(monster.img_coords[0], \
							monster.img_coords[1] + 4)
				else:
					monster.img_coords = \
						(monster.img_coords[0], \
							monster.img_coords[1] - 4)
							
				screen.blit(monster.img, monster.img_coords)
			
		if frame_counter in [30, 90, 150, 210]:
			screen.blit(attack_cursor_blank, cursor_location)
		
		# Reset frame counter responsible for looping animations	
		if frame_counter == 240:
			screen.blit(attack_cursor_img, cursor_location)
			frame_counter = 0
		
		# Shine enemy monster name
		if (frame_counter == shine_char_index * 3) and \
			(shine_char_index <= len(monster_shine_names[cursor_x_index])):
				screen.blit\
					(monster_erase_names[cursor_x_index], (75,150))
				screen.blit\
					(monster_display_names[cursor_x_index], (75, 150))
				screen.blit(monster_shine_names[cursor_x_index][shine_char_index], (75, 150))
				shine_char_index += 1
		
		# Reset varaible used to increment through name shine images
		if shine_char_index == \
			len(monster_shine_names[cursor_x_index]):
				shine_char_index = 0

		# Display normal enemy name after shine is completed
		if frame_counter == \
			((len(monster_shine_names[cursor_x_index]) * 3) + 3):
				screen.blit\
					(monster_display_names[cursor_x_index], (75,150))
				
		pygame.display.flip()
		clock.tick(FPS)

# Check if player should enter random battle
def battle_check():
	global battle_step_counter
	if battle_step_counter >= 8:
		battle_chance = random.randint(0,16)
		if battle_chance == 1:
			battle_manager()
	if battle_step_counter >= 16:
		battle_manager()
		

### SCROLLING TEXT SYSTEM ###

# Blit the next word in a string to the screen, one character at once.
def scroll_next_word():
	global total_chars
	global text_x_pos
	global text_y_pos
	
	for char in next_word:
		next_character = text_font.render(char, True, WHITE)
		text_x_pos = 20 + (total_chars * 16)
		screen.blit(next_character,(text_x_pos,text_y_pos))
		pygame.display.flip()
		pygame.time.delay(25)
		total_chars += 1


# Play appropriate-length sound file based on length of text message.
def play_dialogue_sound():
	global text_for_sound
	global text_phrase
	# Cut off chunks from front of test_for_sound smaller than 4 lines
	# at a time. Use these to play appropriate sound file.
	
	# Copy text from text_for_sound to next_page
	if len(text_for_sound) >= 108:
		next_page = text_for_sound[0:108]
	else:
		next_page = text_for_sound[0:]
		
	# Remove copied text from text_for_sound
	if len(text_for_sound) - len(next_page) < 108:
		text_for_sound = text_for_sound[len(next_page):]
	else:
		text_for_sound = \
			text_for_sound[len(next_page):len(next_page) + 108]
	
	if text_for_sound == next_page:
		text_for_sound = ""
	
	# Play appropriate-length audio clip based on length of next page.
	if len(next_page) <= 27:
		speech_8_sound.play()
		print("Playing speech_8")
	if 27 < len(next_page) <= 54:
		speech_16_sound.play()
		print("Playing speech_16")
	if 54 < len(next_page) <= 81:
		speech_24_sound.play()
		print("Playing speech_24")
	if len(next_page) > 81:
		speech_32_sound.play()
		print("Playing speech_32")


# Line break or page break, if appropriate.
def check_line_length():
	global total_chars
	global text_x_pos
	global text_y_pos
	global current_text_row
	
	# If text is about to reach the end of a line...
	if (total_chars + len(next_word)) >= 26:
			# If text has reached end of fourth row, clear box
			# and return to top of text box.
			if current_text_row == 4:
				text_x_pos += 20
				get_enter()
				screen.blit(text_box,(0,352))
				total_chars = 0
				text_y_pos = 380
				current_text_row = 1
				play_dialogue_sound()
			# Otherwise, go to start of next row down.
			else:
				total_chars = 0
				total_chars = 0
				text_y_pos += 20
				current_text_row += 1
		
		
# Main scrolling text system
def scroll_text(text_phrase, is_dialogue, speaker, use_portrait):
	global text_for_sound
	global next_word
	global total_chars
	global current_text_row
	global text_x_pos
	global text_y_pos
	
	# Display text box and, if necessary, speaker portrait
	if use_portrait == True:
		screen.blit(speaker.portrait,(0,206))
	screen.blit(text_box,(0,352))
	pygame.display.flip()
	
	reset_text_coords()
	
	# Make two copies of text_phrase - one for text, and one for sound.
	text_to_print = text_phrase[:]
	text_for_sound = text_phrase[:]

	# If text to display is dialogue, play sound and display speaker's
	# name, then go to the next line down.
	if is_dialogue == True:
		play_dialogue_sound()
		next_word = speaker.name + ":"
		scroll_next_word()
		total_chars = 26
		check_line_length()

	while " " in text_to_print:
		# Slice the first word off of text_to_print.
		space_pos = text_to_print.index(" ")
		next_word = " " + text_to_print[0:space_pos]
		check_line_length()
		scroll_next_word()
		text_to_print = text_to_print[space_pos + 1:]

	# Scroll final word in the string.
	check_line_length()
	next_word = " " + text_to_print
	scroll_next_word()
	text_to_print = ""
	
	# Display cursor at end of text, wait for player input.
	text_x_pos += 20
	get_enter()
	
	# Reset text coordinates
	total_chars = 0
	text_x_pos = 20
	text_y_pos = 380
	current_text_row = 1
	
	reset_text_coords()
	
	
# Reset text coordinates		
def reset_text_coords():
	global total_chars
	global text_x_pos
	global text_y_pos
	global current_text_row
	
	total_chars = 0
	text_x_pos = 20
	text_y_pos = 380
	current_text_row = 1
	

# Display Yes or No prompt and return player selection
def yes_or_no():
	screen.blit(yes_or_no_prompt, (164,164))
	yes_text = menu_font.render('YES', True, WHITE)
	no_text = menu_font.render('NO', True, WHITE)
	screen.blit(yes_text, (218, 200))
	screen.blit(no_text, (218, 240))
	pygame.display.flip()
	
	# If player hits back button, repeat prompt
	player_selection = 'BACK'
	while player_selection == 'BACK':
		player_selection = cursor_system(192, 200, 1, 2, 0, 40)

	return(player_selection)
	

# Start Prototype title screen
def title_screen():
	pygame.mixer.music.set_volume(0.30)
	# pygame.mixer.music.play(-1)
	frame_counter = 0
	pressed_enter = False
	screen.blit(prototype_title_screen_img,(0,0))
	pygame.display.flip()

	prototype_title_screen_header = \
		menu_font.render("GOBLIN HERO", True, GREEN)
	press_enter_text = big_font.render("PRESS ENTER", True, WHITE)
	press_enter_erase_box = pygame.image.load\
		("Assets/Exports/Art/Backgrounds/press_start_erase_box.png")
	
	screen.blit(title_screen_star_img,(75,150))
	screen.blit(title_screen_star_img,(450,300))
	# screen.blit(title_screen_star_img,(,))

	loop_total = 0
	# Wait for player to press Enter
	while pressed_enter == False:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					screen.blit(press_enter_erase_box, (150, 400))
					pygame.display.flip()
					for i in range(25):
						pygame.mixer.music.set_volume(0.25 - (i / 100))
						pygame.time.delay(200)
					pygame.mixer.music.stop()
					pressed_enter = True
			if event.type == pygame.QUIT:
					sys.exit()
					
		# Display animated graphics
		frame_counter += 1
		if frame_counter == 5:
			screen.blit(time_portal_img_1, (430,33))
			pygame.display.flip()
	
		if frame_counter == 10:
			screen.blit(time_portal_img_2, (430,33))
			pygame.display.flip()
		
		if frame_counter == 15:
			screen.blit(time_portal_img_3, (430,33))
			pygame.display.flip()
		
		if frame_counter == 20:
			screen.blit(press_enter_text, (150, 415))
			screen.blit(time_portal_img_4, (430,33))			
			pygame.display.flip()
				
		if frame_counter == 25:
			screen.blit(time_portal_img_1, (430,33))
			pygame.display.flip()
		
		if frame_counter == 30:
			screen.blit(time_portal_img_2, (430,33))
			pygame.display.flip()
		
		if frame_counter == 35:
			screen.blit(time_portal_img_3, (430,33))
			pygame.display.flip()
		
		if frame_counter == 40:
			frame_counter = 0
			screen.blit(press_enter_erase_box, (150, 400))
			screen.blit(time_portal_img_4, (430,33))
			if loop_total == 10:
				screen.blit(title_screen_star_blank_img,(75,150))
			if loop_total == 11:
				screen.blit(title_screen_star_img,(75,150))
			if loop_total == 20:
				screen.blit(title_screen_star_blank_img,(450,300))
			if loop_total == 21:
				screen.blit(title_screen_star_img,(450,300))
			if loop_total == 30:
				loop_total = 0
			loop_total += 1
	
			pygame.display.flip()
		clock.tick(FPS)


# Define and begin animation thread
t1 = threading.Thread(target = idle_animations, args = (), \
	daemon = True)
t1.start()
pygame.time.delay(1000)
