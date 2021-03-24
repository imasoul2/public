import pygame

# initialise reset
pygame.init() 

# screen resolution
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# display title
pygame.display.set_caption("Pang game") # setting the name

# load background
background = pygame.image.load(r"C:\Users\cj\python\pygame_basic\background.png")

# load sprite/character 
character = pygame.image.load(r"C:\Users\cj\python\pygame_basic\character.png")
character_size = character.get_rect().size  # get the size of rect
character_width = character_size[0] # get width of the sprite
character_height = character_size[1] # get height of the sprite
character_x_pos = screen_width/2 - character_width/2 # init x pos as mid point of width
character_y_pos = screen_height-character_height # init y pos as end of the height



# event loop
running = True
while running:
    # going thruogh all the events in the loop
    for event in pygame.event.get():
        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop
    
    # setting the background
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    # or use RGB value for filling out the background
    #screen.fill((0,0,255))

    # update the frame
    pygame.display.update()

# event termination
pygame.quit()
print("game terminated")
