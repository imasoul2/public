import pygame

# initialise reset
pygame.init() 

# screen resolution
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# display title
pygame.display.set_caption("Pang game") # setting the name

# event loop
running = True
while running:
    # going thruogh all the events in the loop
    for event in pygame.event.get():

        # if the window is closed, stop running the game
        if event.type == pygame.QUIT:
            running = False # break out of the event loop

# event termination
pygame.quit()
print("game terminated")
