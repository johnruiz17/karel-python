from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    karel draws a checkerboard pattern using beepers and adapts to the dimensions of each world it is placed in
    the 1x1 and 1x8 worlds have their own set of instructions for karel
    """
    # 1x1 world
    if left_is_blocked():
        put_beeper()
    else:
    # 1x8 world
        if front_is_blocked():
            turn_left()
            place_row()
        else:
    # all other worlds
            while left_is_clear():
                place_row()
                turn_left()
                place_next_row()
            fence_post_check()

def place_row():
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

def move_up():
    """
    pre-condition: karel is facing north
    post-condition: karel is facing west
    conditionally begins the next row of beepers with either a beeper or no beeper based on whether the
    first row ends with or without a beeper
    """
    if no_beepers_present():
        move()
        put_beeper()
        turn_left()
    else:
        move()
        turn_left()

def reposition():
    """
    pre-condition: karel is facing west
    post-condition: karel is facing west and is now placed in the appropriate position to start the next row
    """
    if no_beepers_present():
        move()
    else:
        move()
        if front_is_clear():
            move()

def place_next_row():
    """
    pre-condition: karel is facing north
    post-condition: karel is facing east in the next row up and is positioned in the leftmost part of the row
    if there is not another row to move up to, karel does not move up and place another row
    """
    if front_is_clear():
        move_up()
        reposition()
        place_row()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_right()
    else:
        turn_right()

def fence_post_check():
    """
    pre-condition: karel is facing east and the main while loop has finished running
    post-condition: karel is facing east and another row is placed if there is not a beeper in the second spot
    """
    move()
    if no_beepers_present():
        move_backwards()
        turn_around()
        place_row()

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

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
