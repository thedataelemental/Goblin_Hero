# conversation.py
# Conversation / party chat between one or more characters


class Conversation:
	def __init__(self, form, position_x, position_y, speaker_list, \
		speech_list):
			self.render_type = False
			self.type = 'Conversation'
			self.race = None
			self.current_image = None
			self.collision = False
			
			self.position_x = position_x
			self.position_y = position_y
			# form defines if the conversation is played after
			# stepping onto a tile or interacting with an object
			# ('Tile' or 'Touch')
			self.form = form
			self.speaker_list = speaker_list
			self.speech_list = speech_list
			self.played = False

