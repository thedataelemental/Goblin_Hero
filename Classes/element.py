# element.py

# Elemental type w/ type it's strong against. For spells & creatures
# Advantages are added after intialization
class Element:
	def __init__(self, name):
		self.name = name
		self.advantage = None
		
