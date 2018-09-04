import pydux
from copy import deepcopy
from pprint import pprint

from fixtures.defaults import DEFAULT_PLAYER_STATE, DEFAULT_STATE
from actions.play_creature import play_creature
from actions.consume_action import consume_action


def create_state(state, action):
    return deepcopy(DEFAULT_STATE)
    

def reducer(state, action):
    cases = {
        'play_creature': play_creature,
        'create_state': create_state,
        'consume_action': consume_action
    }

    if action['type'] in cases.keys():
        return cases[action['type']](state, action)
    else:
        print('action type "{}" not found'.format(action['type']))
