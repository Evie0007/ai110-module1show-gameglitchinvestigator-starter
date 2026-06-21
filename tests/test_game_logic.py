import pytest

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_go_lower():
    # Regression test for the high/low bug: when the guess is TOO HIGH,
    # the hint must tell the player to go LOWER (it used to say HIGHER).
    _outcome, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_hint_says_go_higher():
    # Regression test for the high/low bug: when the guess is TOO LOW,
    # the hint must tell the player to go HIGHER (it used to say LOWER).
    _outcome, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message

def test_int_secret_exact_match_is_win():
    # Regression test for the type-coercion bug: app.py used to convert the
    # secret to a str on even-numbered attempts, so an exact match like
    # check_guess(50, "50") was NOT equal (50 == "50" is False) and wins were
    # missed. With the secret kept as an int, an exact int match always wins.
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"

def test_string_secret_raises_type_error():
    # Documents WHY the app.py fix is needed: comparing an int guess against a
    # str secret (the old even-attempt behavior) raises TypeError in Python 3.
    # Keeping the secret an int every attempt is what prevents this glitch.
    with pytest.raises(TypeError):
        check_guess(60, "50")
