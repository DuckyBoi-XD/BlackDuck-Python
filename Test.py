import sys
import time
import random
import getch

#----Typewriter Function----
def print_tw(sentence, type_delay=0.02):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)
#----Typewriter Function----

#----Ace Handler Function----
def handle_aces(hand):
    """
    Handle Aces in a hand by converting them from 11 to 1 if the total is over 21.
    Returns the updated total.
    """
    total = sum(hand.values())
    # Keep converting Aces from 11 to 1 until we're under 22 or no more 11-value Aces
    while total > 21:
        ace_found = False
        for card_name in hand:
            if "A" in card_name and hand[card_name] == 11:
                hand[card_name] = 1  # Change Ace from 11 to 1
                total = sum(hand.values())  # Recalculate total
                ace_found = True
                break  # Only change one Ace at a time
        if not ace_found:  # No more Aces to convert
            break
    return total
#----Ace Handler Function----

#----Variables----
GAME_MODE = None
USER_WALLET = 1000  # Users money
USER_BANK = random.randrange(5000, 7500)
USER_HAND = 0
USER_NAME = None
CARD_SUITS = ("D", "H", "S", "C")
ATM_NUMBER = str(int(random.random() * 1000000000000000 + 4000000000000000))
ID_ATM_NUMBER = int(ATM_NUMBER) * 3
BlackDuck_Mode = 0
BlackDuck_Total = True
GAME_SCORE = 0

def TERMINOLOGY():
    print_tw(
        "\nTERMINOLOGY:\n"
        "\nHand: The cards that the payer bets with"
        "\nHit: To be given another card"
        "\nStand: To revice no more cards (note you can not hit after standing)"
        "\nBust: The value of all your cards is higher than 21 therefore you lose"
        "\nPush: If both the dealer and player has the same total value, no one wins and all bets and given back"
        "\nBlackjack: The value of all your cards total up to exactly 21, giving you 2.5x your bet ammount (unless push)"
        "\n\nDouble Down: After being dealt you can double your bet, but after a hitting won't be able to"
        "\nSplit: After being dealt, you can make another hand by using one of the cards given to you (you add the same bet as the first hand)"
        "\nSurrender: Give up your the hand and recive half of your bet back", 0.003
)

def CARD_VALUES():
    print_tw(
        "\nCARD VALUES:\n"
        "\nCard are labeled with the suit in front and value on the end. For example: C9 = 9 of Clubs or DK = King of Diamonds"
        "\nThe number on the card is repersents it's value, for example: "
        "\nH6 = 6"
        "\nWith cards like Duck (Jack), King and Queen, they all have a value of 10, for example:\nSQ = 10"
        "\nAces has 2 values, if total value of the player's hand is more than 10, then the value will be 1, otherwise it will have a value of 11. For"
        "example:\nTotal card hand value = 10 | CA = 11", 0.003
)
#----Variables----

#----Card Deck/Value---
CVL = {}

for suit in CARD_SUITS:
    for value in range(2, 11):
        CVL[f"{suit}{value}"] = value

for suit in CARD_SUITS:
    CVL[f"{suit}D"] = CVL[f"{suit}Q"] = CVL[f"{suit}K"] = 10

for suit in CARD_SUITS:
    CVL[f"{suit}A"] = 11
#----Card Deck/Value---

#----Name Function----
def namePick():
    try:
        UP_Exit = False
        while True:
            global USER_NAME
            print_tw("\nPlease insert name: ")
            USER_NAME = input()
            if USER_NAME.isalpha():
                while True:
                    print_tw(
                        f"\nYou have inserted: \"{USER_NAME}\""
                        "\n\n1) CONFIRM"
                        "\n2) REDO\n\n"
                    )
                    userNameComfirm = input().strip().lower()
                    if userNameComfirm in ("1", "confirm"):
                        UP_Exit = True
                        break
                    elif userNameComfirm in ("2", "redo"):
                        break
                    else:
                        print_tw("\nOption unavaliable, please try again!")
                        continue
                if UP_Exit:
                    UP_Exit = False
                    break
            else:
                print_tw("\nERROR: Please use letter")
    except KeyboardInterrupt:
        print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Program\n")
        exit()
    except EOFError:
        print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Program\n")
        exit()
#----Name Function----

