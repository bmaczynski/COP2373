import random

# Define Card class
class Card:
    # Suits and ranks of the cards
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # Initialize card with a suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # String representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Define Deck class
class Deck:
    # Initialize deck with 52 shuffled cards
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    # Draw a card from the deck
    def draw(self):
        # Return top card from deck if not empty
        return self.cards.pop() if self.cards else None

# Define PokerHand class
class PokerHand:
    # Initialize hand by drawing five cards from the deck
    def __init__(self, deck):
        self.cards = [deck.draw() for _ in range(5)]

    # String representation of the hand
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

    # Replace specified cards in the hand with new cards from the deck
    def replace_cards(self, positions, deck):
        for i in positions:
            self.cards[i] = deck.draw()

def main():
    # Create a deck of cards
    deck = Deck()
    # Deal an initial poker hand
    hand = PokerHand(deck)
    print("Initial hand:")
    print(hand)

    # Prompt user to enter positions of cards to replace
    positions = input("Enter the positions of cards to replace (e.g., 1, 3, 5): ")
    positions = [int(pos) - 1 for pos in positions.split(',')]
    
    # Replace specified cards in the hand
    hand.replace_cards(positions, deck)
    
    # Display new hand
    print("New hand:")
    print(hand)

if __name__ == "__main__":
    main()