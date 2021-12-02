# images.py
# Start game window and load images to be used by Goblin Hero
# Author: Jackie P, aka TheDataElemental


import pygame


# Start game window
pygame.init()
screen = pygame.display.set_mode((512, 480), \
	pygame.HWSURFACE | pygame.DOUBLEBUF, vsync = 1)
pygame.display.set_caption("GOBLIN HERO DEMO")
GH_icon = pygame.image.load("Assets/Exports/Art/Backgrounds/ivy_icon_32_x_32.png")
pygame.display.set_icon(GH_icon)


cursor = pygame.image.load("Assets/Exports/Art/Backgrounds/cursor.png").convert()
blank_cursor = pygame.image.load("Assets/Exports/Art/Backgrounds/blank_cursor.png").convert()
attack_cursor_img = pygame.image.load("Assets/Exports/Art/Backgrounds/attack_cursor_img.png").convert()
attack_cursor_blank = pygame.image.load("Assets/Exports/Art/Backgrounds/attack_cursor_blank.png").convert()

# Load background images
battle_frame = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/battle_frame.png").convert_alpha()
black_monster_square = pygame.image.load\
	("Assets/Exports/Art/Monsters/black_monster_square.png").convert()
black_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/black_screen.png").convert()
gray_screen_1 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/gray_screen_1.png").convert()
gray_screen_2 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/gray_screen_2.png").convert()
gray_screen_3 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/gray_screen_3.png").convert()
white_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/white_screen.png").convert()
brown_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/brown_screen.png").convert()
tan_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/tan_screen.png").convert()
orange_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/orange_screen.png").convert()
yellow_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/yellow_screen.png").convert()
bright_yellow_screen = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/bright_yellow_screen.png").convert()
	
red_tile = pygame.image.load\
	("Assets/Exports/Art/Tiles/red_tile.png").convert()

text_box = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/text_box_blank.png").convert()
text_box_barred = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/text_box_barred.png").convert()
text_box_barred_vines = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/text_box_barred_vines.png")\
	.convert()
ui_box_1 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/ui_box_1.png").convert()
ui_box_erase = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/ui_box_erase.png").convert()
command_menu_frame = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/command_menu_frame.png").convert()
shop_buy_frame = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/shop_buy_frame.png").convert()
yes_or_no_prompt = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/yes_or_no.png").convert()
	
prototype_title_screen_img = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/goblin_hero_prototype_title_screen.png").convert()	
press_enter_prototype_title_screen_img = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/enter_goblin_hero_prototype_title_screen.png").convert()

teeth_display_frame = pygame.image.load("Assets/Exports/Art/Backgrounds/teeth_display_frame.png").convert()
vine_frame = pygame.image.load("Assets/Exports/Art/Backgrounds/vine_frame.png").convert()
spell_frame_battle = pygame.image.load("Assets/Exports/Art/Backgrounds/spell_frame_battle.png").convert()
spell_frame_battle_erase = pygame.image.load("Assets/Exports/Art/Backgrounds/spell_frame_battle_erase.png").convert()
item_frame_battle = pygame.image.load("Assets/Exports/Art/Backgrounds/item_frame_battle.png").convert()
item_frame_battle_erase = spell_frame_battle_erase

title_screen = pygame.image.load("Assets/Exports/Art/Backgrounds/title_screen_castle.png").convert()
title_screen = pygame.transform.scale(title_screen,(512,480))
splash_screen = pygame.image.load("Assets/Exports/Art/Backgrounds/splash_screen.png").convert()
title_screen = pygame.transform.scale(title_screen,(512,480))
the_end = pygame.image.load("Assets/Exports/Art/Backgrounds/the_end.png").convert()

time_portal_img_1 = pygame.image.load("Assets/Exports/Art/Backgrounds/time_portal_1.png").convert()
time_portal_img_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/time_portal_2.png").convert()
time_portal_img_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/time_portal_3.png").convert()
time_portal_img_4 = pygame.image.load("Assets/Exports/Art/Backgrounds/time_portal_4.png").convert()
title_screen_star_img = pygame.image.load("Assets/Exports/Art/Backgrounds/title_screen_star.png").convert()
title_screen_star_blank_img = pygame.image.load("Assets/Exports/Art/Backgrounds/title_screen_star_blank.png").convert()

prototype_end_screen = pygame.image.load("Assets/Exports/Art/Backgrounds/prototype_end_screen.png").convert()

