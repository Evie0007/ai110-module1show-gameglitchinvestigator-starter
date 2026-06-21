import pytest

from logic_utils import check_guess, parse_guess, update_score

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

def test_regression_low_guess_hint_direction():
    # Directly reproduces the reported bug: guessing 5 when secret is 15
    # used to return "Go LOWER" — the opposite of the correct direction.
    # The fix ensures a too-low guess always says "Go HIGHER".
    outcome, message = check_guess(5, 15)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER but got: {message}"
    assert "LOWER" not in message, f"Hint must not say LOWER when guess is too low: {message}"


# ---------------------------------------------------------------------------
# Edge case 1: Decimal input is silently truncated
# ---------------------------------------------------------------------------

def test_decimal_is_truncated_to_int():
    # "50.9" should parse to 50 via int(float(...)), not be rejected outright.
    # Verifies the truncation is floor (not rounding) and ok=True is returned.
    ok, value, err = parse_guess("50.9")
    assert ok is True
    assert value == 50
    assert err is None


def test_decimal_truncation_is_floor_not_round():
    # "3.9" must become 3, not 4. Confirms int(float(...)) truncates toward zero.
    ok, value, err = parse_guess("3.9")
    assert ok is True
    assert value == 3


def test_decimal_zero_fraction_is_accepted():
    # "7.0" is technically an integer value; should parse cleanly to 7.
    ok, value, err = parse_guess("7.0")
    assert ok is True
    assert value == 7


# ---------------------------------------------------------------------------
# Edge case 2: Scientific notation is rejected as "not a number"
# ---------------------------------------------------------------------------

def test_scientific_notation_lowercase_e_is_rejected():
    # "1e2" has no "." so the parser tries int("1e2"), which raises ValueError.
    # Outcome: ok=False with an error message, even though 1e2 == 100 is valid.
    ok, value, err = parse_guess("1e2")
    assert ok is False
    assert value is None
    assert err is not None


def test_scientific_notation_uppercase_E_is_rejected():
    # Same edge case with uppercase E — "1E2" should also be rejected.
    ok, value, err = parse_guess("1E2")
    assert ok is False
    assert value is None
    assert err is not None


def test_valid_integer_100_is_accepted():
    # Confirms that 100 entered as a plain integer IS accepted, distinguishing
    # it from the "1e2" case above.
    ok, value, err = parse_guess("100")
    assert ok is True
    assert value == 100


# ---------------------------------------------------------------------------
# Edge case 3: update_score bug — wrong guess on even attempt adds points
# ---------------------------------------------------------------------------

def test_too_high_on_even_attempt_decreases_score():
    # Bug: update_score returns current_score + 5 for "Too High" when
    # attempt_number is even (e.g. 2, 4, 6, 8), rewarding a wrong guess.
    # A wrong guess must ALWAYS decrease the score.
    score_before = 50
    score_after = update_score(score_before, "Too High", 2)
    assert score_after < score_before, (
        f"Wrong guess on even attempt should decrease score, "
        f"but went {score_before} -> {score_after}"
    )


def test_too_high_on_odd_attempt_decreases_score():
    # Odd attempts don't hit the even-branch bug; verify they also subtract.
    score_before = 50
    score_after = update_score(score_before, "Too High", 3)
    assert score_after < score_before


def test_too_low_on_even_attempt_decreases_score():
    # "Too Low" always subtracts (no even/odd branch), but verify explicitly
    # to ensure a refactor doesn't accidentally introduce the same bug.
    score_before = 50
    score_after = update_score(score_before, "Too Low", 2)
    assert score_after < score_before


def test_win_on_first_attempt_gives_max_score():
    # Winning early should yield the highest bonus. With attempt_number=1:
    # points = max(100 - 10*(1+1), 10) = max(80, 10) = 80.
    score_after = update_score(0, "Win", 1)
    assert score_after == 80


def test_win_score_never_drops_below_minimum_bonus():
    # Late wins (high attempt_number) should still award at least 10 points.
    score_after = update_score(0, "Win", 20)
    assert score_after >= 10
