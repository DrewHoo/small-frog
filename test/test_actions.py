from fixtures.defaults import DEFAULT_STATE, DEFAULT_PLAYER_STATE
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


def test_consume_action_play_creature():
    old_state = deepcopy(DEFAULT_STATE)
    action = {
        'type': 'play_creature',
        'card_index': 0,
        'player': 'p1',
        'lane': 'shadow_lane'
    }
    p1 = deepcopy(DEFAULT_PLAYER_STATE)
    p1.update({'hand': [{'name': 'marauder', 'cost': 0}]})
    old_state.update({'queued_action': action, 'p1': p1})
    new_state = consume_action(old_state, action)

    assert new_state['p1']['hand'] == []
    assert new_state['p1']['shadow_lane'] == [old_state['p1']['hand'][0]]


def test_consume_action_attack():
    old_state = deepcopy(DEFAULT_STATE)
    action = {
        'type': 'attack',
        'player': 'p1',
        'target': 'face',
        'lane': 'field_lane',
        'lane_index': 0
    }
    p1 = deepcopy(DEFAULT_PLAYER_STATE)
    p1.update({'field_lane': [{
        'power': 5,
        'health': 1,
        'can_attack': True,
        'name': 'Mudcrab Merchant'
    }]})
    old_state.update({'p1': p1})
    new_state = consume_action(old_state, action)

    assert new_state != old_state
    assert new_state['p1']['field_lane'][0]['can_attack'] == False
    assert new_state['p2']['health'] == 25