# Screen transition effects
battle_wipe_right_1 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_1.png").convert_alpha()
battle_wipe_right_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_2.png").convert_alpha()
battle_wipe_right_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_3.png").convert_alpha()
battle_wipe_right_4 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_4.png").convert_alpha()
battle_wipe_right_5 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_5.png").convert_alpha()
battle_wipe_right_6 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_6.png").convert_alpha()
battle_wipe_right_7 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_7.png").convert_alpha()
battle_wipe_right_8 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_8.png").convert_alpha()
battle_wipe_right_9 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_9.png").convert_alpha()
battle_wipe_right_10 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_10.png").convert_alpha()
battle_wipe_right_11 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_11.png").convert_alpha()
battle_wipe_right_12 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_12.png").convert_alpha()
battle_wipe_right_13 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_13.png").convert_alpha()
battle_wipe_right_14 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_14.png").convert_alpha()
battle_wipe_right_15 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_right_15.png").convert_alpha()

battle_wipe_right = [battle_wipe_right_1, battle_wipe_right_2, \
	battle_wipe_right_3, battle_wipe_right_4, battle_wipe_right_5, \
	battle_wipe_right_6, battle_wipe_right_7, battle_wipe_right_8, \
	battle_wipe_right_9, battle_wipe_right_10, battle_wipe_right_11, \
	battle_wipe_right_12, battle_wipe_right_13, battle_wipe_right_14, \
	battle_wipe_right_15]
	
battle_wipe_down_1 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_1.png").convert_alpha()
battle_wipe_down_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_2.png").convert_alpha()
battle_wipe_down_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_3.png").convert_alpha()
battle_wipe_down_4 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_4.png").convert_alpha()
battle_wipe_down_5 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_5.png").convert_alpha()
battle_wipe_down_6 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_6.png").convert_alpha()
battle_wipe_down_7 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_7.png").convert_alpha()
battle_wipe_down_8 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_down_8.png").convert_alpha()

battle_wipe_down = [battle_wipe_down_1, battle_wipe_down_2, \
	battle_wipe_down_3, battle_wipe_down_4, battle_wipe_down_5, \
	battle_wipe_down_6, battle_wipe_down_7, battle_wipe_down_8]
	
battle_wipe_bite_1 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_1.png").convert_alpha()
battle_wipe_bite_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_2.png").convert_alpha()
battle_wipe_bite_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_3.png").convert_alpha()
battle_wipe_bite_4 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_4.png").convert_alpha()
battle_wipe_bite_5 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_5.png").convert_alpha()
battle_wipe_bite_6 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_6.png").convert_alpha()
battle_wipe_bite_7 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_7.png").convert_alpha()
battle_wipe_bite_8 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_bite_8.png").convert_alpha()

battle_wipe_bite = [battle_wipe_bite_1, battle_wipe_bite_2, \
	battle_wipe_bite_3, battle_wipe_bite_4, battle_wipe_bite_5, \
	battle_wipe_bite_6, battle_wipe_bite_7, battle_wipe_bite_8]
	
battle_wipe_clock_1 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_1.png").convert_alpha()
battle_wipe_clock_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_2.png").convert_alpha()
battle_wipe_clock_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_3.png").convert_alpha()
battle_wipe_clock_4 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_4.png").convert_alpha()
battle_wipe_clock_5 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_5.png").convert_alpha()
battle_wipe_clock_6 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_6.png").convert_alpha()
battle_wipe_clock_7 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_7.png").convert_alpha()
battle_wipe_clock_8 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_8.png").convert_alpha()
battle_wipe_clock_9 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_clock_9.png").convert_alpha()
	
battle_wipe_clock = [battle_wipe_clock_1, battle_wipe_clock_2, \
battle_wipe_clock_3, battle_wipe_clock_4, battle_wipe_clock_5, \
battle_wipe_clock_6, battle_wipe_clock_7, battle_wipe_clock_8, \
battle_wipe_clock_9]

battle_wipe_dissolve_1 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_1.png").convert_alpha()
battle_wipe_dissolve_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_2.png").convert_alpha()
battle_wipe_dissolve_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_3.png").convert_alpha()
battle_wipe_dissolve_4 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_4.png").convert_alpha()
battle_wipe_dissolve_5 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_5.png").convert_alpha()
battle_wipe_dissolve_6 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_6.png").convert_alpha()
battle_wipe_dissolve_7 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_7.png").convert_alpha()
battle_wipe_dissolve_8 = pygame.image.load("Assets/Exports/Art/Backgrounds/Screen Transitions/battle_wipe_dissolve_8.png").convert_alpha()

