from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    karel moves to the newspaper, picks it up, and goes back home
    """
    move_to_newspaper()
    pick_up_newspaper()
    go_back_home()

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

def move_to_newspaper():
    """
    pre-condition: karel is facing east inside the house at starting position
    post-condition: karel is on newspaper
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()

def pick_up_newspaper():
    """
    pre-condition: karel is standing on beeper facing east
    post-condition: karel picks up beeper and is facing west
    """
    pick_beeper()
    turn_around()

def go_back_home():
    """
    pre-condition: karel is at the newspaper position facing west
    post-condition: karel moves back to starting position and is facing east
    """
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