#----ATM Function----
def ATM():
    try:
        global USER_BANK
        global USER_WALLET
        ATM_W_BP = False
        UP_EXIT = False
        if USER_WALLET <= 0:
            while True:
                print_tw("\nWelcome to the WhiteDuck ATM\n")
                while True:
                    print_tw("\nPLEASE ENTER CARD NUMBER: ")
                    UP_ATM_N = input().strip()
                    while True:
                        if UP_ATM_N in (ATM_NUMBER, "81311312212"):
                            print_tw("\nPLEASE ENTER PIN NUMBER: ")
                            UP_ATM_P = input().strip()
                            if UP_ATM_P in ("412311", "81311312212"):
                                while True:
                                    print_tw(
                                        f"\n{USER_NAME}'s Bank Account\n"
                                        f"\nID NUMBER: {ID_ATM_NUMBER}"
                                        f"\nCARD NUMBER: {ATM_NUMBER}"
                                        f"\nCurrent Balanced: ${USER_BANK}"
                                    )
                                    while True:
                                        print_tw(
                                            "\n\n1) Withdraw"
                                            "\n2) Cancel\n\n"
                                        )
                                        UP_ATM_C = input().strip().lower()
                                        if UP_ATM_C in ("1", "withdraw"):
                                            while True:
                                                print_tw(
                                                    "\nPlease insert withdraw amount ($1000 MAX): "
                                                )
                                                UP_ATM_W = input().strip().lower()
                                                try:
                                                    float(UP_ATM_W)
                                                    while True:
                                                        if ATM_W_BP or "." not in UP_ATM_W:
                                                            ATM_W_BP = False
                                                            if float(UP_ATM_W) < 1000.01 and float(UP_ATM_W) > 0:
                                                                if float(UP_ATM_W) < USER_BANK:
                                                                    while True:
                                                                        print_tw("\nConfirm with pin: ")
                                                                        UP_ATM_Confirmation = input().strip()
                                                                        if UP_ATM_Confirmation in ("412311", "81311312212"):
                                                                            USER_WALLET += float(UP_ATM_W)
                                                                            USER_BANK -= float(UP_ATM_W)
                                                                            print_tw(
                                                                                "\nTransaction Succsessful"
                                                                                f"\nBANK ACCOUNT: ${USER_BANK}"
                                                                                f"\nWALLET: ${USER_WALLET}\n"
                                                                            )
                                                                            return
                                                                        else:
                                                                            print_tw(
                                                                                "\nERROR: INCORRECT PIN"
                                                                                "\nTry Again\n"
                                                                            )
                                                                else:
                                                                    print_tw(
                                                                        "\nERROR: Withdraw amount exceded bank account amount"
                                                                    )
                                                                    UP_EXIT = True
                                                                    break
                                                            else:
                                                                print_tw(
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
                                                                print_tw(
                                                                    "\nERROR: Withdraw amount error, please insert amount with 2 decimal places or less"
                                                                )
                                                                break
                                                    if UP_EXIT:
                                                        UP_EXIT = False
                                                        break
                                                except ValueError:
                                                    print_tw(
                                                        "\nERROR: Please input a number"
                                                    )
                                                    continue
                                        elif UP_ATM_C in ("2", "cancel"):
                                            return
                                        else:
                                            print_tw("\nOption unavaliable, please try again!")
                                            continue
                            else:
                                while True:
                                    print_tw(
                                        "\nERROR: Incorrect PIN\n"
                                        "\n1) Redo"
                                        "\n2) Cancel\n\n"
                                    )
                                    UP_ATM_P0 = input().strip().lower()
                                    if UP_ATM_P0 in ("1", "redo"):
                                        UP_EXIT = True
                                        break
                                    elif UP_ATM_P0 in ("2", "cancel"):
                                        return
                                    else:
                                        print_tw("\nOption unavaliable, please try again!")
                                        continue
                                if UP_EXIT:
                                    UP_EXIT = False
                        else:
                            while True:
                                print_tw(
                                    "\nERROR: Unknown card number\n"
                                    "\n1) Redo"
                                    "\n2) Cancel\n\n"
                                )
                                UP_ATM_N0 = input().strip().lower()
                                if UP_ATM_N0 in ("1", "redo"):
                                    UP_EXIT = True
                                    break
                                elif UP_ATM_N0 in ("2", "cancel"):
                                    return
                                else:
                                    print_tw("\nOption unavaliable, please try again!")
                                    continue
                            if UP_EXIT:
                                UP_EXIT = False
                                break
        else:
            print_tw(
                f"\nYou still have ${USER_WALLET} in your wallet. Also mum said for emergencies only."
                "\n\nPress any key to go back!\n"
            )
            getch.getch()
    except KeyboardInterrupt:
        print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Program\n")
        exit()
    except EOFError:
        print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Program\n")
        exit()
#----ATM Function----

#----Menu Function----
def menu():
    global GAME_MODE
    global GAME_SCORE
    try:
        while True:
            print_tw(
                "\nWhat would you like to do?\n1) Play\n2) Information \n"
                "3) Settings \n4) ATM \n5) Wallet \n6) Quit\n\n", 0.01
            )
            UP_M = input().strip().lower()
            if UP_M in ("1", "blackduck", "play"):
                GAME_MODE = "BlackDuck"
                if BlackDuck_Mode == 0:
                    while True:
                        print_tw(
                            "\nBlackDuck Mode:"
                            "\n\n1) Normal"
                            "\n2) Advanced"
                            "\n3) Back\n\n"
                        )
                        BD_GM = input().strip().lower()
                        if BD_GM in ("1", "normal"):
                            print_tw(
                            "\nWelcome to BlackDuck Normal. Just like Blackjack, but with ducks!"
                            )
                            blackDuckNormal()
                        elif BD_GM in ("2", "advanced"):
                            print_tw(
                            "\nWelcome to BlackDuck Advanced. Just like Blackjack, but with ducks!"
                            )
                            blackDuckAdvanced()
                        elif BD_GM in ("3", "back"):
                            break
                        else:
                            print_tw("\nOption unavaliable, please try again!")
                        break
                elif BlackDuck_Mode == 1:
                    blackDuckNormal()
                elif BlackDuck_Mode == 2:
                    blackDuckAdvanced()
            elif UP_M in ("2", "information"):
                UP_Exit = False
                while True:
                    print_tw(
                        "\nInformation about this game!\n1) How to play (Normal)\n2) How to play "
                        "(Advanced)\n"
                        "3) Terminology\n4) Card Values\n5) Tips and Tricks\n6) Back\n\n"
                    , 0.01)
                    UP_I = input().strip().lower()
                    if UP_I in ("1", "how to play (normal)", "htpn"):
                        while True:
                            print_tw(
                                "\nHow To Play (NORMAL)\n"
                                "\nThe aim of the game is to get higher than the dealer without going over 21."
                                "\nYou and the dealer get 2 cards each (one of the dealer's cards will be unknown to the player. "
                                "\nYou have 2 options (see terminology), hit: be given another card or stand (can be repeated unless you stand): don't get any more cards (note that after standing, you won't be able to hit ever again)."
                                "\nIf the total value of your cards that you have is over 21, then you lose."
                                "\nOnce you 'hit', your total card value will get closer and closer to 21."
                                "\nIf your total card value goes over 21, then you lose (bust), and lose your bet"
                                "\nIf you don't want to receive any more cards, you stand"
                                "\nAfter standing, the dealer gets to receive cards to match or achieve a higher total card value."
                                "\n\nIf your total card value matches the dealer's total card value, then no one wins and your bet is returned to you (push)"
                                "\nIf your total card value is lower than the dealer's total card value, then you lose, losing your bet."
                                "\nIf your total card value is higher than the dealer's total card value, then you win, receiving double your bet amount"
                                "\nYou win if the dealer busts (like how the player would)"
                                "\n\n1) Back"
                                "\n2) Menu\n\n", 0.005
                            )
                            UP_GN = input().strip().lower()
                            if UP_GN in ("1", "back"):
                                break
                            elif UP_GN in ("2", "menu"):
                                UP_Exit = True
                                break
                            else:
                                print_tw("\nOption unavaliable, please try again!")
                        if UP_Exit:
                            break
                    elif UP_I in ("2", "how to play (advanced)", "htpa"):
                        while True:
                            print_tw(
                                "\nHow To Play (ADVANCED) (Game rules are the same as NORMAL mode except for a few actions)\n"
                                "\nWhen being dealt the first 2 cards, you are given the option to split and double down. (Terminology)"
                                "\nWhen you split, you create a second hand and bet the same amount as the first hand."
                                "\nWhen you doubling down you double your bet amount."
                                "\nThese 2 actions can only be used when you are dealt the first 2 cards. You cannot hit then double down."
                                "\nYou can however split then double down one or both of your hands."
                                "\nThrough the game you can surrender which will give you back half of your bet but give up your hand"
                                "\n\n1) Back"
                                "\n2) Menu\n\n", 0.005
                            )
                            UP_GA = input().strip().lower()
                            if UP_GA in ("1", "back"):
                                break
                            elif UP_GA in ("2", "menu"):
                                UP_Exit = True
                                break
                            else:
                                print_tw("\nOption unavaliable, please try again!")
                        if UP_Exit:
                            break
                    elif UP_I in ("3", "terminology", "term"):
                        while True:
                            TERMINOLOGY()
                            print_tw("\n\n1) Back\n2) Menu\n\n")
                            UP_T = input().strip().lower()
                            if UP_T in ("1", "back"):
                                break
                            elif UP_T in ("2", "menu"):
                                UP_Exit = True
                                break
                            else:
                                print_tw("\nOption unavaliable, please try again!")
                        if UP_Exit:
                            break
                    elif UP_I == "4" or UP_I == "card values":
                        while True:
                            CARD_VALUES()
                            print_tw("\n\n1) Back\n2) Menu\n\n")
                            UP_CV = input().strip().lower()
                            if UP_CV in ("1", "back"):
                                break
                            elif UP_CV in ("2", "menu"):
                                UP_Exit = True
                                break
                            else:
                                print_tw("\nOption unavaliable, please try again!")
                        if UP_Exit:
                            break
                    elif UP_I in ("5", "tips and tricks", "tat", "t&t"):
                        while True:
                            print_tw("\nTips and Tricks\n"
                                "\nJacks are replaced by Ducks in this game. I know, great idea"
                                "\nType the number that is in front of the option to move throught the menu quicker"
                                "\nWhen in an information options you can type \"Menu\" (or 2) to go back to the main menu"
                                "\nRan out of money to gable with? Use the VISA card your mum gave you for emergincies,\n"
                                f"with the card nmber being {ATM_NUMBER} and the pin being 81311312212"
                                "\nIf you want always want to play blackduck on a certain mode, go to setting and switch it to your desired mode"
                                "\nWhen you quit the game, you are given a game score. This game score is calculated by how much money you win"
                                "\n----MORE TIPS IN THE FUTURE----"
                                "\n\n1) Back"
                                "\n2) Menu\n\n", 0.005
                            )
                            UP_TT = input().strip().lower()
                            if UP_TT in ("1", "back"):
                                break
                            elif UP_TT in ("2", "menu"):
                                UP_Exit = True
                                break
                            else:
                                print_tw("\nOption unavaliable, please try again!")
                        if UP_Exit:
                            break
                    elif UP_I in ("6", "back"):
                        break
                    else:
                        print_tw("\nOption unavaliable, please try again!")
            elif UP_M in ("3", "settings"):
                settings()
            elif UP_M in ("4", "atm"):
                ATM()
            elif UP_M in ("5", "wallet"):
                print_tw(f"\nCurrent wallet: ${USER_WALLET}\n")
                continue
            elif UP_M in ("6", "quit"):
                print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Game\n")
                exit()
            else:
                print_tw("\nOption unavaliable, please try again!")
    except KeyboardInterrupt:
        print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Program\n")
        exit()
    except EOFError:
        print_tw(f"\nGame Score: {GAME_SCORE}\n\nQuitting Program\n")
        exit()
#----Menu Function----

#----Blackjack Function Normal----
def blackDuckNormal():
    global USER_WALLET
    global DCL
    global DCB
    global PCL
    global cvl_temp
    global UP_Bet
    global GAME_SCORE
    Stand_Override = False
    if USER_WALLET > 0.99:
        while True:
            print_tw("\nInsert bet amount ($1 MIN): ")
            UP_Bet = input().strip()
            if UP_Bet.isdigit():
                if int(UP_Bet) > 0:
                    if int(UP_Bet) <= USER_WALLET:
                        while True:
                            print_tw(
                                f"\nYou have picked ${UP_Bet} to bet"
                                "\n\n1) Confirm"
                                "\n2) Redo\n\n"
                            )
                            UP_Bet_Confirmation = input().strip().lower()
                            if UP_Bet_Confirmation in ("1", "confirm"):
                                USER_WALLET -= int(UP_Bet)
                                cvl_temp = CVL.copy()
                                DCL = {}
                                PCL = {}
                                DCB = {}
                                key, value = (random.choice(list(cvl_temp.items())))
                                PCL[key] = value
                                cvl_temp.pop(key)
                                key, value = random.choice(list(cvl_temp.items()))
                                DCB[key] = value
                                cvl_temp.pop(key)
                                key, value = (random.choice(list(cvl_temp.items())))
                                PCL[key] = value
                                cvl_temp.pop(key)
                                key, value = (random.choice(list(cvl_temp.items())))
                                DCL[key] = value
                                cvl_temp.pop(key)
                                while True:
                                    if Stand_Override:
                                        pass
                                    else:
                                        D_Total = sum(DCL.values())
                                        P_Total = sum(PCL.values())
                                        print_tw(
                                            f"\nDealers Hand: __ | {' | '.join(list(DCL.keys()))}", 0.01)
                                        if BlackDuck_Total:
                                            print_tw(f" : {D_Total}")
                                        print_tw(
                                            f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                        if BlackDuck_Total:
                                            print_tw(f" : {P_Total}")
                                        print_tw(
                                            "\n\n1) Hit | 2) Stand"
                                            "\n3) Card Values | 4) Terminology\n\n"
                                        , 0.01)
                                        UP_BlackDuck = input().strip().lower()
                                    if  UP_BlackDuck in ("1", "hit"):
                                        while True:
                                            if Stand_Override:
                                                break
                                            key, value = (random.choice(list(cvl_temp.items())))
                                            PCL[key] = value
                                            cvl_temp.pop(key)
                                            D_Total = sum(DCL.values())
                                            P_Total = handle_aces(PCL)  # Handle player Aces automatically
                                            while True:
                                                print_tw(
                                                    f"\nDealers Hand: __ | {' | '.join(list(DCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {D_Total}")
                                                print_tw(
                                                    f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {P_Total}")
                                                    print_tw("")
                                                if P_Total > 21:
                                                    while True:
                                                        print_tw(
                                                            "\n\nYOU BUSTED!!!"
                                                            "\nYou went over 21, better luck next time!"
                                                            f"\nYou lost ${UP_Bet}\n"
                                                            "\n1) Play again"
                                                            "\n2) Back\n\n"
                                                        , 0.01)
                                                        BD_GO = input().strip().lower()
                                                        if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                            blackDuckNormal()
                                                            return
                                                        elif BD_GO in ("2", "back"):
                                                            return
                                                        else:
                                                            print_tw("\nOption not avaliable, please try again!\n")
                                                            continue
                                                print_tw(
                                                    "\n\n1) Hit | 2) Stand"
                                                    "\n3) Card Values | 4) Terminology\n\n"
                                                , 0.01)
                                                UP_BlackDuck = input().strip().lower()
                                                if UP_BlackDuck in ("1", "hit"):
                                                    break
                                                elif UP_BlackDuck in ("2", "stand"):
                                                    Stand_Override = True
                                                    break
                                                elif UP_BlackDuck in ("3", "card value"):
                                                    CARD_VALUES()
                                                    continue
                                                elif UP_BlackDuck in ("4", "terminology"):
                                                    TERMINOLOGY()
                                                    continue
                                                else:
                                                    print_tw("\nOption not avaliable, please try again!\n")
                                                    continue
                                    elif UP_BlackDuck in ("2", "stand") or Stand_Override:
                                        if Stand_Override:
                                            Stand_Override = False
                                        while True:
                                            D_Total = sum(DCL.values()) + sum(DCB.values())
                                            P_Total = sum(PCL.values())
                                            print_tw(
                                                f"\nDealers Hand: {list(DCB.keys())[0]} | {' | '.join(list(DCL.keys()))}", 0.01)
                                            if BlackDuck_Total:
                                                print_tw(f" : {D_Total}")
                                            print_tw(
                                                f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                            if BlackDuck_Total:
                                                print_tw(f" : {P_Total}")
                                            print_tw("\n\nPress any key to continue\n")
                                            getch.getch()
                                            while True:
                                                print("")
                                                if D_Total > 21:
                                                    if P_Total == 21:
                                                        USER_WALLET += 2.5*int(UP_Bet)
                                                        print_tw(
                                                            "YOU WON WITH BLACKJACK!!!"
                                                            "\nThe dealer busted"
                                                            f"\nYou recive ${2.5*int(UP_Bet)}\n"
                                                           "\n1) Play again"
                                                           "\n2) Back\n\n"
                                                        )
                                                        GAME_SCORE += 2.5*int(UP_Bet)
                                                    else:
                                                        USER_WALLET += 2*int(UP_Bet)
                                                        print_tw(
                                                           "YOU WON!!!"
                                                           "\nThe dealer busted"
                                                           f"\nYou recive ${2*int(UP_Bet)}\n"
                                                           "\n1) Play again"
                                                           "\n2) Back\n\n"
                                                        , 0.01)
                                                        GAME_SCORE += 2*int(UP_Bet)
                                                    BD_GO = input().strip().lower()
                                                    if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                        blackDuckNormal()
                                                        return
                                                    elif BD_GO in ("2", "back"):
                                                        return
                                                    else:
                                                        print_tw("\nOption not avaliable, please try again!\n")
                                                        continue
                                                elif D_Total > P_Total:
                                                    while True:
                                                        print_tw(
                                                            "YOU LOST!!!"
                                                            "\nThe dealer got a higher number, better luck next time!"
                                                            f"\nYou lost ${UP_Bet}\n"
                                                            "\n1) Play again"
                                                            "\n2) Back\n\n"
                                                        , 0.01)
                                                        BD_GO = input().strip().lower()
                                                        if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                            blackDuckNormal()
                                                            return
                                                        elif BD_GO in ("2", "back"):
                                                            return
                                                        else:
                                                            print_tw("\nOption not avaliable, please try again!\n\n")
                                                            continue
                                                elif D_Total == P_Total:
                                                    print_tw(
                                                        "YOU TIED!!!"
                                                        "\nThe dealer got the same amount of cards as you"
                                                        f"\n${UP_Bet} is returned to you\n"
                                                        "\n1) Play again"
                                                        "\n2) Back\n\n"
                                                    , 0.01)
                                                    BD_GO = input().strip().lower()
                                                    if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                        blackDuckNormal()
                                                        return
                                                    elif BD_GO in ("2", "back"):
                                                        return
                                                    else:
                                                        print_tw("\nOption not avaliable, please try again!\n\n")
                                                        continue
                                                key, value = (random.choice(list(cvl_temp.items())))
                                                DCL[key] = value
                                                cvl_temp.pop(key)
                                                while D_Total > 21:
                                                    if sum(DCB.values()) == 11:
                                                        for value in DCL:
                                                            value = 1
                                                    for item in DCL.items():
                                                        if value in item == 11:
                                                            item = 1
                                                            D_Total = sum(DCL.values())
                                                            break
                                                D_Total = sum(DCL.values()) + sum(DCB.values())
                                                P_Total = sum(PCL.values())
                                                print_tw(
                                                    f"Dealers Hand: {list(DCB.keys())[0]} | {' | '.join(list(DCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {D_Total}")
                                                print_tw(
                                                    f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {P_Total}")
                                                print("\n")
                                                if D_Total < P_Total:
                                                    continue
                                    elif UP_BlackDuck in ("3", "card value"):
                                        CARD_VALUES()
                                        continue
                                    elif UP_BlackDuck in ("4", "terminology"):
                                        TERMINOLOGY()
                                        continue
                                    else:
                                        print_tw("\nOption not avaliable, please try again!\n")
                                        continue
                            elif UP_Bet_Confirmation in ("2", "redo"):
                                break
                            else:
                                print_tw("\nOption not avaliable, please try again!\n")
                                continue
                    else:
                        print_tw(
                            "\nERROR: Bet amount is larger than player's wallet\n"
                            f"Wallet: ${USER_WALLET}\n"
                        )
                        continue
                else:
                    print_tw("\nERROR: Bet amount is under minimum bet ($1)\n")
            else:
                print_tw("\nERROR: Please input a number\n")
                continue
    else:
        print_tw(
            "\nYou don't have enough money to gamble with"
            "\nPress any key to go back\n"
        )
        getch.getch()
#----Blackjack Function Normal----

#----Blackjack Function Advanced----
def blackDuckAdvanced():
    global USER_WALLET
    global DCL
    global DCB
    global PCL
    global cvl_temp
    global UP_Bet
    global GAME_SCORE
    Stand_Override = False
    if USER_WALLET > 0.99:
        while True:
            print_tw("\nInsert bet amount ($1 MIN): ")
            UP_Bet = input().strip()
            if UP_Bet.isdigit():
                if int(UP_Bet) > 0:
                    if int(UP_Bet) <= USER_WALLET:
                        while True:
                            print_tw(
                                f"\nYou have picked ${UP_Bet} to bet"
                                "\n\n1) Confirm"
                                "\n2) Redo\n\n"
                            )
                            UP_Bet_Confirmation = input().strip().lower()
                            if UP_Bet_Confirmation in ("1", "confirm"):
                                USER_WALLET -= int(UP_Bet)
                                cvl_temp = CVL.copy()
                                DCL = {}
                                PCL = {}
                                DCB = {}
                                key, value = (random.choice(list(cvl_temp.items())))
                                PCL[key] = value
                                cvl_temp.pop(key)
                                key, value = random.choice(list(cvl_temp.items()))
                                DCB[key] = value
                                cvl_temp.pop(key)
                                key, value = (random.choice(list(cvl_temp.items())))
                                PCL[key] = value
                                cvl_temp.pop(key)
                                key, value = (random.choice(list(cvl_temp.items())))
                                DCL[key] = value
                                cvl_temp.pop(key)
                                while True:
                                    if Stand_Override:
                                        pass
                                    else:
                                        D_Total = sum(DCL.values())
                                        P_Total = sum(PCL.values())
                                        print_tw(
                                            f"\nDealers Hand: __ | {' | '.join(list(DCL.keys()))}", 0.01)
                                        if BlackDuck_Total:
                                            print_tw(f" : {D_Total}")
                                        print_tw(
                                            f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                        if BlackDuck_Total:
                                            print_tw(f" : {P_Total}")
                                        print_tw(
                                            "\n\n1) Hit | 2) Stand | 3) Double Down | 4) Split"
                                            "\n5) Card Values | 6) Terminology\n\n"
                                        , 0.01)
                                        UP_BlackDuck = input().strip().lower()
                                    if  UP_BlackDuck in ("1", "hit"):
                                        while True:
                                            if Stand_Override:
                                                break
                                            key, value = (random.choice(list(cvl_temp.items())))
                                            PCL[key] = value
                                            cvl_temp.pop(key)
                                            D_Total = sum(DCL.values())
                                            P_Total = sum(PCL.values())
                                            if P_Total > 21:
                                                for card_name in list(PCL):
                                                    if "A" in card_name and PCL[card_name] == 11:
                                                        PCL[card_name] = 1  # Change Ace from 11 to 1
                                                        P_Total = sum(PCL.values())  # Recalculate total
                                                        break  # Only change one Ace at a time
                                            while True:
                                                print_tw(
                                                    f"\nDealers Hand: __ | {' | '.join(list(DCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {D_Total}")
                                                print_tw(
                                                    f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {P_Total}")
                                                    print_tw("")
                                                if P_Total > 21:
                                                    while True:
                                                        print_tw(
                                                            "\n\nYOU BUSTED!!!"
                                                            "\nYou went over 21, better luck next time!"
                                                            f"\nYou lost ${UP_Bet}\n"
                                                            "\n1) Play again"
                                                            "\n2) Back\n\n"
                                                        , 0.01)
                                                        BD_GO = input().strip().lower()
                                                        if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                            blackDuckAdvanced()
                                                            return
                                                        elif BD_GO in ("2", "back"):
                                                            return
                                                        else:
                                                            print_tw("\nOption not avaliable, please try again!\n")
                                                            continue
                                                print_tw(
                                                    "\n\n1) Hit | 2) Stand"
                                                    "\n3) Card Values | 4) Terminology\n\n"
                                                , 0.01)
                                                UP_BlackDuck = input().strip().lower()
                                                if UP_BlackDuck in ("1", "hit"):
                                                    break
                                                elif UP_BlackDuck in ("2", "stand"):
                                                    Stand_Override = True
                                                    break
                                                elif UP_BlackDuck in ("3", "card value"):
                                                    CARD_VALUES()
                                                    continue
                                                elif UP_BlackDuck in ("4", "terminology"):
                                                    TERMINOLOGY()
                                                    continue
                                                else:
                                                    print_tw("\nOption not avaliable, please try again!\n")
                                                    continue
                                    elif UP_BlackDuck in ("2", "stand") or Stand_Override:
                                        if Stand_Override:
                                            Stand_Override = False
                                        while True:
                                            D_Total = sum(DCL.values()) + sum(DCB.values())
                                            P_Total = sum(PCL.values())
                                            print_tw(
                                                f"\nDealers Hand: {list(DCB.keys())[0]} | {' | '.join(list(DCL.keys()))}", 0.01)
                                            if BlackDuck_Total:
                                                print_tw(f" : {D_Total}")
                                            print_tw(
                                                f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                            if BlackDuck_Total:
                                                print_tw(f" : {P_Total}")
                                            print_tw("\n\nPress any key to continue\n")
                                            getch.getch()
                                            while True:
                                                print("")
                                                if D_Total > 21:
                                                    if P_Total == 21:
                                                        USER_WALLET += 2.5*int(UP_Bet)
                                                        print_tw(
                                                            "YOU WON WITH BLACKJACK!!!"
                                                            "\nThe dealer busted."
                                                            f"\nYou recive ${2.5*int(UP_Bet)}\n"
                                                           "\n1) Play again"
                                                           "\n2) Back\n\n"
                                                        )
                                                        GAME_SCORE += 2.5*int(UP_Bet)
                                                    else:
                                                        USER_WALLET += 2*int(UP_Bet)
                                                        print_tw(
                                                           "YOU WON!!!"
                                                           "\nThe dealer busted."
                                                           f"\nYou recive ${2*int(UP_Bet)}\n"
                                                           "\n1) Play again"
                                                           "\n2) Back\n\n"
                                                        , 0.01)
                                                        GAME_SCORE += 2*int(UP_Bet)
                                                    BD_GO = input().strip().lower()
                                                    if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                        blackDuckAdvanced()
                                                        return
                                                    elif BD_GO in ("2", "back"):
                                                        return
                                                    else:
                                                        print_tw("\nOption not avaliable, please try again!\n")
                                                        continue
                                                elif D_Total > P_Total:
                                                    while True:
                                                        print_tw(
                                                            "YOU LOST!!!"
                                                            "\nThe dealer got a higher number, better luck next time!"
                                                            f"\nYou lost ${UP_Bet}\n"
                                                            "\n1) Play again"
                                                            "\n2) Back\n\n"
                                                        , 0.01)
                                                        BD_GO = input().strip().lower()
                                                        if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                            blackDuckAdvanced()
                                                            return
                                                        elif BD_GO in ("2", "back"):
                                                            return
                                                        else:
                                                            print_tw("\nOption not avaliable, please try again!\n\n")
                                                            continue
                                                elif D_Total == P_Total:
                                                    print_tw(
                                                        "YOU TIED!!!"
                                                        "\nThe dealer got the same amount of cards as you."
                                                        f"\n${UP_Bet} is returned to you\n"
                                                        "\n1) Play again"
                                                        "\n2) Back\n\n"
                                                    , 0.01)
                                                    BD_GO = input().strip().lower()
                                                    if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                        blackDuckAdvanced()
                                                        return
                                                    elif BD_GO in ("2", "back"):
                                                        return
                                                    else:
                                                        print_tw("\nOption not avaliable, please try again!\n\n")
                                                        continue
                                                key, value = (random.choice(list(cvl_temp.items())))
                                                DCL[key] = value
                                                cvl_temp.pop(key)
                                                if P_Total > 21:
                                                    for card_name in list(PCL):
                                                        if "A" in card_name and PCL[card_name] == 11:
                                                            PCL[card_name] = 1  # Change Ace from 11 to 1
                                                            P_Total = sum(PCL.values())  # Recalculate total
                                                            break  # Only change one Ace at a time
                                                D_Total = sum(DCL.values()) + sum(DCB.values())
                                                P_Total = sum(PCL.values())
                                                print_tw(
                                                    f"Dealers Hand: {list(DCB.keys())[0]} | {' | '.join(list(DCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {D_Total}")
                                                print_tw(
                                                    f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                                if BlackDuck_Total:
                                                    print_tw(f" : {P_Total}")
                                                print("\n")
                                                if D_Total < P_Total:
                                                    continue
                                    elif UP_BlackDuck in ("3", "double down", "dd"):
                                        if USER_WALLET >= int(UP_Bet):
                                            USER_WALLET -= int(UP_Bet)
                                            print_tw(f"\nYou have selected double down which bets an extra ${UP_Bet}")
                                            UP_Bet = 2* int(UP_Bet)
                                            key, value = (random.choice(list(cvl_temp.items())))
                                            PCL[key] = value
                                            cvl_temp.pop(key)
                                            D_Total = sum(DCL.values())
                                            P_Total = sum(PCL.values())
                                            if P_Total > 21:
                                                for card_name in list(PCL):
                                                    if "A" in card_name and PCL[card_name] == 11:
                                                        PCL[card_name] = 1  # Change Ace from 11 to 1
                                                        P_Total = sum(PCL.values())  # Recalculate total
                                                        break  # Only change one Ace at a time
                                            print_tw(
                                                f"\nDealers Hand: __ | {' | '.join(list(DCL.keys()))}", 0.01)
                                            if BlackDuck_Total:
                                                print_tw(f" : {D_Total}")
                                            print_tw(
                                                f"\nPlayers Hand: {' | '.join(list(PCL.keys()))}", 0.01)
                                            if BlackDuck_Total:
                                                print_tw(f" : {P_Total}")
                                                print_tw("")
                                            
                                            # Check if still busted after Ace adjustment
                                            if P_Total > 21:
                                                while True:
                                                    print_tw(
                                                        "\n\nYOU BUSTED!!!"
                                                        "\nYou went over 21, better luck next time!"
                                                        f"\nYou lost ${UP_Bet}\n"
                                                        "\n1) Play again"
                                                        "\n2) Back\n\n"
                                                    , 0.01)
                                                    BD_GO = input().strip().lower()
                                                    if BD_GO in ("1", "play", "again", "play again", "pa"):
                                                        blackDuckAdvanced()
                                                        return
                                                    elif BD_GO in ("2", "back"):
                                                        return
                                                    else:
                                                        print_tw("\nOption not avaliable, please try again!\n")
                                                        continue
                                            Stand_Override = True
                                            print_tw("\nPress any button to continue\n")
                                            getch.getch()
                                        elif USER_WALLET < int(UP_Bet):
                                            print_tw("\nYou don't have enough money to double down\n")
                                            continue
                                    elif UP_BlackDuck in ("4", "split"):
                                        pass
                                    elif UP_BlackDuck in ("5", "card value"):
                                        CARD_VALUES()
                                        continue
                                    elif UP_BlackDuck in ("6", "terminology"):
                                        TERMINOLOGY()
                                        continue
                                    else:
                                        print_tw("\nOption not avaliable, please try again!\n")
                                        continue
                            elif UP_Bet_Confirmation in ("2", "redo"):
                                break
                            else:
                                print_tw("\nOption not avaliable, please try again!\n")
                                continue
                    else:
                        print_tw(
                            "\nERROR: Bet amount is larger than player's wallet\n"
                            f"Wallet: ${USER_WALLET}\n"
                        )
                        continue
                else:
                    print_tw("\nERROR: Bet amount is under minimum bet ($1)\n")
            else:
                print_tw("\nERROR: Please input a number\n")
                continue
    else:
        print_tw(
            "\nYou don't have enough money to gamble with"
            "\nPress any key to go back\n"
        )
        getch.getch()
#----Blackjack Function Advanced----

#----Settings Function----
def settings():
    global Settings_Config
    global BlackDuck_Mode
    global BlackDuck_Total
    while True:
        print_tw("\nSettings")
        if BlackDuck_Mode == 0:
            print_tw("\n\n1) BlackDuck Game Mode : | Normal | Advanced |-Manual-|")
        elif BlackDuck_Mode == 1:
            print_tw("\n\n1) BlackDuck Game Mode : |-Normal-| Advanced | Manual |")
        elif BlackDuck_Mode == 2:
            print_tw("\n\n1) BlackDuck Game Mode : | Normal |-Advanced-| Manual |")
        if BlackDuck_Total:
            print_tw("\n2) BlackDuck total counter : |-True-| False |")
        elif not BlackDuck_Total:
            print_tw("\n2) BlackDuck total counter : | True |-False-|")
        print_tw("\n3) Back\n\n")
        Settings_Config = input().strip().lower()
        if Settings_Config in ("1", "blackduck game", "blackduck game mode", "bgm"):
            if BlackDuck_Mode == 2:
                BlackDuck_Mode = 0
            else:
                BlackDuck_Mode += 1
        elif Settings_Config in ("2", "blackduck total", "blackduck total counter", "blackduck counter", "btc"):
            BlackDuck_Total = not BlackDuck_Total
        elif Settings_Config in ("3", "back"):
            break
        else:
            print_tw("\nOption unavaliable, please try again!")
            continue
#----Settings Function----

if __name__ == "__main__":
    print_tw("\nWelcome to DuckyGamble, a game to gamble in.\nYou start with $1000.")
    namePick()
    menu()