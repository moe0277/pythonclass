'''
Created on May 3, 2018

@author: mkhan
'''

import random

def initializeDeck():
    hearts =   [('h',1),('h',2),('h',3),('h',4),('h',5),('h',6),('h',7),('h',8),('h',9),('h',10),('h',11),('h',12),('h',13)]
    spades =   [('s',1),('s',2),('s',3),('s',4),('s',5),('s',6),('s',7),('s',8),('s',9),('s',10),('s',11),('s',12),('s',13)]
    diamonds = [('d',1),('d',2),('d',3),('d',4),('d',5),('d',6),('d',7),('d',8),('d',9),('d',10),('d',11),('d',12),('d',13)]
    clubs =    [('c',1),('c',2),('c',3),('c',4),('c',5),('c',6),('c',7),('c',8),('c',9),('c',10),('c',11),('c',12),('c',13)]
    deck = []
    deck += hearts  
    deck += spades  
    deck += clubs 
    deck += diamonds
    random.shuffle(deck)
    return deck

def deal(deck):
    cards = []
    for i in range(4):
        cards.append(deck.pop())
    return (cards, deck)

def getReadable(card):
    suit = ''
    value = ''
    if card[0] == "h":
        suit = "Hearts"
    elif card[0] == "c":
        suit = "Clubs"
    elif card[0] == "d":
        suit = "Diamonds"
    elif card[0] == "s":
        suit = "Spades"
    if card[1] == 11:
        value = "Jack"
    elif card[1] == 12:
        value = "Queen"
    elif card[1] == 13:
        value = "King"
    elif card[1] == 1:
        value = "Ace"
    else:
        value = card[1]
    return (suit, value)
        

def printCards(p1cards, p2cards):
    p1c1 = getReadable(p1cards[0])
    p2c1 = getReadable(p2cards[0])
    p2c2 = getReadable(p2cards[1])
    
    print("Player 1 Card 1:", p1c1)
    print("Player 1 Card 2:", "Hidden")
    print("----------------")
    print("Player 2 Card 1:", p2c1)
    print("Player 2 Card 2:", p2c2)

def calculateHand(values):
    print(values)
    sum = 0
    for value in values:
        if value > 10:
            value = 10
        if value == 1:
            value = 11
        sum = sum + value
        if sum > 21:
            if value == 1:
                sum = sum - value
                value = 1
                sum = sum + value
    return sum

def hit(deck):
    card = deck.pop()
    print("Hit: %s" % str(getReadable(card)))
    return card[1], deck

def hitorstand(deck):
    value = 0
    while True: 
        res = input("Hit or Stand [h/s]: ")
        if res == 'h' or res == 's':
            break
    if res == 'h':
        value, deck = hit(deck)
        return (value, deck)
    elif res == 's':
        return (None, deck)

def playPlayer(p2cards, deck):
    value1 = p2cards[0][1]
    value2 = p2cards[1][1]
    
    values = [value1, value2]
    sum = 0

    while True:
        sum = calculateHand(values)
        if sum == 21:
            print("Blackjack!")
            break
        elif sum > 21:
            print("Bust!")
            break
        else:
            print ("Player 2 value: %s" % sum)
            value, deck = hitorstand(deck)
            values.append(value)
            if not value:
                break #stand
    return (sum, deck)

def autohitorstand(p2sum, sum, deck):
    if (sum < 18) or (sum < p2sum):
        value, deck = hit(deck)
        return (value, deck)
    else:
        return (None, deck)

def playDealer(p2sum, p1cards, deck):
    value1 = p1cards[0][1]
    value2 = p1cards[1][1]
    print(" Player 1 Card 2: %s" % str(getReadable(p1cards[1])))
    
    values = [value1, value2]
    sum = 0

    while True:
        sum = calculateHand(values)
        if sum == 21:
            print("Blackjack!")
            break
        elif sum > 21:
            print("Bust!")
            break
        else:
            print ("Player 1 value: %s" % sum)
            value, deck = autohitorstand(p2sum, sum, deck)
            values.append(value)
            if not value:
                print("Player 1 wins!")
                break #stand
    return (sum, deck)


    
def playRound():
    deck = initializeDeck()
    cards, deck = deal(deck)
    p1cards = cards[0:2]
    p2cards = cards[2:]
    printCards(p1cards, p2cards)
    sum, deck = playPlayer(p2cards, deck)
    if sum < 21:
        playDealer(sum, p1cards, deck)
    
def playAnother():
    while True:
        res = input("Play another round? [y/n]: ")
        if res == "y" or res == "n":
            return res

def main():
    while True:
        playRound()
        res = playAnother()
        if res == "n":
            print("Goodbye, thanks for playing!")
            break

if __name__ == '__main__':
    main()