# shopcounter.py


# Shopcounter object (interact with these to access in-game stores)
class ShopCounter:
	def __init__(self, position_x, position_y, owner, inventory, \
		prices, current_image):
			
			self.render_type = True
			self.type = 'Shop Counter'
			self.collision = True
			self.position_x = position_x
			self.position_y = position_y
			self.owner = owner
			# inventory and prices are lists. They correspond to each 
			# other: prices[0] is the price for inventory[0], etc.
			self.inventory = inventory
			self.prices = prices
			self.race = None
			