battle_wipe_dissolve = [battle_wipe_dissolve_1, battle_wipe_dissolve_2, \
battle_wipe_dissolve_3, battle_wipe_dissolve_4, battle_wipe_dissolve_5, \
battle_wipe_dissolve_6, battle_wipe_dissolve_7, battle_wipe_dissolve_8]
	
	
screen_transitions = [battle_wipe_clock]


# Game Over screen images

angel_blink_1 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/blink_loop/blink_1.png")\
	.convert()
angel_blink_2 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/blink_loop/blink_2.png")\
	.convert()
angel_blink_3 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/blink_loop/blink_3.png")\
	.convert()
angel_blink_4 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/blink_loop/blink_4.png")\
	.convert()
angel_blink_5 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/blink_loop/blink_5.png")\
	.convert()
angel_blink_6 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/blink_loop/blink_6.png")\
	.convert()

angel_blink_images = [angel_blink_1, 
	angel_blink_2, 
	angel_blink_3,
	angel_blink_4, 
	angel_blink_5, 
	angel_blink_6]

angel_ring_1 = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/Game Over/ring_loop/ring_1.png")\
		.convert()
angel_ring_2 = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/ring_loop/ring_2.png").convert()
angel_ring_3 = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/ring_loop/ring_3.png").convert()

angel_ring_images = [angel_ring_1, 
	angel_ring_2, 
	angel_ring_3]		
	
nines = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/99999.png").convert()
bad_luck = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/bad_luck.png").convert()
be_not_afraid = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/be_not_afraid.png").convert()
hello_again = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/hello_again.png").convert()
one_with_everything = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/one_with_everything.png").convert()
this_too_has_passed = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/this_too_has_passed.png").convert()
time_is_an_illusion = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/time_is_an_illusion.png").convert()
welcome_home = pygame.image.load("Assets/Exports/Art/Backgrounds/Game Over/time_is_an_illusion.png").convert()

angel_dialogues = [nines,
bad_luck,
be_not_afraid,
hello_again,
one_with_everything,
this_too_has_passed,
time_is_an_illusion,
welcome_home]

game_over_image = pygame.image.load\
	("Assets/Exports/Art/Backgrounds/game_over.png").convert()


# Load world map / level images
world_map_1 = pygame.image.load\
	("Assets/Exports/Art/Maps/world_map_1.png").convert()
world_map_1 = pygame.transform.scale(world_map_1,(8208,7680))
world_map_2 = pygame.image.load\
	("Assets/Exports/Art/Maps/world_map_2.png").convert()
world_map_2 = pygame.transform.scale(world_map_2,(8208,7680))

test_room_brick = pygame.image.load\
	("Assets/Exports/Art/Maps/test_room_brick.png").convert()
test_room_brick = pygame.transform.scale(test_room_brick,(8208,7680))
test_room_wood = pygame.image.load\
	("Assets/Exports/Art/Maps/test_room_wood.png").convert()
test_room_wood = pygame.transform.scale(test_room_wood,(8208,7680))
test_room_blue = pygame.image.load\
	("Assets/Exports/Art/Maps/test_room_blue.png").convert()
test_room_blue = pygame.transform.scale(test_room_blue,(8208,7680))

prototype_house_img = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_house_1.png").convert()
prototype_house_img = pygame.transform.scale\
	(prototype_house_img,(8208,7680))
prototype_basement_img = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_basement.png").convert()
prototype_basement_img = pygame.transform.scale\
	(prototype_basement_img,(8208,7680))
	
prototype_basement_2_img = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_basement_level_2.png").convert()
prototype_basement_2_img = pygame.transform.scale\
	(prototype_basement_2_img,(8208,7680))
	
prototype_cave_1 = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_cave_1.png").convert()
prototype_cave_1 = pygame.transform.scale\
	(prototype_cave_1,(8208,7680))
	
prototype_cave_2 = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_cave_2.png").convert()
prototype_cave_2 = pygame.transform.scale\
	(prototype_cave_2,(8208,7680))
	
prototype_cave_3 = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_cave_3.png").convert()
prototype_cave_3 = pygame.transform.scale\
	(prototype_cave_3,(8208,7680))

prototype_house_img_cropped = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_house_1.png").convert()
prototype_house_img_cropped = \
	pygame.transform.scale(prototype_house_img_cropped,(1024,896))
prototype_house_img_cropped_2 = pygame.image.load\
	("Assets/Exports/Art/Maps/prototype_house_2.png").convert()
prototype_house_img_cropped_2 = \
	pygame.transform.scale(prototype_house_img_cropped_2,(1024,896))


