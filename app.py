import random

# Define the card suits and ranks
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create a deck of cards
def create_deck():
    return [{'suit': suit, 'rank': rank} for suit in SUITS for rank in RANKS]

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Deal cards to a player
def deal_cards(deck, num_cards=4):
    hand = deck[:num_cards]# Remove the dealt cards from the deck through slicing
    del deck[:num_cards]
    return hand

# Display the cards in a player's hand
def display_hand(player, hand):
    hand_str = ', '.join(f"({card['rank']} of {card['suit']})" for card in hand)
    print(f"{player}'s hand: {hand_str}")


def show_chips(player, chips):
    print(f"{player}'s chips: {chips}")

# Simple poker hand evaluation placeholder (expand as needed)
def evaluate_hand(hand):
    # For simplicity, return a placeholder score based on ranks
    rank_values = {rank: index for index, rank in enumerate(RANKS, start=2)}
    score = sum(rank_values[card['rank']] for card in hand)
    return score

# Player 2 (Computer) AI logic
def computer_decision():
    decision = random.choice(['Check', 'Bet', 'Fold','Raise'])
    print("Player 2 (Computer) decides to:", decision)
    return decision

# Main game logic
def play_poker():
    print("Welcome to Poker (FOUR-CARD-STUD 😎)!")
    print("RULES AND GAME PLAY")
    print("""
    <--Players are given 4 card at once.-->
    <--There are 3 betting rounds.-->
    <--Player 1 can check, bet, fold or raise.-->
    <--Player 2 (Computer) can check, bet, fold or raise.-->
    <--The player with the highest hand wins.-->  
    """)

    # Initialize and shuffle the deck
    deck = create_deck()
    shuffle_deck(deck)

    # Deal cards to Player 1 and Player 2
    player_1_hand = deal_cards(deck)
    player_2_hand = deal_cards(deck)

    # Display Player 1's hand (hide Player 2's hand for now)
    display_hand("Player 1", player_1_hand)
    show_chips("Player 1", 1000)
    show_chips("Player 2", 1000)
    player_1_chips = 1000
    computer_chips = 1000
    pot = 0

    # Gameplay loop (simplified)
    for round_num in range(1, 4): # Flop, Turn, River
        print(f"\nRound {round_num}:")
        player_1_action = input("Player 1, choose your action (Check, Bet, Fold, Raise): ")
        current_bet = 100
        #if the player folds
        if player_1_action.lower() == 'fold':
            print("Player 1 folds. Player 2 wins!")
            display_hand("Player 1 hand was", player_1_hand)
            display_hand("Player 2 hand was", player_2_hand)
            return

        #if the player bet
        elif player_1_action.lower() == 'bet':
            if current_bet > player_1_chips:
                print("YOU BROKE 🙆🏽‍♂️.You don't have enough chips to bet that amount.")
                print("Player 1 folds. Player 2 wins!")
                display_hand("Player 1 hand was", player_1_hand)
                display_hand("Player 2 hand was", player_2_hand)
                return
            player_1_chips -= current_bet
            pot += current_bet
            print(f"You bet {current_bet} and remain with {player_1_chips} chips.")
            print(f'pot💰 is {pot}')

        #if the player raises
        elif player_1_action.lower() == 'raise':
            raise_amount = int(input(f"current bet is {current_bet}. How much would you like to raise? "))
            if raise_amount < current_bet:
                print("You can't raise below the current bet.")
                continue
            if raise_amount > player_1_chips:
                print("YOU BROKE 🙆🏽‍♂️.You don't have enough chips to raise that amount.")
                print("Player 1 folds. Player 2 wins!🥳")
                display_hand("Player 1 hand was", player_1_hand)
                display_hand("Player 2 hand was", player_2_hand)
                return
            player_1_chips -= raise_amount
            pot += raise_amount
            print(f"You raise and bet by {raise_amount} and remain with {player_1_chips} chips.")
            print(f'pot💰 is {pot}')


        player_2_action = computer_decision()

        if player_2_action == 'Fold':
            print("Player 2 folds. Player 1 wins!")
            display_hand("Player 1 hand was", player_1_hand)
            display_hand("Player 2 hand was", player_2_hand)
            return
        #if the player bet
        elif player_2_action.lower() == 'bet':
            if current_bet > computer_chips:
                print("COMP DOWN 🤖!!I don't have enough chips to bet that amount.")
                print("Player 2 folds. Player 1 wins!🥳")
                display_hand("Player 1 hand was", player_1_hand)
                display_hand("Player 2 hand was", player_2_hand)
                return
            computer_chips -= current_bet
            pot += current_bet
            print(f"computer bets {current_bet} and remains with {computer_chips} chips.")
            print(f'pot💰 is {pot}')

        #if the player raises
        elif player_2_action.lower() == 'raise':
            raise_amount = random.randint(100, 500)
            if raise_amount > computer_chips:
                print("COMP DOWN 🤖!!computer doesn't have enough chips to raise that amount.")
                print("Player 2 folds. Player 1 wins!🥳")
                display_hand("Player 1 hand was", player_1_hand)
                display_hand("Player 2 hand was", player_2_hand)
                return
            computer_chips -= raise_amount
            pot += raise_amount
            print(f"I(comp) raise and bet by {raise_amount} and remain with {computer_chips} chips.")
            print(f'pot💰 is {pot}')

    # Show Player 2's hand at the end
    display_hand("Player 2", player_2_hand)

    # Evaluate and compare hands
    player_1_score = evaluate_hand(player_1_hand)
    player_2_score = evaluate_hand(player_2_hand)

    print("\nFinal Scores:")
    print(f"Player 1: {player_1_score}")
    print(f"Player 2: {player_2_score}")

    if player_1_score > player_2_score:
        print("Player 1 wins!")
    elif player_2_score > player_1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

#run the game
if __name__ == "__main__":
    play_poker()
        