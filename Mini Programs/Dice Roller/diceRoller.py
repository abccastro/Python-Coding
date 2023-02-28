"""
Create a program that uses a function to simulate the roll of a die

Created by: Auradee Castro
"""

import random


def startDiceRoller():
    print("Dice Roller")

    roll_counter = 0
    while True:
        if roll_counter == 0:
            to_roll_dice = input("Roll the dice? (y/n): ")
        else:
            to_roll_dice = input("Roll again? (y/n): ")

        if to_roll_dice.lower() == "y":
            roll_counter += 1

            dice_one = rollDice()
            dice_two = rollDice()
            displayResult(dice_one, dice_two)

        elif to_roll_dice.lower() == "n":
            print("Thank you for using Dice Roller!")
            break
        else:
            print("Invalid input. Try again.")


def rollDice():
    return random.randint(1, 6)


def displayResult(dice_one, dice_two):
    print("Die 1:", dice_one)
    print("Die 2:", dice_two)
    print("Total:", (dice_one + dice_two))

    if dice_one == 1 and dice_two == 1:
        print("Snake eyes!")
    elif dice_one == 6 and dice_two == 6:
        print("Boxcars!")


if __name__ == "__main__":
    startDiceRoller()
