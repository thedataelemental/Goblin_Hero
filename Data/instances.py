# instances.py
# Create instances for use in Goblin Hero
# Author: Jackie P, aka TheDataElemental


import sys

# Import classes
sys.path.append('C:/Users/elimu/Desktop/Goblin Hero/Classes')
from player_character import *
from spell import *
from element import *
from npc import *
from chest import *
from door import *
from portal import *
# from item import *
from wall import *
from level import *
from shopcounter import *
from monster import *
from conversation import *
from golden_flower import *

# Import data
from data import *

### Create instances ###

# Wall coordinates and wall lists for levels #
test_room_wall_1 = Wall(-96, -64, 576, -32)
test_room_walls = {test_room_wall_1}

# Walls for the demo's House level
prototype_house_walls = \
	{
	# SW wall of house
	Wall(1, -2, 6, -1),
	
	# W side of starting path
	Wall(5, 0, 5, 7),
	
	# E side of starting path
	Wall(9, 0, 9, 7),
	
	# Black border S of start
	Wall(6, 8, 8, 8),
	
	# E side of house door
	Wall(8, -2, 8, -1),
	
	# SE side of house
	Wall(9, -5, 9, -1),
	
	# Wall south of bed
	Wall(9, -5, 13, -5),
	
	# E wall of house
	Wall(13, -10, 13, -5),
	
	# N wall of house
	Wall(1, -10, 13, -9),
	
	# Wall between W and E sides of house
	Wall(5, -9, 5, -7),
	
	# Central wall of house
	Wall(5, -6, 6, -5),
	
	# W wall of house (crates)
	Wall(2, -8, 2, 3),
	
	# Wall S of stairs
	Wall(3, -5, 3, 4),
	
	# NW objects
	Wall(3, -8, 7, -8),
	
	# Table
	Wall(9, -6, 9, -6),
	
	# NE bookshelf
	Wall(11, -8, 11, -8),
	
	# Bed
	Wall(12, -8, 12, -7),
	}
	
# Walls for demo's Basement level
prototype_basement_walls = \
	{
	# Stuff W of stairs
	Wall(5, 7, 6, 7),

	# Stuff N of stairs
	Wall(5, 6, 8, 6),

	# Stuff E of stairs
	Wall(8, 7, 10, 7),

	# Stuff at W wall
	Wall(2, 6, 3, 7),
	
	# Long central wall running W to E
	Wall(9, 8, 27, 10),
}

# Walls for demo's Cave level
prototype_cave_walls = \
	{
	# Spikes W of entrance
	Wall(6, 7, 6, 8),
	
	# Wall W of entrance
	Wall(5, 6, 5, 6),
	
	# Wall S of entrance
	Wall(7, 9, 8, 9),
	
	# Spike SE of entrance
	Wall(9, 8, 9, 8),
	
	# Wall N of entrance
	Wall(6, 4, 12, 5),
	
	# E end of Wall N of entrance
	Wall(12, 4, 12, 4),
	
	# Lava and spike E of entrance
	Wall(10, 7, 12, 7),
	
	# Spikes
	Wall(13, 8, 14, 8,),
	
	# Lone spike
	Wall(15, 9, 15, 9),
	
	# Long S wall
	Wall(5, 10, 27, 10),
	
	# 2 SE spikes and lava
	Wall(21, 9, 23, 9),
	
	# Large, vertical SE border
	Wall(26, -8, 27, 10),
	
	# Lava pool and spikes farther E of entrance
	Wall(15, 5, 18, 6),
	Wall(16, 4, 16, 7),
	Wall(19, 4, 19, 5),
	
	# L-shaped wall in SE corner, lava
	Wall(17, 7, 23, 8),
	Wall(22, 5, 23, 6),
	Wall(24, 7, 24, 8),
	
	# Horizontal SE border
	Wall(-7, 3, 12, 3),
	
	# Horizonttal wall in SE quadrant
	Wall(16, 2, 20, 3),
	
	# Wall & stuff at center of SE vertical border
	Wall(22, 1, 25, 3),
	Wall(24, 0, 25, 0),
	Wall(25, 4, 25, 5),
	
	# Vertical NW border
	Wall(-7, -15, -6, 3),

	# Horizontal divider wall
	Wall(5, -2, 13, -1),
	Wall(13, -3, 18, -2),
	Wall(18, -2, 21, -1),
	
	
	# Horizontal NW border
	Wall(-5, -15, 18, -14),
	
	# Vertical NE border
	Wall(18, -14, 18, -7),
	}

