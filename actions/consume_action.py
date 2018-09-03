from copy import deepcopy

def consume_action(old_state, action):
    state = deepcopy(old_state)
    action = state['queued_action']
    player = action['player']
    
    # remove creature from player's hand
    card = state[player]['hand'].pop(action['card_index'])
    
    # add creature to board
    state[player][action['lane']].append(card)
    
    # subtract magicka of player
    state[player]['current_magicka'] -= card['cost']

    return state