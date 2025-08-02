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

#----Card Value Function----
CVL = {} #CVL == Card value list. Create dictionary

for suit in CARD_SUITS: #loops through every card suit
    for value in range(2, 11): #For every card suit this assigns it a number from 2-10
        CVL[f"{suit}{value}"] = value
        #Assigns the value to each card (the last number of varible is value)
for suit in CARD_SUITS:
    CVL[f"{suit}D"] = CVL[f"{suit}Q"] = CVL[f"{suit}K"] = 10
    #Creates Duck(Jack), King and Queen, assigns them the value of 10
for suit in CARD_SUITS:
    CVL[f"{suit}A"] = 11 if USER_HAND <= 10 else 1 #Creates the logic and variable for Ace
#----Card Value Function----

CVL2 = CVL.copy()
print(CVL2)
print(CVL)
print(CVL["SA"])

# | print(CVL["D2"]+CVL["S4"]) | reminder on how to use dictionary

# | print(random.choice(list(CVL2.keys()))) | Reminder on how get random value from dictionary

CP1 = random.choice(list(CVL2.keys()))
print(CP1)
print("\n")
CVL2.pop(CP1)
print(CVL2)