# Walls for demo's Crypt level
prototype_crypt_walls = \
	{
	# Wall W of start
	Wall(6, 7, 6, 9),
	}

all_walls = [prototype_house_walls, prototype_basement_walls, \
	prototype_cave_walls, prototype_crypt_walls]

# Give walls "red tile" image for debugging
for i in range(len(all_walls)):
	for wall in all_walls[i]:
		wall.current_image = red_tile


# Create Elements
fire = Element('Fire')
ice = Element('Ice')
poison = Element('Poison')
earth = Element('Earth')
light = Element('Light')
dark = Element('Dark')

# Designate elemental advantages
fire.advantage = ice
ice.advantage = poison
poison.advantage = earth
earth.advantage = fire
light.advantage = dark
dark.advantage = light

# Create spells

# Fire spells
singe = Spell('Singe', 'Attack', 5, singe_animation, 2, fire)
immolate = Spell('Immolate', 'Attack', 11, None, 5, fire)
inferno = Spell('Inferno', 'Attack', 45, None, 9, fire)

# Ice spells
chill_air = Spell('ChillAir', 'Attack', 6, None, 3, ice)
ice_spear = Spell('IceSpear', 'Attack', 13, ice_spear_animation, 12, ice)
# Blizzard
# Ice Hydra

# Poison spells
vine_stab = \
	Spell('VineStab', 'Attack', 5, None, 3, poison)
bug_swarm = Spell('BugSwarm', 'Attack', 15, None, 10, poison)
# Death Fog

# Earth spells
sand_shot = Spell('SandShot', 'Attack', 6, sand_shot_animation, 3, earth)
# Rock Fall
fissure = Spell('Fissure', 'Attack', 26, fissure_animation, 20, earth)


# Healing / Light spells
mend = Spell('Mend', 'Heal', 5, None, 3, light)
mend_plus = Spell('Mend+', 'Heal', 15, None, 6, light)
mend_plus_plus = Spell('Mend++', 'Heal', 30, None, 10, light)

# Dark spells
# Harm
# Wound
# Misshape

# Status spells
# Molasses- slow enemy
# Purify - cure poison
# Embolden
# Panic

# Master Spell Dictionary - for accessing from spell cursor
master_spell_dict = \
	{"Singe": singe,
	"Immolate": immolate,
	"Inferno": inferno,
	"ChillAir": chill_air,
	"IceSpear": ice_spear,
	"VineStab": vine_stab,
	"BugSwarm": bug_swarm,
	"SandShot": sand_shot,
	"Fissure": fissure,
	"Mend": mend,
	"Mend+": mend_plus,
	"Mend++": mend_plus_plus}
	
# Empty dictionary of number of items owned by a particular party member
items_owned = \
	{'Red Potion': 0,
	'Blue Potion': 0,
	'Green Herb': 0,
	'Gold Herb': 0}

# Create specific instances of enemy monsters, populate zones

# Forest Zone 1 monsters
forest_slime_images = [forest_slime_img]
forest_slime_1 = Monster('Forest Slime',3,1,2,3,2,1, forest_slime_images, 'POISON', 'Forest Slime', poison)
forest_slime_2 = Monster('Forest Slime 2',3,1,2,3,2,1, forest_slime_images, 'POISON', 'Forest Slime', poison)
forest_slime_3 = Monster('Forest Slime 3',3,1,2,3,2,1, forest_slime_images, 'POISON', 'Forest Slime', poison)
forest_slime_4 = Monster('Forest Slime 4',3,1,2,3,2,1, forest_slime_images, 'POISON', 'Forest Slime', poison)

dark_fairie_images = [dark_fairie_img]
dark_fairie_1 = Monster('Wasp Witch',3,2,3,3,4,1, dark_fairie_images, 'DARK', 'Dark Fairie', dark)
dark_fairie_2 = Monster('Wasp Witch 2',3,2,3,3,4,1, dark_fairie_images, 'DARK', 'Dark Fairie', dark)
dark_fairie_3 = Monster('Wasp Witch 3',3,2,3,3,4,1, dark_fairie_images, 'DARK', 'Dark Fairie', dark)
dark_fairie_4 = Monster('Wasp Witch 4',3,2,3,3,4,1, dark_fairie_images, 'DARK', 'Dark Fairie', dark)

