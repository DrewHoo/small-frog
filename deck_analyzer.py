import json
import copy


def read_deck(deck_filename):
    deck_json = {}
    with open(deck_filename) as deck_file:
        deck_json = json.load(deck_file)
        
    return deck_json


def mana_curve(deck):
    curve = {}
    for card_name, card_meta in deck.items():
        if card_meta['cost'] in curve:
            curve[card_meta['cost']] += card_meta['count']
        else:
            curve[card_meta['cost']] = card_meta['count']
    return curve
    

def odds_of_opening_hand_n_drop(deck, n):
    n_drops = 0
    card_count = 0
    for card_name, card_meta in deck.items():
        card_count += card_meta['count']
        if int(card_meta['cost']) == n:
            n_drops += card_meta['count']
    odds = round(100 * n_drops/card_count, 2)

    return "Your odds of having a {} drop in your opening hand is {}%".format(n, odds)


def odds_nothing_playable_by_nth_turn(deck, n):
    card_count = 0
    less_than_n_drops = 0
    for card_name, card_meta in deck.items():
        card_count += card_meta['count']
        if int(card_meta['cost']) <= n:
            less_than_n_drops += card_meta['count']
    odds = round(100 * calc(less_than_n_drops, card_count + 3), 2)
    return 'Your odds of having nothing playable through turn {} is {}%'.format(n, odds)
    #go read statistics book to know what to do here


def calc(a, b):
    if a == 0:
        return 1
    else:
        return (a/b) * calc(a-1, b-1)

if __name__ == "__main__":
    deck = read_deck('./deck.json')
    print(mana_curve(deck))
    print(odds_of_opening_hand_n_drop(deck, 1))
    print(odds_of_opening_hand_n_drop(deck, 2))
    print(odds_nothing_playable_by_nth_turn(deck, 1))
    print(odds_nothing_playable_by_nth_turn(deck, 2))