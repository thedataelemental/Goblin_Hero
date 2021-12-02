# level.py


# Levels (towns, dungeons, overworld, floors of dungeons / houses)
class Level:
	def __init__(self, image_1, image_2, image_3, image_4, entities, \
		walls): # + music...
			self.image_1 = image_1
			self.image_2 = image_2
			self.image_3 = image_3
			self.image_4 = image_4
			self.entities = entities
			self.last_entrance = ''
			self.current_entrance = ''
			self.walls = walls
		
