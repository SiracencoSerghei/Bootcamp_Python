def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_left()
        
    else:
        turn_right()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