scavenger_images = [scavenger_img]
scavenger_1 = Monster('Scavenger',2,1,2,1,2,1, scavenger_images, 'EARTH', 'Scavenger', earth)
scavenger_2 = Monster('Scavenger 2',2,1,2,1,2,1, scavenger_images, 'EARTH', 'Scavenger', earth)
scavenger_3 = Monster('Scavenger 3',2,1,2,1,2,1, scavenger_images, 'EARTH', 'Scavenger', earth)
scavenger_4 = Monster('Scavenger 4',2,1,2,1,2,1, scavenger_images, 'EARTH', 'Scavenger', earth)

forest_slimes = (forest_slime_1, forest_slime_2, forest_slime_3, forest_slime_4)
dark_fairies = (dark_fairie_1, dark_fairie_2, dark_fairie_3, dark_fairie_4)
scavengers = (scavenger_1, scavenger_2, scavenger_3, scavenger_4)

forest_zone_1_monsters = (forest_slimes, dark_fairies, scavengers)
# forest_shrine_monsters = (chomper(), shrine_sentry(), shroom_baby())
# forest_zone_2_monsters = (willowisp(), vine_boa(), bug_badger())

# Create prototype monsters
snowy_owl_1 = Monster \
	('Snowy Owl', 10, 2, 3, 5, 10, 5, snowy_owl_images, 'ICE', 'Snowy Owl', ice)
snowy_owl_2 = Monster \
	('Snowy Owl 2', 10, 2, 3, 5, 10, 5, snowy_owl_images, 'ICE', 'Snowy Owl', ice)
snowy_owl_3 = Monster \
	('Snowy Owl 3', 10, 2, 3, 5, 10, 5, snowy_owl_images, 'ICE', 'Snowy Owl', ice)
snowy_owl_4 = Monster \
	('Snowy Owl 4', 10, 2, 3, 5, 10, 5, snowy_owl_images, 'ICE', 'Snowy Owl', ice)
	
space_crystal_1 = Monster \
	('Space Crystal', 15, 1, 2, 6, 5, 5, space_crystal_images, 'DARK', 'Space Crystal', dark)
space_crystal_2 = Monster \
	('Space Crystal 2', 15, 1, 2, 6, 5, 5, space_crystal_images, 'DARK', 'Space Crystal', dark)
space_crystal_3 = Monster \
	('Space Crystal 3', 15, 1, 2, 6, 5, 5, space_crystal_images, 'DARK', 'Space Crystal', dark)
space_crystal_4 = Monster \
	('Space Crystal 4', 15, 1, 2, 6, 5, 5, space_crystal_images, 'DARK', 'Space Crystal', dark)
	
ruby_golem_1 = Monster\
	('Ruby Golem', 13, 4, 5, 5, 8, 5, ruby_golem_images, 'FLAME', 'Ruby Golem', fire)
ruby_golem_2 = Monster \
	('Ruby Golem 2', 13, 4, 5, 5, 8, 5, ruby_golem_images, 'FLAME', 'Ruby Golem', fire)
ruby_golem_3 = Monster \
	('Ruby Golem 3', 13, 4, 5, 5, 8, 5, ruby_golem_images, 'FLAME', 'Ruby Golem', fire)
ruby_golem_4 = Monster \
	('Ruby Golem 4', 13, 4, 5, 5, 8, 5, ruby_golem_images, 'FLAME', 'Ruby Golem', fire)
	
flying_jack_1 = Monster \
	('Flying Jack', 7, 3, 4, 7, 8, 5,  flying_jack_images, 'EARTH', 'Flying Jack', earth)
flying_jack_2 = Monster \
	('Flying Jack 2', 7, 3, 4, 7, 8, 5,  flying_jack_images, 'EARTH', 'Flying Jack', earth)
flying_jack_3 = Monster \
	('Flying Jack 3', 7, 3, 4, 7, 8, 5,  flying_jack_images, 'EARTH', 'Flying Jack', earth)
flying_jack_4 = Monster \
	('Flying Jack 4', 7, 3, 4, 7, 8, 5,  flying_jack_images, 'EARTH', 'Flying Jack', earth)
	
