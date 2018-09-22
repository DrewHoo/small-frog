from copy import deepcopy

def play_creature(old_state, action):
    state = deepcopy(old_state)
    player = action['player']
    
    # remove creature from player's hand
    print('stateplayerhand: {}'.format(state))
    card = state[player]['hand'].pop(action['card_index'])
    
    # add creature to board
    state[player][action['lane']].append(card)
    
    # subtract magicka of player
    state[player]['current_magicka'] -= card['cost']

    return state