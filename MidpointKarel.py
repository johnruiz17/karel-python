from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    karel finds the midpoint by checkering the row, removing the outer beepers,
    and then checking to see if there is a fifth spot beeper present to determine what the midpoint is
    the midpoint1 and midpoint2 worlds have their own set of instructions for karel
    """
    # midpoint1 world
    if front_is_blocked():
        put_beeper()
    else:
    # midpoint2 world
        move()
        if front_is_blocked():
            move_backwards()
            put_beeper()
        else:
    # all other midpoint worlds
            reset_karel()
            checkerboard_row()
            reset_karel()
            remove_outer_beepers()
            reset_karel()
            mark_midpoint()
            reset_karel()
            check_spot_seven()
            reset_karel()
            check_second_row()

def checkerboard_row():
    """
    pre-condition: karel is facing east at the leftmost part of the row
    post-condition: karel is facing east at the rightmost part of the row and the row is now checkered
    after the while loop, conditionally places correct odd or even pattern based on previous beeper
    """
    while front_is_clear():
        put_beeper()
        for i in range(2):
            if front_is_clear():
                move()
    move_backwards()
    if no_beepers_present():
        move_backwards()
        put_beeper()
    else:
        move_backwards()

def reset_karel():
    """
    pre-condition: karel is facing east
    post-condition: karel is back to starting position
    """
    turn_around()
    go_to_wall()
    turn_around()

def remove_outer_beepers():
    """
    pre-condition: karel is facing east in starting position
    post-condition: karel is facing east and outer beepers have been removed
    """
    safe_pickup()
    go_to_wall()
    safe_pickup()
    move_backwards()
    safe_pickup()
    turn_around()

def turn_right():
    """
    pre-condition: command runs regardless of karel's starting position
    post-condition: karel turns right relative to its starting position
    """
    for i in range(3):
        turn_left()

def turn_around():
    """
    pre-condition: command runs regardless of karel's starting position
    post-condition: karel turns around and faces the opposite way it was facing before command runs
    """
    turn_left()
    turn_left()

def move_backwards():
    """
    pre-condition: command runs regardless of karel's starting position
    post-condition: karel is now facing the opposite direction that it was facing before this command
    ran and has moved once in that direction
    """
    turn_around()
    move()

def safe_pickup():
    """
    pre-condition: command runs regardless of karel's position
    post-condition: karel has picked up a beeper if there was one where it was standing
    """
    if beepers_present():
        pick_beeper()

def go_to_wall():
    """
    pre-condition: command runs regardless of karel's position
    post-condition: karel is facing a wall
    """
    while front_is_clear():
        move()

def go_to_spot_five():
    """
    pre-condition: karel is facing east in starting position
    post-condition: karel is at the fifth column in the first row
    """
    for i in range(4):
        move()

def backtrack():
    """
    pre-condition: command runs regardless of karel's position
    post-condition: karel has turned around to face to opposite direction and moved twice
    """
    move_backwards()
    move()

def paint():
    """
    pre-condition: karel is facing north and is standing on the midpoint
    post-condition: karel is facing east and has painted the corner above the midpoint blue
    """
    move()
    paint_corner(BLUE)
    turn_around()
    move()
    turn_left()

def mark_midpoint():
    """
    pre-condition: karel is facing east at the starting point
    post-condition: karel is facing east and has painted the corner above the midpoint blue
    if there is a beeper in the fifth spot, karel removes the preceding beeper and marks the fifth spot as the midpoint
    if not, karel moves back and marks the third spot as the midpoint
    """
    go_to_spot_five()
    if beepers_present():
        backtrack()
        safe_pickup()
        backtrack()
        turn_left()
        paint()
    else:
        backtrack()
        turn_right()
        paint()

def check_spot_seven():
    """
    pre-condition: karel is facing east
    post-condition: karel is facing east and has removed a beeper from the seventh column if there was one
    """
    go_to_spot_five()
    for i in range(2):
        if front_is_clear():
            move()
    safe_pickup()

def check_second_row():
    """
    pre-condition: karel is facing east in the starting position
    post-condition: karel is facing south and is standing on the midpoint beeper
    """
    turn_left()
    move()
    turn_right()
    while front_is_clear():
        if corner_color_is(BLUE):
            paint_corner(BLANK)
            turn_right()
            move()
        else:
            move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
