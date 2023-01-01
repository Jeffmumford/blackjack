import random
from cards import *

#function to ask user if they want to play again
#used to control a while loop for main game
def play_again():
    acceptable = ['y', 'n']
    choice = ''
    
    while choice not in acceptable:
        choice = input('Would you like to play again (y/n)? ')
        choice = choice.lower()

    if choice == 'y':
        return True
    elif choice == 'n':
        return False




#total up the values of all cards in a hand
def total_hand(hand):
    hand_sum = 0
    for i in hand.all_cards:
        hand_sum += i.value

     #adjust ace value from 11 to 1 if total is over 21
    if hand_sum > 21:
        for i in hand.all_cards:
            if i.rank == 'ace':
                hand_sum -= 10
    return hand_sum

#Loop through asking if player wants to hit or stay
def hit_stay(player):
    choice = True
    while choice:

        print('')
        print(f'Players hand: \n{player}')
        print(f'Players Total: {total_hand(player)}')

        
        #break the loop if player has bust
        if total_hand(player) > 21:
            print('Player is bust!')
            choice = False
            
        #break the loop if player hit blackjack
        elif total_hand(player) == 21:
            print('Blackjack!  Player wins!')
            choice = False
           
        else:
            hit_stay = input('Would you like to hit or stay? (h/s) ')
            print(' ')

            if hit_stay.lower() == 'h':
                player.add_card(deck.deal_one())
            elif hit_stay.lower() == 's':
                choice = False
            else:
                print('Please enter h or s.')


    

def dealers_turn(dealer):

    #keep hitting the dealer until they have at least 17
    while total_hand(dealer) < 17:
        dealer.add_card(deck.deal_one())
    
        print(f'Dealers hand: \n{dealer}')
        
    #prints dealers total if they are already over 17
    if total_hand(dealer) >= 17:
        print(f'Dealers hand: \n{dealer}')
        print(f'Dealers Total: {total_hand(dealer)}')

    
    
def check_for_win(player, dealer):

    if total_hand(dealer) > 21:
        print('Dealer is bust!  Player wins!')
        
    else:
        if total_hand(player) > total_hand(dealer):
            print('Player wins!')
        elif total_hand(player) < total_hand(dealer):
            print('Dealer Wins!')
        else:
            print('Its a push.')





 #set up the deck
deck = Deck()

#shuffle the deck
deck.shuffle_deck()

#set up hands
player = Hand()
dealer = Hand()



game = True

while game:

    #clear out cards from last hand
    player.clear_hand()
    dealer.clear_hand()


    #deal two cards to player and dealer

    for i in range(0,2):
        player.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

    #start players turn
    hit_stay(player)

    #start dealers turn as long as player hasn't bust
    if total_hand(player) < 21:
        dealers_turn(dealer)

        check_for_win(player,dealer)

    #asks the player if they want to play again
    game = play_again()

        
        

