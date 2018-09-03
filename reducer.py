import pydux
from copy import deepcopy
from pprint import pprint

from actions.play_creature import play_creature
from actions.consume_action import consume_action

DEFAULT_PLAYER_STATE = {
    'max_magicka': 0,
    'current_magicka': 0,
    'field_lane': [],
    'shadow_lane': [],
    'active_supports': [],
    'discard_pile': [],
    'hand': [{'name': 'marauder', 'cost': 0}],
    'face': {
        'health': 30,
        'runes':  5
    },
    'is_finished': False
}

DEFAULT_STATE = {
    'turn': 0,
    'queued_action': None,
    'p1': deepcopy(DEFAULT_PLAYER_STATE),
    'p1_deck': [],
    'p2': dict({'ring': 3}, **deepcopy(DEFAULT_PLAYER_STATE)),
    'p2_deck': []
}


def create_state(state, action):
    return DEFAULT_STATE
    

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
