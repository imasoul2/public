balls = [1,2,3,4]
weapons = [4,5,3,7]

for ball_idx,  ball_val in enumerate(balls):
    print(ball_idx)
    for weapon_idx, weapon_val in enumerate(weapons):
        print(weapon_idx)
        if ball_val == weapon_val:
            break
    else:
        continue
    break