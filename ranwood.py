import random
import randolph_flippy, randolph_palindrome

def randolph():
    o = 1
    programs = ['flippy', 'palindrome']
    for i in programs:
        print(f'{o}: {i}')
        o = o + 1
    choice2 = input("Which item would you like to use? just type the number associated with the program.")
    match choice2:
        case '1':
            randolph_flippy.main()
            pass
        case '2':
            randolph_palindrome.main()

def smallwood():
    print('in development')

print("Welcome to RANWOOD, a collaboration project between De'Andre Randolph and Matthew Smallwood. This project will function as a double portfolio, displaying projects from Matthew Smallwood and De'Andre Randolph ( and his Web Development Company, Voyddfolio).")
choice = input("Would you like to pick from Randolph's projects (type 'R'), or Smallwood's projects (type 'S')?").upper()

match choice:
    case 'R':
        randolph()
    case 'S':
        smallwood()

