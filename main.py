class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class CardQueue:
    def __init__(self):
        self.cards = []

    def push(self, card):
        self.cards.append(card)
        print(f"Added {card.rank} of {card.suit} to the deck.")

    def pop(self):
        if not self.is_empty():
            card = self.cards.pop(0)
            print(f"Removed {card.rank} of {card.suit} from the deck.")
            return card
        else:
            print("The deck is empty.")

    def is_empty(self):
        return len(self.cards) == 0

# Example usage:
if __name__ == "__main__":
    # Creating a deck of cards
    deck = CardQueue()
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    for suit in suits:
        for rank in ranks:
            card = Card(suit, rank)
            deck.push(card)

    # Removing cards from the deck
    deck.pop()
    deck.pop()