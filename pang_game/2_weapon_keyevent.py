import pygame
import os

# initialise reset
pygame.init() 

# screen resolution
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# display title
pygame.display.set_caption("Mario Pang") # setting the name

################################################
# 1. user game init

current_path = os.path.dirname(__file__) # current path
image_path = os.path.join(current_path, "images") # image folder

# making the background and stage
background = pygame.image.load(os.path.join(image_path,"background.png"))
stage = pygame.image.load(os.path.join(image_path,"stage.png"))

# setting the stage
stage_size = stage.get_rect().size
stage_height = stage_size[1]
stage_width = stage_size[0] # to put the charcter on top of the stage

#creating charactert
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height - stage_height # taking both heights into account

character_to_x =0
character_speed = 5

# adding the weapon
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

# you can shoot multiple weapons
weapons = []

# weapon speed
weapon_speed = 10

# event loop
running = True
while running:
    # going thruogh all the events in the loop
    for event in pygame.event.get():

        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # create a missile at the position of the character
                weapon_x_pos = character_x_pos + character_width/2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos]) # add to the list of weapons

     # if key is no longer pressed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
                

    # update the position of the character
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # adjust y component of the weapon
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # single line for loop

# single line for loop with ifs
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0] # if the height of pixel is less than zero, keep the weapons in the list

    
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))    
    
    screen.blit(stage,(0,screen_height-stage_height))

    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()


# event termination
pygame.quit()
print("game terminated")