snowy_owls = (snowy_owl_1, snowy_owl_2, snowy_owl_3, snowy_owl_4)

space_crystals = (space_crystal_1, space_crystal_2, space_crystal_3, \
	space_crystal_4)
	
ruby_golems = (ruby_golem_1, ruby_golem_2, ruby_golem_3, ruby_golem_4)

flying_jacks = (flying_jack_1, flying_jack_2, flying_jack_3, \
	flying_jack_4)

prototype_basement_monsters = \
	(snowy_owls, space_crystals, ruby_golems, flying_jacks)


# Default enemy monsters
monster_1 = forest_slime_1
monster_2 = forest_slime_2
monster_3 = forest_slime_3
monster_4 = forest_slime_4



### Create Overworld entities ###


# Create player characters / party members
player = PlayerCharacter('Ivy', 45, 29, 2, 3, 0, 5, 64, [], 224, 224, \
	player_back_idle_1, player_back_idle_2, \
	player_back_1, player_back_2, \
	player_front_idle_1, player_front_idle_2, \
	player_front_1, player_front_2, \
	player_left_idle_1, player_left_idle_2, \
	player_left_1, player_left_2, \
	player_right_idle_1, player_right_idle_2, \
	player_right_1, player_right_2, \
	'Goblin', 0, ivy_portrait, ivy_ghost_back_1, ivy_ghost_back_2, \
	ivy_ghost_front_1, ivy_ghost_front_2, ivy_ghost_left_1, \
	ivy_ghost_left_2, ivy_ghost_right_1, ivy_ghost_right_2, \
	['Singe', 'Immolate', 'Inferno', 'ChillAir', 'IceSpear', \
	'VineStab', 'SandShot', 'Fissure'], poison)
	
player_2 = PlayerCharacter('Skratch', 57, 22, 2, 3, 0, 6, 0, [], 224, 256, \
	skratch_back_idle_1, skratch_back_idle_2, \
	skratch_back_1, skratch_back_2, \
	skratch_front_idle_1, skratch_front_idle_2, \
	skratch_front_1, skratch_front_2, \
	skratch_left_idle_1, skratch_left_idle_2, \
	skratch_left_1, skratch_left_2, \
	skratch_right_idle_1, skratch_right_idle_2, \
	skratch_right_1, skratch_right_2, \
	'Orc', 1, skratch_portrait, skratch_ghost_back_1, \
	skratch_ghost_back_2, skratch_ghost_front_1, skratch_ghost_front_2, \
	skratch_ghost_left_1, skratch_ghost_left_2, skratch_ghost_right_1, \
	skratch_ghost_right_2, ['Singe'], fire)
	
player_3 = PlayerCharacter('Helena', 42, 33, 2, 3, 0, 5, 0, [], 224, 288, \
	helena_back_idle_1, helena_back_idle_2, \
	helena_back_1, helena_back_2, \
	helena_front_idle_1, helena_front_idle_2, \
	helena_front_1, helena_front_2, \
	helena_left_idle_1, helena_left_idle_2, \
	helena_left_1, helena_left_2, \
	helena_right_idle_1, helena_right_idle_2, \
	helena_right_1, helena_right_2, \
	'Skeleton', 2, helena_portrait, helena_ghost_back_1, \
	helena_ghost_back_2, helena_ghost_front_1, helena_ghost_front_2, \
	helena_ghost_left_1, helena_ghost_left_2, helena_ghost_right_1, \
	helena_ghost_right_2, ['IceSpear'], ice)
	
player_4 = PlayerCharacter('Bolder', 64, 15, 2, 3, 0, 5, 0, [], 224, 320, \
	bolder_back_idle_1, bolder_back_idle_2, \
	bolder_back_1, bolder_back_2, \
	bolder_front_idle_1, bolder_front_idle_2, \
	bolder_front_1, bolder_front_2, \
	bolder_left_idle_1, bolder_left_idle_2, \
	bolder_left_1, bolder_left_2, \
	bolder_right_idle_1, bolder_right_idle_2, \
	bolder_right_1, bolder_right_2, \
	'Troll', 3, bolder_portrait, bolder_ghost_back_1,\
	bolder_ghost_back_2, bolder_ghost_front_1, bolder_ghost_front_2, \
	bolder_ghost_left_1, bolder_ghost_left_2, bolder_ghost_right_1, \
	bolder_ghost_right_2, ['SandShot', 'Fissure'], earth)

