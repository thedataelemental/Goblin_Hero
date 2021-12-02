# player_character.py
# Define class for player Characters / party members
# Author: Jackie P, aka TheDataElemental


import pygame


class PlayerCharacter:
		# Define player stats
		def __init__(self, name, max_hp, max_sp, damage_low, damage_high, \
			exp, level, gold, inventory, position_x, position_y, \
			back_idle_1, back_idle_2, back_1, back_2, \
			front_idle_1, front_idle_2, front_1, front_2, \
			left_idle_1, left_idle_2, left_1, left_2,
			right_idle_1, right_idle_2, right_1, right_2, race, \
			party_position, portrait, ghost_back_1, ghost_back_2, \
			ghost_front_1, ghost_front_2, ghost_left_1, ghost_left_2, \
			ghost_right_1, ghost_right_2, spell_list, element):
				
			self.render_type = True
			self.type = 'Player'
			self.collision = 'False'
			self.name = name
			self.max_hp = max_hp
			self.hp = max_hp
			self.max_sp = max_sp
			self.sp = max_sp
			self.damage_low = damage_low
			self.damage_high = damage_high
			self.exp = exp
			self.level = level
			self.gold = gold
			self.inventory = inventory
			self.pose = ''
			
			self.position_x = position_x
			self.position_y = position_y
			
			# Idling animations
			self.back_idles = [back_idle_1, back_idle_2]
			self.right_idles = [right_idle_1, right_idle_2]
			self.front_idles = [front_idle_1, front_idle_2]
			self.left_idles = [left_idle_1, left_idle_2]
			
			self.living_idles = {'Back': self.back_idles,
				'Right': self.right_idles,
				'Front': self.front_idles,
				'Left': self.left_idles}
						
			# Walking animations
			self.back_walks = [back_1, back_2]
			self.right_walks = [right_1, right_2]
			self.front_walks = [front_1, front_2]
			self.left_walks = [left_1, left_2]
			
			self.living_walks = {'Back': self.back_walks,
				'Right': self.right_walks,
				'Front': self.front_walks,
				'Left': self.left_walks}
			
			# Default to living idle and walking animations
			self.idles = self.living_idles
			self.walks = self.living_walks
			
			# Ghost-form idle / walking animations
			self.ghost_backs = [ghost_back_1, ghost_back_2]
			self.ghost_fronts = [ghost_front_1, ghost_front_2]
			self.ghost_lefts = [ghost_left_1, ghost_left_2]
			self.ghost_rights = [ghost_right_1, ghost_right_2]
			
			self.ghost_forms = {'Back': self.ghost_backs,
				'Right': self.ghost_rights,
				'Front': self.ghost_fronts,
				'Left': self.ghost_lefts}
			
			self.current_facing = 'Back'
			self.next_facing = ''
			self.current_idle_images = self.back_idles
			self.current_walking_images = self.back_walks
			self.current_image = self.front_idles[0]
			
			self.race = race
			self.party_position = party_position
			self.portrait = portrait
			self.spell_list = spell_list
			self.element = element
			is_guarding = False
			attack_target = None
			next_action = None
			spell_choice = None
			spell_target = None
		
		
		# When party member dies, replace overworld sprites w ghost sprites
		# (Ghost idle & walking animations are the same)
		def assume_ghost_form(self):
			self.back_idles = self.ghost_backs
			self.back_walks = self.ghost_backs
			
			self.front_idles = self.ghost_fronts
			self.front_walks = self.ghost_fronts
			
			self.left_idles = self.ghost_lefts
			self.left_walks = self.ghost_lefts
			
			self.right_idles = self.ghost_rights
			self.right_walks = self.ghost_rights
			
			self.current_idle_images = \
				self.ghost_forms[self.current_facing]
			self.current_walking_images = \
				self.ghost_forms[self.current_facing]
				
			self.walks = self.ghost_forms
			self.idles = self.ghost_forms
