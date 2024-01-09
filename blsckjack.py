import random

    

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            value += 10
        elif card['rank'] == 'A':
            ace_count += 1
            value += 11
        else:
            value += int(card['rank'])
    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1
    return value


def display_hand(hand, player_name):
    print(f"\n{player_name} karty:")
    for card in hand:
        print("┌───────┐", end=" ")
    print()
    for card in hand:
        print(f"│ {card['rank']: <2}    │", end=" ")
    print()
    for card in hand:
        print("│       │", end=" ")
    print()
    for card in hand:
        print(f"│   {card['suit'][0]: <1}   │", end=" ")
    print()
    for card in hand:
        print("│       │", end=" ")
    print()
    for card in hand:
        print(f"│    {card['rank']:>2} │", end=" ")
    print()
    for card in hand:
        print("└───────┘", end=" ")
    print()


def play_blackjack():
    print("Witam w Blackjacku!")
    print("Jeśli nie znasz zasad, napisz 'r' ")
    print("Jeśli znasz zasady, napisz 'p', aby zagrać")
    question = input("")
    if question == 'r':
        print("rules")
    elif question == 'p':
        player_money = 100  
        while True:
            print(f"\nMasz ${player_money}")
            bet = int(input("Postaw zakład (minimalny zakład wynosi 10): "))
            if bet > player_money:
                print("Nie masz wystarczającej ilości pieniędzy.")
                continue
            if bet < 1:
                print("Minimalny zakład wynosi 10.")
                continue

            deck = create_deck()
            player_hand = []
            dealer_hand = []

            
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())

            
            display_hand(player_hand, "Gracz")
            display_hand(dealer_hand, "Krupier")

            
            while True:
                player_value = calculate_hand_value(player_hand)
                if player_value == 21:
                    print("Blackjack! Wygrałeś!")
                    player_money += bet * 1.5  
                    break
                elif player_value > 21:
                    print("Przegrana! ")
                    player_money -= bet
                    break

                action = input("Chcesz dobrać kartę czy pasować? (d/p): ").lower()
                if action == 'd':
                    player_hand.append(deck.pop())
                    display_hand(player_hand, "Gracz")
                elif action == 'p':
                    break

            
            dealer_value = calculate_hand_value(dealer_hand)
            while dealer_value < 17:
                dealer_hand.append(deck.pop())
                dealer_value = calculate_hand_value(dealer_hand)

            
            print("\nKarty:")
            display_hand(player_hand, "Gracz")
            display_hand(dealer_hand, "Krupier")

            
            if dealer_value > 21:
                print("Krupier przekroczył limit! Wygrywasz!")
                player_money += bet
            elif dealer_value > player_value:
                print("Wygrał krupier!")
                player_money -= bet
            elif player_value > dealer_value:
                print("Wygrywasz!")
                player_money += bet
            else:
                print("Remis!")

            if player_money <= 0:
                print("Składki na stole! Koniec gry.")
                break

            play_again = input("Czy chcesz zagrać ponownie? (t/n): ").lower()
            if play_again != 't':
                print("Dziękujemy za grę!")
                break
    


play_blackjack()
