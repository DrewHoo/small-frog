from copy import deepcopy

DEFAULT_PLAYER_STATE = {
    'max_magicka': 0,
    'current_magicka': 0,
    'field_lane': [],
    'shadow_lane': [],
    'active_supports': [],
    'discard_pile': [],
    'hand': [],
    'health': 30,
    'runes':  5,
    'is_finished': False
}

DEFAULT_STATE = {
    'turn': 1,
    'queued_action': None,
    'p1': deepcopy(DEFAULT_PLAYER_STATE),
    'p1_deck': [],
    'p2': dict({'ring': 3}, **deepcopy(DEFAULT_PLAYER_STATE)),
    'p2_deck': []
}
