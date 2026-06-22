# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

- Game requirements: Guess a number in the range from 1-100. For Normal difficulty, you have 8 attempts to guess the correct number.
For this current demo, the secret number is 57.
1. User inputs their guess "1" in the box then clicks "Submit Guess".
2. The output shows a hint: "Go HIGHER".
3. User enters another guess "60" and clicks Submit.
4. The output shows a hint: "Go LOWER".
5. User enters the correct guess "57".
6. Output says "Congratulations!" and shows the final score.
7. For each wrong guess, the attempt count is reduced and the score is deducted.
8. To start a new game, the user clicks "New Game" to reset everything.


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 19 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  5%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 10%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 15%]
tests/test_game_logic.py::test_too_high_hint_says_go_lower PASSED        [ 21%]
tests/test_game_logic.py::test_too_low_hint_says_go_higher PASSED        [ 26%]
tests/test_game_logic.py::test_int_secret_exact_match_is_win PASSED      [ 31%]
tests/test_game_logic.py::test_string_secret_raises_type_error PASSED    [ 36%]
tests/test_game_logic.py::test_regression_low_guess_hint_direction PASSED [ 42%]
tests/test_game_logic.py::test_decimal_is_truncated_to_int PASSED        [ 47%]
tests/test_game_logic.py::test_decimal_truncation_is_floor_not_round PASSED [ 52%]
tests/test_game_logic.py::test_decimal_zero_fraction_is_accepted PASSED  [ 57%]
tests/test_game_logic.py::test_scientific_notation_lowercase_e_is_rejected PASSED [ 63%]
tests/test_game_logic.py::test_scientific_notation_uppercase_E_is_rejected PASSED [ 68%]
tests/test_game_logic.py::test_valid_integer_100_is_accepted PASSED      [ 73%]
tests/test_game_logic.py::test_too_high_on_even_attempt_decreases_score PASSED [ 78%]
tests/test_game_logic.py::test_too_high_on_odd_attempt_decreases_score PASSED [ 84%]
tests/test_game_logic.py::test_too_low_on_even_attempt_decreases_score PASSED [ 89%]
tests/test_game_logic.py::test_win_on_first_attempt_gives_max_score PASSED [ 94%]
tests/test_game_logic.py::test_win_score_never_drops_below_minimum_bonus PASSED [100%]

============================= 19 passed in 0.08s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
