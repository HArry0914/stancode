"""
File: Steeplechase.py
Name:何竑毅
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()



def jump():
    up()
    cross()
    down()


def up():
   turn_left()
   while not right_is_clear():
       move()


def down():
    while front_is_clear():
        move()
    turn_left()


def cross():
    turn_right()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()












####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
