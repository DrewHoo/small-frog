from copy import deepcopy

def play_creature(old_state, action):
    """play a creature to a lane"""
    state = deepcopy(old_state)
    card_action = {
        'type': action['type'],
        'card_index': action['card_index'],
        'player': action['player'],
        'lane': action['lane']
    }
    state.update({'queued_action': card_action})

    return state