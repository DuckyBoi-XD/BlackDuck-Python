import random

#----Variables----
USER_WALLET = 1000 #Users money
USER_HAND = 0 #Variable to allow Aces work
CARD_SUITS = ("D", "H", "S", "C") #Creates card suits (mainly for CVL code)
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
    "\nSurender: Give up your the hand and recive half of your bet back"
)
#----Variables----

CVL = {} #CVL == Card value list. Create dictionary

for suit in CARD_SUITS: #loops through every card suit
    for value in range(2, 11): #For every card suit this assigns it a number from 2-10
        CVL[f"{suit}{value}"] = value
        #Assigns the value to each card (the last number of varible is value)

CVL[f"{suit}D"] = CVL[f"{suit}Q"] = CVL[f"{suit}K"] = 10
#Creates Duck(Jack), King and Queen, assigns them the value of 10
CVL[f"{suit}A"] = 11 if USER_HAND >= 10 else 1 #Creates the logic and variable for Ace

CVL2 = CVL
# | print(CVL["D2"]+CVL["S4"]) | reminder on how to use dictionary

# | print(random.choices(list(CVL))) | Reminder on how get random value from dictionary
'''
CP1 = random.choices(list(CVL))
CVL2.popitem(CP1)
print(CVL2)
'''
def menu():
    '''menu interface/code'''
    try:
        while True: # creates loop for menu options
            UMP = input(
                "\nWhat would you like to do?\n1) Play\n2) Information \n"
                "3) Settings \n4) Quit\n\n"
            ).strip().lower()
            if UMP in ("1", "play"): #Checks for playing the main game
                print("playing")
            elif UMP in ("2", "information"): #Checks for information
                UPExit = False #turns of multi loop breaker
                while True: #creates loop for infromation menu
                    UIP = input(
                        "\nInformation about this game!\n1) How to play (Normal)\n2) How to play (Advanced)\n"
                        "3) Terminology\n4) Card Values\n5) Tips and Tricks\n6) Back\n\n"
                        ).strip().lower()
                    if UIP in ("1", "how to play (normal)", "htpn"): #checks for How to play normal
                        while True: # creates loop for how to play normal (error checker)
                            UPGN = input(
                                "\nHow To Play (NORMAL)"
                                "\nThe aim of the game is to get higher than the dealer " \
                                "without going over 21." \
                                "\nYou and the dealer gets 2 cards each (one of the dealer's " \
                                "cards will be unknown to the player. " \
                                "\nYou have 2 options (see in terminology), hit: be given " \
                                "another card or stand: don't get anymore cards (note after standing you won't be able to hit)."
                                "\nIf the total value of your cards that you have are over 21, " \
                                "then your lose."
                                "\nOnce you 'hit', your total card value will get closer and " \
                                "closer to 21."
                                "\nIf you your total card value goes over 21, then you lose (bust)"
                                "\nIf you don't want to recive any more cards you stand"
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
                            if UPGN in ("1", "back"): #Checks for back
                                break
                            elif UPGN in ("2", "menu"): #Checks for menu
                                UPExit = True #turns on multi loop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UPExit:#multi loop breaker
                            break
                        while True: #creates loop for how to play advanced
                            UPGA = input(
                                "\nHow To Play (ADVANCED)"
                                    " (Game rules are the same as NORMAL mode except for a few " \
                                    "actions)"
                                    "\nWhen being dealt the first 2 cards, you are given the " \
                                    "option to split and double down. (Terminology)"
                                    "\nWhen you split, you create a second hand and bet the same " \
                                    "amount as the first hand."
                                    "\nWhen you doubling down you double your bet amount."
                                    "\nThese 2 actions can only be used when you are dealt " \
                                    "the first 2 cards. You cannot hit then double down."
                                    "\nYou can however split then double down one or both of your hands."
                                    "\nThrough the game you can surender which will give you back " \
                                    "half of your bet but give up your hand"
                                    "\n\n1) Back"
                                    "\n2) Menu\n\n"
                            ).strip().lower()
                            if UPGA in ("1", "back"): #checks for back
                                break
                            elif UPGA in ("2", "menu"): #checks for menu
                                UPExit = True #turn on milti loop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UPExit: #multi loop breaker
                            break
                    elif UIP == "3" or UIP == "Terminology": #checks for terminology
                        while True: #creates loop for terminology
                            UPT = input(
                                TERMINOLOGY + "\n\n1) Back\n2) Menu\n\n"
                            ).strip().lower()
                            if UPT in ("1", "back"): #checks for back
                                break
                            elif UPT in ("2", "menu"): #checks for menu
                                UPExit = True # turns on multiloop breaker
                                break
                            else:
                                print("\nOption unavaliable, please try again!") #error code
                        if UPExit: #multiloop breaker
                            break
                    elif UIP == "4" or UIP == "Card Values": #checks for vard values
                        while True:
                            CVI = input(
                                "\n"
                            )
                    elif UIP == "5" or UIP == "Tips and Tricks": #checks for tips and tricks
                        print("") ###### NOT DONE
                    elif UIP == "6" or UIP == "Back": #checks for back
                        break
                    else:
                        print("\nOption unavaliable, please try again!") #error code
            elif UMP in ("3", "settings"):
                pass
            elif UMP in ("4", "quit"):
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

menu()