### Load spell images ###

# Fire spell animations
singe_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/singe_0.png").convert()
singe_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/singe_1.png").convert()
singe_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/singe_2.png").convert()
singe_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/singe_3.png").convert()
singe_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/singe_4.png").convert()
singe_animation = [singe_frame_1, singe_frame_2, singe_frame_3, \
	singe_frame_4, singe_frame_5]
	
immolate_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/immolate_1.png").convert()
immolate_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/immolate_2.png").convert()
immolate_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/immolate_3.png").convert()
immolate_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/immolate_4.png").convert()
immolate_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/immolate_5.png").convert()
immolate_frame_6 = pygame.image.load\
	("Assets/Exports/Art/Spells/immolate_6.png").convert()
immolate_animation = [immolate_frame_1, immolate_frame_2, \
	immolate_frame_3, immolate_frame_4, immolate_frame_5, \
	immolate_frame_6]

# Earth spell animations
sand_shot_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/sand_shot_1.png").convert()
sand_shot_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/sand_shot_2.png").convert()
sand_shot_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/sand_shot_3.png").convert()
sand_shot_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/sand_shot_4.png").convert()
sand_shot_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/sand_shot_5.png").convert()
sand_shot_animation = [sand_shot_frame_1, sand_shot_frame_2, \
	sand_shot_frame_3, sand_shot_frame_4, sand_shot_frame_5]
	
fissure_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/fissure_1.png").convert()
fissure_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/fissure_2.png").convert()
fissure_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/fissure_3.png").convert()
fissure_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/fissure_4.png").convert()
fissure_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/fissure_5.png").convert()
fissure_animation = \
	[fissure_frame_1, fissure_frame_2, fissure_frame_3, \
	fissure_frame_4, fissure_frame_5]

# Ice spell animations
chill_air_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/chill_air_1.png").convert()
chill_air_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/chill_air_2.png").convert()
chill_air_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/chill_air_3.png").convert()
chill_air_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/chill_air_4.png").convert()
chill_air_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/chill_air_5.png").convert()
chill_air_frame_6 = pygame.image.load\
	("Assets/Exports/Art/Spells/chill_air_6.png").convert()
chill_air_animation = [chill_air_frame_1, chill_air_frame_2, \
	chill_air_frame_3, chill_air_frame_4, chill_air_frame_5, \
	chill_air_frame_6]

ice_spear_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/ice_spear_1.png").convert()
ice_spear_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/ice_spear_2.png").convert()
ice_spear_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/ice_spear_3.png").convert()
ice_spear_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/ice_spear_4.png").convert()
ice_spear_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/ice_spear_5.png").convert()
ice_spear_frame_6 = pygame.image.load\
	("Assets/Exports/Art/Spells/ice_spear_6.png").convert()
ice_spear_animation = [ice_spear_frame_1, ice_spear_frame_2, \
	ice_spear_frame_3, ice_spear_frame_4, ice_spear_frame_5, \
	ice_spear_frame_6]
	
# Poison spells
vine_stab_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/vine_stab_1.png").convert()
vine_stab_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/vine_stab_2.png").convert()
vine_stab_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/vine_stab_3.png").convert()
vine_stab_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/vine_stab_4.png").convert()
vine_stab_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/vine_stab_5.png").convert()
vine_stab_frame_6 = pygame.image.load\
	("Assets/Exports/Art/Spells/vine_stab_6.png").convert()

bug_swarm_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/bug_swarm_1.png").convert()
bug_swarm_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/bug_swarm_2.png").convert()
bug_swarm_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/bug_swarm_3.png").convert()
bug_swarm_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/bug_swarm_4.png").convert()
bug_swarm_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/bug_swarm_5.png").convert()

# Healing / Light spell animations
mend_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_1.png").convert()
mend_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_2.png").convert()
mend_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_3.png").convert()
mend_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_4.png").convert()
mend_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_5.png").convert()
mend_frame_6 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_6.png").convert()
	
mend_plus_frame_1 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_1.png").convert()
mend_plus_frame_2 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_2.png").convert()
mend_plus_frame_3 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_3.png").convert()
mend_plus_frame_4 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_4.png").convert()
mend_plus_frame_5 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_5.png").convert()
mend_plus_frame_6 = pygame.image.load\
	("Assets/Exports/Art/Spells/mend_6.png").convert()

### Load player idle images ###

# Ivy idle sprites
player_front = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_front.png").convert_alpha()
player_left = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_left.png").convert_alpha()
player_right = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_right.png").convert_alpha()
player_back = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_back.png").convert_alpha()

