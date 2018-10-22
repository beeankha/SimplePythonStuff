from sys import exit
import time

def start():
    print("You are in a dark room.")
    time.sleep(1)
    print("There is a door to your right and left.")
    time.sleep(1)
    print("Which one do you open?")
    time.sleep(1)
    print("Type in 'right' or 'left':")

    choice = input("> ")

    if choice == "left":
        feast_room()
    elif choice == "right":
        cthulhu_room()
    else:
        escape("You don't know how to type, so you stumble around the room until you starve.")


def feast_room():
    print("There is an enormous table in this room.")
    time.sleep(1)
    print("A lavish feast is laid out on it.")
    time.sleep(1)
    print("Do you eat any of the food?.")
    time.sleep(1)
    print("Type in 'yes' or 'no':")
    feast_eaten = False

    while True:
        choice = input("> ")

        if choice == "yes":
            print("You start to froth at the mouth.")
            time.sleep(1)
            print("You totes die.")
            time.sleep(1)
            exit(0)
        elif choice == "no" and not feast_eaten:
            print("You walk past the table and see a door.")
            time.sleep(1)
            print("Do you open it?")
            time.sleep(1)
            print("Type in 'yes' or 'no':")
            choice = input("> ")

            if choice == "yes":
                gold_room()
            if choice == "no":
                print("You wander around aimlessly...")
                time.sleep(1)
                print("...and eventually starve to death.")
                time.sleep(1)
                exit(0)

        elif choice == "yes" and feast_eaten:
            gold_room()
        else:
            print("I have no idea what that means.")


def gold_room():
    print("This room is full of gold.  How much do you take?")
    time.sleep(1)
    print("Enter a digit in multiples of ten.")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        escape("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        escape("You greedy bastard!")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    time.sleep(1)
    print("He, it, whatever, stares at you and you go insane.")
    time.sleep(1)
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        escape("Well that was tasty!")
    else:
        cthulhu_room()


def escape(why):
    print(why, "You find an exit and escape the trap!")
    exit(0)


start()
