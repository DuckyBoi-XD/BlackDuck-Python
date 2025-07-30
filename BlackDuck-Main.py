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

print("Welcome to BlackDuck. Just like Blackjack, but with ducks!\nYou start with $1000.")

def Menu():
    try:
        while True:
            UserMenuPick = input("What would you like to do?\n1) Play\n2) Information \n3) Settings \n4) Quit")
            if UserMenuPick == "1" or "Play":
                print("playing")
    except:
        pass