party_members = [player_4, player_3, player_2, player]
non_player_party_members = [player_2, player_3, player_4]
party_members_ordered = [player, player_2, player_3, player_4]
living_party_members =[player, player_2, player_3, player_4]
dead_party_members = []

# Create NPC characters
goblin_woman_1_test_room_floor_1 = NPC(320, 384, 2, \
	goblin_woman_back_1_img, goblin_woman_back_2_img, \
	goblin_woman_right_1_img, goblin_woman_right_2_img, \
	goblin_woman_front_1_img, goblin_woman_front_2_img, \
	goblin_woman_left_1_img, goblin_woman_left_2_img, \
	look_same_script_1, look_same_script_2, 1, 'Goblin', 'Major NPC', \
	ivy_portrait, 'LEAF', True)
	
skratch_example_test_room_floor_3 = NPC(224, 128, 2, \
	skratch_back_idle_1, skratch_back_idle_2, \
	skratch_right_idle_1, skratch_right_idle_2, \
	skratch_front_idle_1, skratch_front_idle_2, \
	skratch_left_idle_1, skratch_left_idle_2, \
	skratch_example_dialogue_1, skratch_example_dialogue_1, 1, 'Orc', \
	'Major NPC', skratch_portrait, 'SKRATCH', True)
	
helena_example_test_room_floor_3 = NPC(160, 128, 2, \
	helena_back_idle_1, helena_back_idle_2, \
	helena_right_idle_1, helena_right_idle_2, \
	helena_front_idle_1, helena_front_idle_2, \
	helena_left_idle_1, helena_left_idle_2, \
	helena_example_dialogue_1, helena_example_dialogue_1, 1, 'Skeleton', \
	'Major NPC', helena_portrait, 'HELENA', True)
	
bolder_example_test_room_floor_3 = NPC(288, 128, 2, \
	bolder_back_idle_1, bolder_back_idle_2, \
	bolder_right_idle_1, bolder_right_idle_2, \
	bolder_front_idle_1, bolder_front_idle_2, \
	bolder_left_idle_1, bolder_left_idle_2, \
	bolder_example_dialogue_1, bolder_example_dialogue_1, 1, 'Troll', \
	'Major NPC', bolder_portrait, 'BOLDER', True)

ivy_example_test_room_floor_3 = NPC(224, 64, 2, \
	player_back_idle_1, player_back_idle_2, \
	player_right_idle_1, player_right_idle_2, \
	player_front_idle_1, player_front_idle_2, \
	player_left_idle_1, player_left_idle_2, \
	ivy_example_dialogue_1, ivy_example_dialogue_1, 1, 'Goblin', \
	'Major NPC', ivy_portrait, 'IVY', True)

fish_guard_test_room_floor_2 = NPC(160, 384, 2, \
	fish_guard_back_1_img, fish_guard_back_2_img, \
	fish_guard_right_1_img, fish_guard_right_2_img, \
	fish_guard_front_1_img, fish_guard_front_2_img, \
	fish_guard_left_1_img, fish_guard_left_2_img, \
	example_guard_dialogue, example_guard_dialogue, 1, 'Fish', \
	'Minor NPC', 'None', 'FISHMAN GUARD', True)
	
goblin_guard_test_room_floor_2 = NPC(224, 384, 2, \
	goblin_guard_back_1_img, goblin_guard_back_2_img, \
	goblin_guard_right_1_img, goblin_guard_right_2_img, \
	goblin_guard_front_1_img, goblin_guard_front_2_img, \
	goblin_guard_left_1_img, goblin_guard_left_2_img, \
	example_guard_dialogue, example_guard_dialogue, 1, 'Goblin', \
	'Minor NPC', 'None', 'GOBLIN GUARD', False)
	
orc_guard_test_room_floor_2 = NPC(288, 384, 2, \
	orc_guard_back_1_img, orc_guard_back_2_img, \
	orc_guard_right_1_img, orc_guard_right_2_img, \
	orc_guard_front_1_img, orc_guard_front_2_img, \
	orc_guard_left_1_img, orc_guard_left_2_img, \
	example_guard_dialogue, example_guard_dialogue, 1, 'Orc', \
	'Minor NPC', 'None', 'ORC GUARD', True)

