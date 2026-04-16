#!/usr/bin/env python3
"""
21 Number Game (Blackjack)
Author: brainiacweb-tech
"""
import random

def deal(): return random.randint(1, 11)

def hand_value(hand): return sum(hand)

def show(hand, name, hide_second=False):
    if hide_second:
        print(f"{name}: [{hand[0]}, ?]")
    else:
        print(f"{name}: {hand} = {hand_value(hand)}")

def play():
    print("\n" + "=" * 38)
    print("          21 / Blackjack")
    print("=" * 38)
    player = [deal(), deal()]
    dealer = [deal(), deal()]
    show(dealer, "Dealer", hide_second=True)
    show(player, "You")
    while hand_value(player) < 21:
        move = input("\nHit or Stand? (h/s): ").strip().lower()
        if move == 'h':
            player.append(deal())
            show(player, "You")
        elif move == 's':
            break
    print()
    if hand_value(player) > 21:
        print("Bust! You lose."); return
    show(dealer, "Dealer")
    while hand_value(dealer) < 17:
        dealer.append(deal())
        show(dealer, "Dealer")
    p, d = hand_value(player), hand_value(dealer)
    if d > 21 or p > d:
        print("You win!")
    elif p == d:
        print("It's a tie!")
    else:
        print("Dealer wins!")

if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != 'y':
            break