player_front_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_front_idle_1.png").convert_alpha()
player_front_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_front_idle_2.png").convert_alpha()

player_left_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_left_idle_1.png").convert_alpha()
player_left_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_left_idle_2.png").convert_alpha()

player_right_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_right_idle_1.png").convert_alpha()
player_right_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_right_idle_2.png").convert_alpha()

player_back_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_back_idle_1.png").convert_alpha()
player_back_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_back_idle_2.png").convert_alpha()


# Bolder idle sprites
bolder_back_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_back_idle_1.png").convert_alpha()
bolder_back_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_back_idle_2.png").convert_alpha()

bolder_front_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_front_idle_1.png").convert_alpha()
bolder_front_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_front_idle_2.png").convert_alpha()

bolder_left_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_left_idle_1.png").convert_alpha()
bolder_left_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_left_idle_2.png").convert_alpha()

bolder_right_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_right_idle_1.png").convert_alpha()
bolder_right_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_right_idle_2.png").convert_alpha()


# Helena idle sprites
helena_back_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_back_idle_1.png").convert_alpha()
helena_back_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_back_idle_2.png").convert_alpha()

helena_front_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_front_idle_1.png").convert_alpha()
helena_front_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_front_idle_2.png").convert_alpha()

helena_left_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_left_idle_1.png").convert_alpha()
helena_left_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_left_idle_2.png").convert_alpha()

helena_right_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_right_idle_1.png").convert_alpha()
helena_right_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_right_idle_2.png").convert_alpha()


# Skratch idle sprites
skratch_back_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_back_idle_1.png").convert_alpha()
skratch_back_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_back_idle_2.png").convert_alpha()

skratch_front_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_front_idle_1.png").convert_alpha()
skratch_front_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_front_idle_2.png").convert_alpha()

skratch_left_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_left_idle_1.png").convert_alpha()
skratch_left_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_left_idle_2.png").convert_alpha()

skratch_right_idle_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_right_idle_1.png").convert_alpha()
skratch_right_idle_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_right_idle_2.png").convert_alpha()


### Load player walking images ###

# Ivy walking sprites
player_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_front_1.png").convert_alpha()
player_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_front_2.png").convert_alpha()

player_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_right_1.png").convert_alpha()
player_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_right_2.png").convert_alpha()

player_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_left_1.png").convert_alpha()
player_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_left_2.png").convert_alpha()

player_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_back_1.png").convert_alpha()
player_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/player_sprite_back_2.png").convert_alpha()
player_pose = player_front


# Bolder walking sprites
bolder_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_back_1.png").convert_alpha()
bolder_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_back_2.png").convert_alpha()

bolder_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_front_1.png").convert_alpha()
bolder_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_front_2.png").convert_alpha()

bolder_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_left_1.png").convert_alpha()
bolder_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_left_2.png").convert_alpha()

bolder_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_right_1.png").convert_alpha()
bolder_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_sprite_right_2.png").convert_alpha()


# Helena walking sprites
helena_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_back_1.png").convert_alpha()
helena_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_back_2.png").convert_alpha()

helena_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_front_1.png").convert_alpha()
helena_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_front_2.png").convert_alpha()

helena_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_left_1.png").convert_alpha()
helena_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_left_2.png").convert_alpha()

helena_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_right_1.png").convert_alpha()
helena_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_sprite_right_2.png").convert_alpha()


# Skratch walking sprites
skratch_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_back_1.png").convert_alpha()
skratch_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_back_2.png").convert_alpha()

skratch_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_front_1.png").convert_alpha()
skratch_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_front_2.png").convert_alpha()

skratch_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_left_1.png").convert_alpha()
skratch_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_left_2.png").convert_alpha()

skratch_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_right_1.png").convert_alpha()
skratch_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_sprite_right_2.png").convert_alpha()

# Party member portraits
ivy_portrait = pygame.image.load("Assets/Exports/Art/Sprites/ivy_portrait.png").convert_alpha()
skratch_portrait = pygame.image.load("Assets/Exports/Art/Sprites/skratch_portrait.png").convert_alpha()
helena_portrait = pygame.image.load("Assets/Exports/Art/Sprites/helena_portrait.png").convert_alpha()
bolder_portrait = pygame.image.load("Assets/Exports/Art/Sprites/bolder_portrait.png").convert_alpha()

empty_frame = pygame.image.load("Assets/Exports/Art/Backgrounds/empty_frame.png").convert_alpha()
erase_portrait = pygame.image.load("Assets/Exports/Art/Backgrounds/erase_portrait.png").convert()


