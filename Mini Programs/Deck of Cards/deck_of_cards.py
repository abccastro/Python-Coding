"""
Create an object-oriented program that creates a deck of cards, shuffles them,
and deals the specified number of cards to the player.

Submitted by: Auradee Castro
"""
import itertools
import random


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getCardName(self):
        return self.rank + " of " + self.suit


class Deck:

    _ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"]
    _suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self):
        self._cards = self.populateDeck()

    def populateDeck(self):
        cards = []
        temp_cards = list(itertools.product(self._ranks, self._suits))
        for rank, suit in temp_cards:
            cards.append(Card(rank, suit).getCardName())
        return cards

    def getCards(self):
        return self._cards

    def countCards(self):
        return len(self._cards)

    def shuffleCards(self):
        return random.shuffle(self._cards)

    def dealCard(self):
        return self._cards.pop()


def startCardDealer():

    deck = Deck()
    deck.shuffleCards()

    total_num_of_cards = deck.countCards()

    print("CARD DEALER")
    print(f"I have shuffled a deck of {total_num_of_cards} cards.")

    req_num_of_cards = input("How many cards would you like? ")

    if req_num_of_cards.isdigit() and total_num_of_cards >= int(req_num_of_cards) >= 1:
        print("\nHere are your cards:")

        for i in range(int(req_num_of_cards)):
            print(f"- {deck.dealCard()}")

        print(f"\nThere are {deck.countCards()} cards left in the deck.")
        print("Good luck!")

    else:
        print(f"Invalid input. Choose only from 1 to {total_num_of_cards}")

if __name__ == "__main__":
    startCardDealer()
