from deck_analyzer.deck_analyzer import mana_curve
from test import mana_curve_fixture


def test_mana_curve():
    result = mana_curve(mana_curve_fixture.mana_curve_deck)
    assert result == {'1': 5, '0': 1, '2': 3, '5': 2}
