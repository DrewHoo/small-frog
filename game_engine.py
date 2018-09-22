

class GameEngine:
    store = {}

    def __init__(self, store):
        self.store = store
    

    def request(self, request):
        self.store.dispatch(request)
        if 'player' in request:
            return self.prepare_state_for_player(request)
        else:
            return {}


    def prepare_state_for_player(self, action):
        player = action['player']
        opponent = 'p1' if player == 'p2' else 'p1'

        return {
            'field_lane': {
                'opponent': [],
                'own': []
            },
            'shadow_lane': {
                'opponent': [],
                'own': []
            },
            'hand': [],
            'health': 30,
            'runes': 5,
            'discard_pile': [],
            'opponent_discard_pile': [],
            'opponent_hand': 4,
            'max_magicka': 1,
            'current_magicka': 0,
            'turn': 0
        }