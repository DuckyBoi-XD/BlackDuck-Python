import random
import getch

#----Variables----
GAME_MODE = None
USER_WALLET = 1000 #Users money
USER_BANK = random.randrange(1000, 20000)
USER_HAND = 0 #Variable to allow Aces work
USER_NAME = None
CARD_SUITS = ("D", "H", "S", "C") #Creates card suits (mainly for CVL code)
ATM_NUMBER = str(int(random.random() * 1000000000000000 + 4000000000000000))
ID_ATM_NUMBER = int(ATM_NUMBER) * 3
BlackDuck_Mode = 0
BlackDuck_Total = True

#create atm nember to 16 digits, 4 at start for VISA
#crate id number by times inthe atm number by 3
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
) #to use in multiple places
CARD_VALUES = (
    "\nCARD VALUES:\n"
    "\nCard are labeled with the suit in front and value on the end. For " \
    "example: C9 = 9 of Clubs or DK = King of Diamonds"
    "\nThe number on the card is repersents it's value, for example: "
    "\nH6 = 6" \
    "\nWith cards like Duck (Jack), King and Queen, they all have a value of 10, "
    "for example:\nSQ = 10"
    "\nAces has 2 values, if total value of the player's hand is more than 10, "
    "then the value will be 1, otherwise it will have a value of 11. For"
    "example:\nTotal card hand value = 10 | CA = 11"
) #to use in multiple places
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

for suit in CARD_SUITS: #Creates the logic and variable for Ace
    if GAME_MODE == "BlackDuck":
        CVL[f"{suit}A"] = 11 if USER_HAND >= 10 else 1
    elif GAME_MODE == "RTD":
        CVL[f"{suit}A"] = 11

# | print(CVL["D2"]+CVL["S4"]) | reminder on how to use dictionary
# | print(random.choices(list(CVL))) | Reminder on how get random value from dictionary
#----Card Deck/Value---

#----
#----Name Function----
def namePick(): #creates function where it lets usert oassign a name
    try:
        UP_Exit = False
        while True:
            global USER_NAME
            USER_NAME = input(
                "\nPlease insert name: "
            )
            if USER_NAME.isalpha():
                while True:
                    userNameComfirm = input(
                        f"\nYou have inserted: \"{USER_NAME}\""
                        "\n\n1) CONFIRM"
                        "\n2) REDO\n\n"
                    ).strip().lower()
                    if userNameComfirm in ("1", "confirm"):
                        UP_Exit = True
                        break
                    elif userNameComfirm in ("2", "redo"):
                        break
                    else:
                        print("\nOption unavaliable, please try again!")
                        continue
                if UP_Exit:
                    UP_Exit = False
                    break
            else:
                print(
                    "\nERROR: Please use letter"
                )
    except KeyboardInterrupt:
        print("\nQuitting Program\n")
        exit()

    except EOFError:
        print("\nQuitting Program\n")
        exit()
#----Name Function----

