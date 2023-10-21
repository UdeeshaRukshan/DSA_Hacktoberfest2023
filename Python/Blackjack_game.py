import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(rank, suit) for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal two cards to the player and two cards to the dealer
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# Show the player's cards and one of the dealer's cards
print("Player's hand:", player_hand)
print("Dealer's hand:", [dealer_hand[0], 'XX'])

# Ask the player if they want to hit or stand
while True:
    action = input("Do you want to hit or stand? ")
    if action.lower() == 'hit':
        player_hand.append(deck.pop())
        print("Player's hand:", player_hand)
        if sum([int(rank) if rank.isdigit() else 10 if rank != 'Ace' else 11 for rank, suit in player_hand]) > 21:
            print("Bust! You lose.")
            break
    elif action.lower() == 'stand':
        break

# Reveal the dealer's second card
print("Dealer's hand:", dealer_hand)

# Dealer hits until their hand is 17 or greater
while sum([int(rank) if rank.isdigit() else 10 if rank != 'Ace' else 11 for rank, suit in dealer_hand]) < 17:
    dealer_hand.append(deck.pop())
    print("Dealer's hand:", dealer_hand)

# Determine the winner
player_score = sum([int(rank) if rank.isdigit() else 10 if rank != 'Ace' else 11 for rank, suit in player_hand])
dealer_score = sum([int(rank) if rank.isdigit() else 10 if rank != 'Ace' else 11 for rank, suit in dealer_hand])
if player_score > 21:
    print("Bust! You lose.")
elif dealer_score > 21:
    print("Dealer busts! You win.")
elif player_score > dealer_score:
    print("You win!")
elif dealer_score > player_score:
    print("You lose.")
else:
    print("It's a tie.")

# Ask the player if they want to play again
while True:
    play_again = input("Do you want to play again? ")
    if play_again.lower() == 'yes':
        # Reset the deck and hands
        deck = [(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(deck)
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        break
    elif play_again.lower() == 'no':
        break