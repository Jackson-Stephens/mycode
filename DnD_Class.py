#!/usr/bin/env python3

def main():
    print("Dungeons and Dragons, what class are you Quiz? ")
    print("For every question answer with either a) or b)")
    tree()
name = input("What is your name? ")
def tree():
    Answer = input(" How do you face dangerous situation?\n a) Charge in or b) Attack from afar? ")
    
    if Answer == ("a)"):
        print(" Brave! Next Question! ")
        branch_one()
    if Answer == ("b)"):
        print(" Smart! Next Question! ")
        branch_two()
    else:
        print(" Try answering with a) or b) ")

def branch_one():
    Answer = input(" Do you prefer,\n a) speed or b) strength? ")

    if Answer == ("a)"):
        print(" I agree! Next Question! ")
        branch_three()
    if Answer == ("b)"):
        print(" I like your choice, Next Question! ")
        branch_four()
    else:
        print(" Try answering with a) or b) ")

def branch_two():
    Answer = input(" What do you rely on most, \n a) your skill or b) magic? ")

    if Answer == ("a)"):
        print("Good, next question!")
        branch_five()
    elif Answer == ("b)"):
        print("Good, next question!")
        branch_six()
    else:
        print("Try answering with a) or b) ")
def branch_three():
    Answer = input("Do you love kung-fu movies? \n a) Yes! Bruce Lee is my idol or b) Not really into those. ")
    
    if Answer == ("a)"):
        print(" Congratulations, " + name + " your class is the Monk, you are wise, and you use your deadly trained fists to defeat opponents.")
    elif Answer == ("b)"):
        print(" Ok, next question.")
        branch_seven()
    else:
        print("Try again! ")
def branch_four():
    Answer = input(" Are you good with the Gods?\n a) Got em on speed dial or b) Nope, not really. ")

    if Answer == ("a)"):
        print(" Congratulations, " + name + " your class is the Paladin! A holy warrior dedicated to righteousness and spreading good where-ever they go.")
    elif Answer == ("b)"):
        print( " Congratulations, " + name + " your class is the Barbarian! A savage warrior who embraces their animal nature. You are toughened by wild homelands and despise civilation.")
    else:
        print("Play again!")
def branch_five():
    Answer = input(" How good are you at keeping quiet?\n a) ..pure silence.. or b) I don't know I've never tried! ")

    if Answer == ("a)"):
        print("..........")
        branch_eight()
    elif Answer == ("b)"):
        print("Congratulations " + name + " your class is the Bard! A quick witted musical warrior. Most stick to casting righteous lute solos, but  some inspired by songs of valor take up the sword.")
    else:
        print("Try again! ")
def branch_six():
    Answer = input(" Where does your power come from,\n a) The Gods or b) From within, and self taught? ")
    
    if Answer == ("a)"):
        print("Congratulations, " + name + " your class is the Cleric! A chosen agent of the gods who channel divine power!")
    elif Answer == ("b)"):
        print("Congratulations, " + name + " your class is the Wizard! A wise arcane scholar whose power has come from intensive studies of magical books! ")
    else:
        print("Play again!")

def branch_seven():
    Answer = input(" You are most deadly because,\n  a) you are a master hunter or b) you are a born schemer?" )

    if Answer == ("a)"):
        print("congratulations, " + name + " your class is the Ranger. Uses a mix of nature magic and martial training to quickly hunt anything.")
    elif Answer == ("b)"):
        print("Congratulations, " + name + " your class is the Rogue. Skilled and resourceful they execute all their plans with cunning and precision, often times luring there foes into traps.")
    else:
        print("Play again!")

def branch_eight():
    Answer = input("Do you keep any pets,\n a) My best friends are ferocious beasts or b) What like a gerbil?" )

    if Answer == ("a)"):
        print("Congratulations," + name + " your class is the ranger. Uses a mix of nature magic and martial training to quickly hunt anything.")
    elif Answer == ("b)"):
        print("Congratulations," + name + " your class is the rouge. Skilled and resourceful they execute all their plans with cunning and precision, often times luring there foes into traps.")

main()