#----ATM Fucntion----
def ATM(): #creates function what allows players to take money from bank
    try:
        global USER_BANK
        global USER_WALLET
        global USER_WALLET
        ATM_W_BP = False
        UP_EXIT = False
        if USER_WALLET <= 0:
            while True:
                print(
                    "\nWelcome to the WhiteDuck ATM\n"

                 )
                while True:
                    UP_ATM_N = input(
                        "\nPLEASE ENTER CARD NUMBER: "
                    ).strip()
                    while True:
                        if UP_ATM_N in (ATM_NUMBER, "81311312212"):
                            UP_ATM_P = input(
                                "\nPLEASE ENTER PIN NUMBER: "
                            ).strip()
                            if UP_ATM_P in ("412311", "81311312212"):
                                while True:
                                    print(
                                        f"\n{USER_NAME}'s Bank Account\n"
                                        f"\nID NUMBER: {ID_ATM_NUMBER}"
                                        f"\nCARD NUMBER: {ATM_NUMBER}"
                                        f"\nCurrent Balanced: ${USER_BANK}"
                                    )
                                    while True:
                                        UP_ATM_C = input(
                                            "\n\n1) Withdraw"
                                            "\n2) Cancel\n\n"
                                        ).strip().lower()
                                        if UP_ATM_C in ("1", "withdraw"):
                                            while True:
                                                UP_ATM_W = input(
                                                    "\nPlease insert withdraw amount ($1000 MAX):"
                                                ).strip().lower()
                                                try:
                                                    float(UP_ATM_W)
                                                    while True:
                                                        if ATM_W_BP or "." not in UP_ATM_W:
                                                            ATM_W_BP = False
                                                            if float(UP_ATM_W) < 1000.01 and float(UP_ATM_W) > 0:
                                                                if float(UP_ATM_W) < USER_BANK:
                                                                    while True:
                                                                        UP_ATM_Confirmation = input(
                                                                            "\nConfirm with pin: "
                                                                        ).strip()
                                                                        if UP_ATM_Confirmation in ("412311", "81311312212"):
                                                                            USER_WALLET += float(UP_ATM_W)
                                                                            USER_BANK -= float(UP_ATM_W)
                                                                            print(
                                                                                "\nTransaction Succsessful"
                                                                                f"\nBANK ACCOUNT: ${USER_BANK}"
                                                                                f"\nWALLET: ${USER_WALLET}"
                                                                            )
                                                                            return
                                                                        else:
                                                                            print(
                                                                                "\nERROR: INCORRECT PIN"
                                                                                "\nTry Again\n"
                                                                            )
                                                                else:
                                                                    print(
                                                                        "\nERROR: Withdraw " \
                                                                        "amount exceded bank " \
                                                                        "account amount"
                                                                    )
                                                                    UP_EXIT = True
                                                                    break
                                                            else:
                                                                print(
                                                                    "\nERROR: Withdraw amount exceded maximum"
                                                                )
                                                                break
                                                        elif "." not in UP_ATM_W:
                                                            ATM_W_BP = True
                                                            continue
                                                        elif "." in UP_ATM_W:
                                                            UP_ATM_W_TEMP = (UP_ATM_W.split(".")[1])
                                                            if len(str(UP_ATM_W_TEMP)) < 2:
                                                                ATM_W_BP = True
                                                                continue
                                                            else:
                                                                print(
                                                                    "\nERROR: Withdraw amount error," \
                                                                    " please insert amount with 2 decimal " \
                                                                    "places or less"
                                                                )
                                                                break
                                                    if UP_EXIT:
                                                        UP_EXIT = False
                                                        break
                                                except ValueError:
                                                    print(
                                                        "\nERROR: Please input a number" \
                                                    )
                                                    continue
                                        elif UP_ATM_C in ("2", "cancel"):
                                            return
                                        else:
                                            print("\nOption unavaliable, please try again!")
                                            continue
                            else:
                                while True:
                                    UP_ATM_P0 = input(
                                        "\nERROR: Incorrect PIN\n"
                                        "\n1) Redo"
                                        "\n2) Cancel\n\n"
                                    ).strip().lower()
                                    if UP_ATM_P0 in ("1", "redo"):
                                        UP_EXIT = True
                                        break
                                    elif UP_ATM_P0 in ("2", "cancel"):
                                        return
                                    else:
                                        print("\nOption unavaliable, please try again!")
                                        continue
                                if UP_EXIT:
                                    UP_EXIT = False
                        else:
                            while True:
                                UP_ATM_N0 = input(
                                    "\nERROR: Unknown card number\n" \
                                    "\n1) Redo" \
                                    "\n2) Cancel\n\n"
                                ).strip().lower()
                                if UP_ATM_N0 in ("1", "redo"):
                                    UP_EXIT = True
                                    break
                                elif UP_ATM_N0 in ("2", "cancel"):
                                    return
                                else:
                                    print("\nOption unavaliable, please try again!")
                                    continue
                            if UP_EXIT:
                                UP_EXIT = False
                                break
        else:
            print(
            f"\nYou still have ${USER_WALLET} in your wallet. Also mum said for emergencies only."
            "\n\nPress any key to go back!"  
        )
        getch.getch()    
    except KeyboardInterrupt:
        print("\nQuitting Program\n")
        exit()

    except EOFError:
        print("\nQuitting Program\n")
        exit()
#----ATM Fucntion----

