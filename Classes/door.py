# door.py


# Doors. Impassable until opened.
class Door:
	def __init__(self, position_x, position_y, closed_image, \
		open_image):
			self.render_type = True
			self.type = 'Door'
			self.state = 'Closed'
			self.collision = True
			self.position_x = position_x
			self.position_y = position_y
			self.closed_image = closed_image
			self.open_image = open_image
			self.current_image = self.closed_image
			self.race = None
		
	# Open the door.
	def open(self, opener):
		self.state = 'Open'
		self.collision = False
		self.current_image = self.open_image
		
		screen.blit(self.current_image,\
			(self.position_x, self.position_y))
		pygame.display.flip()
