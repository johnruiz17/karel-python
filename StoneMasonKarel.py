from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    karel repairs the column going upwards, moves down the column, moves to the next column, and continues
    until all columns have been repaired
    """
    while front_is_clear():
        repair_up()
        move_down()
        if front_is_clear():
            next_repair()
    repair_up()
    move_down()

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

def repair():
    """
    pre-condition: karel is on a spot that needs to be checked for a repair
    post-condition: if there are no beepers present, karel places beeper
    """
    if no_beepers_present():
        put_beeper()

def repair_up():
    """
    pre-condition: karel is facing east and is positioned on the column that needs to be repaired
    post-condition: karel is facing south and a beeper was placed in each position that did not have one in column
    """
    turn_left()
    repair()
    while front_is_clear():
        move()
        repair()
    repair()
    turn_around()

def move_down():
    """
    pre-condition: karel is facing south
    post-condition: karel is facing east and has moved down the column
    """
    while front_is_clear():
        move()
    turn_left()

def next_repair():
    """
    pre-condition: karel is facing east at the bottom of the column that was just repaired
    post-condition: karel is facing east positioned at the new column that needs to be repaired
    """
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
