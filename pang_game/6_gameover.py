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

# FPS
clock = pygame.time.Clock()

################################################
# 1. user game init

current_path = os.path.dirname(__file__) # current path
image_path = os.path.join(current_path, "images") # image folder

# making the background and stage
background = pygame.image.load(os.path.join(image_path,"background.png"))
stage = pygame.image.load(os.path.join(image_path,"stage.png"))

heart = pygame.image.load(os.path.join(image_path,"heart.png"))

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

character_to_x = 0
character_speed = 5

# adding the weapon
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]

# life
life = 1

# you can shoot multiple weapons
weapons = []

# weapon speed
weapon_speed = 5

# make balloons in the list
ball_images = [
    pygame.image.load(os.path.join(image_path,"balloon1.png")),
    pygame.image.load(os.path.join(image_path,"balloon2.png")),
    pygame.image.load(os.path.join(image_path,"balloon3.png")),
    pygame.image.load(os.path.join(image_path,"balloon4.png"))]

# balloon speed depends on the size of the ball
ball_speed_y = [-18, -15, -12, -9] # values for index 0,1,2,3 

# balloons
balls = []

# init ball
balls.append({
    "pos_x" : 50, 
    "pos_y" : 50,
    "img_idx": 0,
    "to_x":3,  # x-direction, left if -3 , right if +3
    "to_y":-6,  # y-diecrtion,initially falls down as -6
    "init_spd_y":ball_speed_y[0]})


# variables for balls and weapons to disappear
weapon_to_remove = -1
ball_to_remove = -1

# Font
game_font = pygame.font.Font(None,40)
total_time = 100
start_time = pygame.time.get_ticks()

# game result message / variable : Timeout, Game Over, Finished
game_result = "Game Over"

# event loop
running = True
while running:
    dt = clock.tick(60)
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

# define the position of balls
    for ball_idx, ball_val in enumerate(balls):
        # get the position of the balls and image
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # define the ball size using the index
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # if the ball hits the side boundaries then change its direction
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1 # change the sign

        # if the ball hits the stage
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"] # negative number
        else:
            ball_val["to_y"] += 0.5 # this will make the ball projectile, eventually hitting the stage again

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
# collision between character and balls

# update character rect
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        # get the position of the balls and image
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # update ball rect
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        if character_rect.colliderect(ball_rect):
            
            life -= 1
            if life < 0:
                game_result = "Game Over"
                life = 0
                running = False

            break
            
# collision between balls and weapons
        for weapon_idx, weapon_val in enumerate(weapons):
            # update pos and rect of each weapon
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # collision check
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # value set to remove
                ball_to_remove = ball_idx  

                # if it's not the smallest sized ball, split it
                if ball_img_idx < 2:
                    # Get current ball size
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # Info about the split ball
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect[0]
                    small_ball_height = small_ball_rect[1]


                    # split to the left
                    balls.append({
                        "pos_x" : ball_pos_x + ball_width / 2 - small_ball_width/2, # (  X(  )  )
                        "pos_y" : ball_pos_y + ball_height/2 - small_ball_height/2,
                        "img_idx": ball_img_idx + 1,
                        "to_x":-3,  # x-direction, left if -3 , right if +3
                        "to_y":-6,  # y-diecrtion,initially falls down as -6
                        "init_spd_y":ball_speed_y[ball_img_idx + 1]})
                    # split to the right
                    balls.append({
                        "pos_x" : ball_pos_x + ball_width/2 - small_ball_width/2, 
                        "pos_y" : ball_pos_y + ball_height/2 - small_ball_height/2,
                        "img_idx": ball_img_idx + 1,
                        "to_x":3,  # x-direction, left if -3 , right if +3
                        "to_y":-6,  # y-diecrtion,initially falls down as -6
                        "init_spd_y":ball_speed_y[ball_img_idx + 1]})

                break
        else: # continue the game
            continue # if the for weapons 
        break
    # remove the colliding weapons and balls
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False



# display 
    
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))    
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage,(0,screen_height-stage_height))

    screen.blit(character,(character_x_pos,character_y_pos))

# work out the time diff
    elapsed_time = (pygame.time.get_ticks() - start_time)/1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)),True,(255,255,255))
    screen.blit(timer, (10,10))
    screen.blit(heart,(600,10))
    life_count = game_font.render(str(life),True,(255,255,0))
    screen.blit(life_count,(580,15))

    if total_time - elapsed_time < 0:
        game_result = "Time Out"
        running = False

    pygame.display.update()


msg = game_font.render(game_result, True, (255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)

pygame.display.update()


# event termination
pygame.time.delay(2000)
pygame.quit()
print("game terminated")
