# wall.py


# Wall objects (non-entity tiles where player can't walk).
# Defined as rectangles with x and y coordinates.
# upper_x and upper_y = x and y coords of top-left tile of wall square.
# lower_x and lower_y = x and y coords of lower-right tile.

# Give Wall position arguments by tile.
# Tile values are converted to coordinates automatically.
# e.g: Center of screen / player sprite is at (7, 7) = (224, 224)
class Wall:
	def __init__(self, upper_x, upper_y, lower_x, lower_y):
		self.upper_x = upper_x * 32
		self.upper_y = upper_y * 32
		self.lower_x = lower_x * 32
		self.lower_y = lower_y * 32
		
