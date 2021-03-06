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

# move co
to_x = 0
to_y = 0


# event loop
running = True
while running:
    # going thruogh all the events in the loop
    for event in pygame.event.get():
        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop
        
        # is the key down?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
        
        # if the key is no longer pressed, reset the move co-ordinate
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # reflect the change
    character_x_pos += to_x
    character_y_pos += to_y

    # setting the move boundary
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
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
