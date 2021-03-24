import pygame

# initialise reset
pygame.init() 

# screen resolution
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# display title
pygame.display.set_caption("Pang game") # setting the name

# FPS
clock = pygame.time.Clock()

# load background
background = pygame.image.load(r"C:\Users\cj\python\pygame_basic\background.png")

# load sprite/character 
character = pygame.image.load(r"C:\Users\cj\python\pygame_basic\character.png")
character_size = character.get_rect().size  # get the size of rect
character_width = character_size[0] # get width of the sprite
character_height = character_size[1] # get height of the sprite
character_x_pos = screen_width/2 - character_width/2 # init x pos as mid point of width
character_y_pos = screen_height-character_height # init y pos as end of the height

# speed variables for character
to_x = 0
to_y = 0
character_speed = 0.6

# enemy
enemy = pygame.image.load(r"C:\Users\cj\python\pygame_basic\enemy.png")
enemy_size = enemy.get_rect().size  # get the size of rect
enemy_width = enemy_size[0] # get width of the sprite
enemy_height = enemy_size[1] # get height of the sprite
enemy_x_pos = screen_width/2 - enemy_width/2 # init x pos as mid point of width
enemy_y_pos = screen_height/2 -enemy_height # init y pos as end of the height


# event loop
running = True
while running:
    # setting the FPS
    # chracter is suppoed to move 100 
    # if the fps is 20, then it should move by 5
    # if the fps is 100, then it should move by 1
    dt = clock.tick(60)
    
    # going thruogh all the events in the loop
    for event in pygame.event.get():
        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop
        
        # is the key down?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        # if the key is no longer pressed, reset the move co-ordinate
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # reflect the change
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt

    # setting the move boundary
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    #  COLLISION

    # RECT update
    character_rect = character.get_rect()
    # updating the actual image's coordinate
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
 
    enemy_rect = enemy.get_rect()
    # updating the actual image's coordinate
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
   
    # check collision
    if character_rect.colliderect(enemy_rect):
        print("Crashed")
        running = False
    
    # setting the background
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    # or use RGB value for filling out the background
    #screen.fill((0,0,255))

    # update the frame
    pygame.display.update()

# event termination
pygame.quit()
print("game terminated")
