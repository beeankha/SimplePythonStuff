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
        pit_room()
    else:
        print("You apparently don't know how to type, so you stumble around the room until you starve.")
        time.sleep(1)
        play_again()

def feast_room():
    print("There is an enormous table in this room.")
    time.sleep(1)
    print("A lavish feast is laid out on it.")
    time.sleep(1)
    print("Do you eat any of the food?.")
    time.sleep(1)
    print("Type in 'yes' or 'no':")
    choice = input("> ")

    if choice == "yes":
        print("You start to froth at the mouth.")
        time.sleep(1)
        print("You totes die.")
        time.sleep(1)
        play_again()
    if choice == "no":
        feast_door()
    else:
        print("I have no idea what that means.")
        time.sleep(1)
        feast_room()

def feast_door():
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
        play_again()
    else:
        print("Sorry, that input is invalid.")
        time.sleep(1)
        feast_door()


def gold_room():
    print("This room is full of gold.  How much do you take?")
    time.sleep(1)
    print("Enter a digit in multiples of ten.")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        print("You need to type a number!")
        time.sleep(1)
        gold_room()

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        escape("Wow, you're super greedy!")

def pit_room():
    print("There is an enormous pit in the middle of the room.")
    time.sleep(1)
    print("It looks like you might be able to jump over it...")
    time.sleep(1)
    print("...or you can shimmy around the edge.")
    time.sleep(1)
    print("Do you jump or walk carefully around the edge?")
    time.sleep(1)
    print("Type in 'leap' or 'shimmy':")

    choice = input("> ")

    if choice == "leap":
        print("You jump, and are over the pit...")
        time.sleep(1)
        print("...but it turns out that you haven't trained for this so you fall and die.")
        time.sleep(1)
        exit(0)
    elif "shimmy" in choice:
        cube_room()
    else:
        print("I have no idea what that means.")
        time.sleep(1)
        pit_room()

def cube_room():
    print("You find an opening in the wall and go through it...")
    time.sleep(1)
    print("...and find yourself in a room with a glowing cube on top of a pedestal.")
    time.sleep(1)
    print("Do you touch the cube?")
    time.sleep(1)
    print("Type in 'yes' or 'no':")
    choice = input("> ")

    if choice == "yes":
        print("The glow of the cube engulfs you.")
        time.sleep(1)
        print("Then you start vibrating until all of your atoms come apart...")
        time.sleep(1)
        print("...and you die.")
        time.sleep(1)
        exit(0)
    elif choice == "no":
        escape("Good choice!")
    else:
        print("Sorry, that wasn't a valid choice.")
        time.sleep(1)
        cube_room()

def escape(why):
    print(why, "You find an exit and escape the trap!")
    play_again()

def play_again():
    print("Play again? Type 'yes' or 'no':")

    play_choice = input("> ")
    if play_choice == "yes":
        start()
    if play_choice == "no":
        print("Bye!")
        time.sleep(1)
        exit(0)
    else:
        print("Sorry, I didn't understand that.")
        time.sleep(1)
        play_again()

start()
