import random

USER_WALLET = 1000 #Users money
USER_HAND = 0 #Variable to allow Aces work
CARD_SUITS = ("D", "H", "S", "C") #Creates card suits (mainly for CVL code)

CVL = {} #CVL == Card value list. Create dictionary

for suit in CARD_SUITS: #loops through every card suit
    for value in range(2, 11): #For every card suit this assigns it a number from 2-10
        CVL[f"{suit}{value}"] = value #Assigns the value to each card (the last number of varible is value)

CVL[f"{suit}D"] = CVL[f"{suit}Q"] = CVL[f"{suit}K"] = 10 #Creates Duck(Jack), King and Queen, assigns them the value of 10
    
CVL[f"{suit}A"] = 11 if USER_HAND >= 10 else 1 #Creates the logic and variable for Ace


# |print(CVL["D2"]+CVL["S4"])| reminder on how to use dictionary

def Menu():
    try:
        while True:
            UMP = input(
                "\nWhat would you like to do?\n1) Play\n2) Information \n"
                "3) Settings \n4) Quit\n\n"
            ).strip().lower()
            if UMP in ("1", "play"):
                print("playing")
            elif UMP in ("2", "information"):
                UPExit = False
                while True:
                    UIP = input(
                        "\nInformation about this game!\n1) How to play (Normal)\n2) How to play (Advanced)\n"
                        "3) Terminology\n4) Card Values\n5) Tips and Tricks\n6) Back\n\n"
                        ).strip().lower()
                    if UIP in ("1", "how to play (normal)", "htpn"):
                        while True:
                            UPGN = input(
                                "\nHow to play (NORMAL)"
                                "\nThe aim of the game is to get higher than the dealer without going over 21." \
                                "\nYou are first given 2 cards where you have 2 options (see in terminology), hit: be given another card or stand: don't get anymore cards."
                                "\nIf the value of the cards that you have are over 21, then your lose."
                                "\nOnce you 'hit', your total card value will get closer and closer to 21."
                                "\nIf you your total card value goes over 21, then you lose (bust)"
                                "\nIf you don't want to recive any more cards you stand"
                                "\nAfter standing, dealer gets to recive cards to match or achieve a higher total card value."
                                "\n\nIf your total card value matchs the dealer's total card value, then no one wins and your bet is returned to you (push)"
                                "\nIf your total card value is lower than the dealer's total card value, then you win, reciving double your bet amount"
                                "\nYou win if the dealer bust (like how the payer would)"
                                "\n\n1) Back"
                                "\n2) Menu\n"
                            ).strip().lower()
                            if UPGN in ("1", "back"):
                                break
                            elif UPGN in ("2", "menu"):
                                UPExit = True
                                break
                            else:
                                print("\nOption unavaliable, please try again!")
                        if UPExit:
                            break
                    elif UIP == "2" or UIP == "How to play (Advanced)":
                        UPGA = input(
                            "\n"
                        )
                    elif UIP == "3" or UIP == "Terminology":
                        while True:
                            UPT = input(
                                "\nTERMINOLOGY:\n"
                                "\nHand: The cards that the payer bets with"
                                "\nHit: To be given another card\nStand: To revice no more cards"
                                "\nBust: The value of all your cards is higher than 21 therefore you lose"
                                "\nPush: If both the dealer and player has the same total value, no one wins and all bets and given back"
                                "\nBlackjack: The value of all your cards total up to exactly 21, giving you 2.5x your bet ammount (unless push)"
                                "\n\nDouble Down: After being dealt you can double your bet, but after a hitting won't be able to"
                                "\nSplit: After being dealt, you can make another hand by using one of the cards given to you (you add the same bet as the first hand)"
                                "\nSurender: Give up your the hand and recive half of your bet back"
                                "\n\n1) Back"
                                "\n2) Menu\n\n"
                            ).strip().lower()
                            if UPT in ("1", "back"):
                                break
                            elif UPT in ("2", "menu"):
                                UPExit = True
                                break
                            else:
                                print("\nOption unavaliable, please try again!")
                        if UPExit:
                            break
                    elif UIP == "4" or UIP == "Card Values":
                        print("") ###### NOT DONE
                    elif UIP == "5" or UIP == "Tips and Tricks":
                        print("") ###### NOT DONE
                    elif UIP == "6" or UIP == "Back":
                        break
                    else:
                        print("\nOption unavaliable, please try again!")
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

Menu()