goblin_salesman_test_room_floor_1 = NPC(224, 32, 2, \
	goblin_salesman_back_1_img, goblin_salesman_back_2_img,
	goblin_salesman_right_1_img, goblin_salesman_right_2_img, \
	goblin_salesman_front_1_img, goblin_salesman_front_2_img, \
	goblin_salesman_left_1_img, goblin_salesman_left_2_img, \
	item_vendor_script, item_vendor_script, 1, 'Goblin', \
	'Minor NPC', 'None', 'GOBLIN VENDOR', False)
	
collector_hermit = NPC(352, -224, 2, \
	goblin_elder_back_1_img, goblin_elder_back_2_img,
	goblin_elder_right_1_img, goblin_elder_right_2_img, \
	goblin_elder_front_1_img, goblin_elder_front_2_img, \
	goblin_elder_left_1_img, goblin_elder_left_2_img, \
	collector_hermit_script_1, collector_hermit_script_2, 1, 'Goblin', \
	'Minor NPC', 'None', 'COLLECTOR HERMIT', True)

# Create treasure chests
chest_1_test_room_floor_1 = Chest(128, 384, treasure_chest_closed, \
	treasure_chest_open, 'Red Potion')
	
chest_2_test_room_floor_1 = Chest(224, 0, treasure_chest_closed, \
	treasure_chest_open, 'Red Potion')
	
chest_3_test_room_floor_1 = Chest(192, 0, treasure_chest_closed, \
	treasure_chest_open, 'Red Potion')
	
chest_4_test_room_floor_1 = Chest(256, 0, treasure_chest_closed, \
	treasure_chest_open, 'Red Potion')

chest_1_test_room_floor_2 = Chest(160, 160, treasure_chest_closed, \
	treasure_chest_open, 'Blue Potion')
	
chest_2_test_room_floor_2 = Chest(288, 160, treasure_chest_closed, \
	treasure_chest_open, 'Silver Sword')
	
# Prototype chests
prototype_basement_chest = Chest(992, 288, treasure_chest_closed, \
	treasure_chest_open, 'Ancient Key')
	
prototype_crypt_chest_1 = Chest(-96, 160, treasure_chest_right_closed, \
	treasure_chest_right_open, '22 Gold')

prototype_crypt_chest_2 = Chest(608, 128, treasure_chest_left_closed, \
	treasure_chest_left_open, 'Chain Wrist Wraps')
	
# prototype_crypt_chest_3 = Chest(
	
	
# Create doors
door_1_test_room_floor_1 = Door(224, 288, red_door_closed, red_door_open)
door_2_test_room_floor_1 = Door(224, 416, red_door_closed, red_door_open)

# Create shop counters
shop_counter_test_room_floor_1 = ShopCounter(224, 64, \
	goblin_salesman_test_room_floor_1, ['Sharp Stick', 'Bark Shield', \
	'Leather Tunic', 'Fur Hood', 'Red Drink', 'Blue Drink'], \
	['90', '55', '75', '30', '10', '15'], shop_counter_img)
	
# Create conversations
prototype_statue_conversation = \
	Conversation('Tile', 224, 128, [player, player_3, player_4], \
		[ivy_statue_dialogue, helena_statue_dialogue, \
		bolder_statue_dialogue])
		
# Create Golden Flowers (save points)
prototype_crypt_flower = GoldenFlower(160, 128, golden_flower_img)
		
# Create levels (define level's background image and entities)

# "Test Room" levels
test_room_floor_1 = Level(test_room_wood, test_room_wood, test_room_wood, test_room_wood, \
	[goblin_woman_1_test_room_floor_1, chest_1_test_room_floor_1,\
	door_1_test_room_floor_1, door_2_test_room_floor_1, \
	player_2, player_3, player_4, goblin_salesman_test_room_floor_1, \
	chest_2_test_room_floor_1, chest_3_test_room_floor_1, \
	chest_4_test_room_floor_1, shop_counter_test_room_floor_1], \
	test_room_walls)
		
test_room_floor_2 = Level(test_room_brick, test_room_brick, test_room_brick, test_room_brick, \
	[chest_1_test_room_floor_2, chest_2_test_room_floor_2, \
	fish_guard_test_room_floor_2, goblin_guard_test_room_floor_2, \
	orc_guard_test_room_floor_2], test_room_walls)
		
