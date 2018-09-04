from copy import deepcopy

def consume_action(state, action):
    consumable_actions = {
        'play_creature': play_creature,
        'attack': attack
    }
    if action['type'] in consumable_actions.keys():
        return consumable_actions[action['type']](state, action)
    else:
        print('consumable action type {} not recognized'.format(action['type']))
        return state


def attack(old_state, action):
    state = deepcopy(old_state)
    player = action['player']
    opposing_player = 'p1' if player == 'p2' else 'p2'
    lane = action['lane']
    lane_index = action['lane_index']
    attacking_creature = state[player][lane][lane_index]

    if not attacking_creature['can_attack']:
        print('invalid move; {} cannot attack'.format(attacking_creature['name']))
    else:
        state[player][lane][lane_index]['can_attack'] = False

    attack_power = attacking_creature['power']
    if 'target' in action:
        target = action['target']
        target_creature = state[opposing_player][lane][target['lane_index']]
        
        if target_creature['health'] <= attack_power:
            state[opposing_player][lane].pop(target['lane_index'])
            state[opposing_player]['discard_pile'].insert(0, target_creature)
        else:
            target_creature['health'] -= attack_power
        
        if attacking_creature['health'] <= target_creature['power']:
            state[player][lane].pop(lane_index)
            state[player]['discard_pile'].insert(0, attacking_creature)
        else:
            attacking_creature['health'] -= target_creature['power']
    else:
        state[opposing_player]['health'] -= attack_power
    
    return state


def play_creature(old_state, action):
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