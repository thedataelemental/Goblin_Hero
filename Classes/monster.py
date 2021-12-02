# monster.py


# Enemy monsters
class Monster:
	def __init__(self, name, max_hp, attack_low, attack_high, \
		gold, exp, level, attack_images, element, true_name, \
		elemental_type):
		self.name = name
		self.max_hp = max_hp
		self.hp = max_hp
		self.attack_low = attack_low
		self.attack_high = attack_high
		self.gold = gold
		self.exp = exp
		self.level = level
		self.attack_images = attack_images
		self.img = attack_images[0]
		# Element used for name display
		self.element = element
		self.img_coords = (0,0)
		self.true_name = true_name
		# Element used for combat advantage / disadvantage
		self.elemental_type = elemental_type
