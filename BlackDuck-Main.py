import random

UserWallet = 1000
UserHand = 0
CP1 = 1
CP2 = 1
CP3 = 1
CP4 = 1
CP5 = 1
CP6 = 1 
CP7 = 1 
CP8 = 1 
CP9 = 1
CP10 = 1
CP11 = 1

H2 = 2
H3 = 3
H4 = 4
H5 = 5
H6 = 6
H7 = 7
H8 = 8
H9 = 9
H10 = 10
HD = 10
HQ = 10
HK = 10
HA = 11 if UserHand >=10 else 1

S2 = 2
S3 = 3
S4 = 4
S5 = 5
S6 = 6
S7 = 7
S8 = 8
S9 = 9
S10 = 10
SD = 10
SQ = 10
SK = 10
SA = 11 if UserHand >=10 else 1

D2 = 2
D3 = 3
D4 = 4
D5 = 5
D6 = 6
D7 = 7
D8 = 8
D9 = 9
D10 = 10 
DD = 10
DQ = 10
DK = 10
DA = 11 if UserHand >=10 else 1

C2 = 2
C3 = 3
C4 = 4
C5 = 5
C6 = 6
C7 = 7
C8 = 8
C9 = 9
C10 = 10
CD = 10
CQ = 10
CK = 10
CA = 11 if UserHand >=10 else 1

CardDeck = (
    H2, H3, H4, H5, H6, H7, H8, H9, H10, HD, HQ, HK, HA,
    S2, S3, S4, S5, S6, S7, S8, S9, S10, SD, SQ, SK, SA,
    D2, D3, D4, D5, D6, D7, D8, D9, D10, DD, DQ, DK, DA,
    C2, C3, C4, C5, C6, C7, C8, C9, C10, CD, CQ, CK, CA
)

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
                    if UIP == "1" or UIP == "How to play (Normal)":
                        while True:
                            UPGN = input("\nThe aim of the game is to get higher than the dealer without going over 21." \
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
                            "\n2) Menu"
                        ).strip().lower()
                            if UPGN == ("1", "back"):
                                break
                            elif UPGN == ("2", "menu"):
                                UPExit = True
                                break
                    elif UIP == "2" or UIP == "How to play (Advanced)":
                        print("") ###### NOT DONE
                    elif UIP == "3" or UIP == "Terminology":
                        while True:
                            UPT = input(
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


