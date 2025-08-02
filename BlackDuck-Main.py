import random
import getch

#----Variables----
USER_WALLET = 1000 #Users money
USER_BANK = random.randrange(1000, 20000)
USER_HAND = 0 #Variable to allow Aces work
USER_NAME = None
CARD_SUITS = ("D", "H", "S", "C") #Creates card suits (mainly for CVL code)
ATM_NUMBER = str(int(random.random() * 1000000000000000 + 4000000000000000))
ID_ATM_NUBMER = ATM_NUMBER * 3
#create atm nember to 16 digits, 4 at start for VISA
TERMINOLOGY = (
    "\nTERMINOLOGY:\n"
    "\nHand: The cards that the payer bets with"
    "\nHit: To be given another card" \
    "\nStand: To revice no more cards (note you can not hit after standing)"
    "\nBust: The value of all your cards is higher than 21" \
    " therefore you lose"
    "\nPush: If both the dealer and player has the same total value, " \
    "no one wins and all bets and given back"
    "\nBlackjack: The value of all your cards total up to exactly " \
    "21, " \
    "giving you 2.5x your bet ammount (unless push)"
    "\n\nDouble Down: After being dealt you can double your bet, but " \
    "after a hitting won't be able to"
    "\nSplit: After being dealt, you can make another hand by using " \
    "one of the cards given to you (you add the same bet as the " \
    "first hand)"
    "\nSurrender: Give up your the hand and recive half of your bet back"
)
CARD_VALUES = (
    "\nCARD VALUES:\n"
    "\nThe number on the card is repersents it's value, for example: "
    "\n6 of Hearts = 6" \
    "\nWith cards like Duck (Jack), King and Queen, they all have a value of 10, "
    "for example:\nQueen of Spades = 10"
    "\nAces has 2 values, if total value of the player's hand is more than 10, "
    "then the value will be 1, otherwise it will have a value of 11. For"
    "example:\nTotal card hand value = 10 | Ace of Clubs = 11"
)
#----Variables----
#----Card Deck/Value---
CVL = {} #CVL == Card value list. Create dictionary

for suit in CARD_SUITS: #loops through every card suit
    for value in range(2, 11): #For every card suit this assigns it a number from 2-10
        CVL[f"{suit}{value}"] = value
        #Assigns the value to each card (the last number of varible is value)

for suit in CARD_SUITS:
    CVL[f"{suit}D"] = CVL[f"{suit}Q"] = CVL[f"{suit}K"] = 10
#Creates Duck (Jack), King and Queen, assigns them the value of 10
for suit in CARD_SUITS:
    CVL[f"{suit}A"] = 11 if USER_HAND >= 10 else 1 #Creates the logic and variable for Ace

#This code is temp to show how copying, getting random card and removing it.
CVL_Temp = CVL.copy() #duplicats the dictionary into a changable list
CP1 = random.choice(list(CVL_Temp.keys()))
CVL_Temp.pop(CP1)
# | print(CVL["D2"]+CVL["S4"]) | reminder on how to use dictionary
# | print(random.choices(list(CVL))) | Reminder on how get random value from dictionary
#----Card Deck/Value---

def NamePick(): #creates function where it lets usert oassign a name
    try:
        while True:
            global USER_NAME
            USER_NAME = input(
                "\nPlease insert name: "
            )
            userNameComfirm = input(
                f"\nYou have inserted: \"{USER_NAME}\""
                "\n\n1) CONFIRM"
                "\n2) REDO\n\n"
            ).strip().lower()
            if userNameComfirm in ("1", "confirm"):
                break
            elif userNameComfirm in ("2", "redo"):
                continue
            else:
                print("\nOption unavaliable, please try again!")
                continue
    except KeyboardInterrupt:
        print("\nQuitting Program\n")
        exit()

    except EOFError:
        print("\nQuitting Program\n")
        exit()

