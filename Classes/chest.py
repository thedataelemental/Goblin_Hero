# chest.py


# Treasure chests
class Chest:
	def __init__(self, position_x, position_y, \
		closed_image, open_image, contents):
		
		self.position_x = position_x
		self.position_y = position_y
		self.closed_image = closed_image
		self.open_image = open_image
		self.current_image = self.closed_image
		self.contents = contents
		self.race = None
		
		self.render_type = True
		self.type = 'Chest'
		self.state = 'Closed'
		self.collision = True
		
