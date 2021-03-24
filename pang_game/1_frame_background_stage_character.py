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



# event loop
running = True
while running:
    # going thruogh all the events in the loop
    for event in pygame.event.get():

        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop

    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()


# event termination
pygame.quit()
print("game terminated")
