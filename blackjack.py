#!/usr/bin/python

import random

import getpass

import time

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace", "Ace", "Ace", "Ace", "Ace", "Ace", "Ace"]
#deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

deck52 = deck *4

dealerhand = []

playerhand = []

wallet = 100

acechoice = []

def givevalue(card):
    """
    Returns how many gives a card

    Args:
        card: int ou str

    Return:
        integer: amount of points
    """    

    if type(card) == int:
        return card

    if type(card) == str and card != "Ace":
        return 10

    if card == "Ace":
        return 0

        
#test de def dans une def
def total(hand):
    """
    Returns total number of points in a player's hand

    Args:
        hand(list): player's or dealer's hand

    Return:
        integer: total amount of points
    """
    totalace = 0
    total = 0
    if hand.count("Ace") >= 1:
        for ace in acechoice:
            totalace = totalace + ace
    for card in hand:
        total = total + givevalue(card)
    return totalace + total
  

def styled(hand):
    """
    Displays cards of a deck in a stylized way 

    Args:
        hand(list): player's or dealer's hand

    Return:
        string: < card1 >, < card2 >, etc. 
    """
    styled = []
    for card in hand:
        style = f"< {card} > "
        styled.append(style)
    return " ".join(styled)


def drawcard(hand):
    """
    Draws a random card from the deck and adds it to the list "playerhand"

    Args:
        player: defines which hand will be updated (player or dealer's)
    """
    card = random.choice(deck52)
    hand.append(card)
    deck52.remove(card)

#***à finir***
def getback(bet):
    """
    Refunds your bet by adding back bet value to the variable "wallet"

    Args:
        bet: amount of the bet in dollars
    """
    wallet = wallet + bet


#****************************
#************JEU*************
#****************************

print(f"\nWelcome {getpass.getuser()}\n")

time.sleep(2)

#***à faire***
bet = int(input("How much do yo wish to bet?\n"))

wallet = wallet - bet

#************************************
#**********MAINS DE DEPART***********
#************************************
print("\nLet's look at the hands...\n")

time.sleep(2)

#voir pour faire fonction drawcard avec 2 args où 2ème serait nombre d'itérations
for required in range(2):
    drawcard(dealerhand)

print(f"Dealer:\n< ? >  < {dealerhand[1]} >\n")

time.sleep(1)

for required in range(2):
    drawcard(playerhand)

print(f"Your hand:\n{styled(playerhand)}")

if "Ace" in playerhand:
    newchoice = 0
    while newchoice != 11 and newchoice != 1:
        newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
        acechoice.append(newchoice)
        print(acechoice)
#***QUID SI DEUX AS???***
    if playerhand.count("Ace") == 2:
        newchoice = 0
        while newchoice != 11 and newchoice != 1:
            newchoice = int(input("\n    ---> is second Ace worth 1 or 11?\n"))
            acechoice.append(newchoice)
        print(acechoice)
            
print(f"       => total: {total(playerhand)}")

if total(playerhand) == 21:
    print("     BLACKJACK!\n")

#****************************************
#***********DEMANDE DE CARTES************
#****************************************
time.sleep(1)

if total(playerhand) < 21:
    
    hit = input("\nSay 'hit' if you want another card.\nIf you don't the dealer hand will be revealed.\n")
        
    while hit.lower() == "hit" and total(playerhand) < 21:
        card = random.choice(deck52)
        print("\nHere's your card:")
        time.sleep(1)
        drawcard(playerhand)
        print(styled(playerhand))
        if playerhand[-1] == "Ace":
            newchoice = 0
            while newchoice != 11 and newchoice != 1:
                newchoice = int(input("\n---> is Ace worth 1 or 11?\n"))
                acechoice.append(newchoice)
        print(f"      => total: {total(playerhand)}")
        time.sleep(1)
        if total(playerhand) == 21:
            print("     BLACKJACK!\n")
        elif total(playerhand) > 21:
            print("     BUST! You lose, you're over 21.\n")
        else:
            hit = input("\nAgain? Say 'hit'\n")

#***************************************************
#******REVEAL ET COMPLETE DE LA MAIN DU DEALER******
#***************************************************
time.sleep(2)

print("\nThe hand ends. Revealing dealer's hand...\n")

time.sleep(2)

print(f"Dealer:\n{styled(dealerhand)}")

#print(f"       => total: {total(dealerhand)}\n")

if total(dealerhand) < 17:
    time.sleep(1)
    print("Completing dealer's hand until 17...\n")    
while total(dealerhand) < 17:
    time.sleep(1)
    print("...\n")
    drawcard(dealerhand)
    print(styled(dealerhand))
print(f"       => total: {total(dealerhand)}")
if total(dealerhand) > 21:
    print("Dealer loses")

#***************************************************
#*********************GAINS*************************
#*************************************************** 
if total(playerhand) == 21 and total(dealerhand) != 21:
    time.sleep(1)
    print("BLACKJACK! You win")
    wallet = wallet + bet + 1.5*bet

if total(dealerhand) == total(playerhand) == 21:
    time.sleep(1)
    print("PUSH! Your bet is returned to you")
    wallet = wallet + bet
    
if total(dealerhand) > total(playerhand):
    time.sleep(1)
    print("Dealer wins")
    
if total(playerhand) > total(dealerhand):
    time.sleep(1)
    print("Player wins")

print(f"Wallet: {wallet}")