def menu():
    '''menu interface/code'''
    try:
        while True: # creates loop for menu options
            UP_M = input(
                "\nWhat would you like to do?\n1) Play\n2) Information \n"
                "3) Settings \n4) ATM \n5) Quit\n\n"
            ).strip().lower()
            if UP_M in ("1", "play"): #Checks for playing the main game
                print("playing")
            elif UP_M in ("2", "information"): #Checks for information
                UP_Exit = False #turns of multi loop breaker
                while True: #creates loop for infromation menu
                    UP_I = input(
                        "\nInformation about this game!\n1) How to play (Normal)\n2) How to play "
                        "(Advanced)\n"
                        "3) Terminology\n4) Card Values\n5) Tips and Tricks\n6) Back\n\n"
                        ).strip().lower()
                    if UP_I in ("1", "how to play (normal)", "htpn"): #checks for How to play normal
                        while True: # creates loop for how to play normal (error checker)
                            UP_GN = input(
                                "\nHow To Play (NORMAL)\n"
                                "\nThe aim of the game is to get higher than the dealer " \
                                "without going over 21." \
                                "\nYou and the dealer gets 2 cards each (one of the dealer's " \
                                "cards will be unknown to the player. " \
                                "\nYou have 2 options (see in terminology), hit: be given " \
                                "another card or stand: don't get anymore cards (note after " \
                                "standing you won't be able to hit)."
                                "\nIf the total value of your cards that you have are over 21, " \
                                "then your lose."
                                "\nOnce you 'hit', your total card value will get closer and " \
                                "closer to 21."
                                "\nIf you your total card value goes over 21, then you lose (bust)"
                                "\nIf you d2n't want to recive any more cards you stand"
                                "\nAfter standing, dealer gets to recive cards to match or " \
                                "achieve a higher total card value."
                                "\n\nIf your total card value matchs the dealer's total " \
                                "card value, " \
                                "then no one wins and your bet is returned to you (push)"
                                "\nIf your total card value is lower than the dealer's total " \
                                "card value, then you win, reciving double your bet amount"
                                "\nYou win if the dealer bust (like how the payer would)"
                                "\n\n1) Back"
                                "\n2) Menu\n\n"
                            ).strip().lower()
                            if UP_GN in ("1", "back"): #Checks for back
                                break
                            elif UP_GN in ("2", "menu"): #Checks for menu
                                UP_Exit = True #turns on multi loop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UP_Exit:#multi loop breaker
                            break
                    elif UP_I in ("2", "how to play (advanced)", "htpa"):
                        while True: #creates loop for how to play advanced
                            UP_GA = input(
                                "\nHow To Play (ADVANCED)"
                                    " (Game rules are the same as NORMAL mode except for a few " \
                                    "actions)\n"
                                    "\nWhen being dealt the first 2 cards, you are given the " \
                                    "option to split and double down. (Terminology)"
                                    "\nWhen you split, you create a second hand and bet the same " \
                                    "amount as the first hand."
                                    "\nWhen you doubling down you double your bet amount."
                                    "\nThese 2 actions can only be used when you are dealt " \
                                    "the first 2 cards. You cannot hit then double down."
                                    "\nYou can however split then double down one or both of " \
                                    "your hands."
                                    "\nThrough the game you can surrender which will give you " \
                                    "back half of your bet but give up your hand"
                                    "\n\n1) Back"
                                    "\n2) Menu\n\n"
                            ).strip().lower()
                            if UP_GA in ("1", "back"): #checks for back
                                break
                            elif UP_GA in ("2", "menu"): #checks for menu
                                UP_Exit = True #turn on milti loop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UP_Exit: #multi loop breaker
                            break
                    elif UP_I in ("3", "terminology", "term"):
                        while True: #creates loop for terminology
                            UP_T = input(
                                TERMINOLOGY + "\n\n1) Back\n2) Menu\n\n"
                            ).strip().lower()
                            if UP_T in ("1", "back"): #checks for back
                                break
                            elif UP_T in ("2", "menu"): #checks for menu
                                UP_Exit = True # turns on multiloop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UP_Exit: #multiloop breaker
                            break
                    elif UP_I == "4" or UP_I == "Card Values": #checks for vard values
                        while True: #creats a loop for Card values
                            UP_CV = input(
                                CARD_VALUES +
                                "\n\n1) Back"
                                "\n2) Menu\n\n"
                            ).strip().lower()
                            if UP_CV in ("1", "back"): #checks for back
                                break
                            elif UP_CV in ("2", "menu"): #checks for menu
                                UP_Exit = True # turns on multiloop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UP_Exit: #multiloop breaker
                            break
                    elif UP_I in ("5", "tips and tricks", "tat", "t&t"): #checks for tips and tricks
                        while True: #creates loop for Tips and Tricks
                            UP_TT = input(
                                "\nTips and Tricks\n"
                                "\nJacks are replaced by Ducks in this game. I know, great idea"
                                "\nType the number that is in front of the option to move throught" \
                                "the menu quicker"
                                "\nWhen in an information options you can type \"Menu\" (or 2) to go back" \
                                "to the main menu"
                                "\n----MORE TIPS IN THE FUTURE----"
                                "\n\n1) Back"
                                "\n2) Menu"
                            ).strip().lower()
                            if UP_TT in ("1", "back"): #checks for back
                                break
                            elif UP_TT in ("2", "menu"): #checks for menu
                                UP_Exit = True # turns on multiloop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UP_Exit: #multiloop breaker
                            break
                    elif UP_I in ("6", "Back"): #checks for back
                        break
                    else:
                        print("\nOption unavaliable, please try again!") #error code
            elif UP_M in ("3", "settings"):
                pass
            elif UP_M in ("4", "atm"):
                if USER_WALLET <= 0:
                    while True:
                        UP_ATM_N = input(
                            "\nATM\n"
                            "\nPLEASE ENTER CARD NUMBER: "
                        ).strip()
                        if UP_ATM_N == ATM_NUMBER:
                            UP_ATM_P = input(
                                "\nPLEASE ENTER PIN NUMBER: "
                            )
                            if UP_ATM_P == 412311:
                                UP_ATM_W = input(
                                    f"\n{USER_NAME}'s Bank Account\n"
                                    f"\nID NUMBER: {ID_ATM_NUBMER}"
                                    f"\nCARD NUMBER: {ATM_NUMBER}"
                                    f"\nCurrent Balanced: {USER_BANK}"
                                    "\nHow much would you like to withdraw? ($1000 MAX)\n"
                                ).strip().lower()
                                if UP_ATM_W.isdigit():
                                    pass #NOT FINISHED_________________
                else:
                    print(
                        f"\nYou still have ${USER_WALLET} and Mum said for ERERGENCIES ONLY."
                        "\n\nPress any key to go back!"  
                    )
                    getch.getch()
            elif UP_M in ("5", "quit"): 
                print("\nQuitting Game\n")
                exit()
            else:
                print("\nOption unavaliable, please try again!")

    except KeyboardInterrupt:
        print("\nQuitting Program\n")
        exit()

    except EOFError:
        print("\nQuitting Program\n")
        exit()

print("\nWelcome to BlackDuck. Just like Blackjack, but with ducks!\nYou start with $1000.")
NamePick()
menu()
