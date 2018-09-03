from reducer import DEFAULT_STATE
from actions.play_creature import play_creature
from actions.consume_action import consume_action
from copy import deepcopy


def test_play_creature():
    old_state = deepcopy(DEFAULT_STATE)
    action = {
        'type': 'play_creature',
        'card_index': 0,
        'player': 'p1',
        'lane': 'shadow_lane'
    }
    new_state = play_creature(old_state, action)

    assert new_state != old_state
    assert new_state['queued_action'] == action

def test_consume_action():
    old_state = deepcopy(DEFAULT_STATE)
    action = {
        'type': 'play_creature',
        'card_index': 0,
        'player': 'p1',
        'lane': 'shadow_lane'
    }
    old_state.update({'queued_action': action})
    new_state = consume_action(old_state, action)

    assert new_state['p1']['hand'] == []
    assert new_state['p1']['shadow_lane'] == [old_state['p1']['hand'][0]]