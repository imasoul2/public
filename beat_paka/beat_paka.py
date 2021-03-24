import pygame
import os
import random

# initialise reset
pygame.init() 

# screen resolution
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))

# display title
pygame.display.set_caption("Beat the man of 0.006s") # setting the name

# FPS
clock = pygame.time.Clock()

# get current path
current_path = os.path.dirname(__file__) # current path
image_path = os.path.join(current_path, "images") # image folder

#import image
init_background = pygame.image.load(os.path.join(image_path,"grey.png"))
go_background = pygame.image.load(os.path.join(image_path,"green.png"))
gameover_background = pygame.image.load(os.path.join(image_path,"game_over.png"))

# font
game_font = pygame.font.Font(None,40)

#pygame.event.get()
#pygame.mouse.get_pressed() == (1,0,0)

# global variables
rand_num = 0
running = True
lower_bound = 1
higher_bound = 1501
go_condition = False

default_time = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()
game_result = "Get Ready"


while running:
    dt = clock.tick(300)
    # going thruogh all the events in the loop

    for event in pygame.event.get():

        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop       

       # Check the mouse click and the condition
        if pygame.mouse.get_pressed()== (1,0,0) and go_condition :
            print("Mouse 1 button pressed")
            elapsed_time = pygame.time.get_ticks() - default_time
            print("Elapsed" + str(elapsed_time))
            if elapsed_time - start_time < 160:
                game_result = "You beat Paka, your score is {} ms".format(elapsed_time - start_time)
            else:
                game_result = "Paka always wins, your score is {} ms".format(elapsed_time - start_time)

            screen.blit(gameover_background,(0,0)) 
            running = False

    rand_num = random.randint(lower_bound,higher_bound)  
    if rand_num < 1500:
        screen.blit(init_background,(0,0)) 
    elif lower_bound != higher_bound:
        lower_bound,higher_bound = rand_num, rand_num
        screen.blit(go_background,(0,0))
        start_time = pygame.time.get_ticks() - default_time 
        print("Start time" + str(start_time))
        go_condition = True
        game_result = "Click !"
    elif lower_bound == higher_bound:
        pass


    game_body = game_font.render(game_result,True,(255,255,0))
    game_body_rect = game_body.get_rect(center=(int(screen_width/2), int(screen_height/2)))
    screen.blit(game_body,game_body_rect)


        
    
    pygame.display.update()

print("Game terminated")
pygame.time.delay(2000)
