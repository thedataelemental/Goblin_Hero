# npc.py


# NPCs
class NPC:
	def __init__(self, position_x, position_y, current_facing, \
		back_idle_1, back_idle_2, right_idle_1, right_idle_2, \
		front_idle_1, front_idle_2, left_idle_1, left_idle_2, \
		dialogue_1, dialogue_2, max_talk_counter, race, NPC_type, \
		portrait, name, does_idle):
		
		self.render_type = True
		self.type = 'NPC'
		self.collision = True
		# Position coordinates
		self.position_x = position_x
		self.position_y = position_y
		
		# Current NPC facing (N, E, S, W = 0, 1, 2, 3)
		self.current_facing = current_facing
		
		# Idle animation frames
		self.back_idles = [back_idle_1, back_idle_2]
		self.right_idles = [right_idle_1, right_idle_2]
		self.front_idles = [front_idle_1, front_idle_2]
		self.left_idles = [left_idle_1, left_idle_2]
		
		self.idle_directions = [self.back_idles, self.right_idles, \
			self.front_idles, self.left_idles]
			
		self.current_idle_images = \
			self.idle_directions[self.current_facing]
			
		# Placeholder starting position image
		self.current_image = self.idle_directions[current_facing][0]
		
		# Walking animation frames
#		self.walking_front_1 = 
#		self.walking_front_2 = 
#		self.walking_right_1 = 
#		self.walking_right_2 = 
#		self.walking_left_1 = 
#		self.walking_left_2 = 
#		self.walking_back_1 = 
#		self_walking_back_2 = 
			
		# Dialogue scripts
		self.dialogues = [dialogue_1, dialogue_2]
		self.talk_counter = 0
		self.max_talk_counter = max_talk_counter
		
		self.race = race
		# NPC type ('Major NPC' (has portrait) or 'Minor NPC')
		self.NPC_type = NPC_type
		self.portrait = portrait
		self.name = name
		self.does_idle = does_idle
		self.has_done_idle = False
