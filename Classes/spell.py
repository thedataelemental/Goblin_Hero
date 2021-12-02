# spell.py
# Define spell class for use in Goblin Hero
# Author: Jackie P, aka TheDataElemental

# Spells to be cast by player
# Spell_type = heal, attack, status...
# Value = amount of damage, health, etc
class Spell:
	def __init__(self, name, spell_type, value, animation, mana_cost, \
		element):
		self.name = name
		self.spell_type = spell_type
		self.value = value
		self.animation = animation
		self.mana_cost = mana_cost
		self.element = element
		self.target = None

	# Carry out effects of spell
	def effect(self, target):
		self.target = target
		
		if self.spell_type == 'Heal':
			self.target.hp += self.value
			
		elif self.spell_type == 'Attack':
			# Check for elemental advantage
			if target.elemental_type == self.element.advantage:
				# Deal advantage damage
				damage_dealt = self.value * 2
				self.target.hp -= damage_dealt
			
			# If no advantage, deal standard damage
			else:
				damage_dealt = self.value
				self.target.hp -= damage_dealt	

		return damage_dealt