### Load player ghost images ###

# Ivy ghost images
ivy_ghost_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_back_1.png").convert_alpha()
ivy_ghost_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_back_2.png").convert_alpha()

ivy_ghost_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_front_1.png").convert_alpha()
ivy_ghost_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_front_2.png").convert_alpha()

ivy_ghost_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_left_1.png").convert_alpha()
ivy_ghost_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_left_2.png").convert_alpha()

ivy_ghost_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_right_1.png").convert_alpha()
ivy_ghost_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/ivy_ghost_right_2.png").convert_alpha()


# Skratch ghost images
skratch_ghost_back_1 = \
	pygame.image.load\
	("Assets/Exports/Art/Sprites/skratch_ghost_back_1.png")\
	.convert_alpha()
	
skratch_ghost_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_back_2.png").convert_alpha()

skratch_ghost_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_front_1.png").convert_alpha()
skratch_ghost_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_front_2.png").convert_alpha()

skratch_ghost_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_left_1.png").convert_alpha()
skratch_ghost_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_left_2.png").convert_alpha()

skratch_ghost_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_right_1.png").convert_alpha()
skratch_ghost_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/skratch_ghost_right_2.png").convert_alpha()

# Helena ghost images
helena_ghost_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_back_1.png").convert_alpha()
helena_ghost_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_back_2.png").convert_alpha()

helena_ghost_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_front_1.png").convert_alpha()
helena_ghost_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_front_2.png").convert_alpha()

helena_ghost_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_left_1.png").convert_alpha()
helena_ghost_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_left_2.png").convert_alpha()

helena_ghost_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_right_1.png").convert_alpha()
helena_ghost_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/helena_ghost_right_2.png").convert_alpha()

# Bolder ghost images
bolder_ghost_back_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_back_1.png").convert_alpha()
bolder_ghost_back_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_back_2.png").convert_alpha()

bolder_ghost_front_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_front_1.png").convert_alpha()
bolder_ghost_front_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_front_2.png").convert_alpha()

bolder_ghost_left_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_left_1.png").convert_alpha()
bolder_ghost_left_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_left_2.png").convert_alpha()

bolder_ghost_right_1 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_right_1.png").convert_alpha()
bolder_ghost_right_2 = pygame.image.load("Assets/Exports/Art/Sprites/bolder_ghost_right_2.png").convert_alpha()


### Load NPC images ###

# Fish people images

fish_guard_back_1_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_back_1.png").convert_alpha()
fish_guard_back_2_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_back_2.png").convert_alpha()
fish_guard_front_1_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_front_1.png").convert_alpha()
fish_guard_front_2_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_front_2.png").convert_alpha()
fish_guard_left_1_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_left_1.png").convert_alpha()
fish_guard_left_2_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_left_2.png").convert_alpha()
fish_guard_right_1_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_right_1.png").convert_alpha()
fish_guard_right_2_img = pygame.image.load("Assets/Exports/Art/Sprites/fish_guard_right_2.png").convert_alpha()

# Goblin images

goblin_guard_back_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_back_1.png").convert_alpha()
goblin_guard_back_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_back_2.png").convert_alpha()
goblin_guard_front_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_front_1.png").convert_alpha()
goblin_guard_front_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_front_2.png").convert_alpha()
goblin_guard_left_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_left_1.png").convert_alpha()
goblin_guard_left_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_left_2.png").convert_alpha()
goblin_guard_right_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_right_1.png").convert_alpha()
goblin_guard_right_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_guard_right_2.png").convert_alpha()

goblin_woman_front_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_front_1.png").convert_alpha()
goblin_woman_front_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_front_2.png").convert_alpha()
goblin_woman_right_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_right_1.png").convert_alpha()
goblin_woman_right_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_right_2.png").convert_alpha()
goblin_woman_left_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_left_1.png").convert_alpha()
goblin_woman_left_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_left_2.png").convert_alpha()
goblin_woman_back_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_back_1.png").convert_alpha()
goblin_woman_back_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_woman_back_2.png").convert_alpha()

goblin_salesman_front_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_front_1.png").convert_alpha()
goblin_salesman_front_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_front_2.png").convert_alpha()
goblin_salesman_right_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_right_1.png").convert_alpha()
goblin_salesman_right_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_right_2.png").convert_alpha()
goblin_salesman_left_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_left_1.png").convert_alpha()
goblin_salesman_left_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_left_2.png").convert_alpha()
goblin_salesman_back_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_back_1.png").convert_alpha()
goblin_salesman_back_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_salesman_back_2.png").convert_alpha()

