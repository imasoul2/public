import pygame
import random
################################
# INIT #
################################
# initialise reset (MUST USE)
pygame.init() 

# screen resolution
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# display title
pygame.display.set_caption("Pang game") # setting the name

# FPS (MUST USE)
clock = pygame.time.Clock()

# score

score = 0

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

enemy_x_pos = random.randint(0,int(screen_width- enemy_width/2))
enemy_y_pos = enemy_height # init y pos as end of the height


# speed variables for enemy
enemy_speed = 0.2

# font definition
game_font = pygame.font.Font(None,40)
score_font = pygame.font.Font(None, 30)

# Total Time
total_time = 20

# start time
start_ticks = pygame.time.get_ticks() # get start ticks

################################
# GAME INIT #
################################


# event loop
running = True
while running:
    # setting the FPS
    # chracter is suppoed to move 100 
    # if the fps is 20, then it should move by 5
    # if the fps is 100, then it should move by 1
    dt = clock.tick(60)

################################
# GAME EVENT #
################################
    
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
                pass
            
            elif event.key == pygame.K_DOWN:
                pass
              
        
        # if the key is no longer pressed, reset the move co-ordinate
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # reflect the change
    character_x_pos += to_x*dt
    character_y_pos += to_y*dt
    enemy_y_pos += enemy_speed*dt

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

    # Put the timer in seconds
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000

    timer = game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    screen.blit(timer, (10,10))
    score_points = score_font.render("Score: "+str(score),True,(255,255,255))
    screen.blit(score_points, (10,40))
    
   
    # if the enemy is passed the lower boundary
    if enemy_y_pos > screen_height :
        score += 1
        # reset
        enemy_x_pos = random.randint(0,int(screen_width- enemy_width/2))
        enemy_y_pos = enemy_height 

    if total_time - elapsed_time < 0:
        print("Time out")
        running = False
    

   


    # update the frame
    pygame.display.update()

# event termination
score_font.set_bold(True)
score_points = score_font.render("Your Final Score: "+str(score),True,(255,255,255))
screen.blit(score_points, (10,40))
pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
print("game terminated")
