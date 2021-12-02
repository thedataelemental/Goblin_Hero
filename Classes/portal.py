# portal.py


# Portals (stairs, town / dungeon entrances / exits, portals)
class Portal:
	def __init__(self, position_x, position_y, image, destination_level, \
		destination_object, set_world_x, set_world_y, portal_exit_facing, \
		destination_zone):
			
			self.render_type = True
			self.type = 'Portal'
			self.collision = 'False'
			self.position_x = position_x
			self.position_y = position_y
			self.image = image
			self.current_image = image
			self.destination_level = destination_level
			self.set_world_x = set_world_x
			self.set_world_y = set_world_y
			self.portal_facing = portal_exit_facing
			self.destination_zone = destination_zone
			self.race = None
	
	# Note on possible problem:
	# Entity position adjustment for multiple-level-entrance problem
	# Give each level a "most recent entrance" attribute and a
	# "current entrance" attribute.
	# (The portal the player last used to enter the level.)
	# if entrance / portal player enters level through is not the level's
	# most recent entrance / portal:
	# Calculate distance (X and Y) between portal player entered level
	# through and level's most recent entrance / portal.
	# Adjust all of level's entities' x and y positions by that distance.
