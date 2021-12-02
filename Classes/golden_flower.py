# golden_flower.py


# "Golden Flower" save points found throughout Goblin Hero
class GoldenFlower:
	def __init__(self, position_x, position_y, image,):
		self.position_x = position_x
		self.position_y = position_y
		self.current_image = image
		self.render_type = True
		self.type = 'Heal Point'
		self.collision = True
		self.race = None

