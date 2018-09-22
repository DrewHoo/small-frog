import pydux
from copy import deepcopy
from pprint import pprint

from fixtures.defaults import DEFAULT_PLAYER_STATE, DEFAULT_STATE
from actions.play_creature import play_creature
from actions.attack import attack


def create_state(state, action):
    return deepcopy(DEFAULT_STATE)
    

def reducer(state, action):
    cases = {
        'play_creature': play_creature,
        'attack': attack
    }
    if action['type'] in cases.keys():
        return cases[action['type']](state, action)
    else:
        print('consumable action type {} not recognized'.format(action['type']))
        return state
    
