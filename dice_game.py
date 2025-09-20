import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total
def main():
    print("Welcome to the Dice Game!")
    # Get player names
    player1 = input("enter player 1 name: \n")
    player2 = input("enter player 2 name: \n")

    roll1 = roll_dice()
    roll2 = roll_dice()
    print(player1, "rolled a", roll1)
    print(player2, "rolled a", roll2)
    if roll1 > roll2:
        print(player1, "wins!")
    elif roll2 > roll1:
        print(player2, "wins!")
    else:
        print("It's a tie!")

main()