test_room_floor_3 = Level(test_room_blue, test_room_blue, test_room_blue, test_room_blue, \
	[skratch_example_test_room_floor_3, \
	helena_example_test_room_floor_3, \
	bolder_example_test_room_floor_3, \
	ivy_example_test_room_floor_3], test_room_walls)
	
	
# "Prototype" levels

# Demo House level (starting area)
prototype_house = Level(prototype_house_img_cropped, \
	prototype_house_img_cropped_2, prototype_house_img_cropped, \
	prototype_house_img_cropped_2, [collector_hermit], \
	prototype_house_walls)

# Demo Basement level
prototype_basement = Level(prototype_basement_img, prototype_basement_img, prototype_basement_img, prototype_basement_img, \
	[prototype_basement_chest], \
	prototype_basement_walls)
	
# Demo Cave level
prototype_cave = Level(prototype_cave_1, prototype_cave_2, \
	prototype_cave_3, prototype_cave_2, [], prototype_cave_walls)

# Demo Crypt level
prototype_basement_level_2 = Level(prototype_basement_2_img, prototype_basement_2_img, prototype_basement_2_img, prototype_basement_2_img, \
	[prototype_statue_conversation, prototype_crypt_chest_1, \
	prototype_crypt_chest_2, prototype_crypt_flower], \
	prototype_crypt_walls)
	
# Demo Church level (final area)



# Create portals (stairs, etc) between levels

# Test level portals
test_stairs_1 = Portal(224, 224, \
	stairs_up_img, test_room_floor_2, '', -256, -6048, 'North', 'Safe')
	
test_stairs_2 = Portal(224, 288, \
	stairs_up_img, test_room_floor_3, '', -256, -6048, 'North', 'Safe')
	
test_stairs_3 = Portal(224, 224, \
	stairs_down_img, test_room_floor_2, '', -256, -6048, 'South', \
		'Safe')
	
test_stairs_4 = Portal(224, 224, \
	stairs_down_img, test_room_floor_1, '', -256, -5984, 'South', \
		'Safe')

# Prototype portals
prototype_house_stairs = Portal(96, -192, \
	stairs_down_stone_img, prototype_basement, '', -128, -192, \
		'North', 'Safe')
		
prototype_basement_stairs = Portal(224, 224, \
	stairs_up_stone_img, prototype_house, '', -256, -6048, 'South', \
		'Safe')
		
prototype_basement_exit = Portal(-96, -192, \
	stairs_down_stone_img, prototype_cave, '', -128, -192, \
	'South', 'Safe')
	
prototype_crypt_south_exit = Portal(224, 224, \
	stairs_up_stone_img, prototype_basement, '', -576, -6464, \
		'North', 'Safe')
		
prototype_cave_south_stairs = Portal(224, 224, \
	stairs_up_stone_img, prototype_basement, '', -544, -6368, \
		'North', 'Safe')


# Link portals to levels

# This method is bad - don't do this:
test_room_floor_1.entities.append(test_stairs_1)
test_room_floor_2.entities.append(test_stairs_2)
test_room_floor_3.entities.append(test_stairs_3)
test_room_floor_2.entities.append(test_stairs_4)

# Do this instead:
# Insert given portal at beginning of list of entities in a given level
# This is so other sprites {ie, Trolls) aren't overlapped by stairs, etc
prototype_house.entities.insert(0, prototype_house_stairs)

prototype_basement.entities.insert(0, prototype_basement_stairs)
prototype_basement.entities.insert(0, prototype_basement_exit)	

prototype_cave.entities.insert(0, prototype_cave_south_stairs)

# Link portals to each other
test_stairs_1.destination_object = test_stairs_4
test_stairs_2.destination_object = test_stairs_3
test_stairs_3.destination_object = test_stairs_2
test_stairs_4.destination_object = test_stairs_1

prototype_house_stairs.destination_object = prototype_basement_stairs
prototype_basement_stairs.destination_object = prototype_house_stairs
prototype_basement_exit.destination_object = prototype_cave_south_stairs
prototype_crypt_south_exit.destination_object = prototype_basement_exit
prototype_cave_south_stairs.destination_object = prototype_basement_exit

# Define starting area
current_level = prototype_house
current_entities = prototype_house.entities
current_walls = prototype_house.walls
world_map = prototype_house_img_cropped
current_zone = 'Safe'
