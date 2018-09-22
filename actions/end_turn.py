from copy import deepcopy

def end_turn(old_state, action):
    state = deepcopy(old_state)
    card_action = {
        'type': action['type'],
        
    }
    state.update({'queued_action': card_action})