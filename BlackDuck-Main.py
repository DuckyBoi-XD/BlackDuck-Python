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
            UserMenuPick = input(
                "What would you like to do?\n1) Play\n2) Information \n"
                "3) Settings \n4) Quit\n"
            ).strip().lower()
            if UserMenuPick == "1" or UserMenuPick == "Play":
                print("playing")

            elif UserMenuPick == "2" or UserMenuPick == "Information":
                    UIP = (
                        "Information about this game!\n1) How to play (Normal)\n2) How to play (Advanced)\n"
                        "3) Terminology\n4) Card Values\n5) Tips and Tricks\n 6) Back\n"
                        ).strip().lower()
                    if UIP == "1" or UIP == "How to play (Normal)":
                        print("") ###### NOT DONE
                    elif UIP == "2" or UIP == "How to play (Advanced)":
                        print("") ###### NOT DONE
                    elif UIP == "3" or UIP == "Terminology":
                        print("") ###### NOT DONE
                    elif UIP == "4" or UIP == "Card Values":
                        print("") ###### NOT DONE
                    elif UIP == "5" or UIP == "Tips and Tricks":
                        print("") ###### NOT DONE
                    elif UIP == "6" or UIP == "Back":
                        break
                    else:
                        print("\nOption not avaliable\n")


    except KeyboardInterrupt:
        print("Quitting")
        exit()

    except EOFError:
        print("Quitting")
        exit()

print("\nWelcome to BlackDuck. Just like Blackjack, but with ducks!\nYou start with $1000.")

Menu()


# How to play (Normal):\nThe aim of the game is to get higher than the dealer without going over 21.\nYou are first given 2 cards where you have 2 options (see in terminology), be given another card or don't get anymore.\nIf the value of the cards that you have are over 21, then your lose.\n")