goblin_elder_front_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_front_1.png").convert_alpha()
goblin_elder_front_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_front_2.png").convert_alpha()
goblin_elder_right_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_right_1.png").convert_alpha()
goblin_elder_right_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_right_2.png").convert_alpha()
goblin_elder_left_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_left_1.png").convert_alpha()
goblin_elder_left_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_left_2.png").convert_alpha()
goblin_elder_back_1_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_back_1.png").convert_alpha()
goblin_elder_back_2_img = pygame.image.load("Assets/Exports/Art/Sprites/goblin_elder_back_2.png").convert_alpha()

# Orc images

orc_guard_back_1_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_back_1.png").convert_alpha()
orc_guard_back_2_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_back_2.png").convert_alpha()
orc_guard_front_1_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_front_1.png").convert_alpha()
orc_guard_front_2_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_front_2.png").convert_alpha()
orc_guard_left_1_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_left_1.png").convert_alpha()
orc_guard_left_2_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_left_2.png").convert_alpha()
orc_guard_right_1_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_right_1.png").convert_alpha()
orc_guard_right_2_img = pygame.image.load("Assets/Exports/Art/Sprites/orc_guard_right_2.png").convert_alpha()

# Load object images
golden_flower_img = pygame.image.load("Assets/Exports/Art/Sprites/golden_flower.png").convert_alpha()

treasure_chest_closed = pygame.image.load("Assets/Exports/Art/Sprites/treasure_chest_closed.png").convert_alpha()
treasure_chest_open = pygame.image.load("Assets/Exports/Art/Sprites/treasure_chest_open.png").convert_alpha()
treasure_chest_right_closed = pygame.image.load("Assets/Exports/Art/Sprites/treasure_chest_right_closed.png").convert_alpha()
treasure_chest_right_open = pygame.image.load("Assets/Exports/Art/Sprites/treasure_chest_right_open.png").convert_alpha()
treasure_chest_left_closed = pygame.image.load("Assets/Exports/Art/Sprites/treasure_chest_left_closed.png").convert_alpha()
treasure_chest_left_open = pygame.image.load("Assets/Exports/Art/Sprites/treasure_chest_left_open.png").convert_alpha()

red_door_closed = pygame.image.load("Assets/Exports/Art/Sprites/red_door_closed.png").convert_alpha()
red_door_open = pygame.image.load("Assets/Exports/Art/Sprites/red_door_open.png").convert_alpha()
stairs_up_img  = pygame.image.load("Assets/Exports/Art/Sprites/stairs_up.png").convert_alpha()
stairs_down_img = pygame.image.load("Assets/Exports/Art/Sprites/stairs_down.png").convert_alpha()
stairs_up_stone_img = pygame.image.load("Assets/Exports/Art/Sprites/stairs_up_stone.png").convert_alpha()
stairs_down_stone_img = pygame.image.load("Assets/Exports/Art/Sprites/stairs_down_stone.png").convert_alpha()
shop_counter_img = pygame.image.load("Assets/Exports/Art/Sprites/shop_counter.png").convert_alpha()

# Load monster images
forest_slime_img = pygame.image.load("Assets/Exports/Art/Monsters/slime_1_forest_blob.png").convert()

batro_img = pygame.image.load("Assets/Exports/Art/Monsters/batro.png").convert()
bug_badger_img = pygame.image.load("Assets/Exports/Art/Monsters/bug_badger.png").convert()
cactus_swarm_img = pygame.image.load("Assets/Exports/Art/Monsters/cactus_swarm.png").convert()
chomper_img = pygame.image.load("Assets/Exports/Art/Monsters/chomper.png").convert()
dark_fairie_img = pygame.image.load("Assets/Exports/Art/Monsters/fairie_1_wasp_witch.png").convert()
dimetrodon_img = pygame.image.load("Assets/Exports/Art/Monsters/dimetrodon.png").convert()
forest_guardian_img = pygame.image.load("Assets/Exports/Art/Monsters/tiger.png").convert()
lost_skull_img = pygame.image.load("Assets/Exports/Art/Monsters/skull_1_lost_skull.png").convert()
shroom_baby_img = pygame.image.load("Assets/Exports/Art/Monsters/mushroom_1_hungry_shroom.png").convert()
sand_shark_img = pygame.image.load("Assets/Exports/Art/Monsters/shark_1_sand_shark_1.png").convert()
scavenger_img = pygame.image.load("Assets/Exports/Art/Monsters/scavenger_black.png").convert()
blue_worm_img = pygame.image.load("Assets/Exports/Art/Monsters/blue_worm.png").convert()
skeleton_emperor_img = pygame.image.load("Assets/Exports/Art/Monsters/skeleton_1_mad_undead_orc.png").convert()
swamp_tree_img = pygame.image.load("Assets/Exports/Art/Monsters/swamp_tree.png").convert()
shrine_watcher_img = pygame.image.load("Assets/Exports/Art/Monsters/temple_watcher.png").convert()
tulip_img = pygame.image.load("Assets/Exports/Art/Monsters/flower_1_tulip_head.png").convert()
vine_boa_img = pygame.image.load("Assets/Exports/Art/Monsters/snake_1_vine_boa.png").convert()
water_elemental_img = pygame.image.load("Assets/Exports/Art/Monsters/water_elemental.png").convert()
willowisp_img = pygame.image.load("Assets/Exports/Art/Monsters/willow_wisp.png").convert()
woolly_mammoth_img = pygame.image.load("Assets/Exports/Art/Monsters/woolly_mammoth.png").convert()

