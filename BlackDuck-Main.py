import random

USER_WALLET = 1000 #Users money
UserHand = 0 #Variable to allow Aces work

for i in range(1, 11): #Collects each number in the range
    exec("H{i} = {i}") #Create/assigns each variable with the value 
HD = HQ = HK = 10 #Assigns variables with value
HA = 11 if UserHand >=10 else 1 #assigns if statement to ace and assigns the main value

for i in range(1, 11): #Repeat
    exec("S{i} = {i}")
SD = SQ = SK = 10
SA = 11 if UserHand >=10 else 1

for i in range(1, 11): #Repeat
    exec(f"D{i} = {i}")
DD = DQ = DK = 10
DA = 11 if UserHand >=10 else 1

for i in range(1, 11): #Repeat
    exec(f"C{i} = {i}")
CD = CQ = CK = 10
CA = 11 if UserHand >=10 else 1

CardDeck = (
    H2, H3, H4, H5, H6, H7, H8, H9, H10, HD, HQ, HK, HA,
    S2, S3, S4, S5, S6, S7, S8, S9, S10, SD, SQ, SK, SA,
    D2, D3, D4, D5, D6, D7, D8, D9, D10, DD, DQ, DK, DA,
    C2, C3, C4, C5, C6, C7, C8, C9, C10, CD, CQ, CK, CA
)

print(H1)
'''
CurrentCardDeck = CardDeck

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


'''