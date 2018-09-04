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


def test_consume_action_attack_face():
    old_state = deepcopy(DEFAULT_STATE)
    action = {
        'type': 'attack',
        'player': 'p1',
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


def test_consume_action_attack_creature():
    mudcrab_merchant = {
        'power': 5,
        'health': 1,
        'can_attack': True,
        'name': 'Mudcrab Merchant'
    }
    creeper = {
        'power': 1,
        'health': 1,
        'can_attack': False,
        'name': 'Creeper'
    }
    old_state = deepcopy(DEFAULT_STATE)
    action = {
        'type': 'attack',
        'player': 'p1',
        'target': {'lane_index': 0},
        'lane': 'field_lane',
        'lane_index': 0
    }
    p1 = deepcopy(DEFAULT_PLAYER_STATE)
    p1.update({'field_lane': [mudcrab_merchant]})
    p2 = deepcopy(DEFAULT_PLAYER_STATE)
    p2.update({'field_lane': [creeper]})
    old_state.update({'p1': p1, 'p2': p2})
    new_state = consume_action(old_state, action)

    assert new_state != old_state
    assert new_state['p1']['field_lane'] == []
    assert new_state['p2']['field_lane'] == []
    assert new_state['p1']['discard_pile'][0]['name'] == 'Mudcrab Merchant'
    assert new_state['p2']['discard_pile'][0]['name'] == 'Creeper'