# Prototype Enemy Monsters
snowy_owl_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/owl_1_snowy_owl_1.png").convert()
snowy_owl_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/owl_1_snowy_owl_2.png").convert()
snowy_owl_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/owl_1_snowy_owl_3.png").convert()
snowy_owl_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/owl_1_snowy_owl_4.png").convert()
snowy_owl_images = [snowy_owl_img_1, snowy_owl_img_2, snowy_owl_img_3, snowy_owl_img_4]

space_crystal_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/crystal_1_space_crystal_1.png").convert()
space_crystal_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/crystal_1_space_crystal_2.png").convert()
space_crystal_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/crystal_1_space_crystal_3.png").convert()
space_crystal_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/crystal_1_space_crystal_4.png").convert()
space_crystal_images = [space_crystal_img_1, space_crystal_img_2, space_crystal_img_3, space_crystal_img_4]

ruby_golem_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/golem_3_ruby_golem_1.png").convert()
ruby_golem_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/golem_3_ruby_golem_2.png").convert()
ruby_golem_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/golem_3_ruby_golem_1.png").convert()
ruby_golem_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/golem_3_ruby_golem_2.png").convert()
ruby_golem_images = [ruby_golem_img_1, ruby_golem_img_2, ruby_golem_img_3, ruby_golem_img_4]

flying_jack_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/pumpkin_1_flying_jack_1.png").convert()
flying_jack_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/pumpkin_1_flying_jack_2.png").convert()
flying_jack_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/pumpkin_1_flying_jack_3.png").convert()
flying_jack_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/pumpkin_1_flying_jack_4.png").convert()
flying_jack_images = [flying_jack_img_1, flying_jack_img_2, flying_jack_img_3, flying_jack_img_4]

# Moss walker attacks are "slow type" - only play once, but at half speed.
# Need to add this as a monter attribute. Amination types, fast or slow.
moss_walker_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/rock_2_moss_walker_1.png").convert()
moss_walker_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/rock_2_moss_walker_2.png").convert()
moss_walker_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/rock_2_moss_walker_3.png").convert()
moss_walker_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/rock_2_moss_walker_4.png").convert()
moss_walker_images = [moss_walker_img_1, moss_walker_img_2, moss_walker_img_3, moss_walker_img_4]


# Other enemy images
rock_walker_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/rock_1_rock_walker_1.png").convert()
rock_walker_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/rock_1_rock_walker_2.png").convert()
rock_walker_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/rock_1_rock_walker_3.png").convert()
rock_walker_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/rock_1_rock_walker_4.png").convert()
rock_walker_images = [rock_walker_img_1, rock_walker_img_2, rock_walker_img_3, rock_walker_img_4]

boulder_bruiser_img_1 = pygame.image.load("Assets/Exports/Art/Monsters/rock_3_boulder_bruiser_1.png").convert()
boulder_bruiser_img_2 = pygame.image.load("Assets/Exports/Art/Monsters/rock_3_boulder_bruiser_2.png").convert()
boulder_bruiser_img_3 = pygame.image.load("Assets/Exports/Art/Monsters/rock_3_boulder_bruiser_3.png").convert()
boulder_bruiser_img_4 = pygame.image.load("Assets/Exports/Art/Monsters/rock_3_boulder_bruiser_4.png").convert()
boulder_bruiser_images = [boulder_bruiser_img_1, boulder_bruiser_img_2, boulder_bruiser_img_3, boulder_bruiser_img_4]

