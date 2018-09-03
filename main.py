import pydux
from pprint import pprint
from reducer import reducer


def play():
    store = pydux.create_store(reducer)
    store.subscribe(lambda: print(pprint(store.get_state())))

    store.dispatch({'type': 'create_state'})
    store.dispatch({
        'type': 'play_creature',
        'card_index': 0,
        'player': 'p1',
        'lane': 'field_lane'
    })
    store.dispatch({
        'type': 'consume_action'
    })
    print('get state {}'.format(pprint(store.get_state())))


if __name__ == '__main__':
    play()