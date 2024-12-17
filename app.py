import random

#Define the card suits and ranks
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

#Create a deck of cards
def create_deck():
    return [{'suit': suit, 'rank': rank} for suit in SUITS for rank in RANKS]

#Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(deck, num_cards=4):
    hand = deck[:num_cards]# Remove the dealt cards from the deck through slicing
    del deck[:num_cards]
    return hand

# Display the cards in a player's hand
def display_hand(player, hand):
    hand_str = ', '.join(f"({card['rank']} of {card['suit']})" for card in hand)
    print(f"{player}'s hand: {hand_str}")
    
"""Simple poker hand evaluation placeholder (expand as needed)"""
def evaluate_hand(hand):

# For simplicity, return a placeholder score based on ranks
    rank_values = {rank: index for index, rank in enumerate(RANKS, start=2)}
    score = sum(rank_values[card['rank']] for card in hand)
    return score
"""Player 2 (Computer) AI logic"""
def computer_decision():
    decision = random.choice(['Check', 'Bet', 'Fold','Raise'])
    print("Player 2 (Computer) decides to:", decision)
    return decision