#----Menu Function----
def menu():
    global GAME_MODE
    try:
        while True: # creates loop for menu options
            UP_M = input(
                "\nWhat would you like to do?\n1) Play\n2) Information \n"
                "3) Settings \n4) ATM \n5) Quit\n\n"
            ).strip().lower()
            if UP_M in ("1", "BlackDuck"): #Checks for playing game
                GAME_MODE = "BlackDuck"
                if BlackDuck_Config == 0:
                    while True:
                        BD_GM = input("\nBlackDuck Mode:"
                            "\n\n1) Normal"
                            "\n2) Advanced\n"
                            "\n3) Back\n"
                        ).strip().lower() ##### NOT DONE
                        if BD_GM in ("1", "normal"):
                            blackDuckNormal()
                        elif BD_GM in ("2", "advanced"):
                            blackDuckAdvanced()
                        elif BD_GM in ("3", "back"):
                            break
                        else:
                            print("\nOption unavaliable, please try again!")
                elif BlackDuck_Config == 1:
                    blackDuckNormal()
                elif BlackDuck_Config == 2:
                    blackDuckAdvanced()
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
                            UP_GN = input("\nHow To Play (NORMAL)\n"
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
                            UP_TT = input("\nTips and Tricks\n"
                                "\nJacks are replaced by Ducks in this game. I know, great idea"
                                "\nType the number that is in front of the option to move throught" \
                                "the menu quicker"
                                "\nWhen in an information options you can type \"Menu\" (or 2) to go back" \
                                "to the main menu"
                                "\nRan out of money to gable with? Use the VISA card your mum gave you"
                                f"({ATM_NUMBER})."
                                "\nIf you want always want to play black on a certain mode, go to setting " \
                                "and switch it to your desired mode"
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
                settings()
            elif UP_M in ("4", "atm"):
                ATM()
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
#----Menu Function----

#----Blackjack Function Normal----
def blackDuckNormal():
    print(
        "\nWelcome to BlackDuck. Just like Blackjack, but with ducks!"
    )
    if USER_WALLET > 0.99:
        while True:
            UP_Bet = input(
                "\nInsert bet amount ($1 MIN): "
            ).strip()
            if UP_Bet.isdigit():
                if UP_Bet > 0:
                    if UP_Bet < USER_WALLET:
                        while True:
                            UP_Bet_Confirmation = input(
                                f"\nYou have picked ${UP_Bet} to bet"
                                "\n\n1) Confirm"
                                "\n2) Redo"
                            )
                            if UP_Bet_Confirmation in ("1", "confirm"):
                                cvl_temp = CVL.copy()
                                DC1 = random.choice(list(cvl_temp.keys()))
                                cvl_temp.pop(DC1)
                                PC1 = random.choice(list(cvl_temp.keys()))
                                cvl_temp.pop(PC1)
                                DC2 = random.choice(list(cvl_temp.keys()))
                                cvl_temp.pop(DC2)
                                PC2 = random.choice(list(cvl_temp.keys()))
                                cvl_temp.pop(PC2)
                                while True:
                                    print(
                                        f"\nDealers Hand: ## | {DC2} : "
                                    )
                                    print(
                                        f"\nPlayers Hand: {PC1} | {PC2} : "
                                    )
                                    UP_BlackDuck = input(
                                        f"\nDealers hand: ##, {DC2}"
                                    )
                            elif UP_Bet_Confirmation in ("2", "confirm"):
                                break
                            else:
                                print(
                                    "\nOption not avaliable, please try again!"
                                )
                                continue
                    else:
                        print(
                            "\nERROR: Bet amount is larger than player's wallet"
                        )
                        continue
                else:
                    print(
                        "\nERROR: Bet amount is under minimum bet ($1)\n"
                )
            else:
                print(
                    "\nERROR: Please input a number\n"
                )
                continue
    else:
        print(
            "\nYou don't have enough money to gable with" \
            "\nPress any key to go back"
        )
        getch.getch()

#----Blackjack Function Normal----

#----Blackjack Function Advanced----
def blackDuckAdvanced():
    pass
#----Blackjack Function Advanced----

#----Settings Function----
def settings():
    global BlackDuck_Config
    global Settings_Config
    global BlackDuck_Mode
    global BlackDuck_Total
    while True:
        print("\nSettings")
        if BlackDuck_Mode == 0:
            print("\n\n1) BlackDuck Game Mode : | Normal | Advanced |-Manual-|")
        elif BlackDuck_Mode == 1:
            print("\n\n1) BlackDuck Game Mode : |-Normal-| Advanced | Manual |")
        elif BlackDuck_Mode == 2:
            print("\n\n1) BlackDuck Game Mode : | Normal |-Advanced-| Manual |")
        if BlackDuck_Total:
            print("\n2) BlackDuck total counter : |-True-| False |")
        elif not BlackDuck_Total:
            print("\n2) BlackDuck total counter : | True |-False-|")
        #Add here for different settings
        Settings_Config = input(
            "\n3) Back\n"
        ).strip().lower()
        if Settings_Config in ("1", "blackduck game", "blackDuck game mode", "bgm"):
            if BlackDuck_Config == 3:
                BlackDuck_Config = 0
            else:
                BlackDuck_Config += 1
        elif Settings_Config in ("2", "blackduck total", "blackduck total counter", "blackduck counter", "btc"):
            BlackDuck_Total = not BlackDuck_Total
        elif Settings_Config in ("3", "back"):
            break
        else:
            print("\nOption unavaliable, please try again!")
            continue
#----Settings Function----


print("\nWelcome to DuckyGamble, a game to gamble in.\nYou start with $1000.")
namePick()
menu()
