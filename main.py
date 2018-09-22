import pydux
from pprint import pprint
from reducer import reducer
from game_engine import GameEngine


def play():
    store = pydux.create_store(reducer)
    game_engine = GameEngine(store)

    game_engine.request({'type': 'create_state'})
    response = game_engine.request({
        'type': 'play_creature',
        'card_index': 0,
        'player': 'p1',
        'lane': 'field_lane'
    })

    print(pprint(response))


if __name__ == '__main__':
    play()