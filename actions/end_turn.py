from copy import deepcopy

def end_turn(old_state, action):
    state = deepcopy(old_state)
    player = int(action['player'][1:])
    turn = state['turn']
    
    if (player % 2 == 0 and turn % 2 == 0) or (player % 2 != 0 and turn % 2 != 0):
        state.update({'turn': turn + 1})
    # might want to throw an error in else case
    return state
    
