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

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 37
2. Game returns "Too High"
3. User enters a guess of 23
4. Game returns "Too Low"
5. Game ends after the correct guess is entered

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.14.2, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\camer\Desktop\AI Engineering\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\camer\Desktop\AI Engineering\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collecting ... collected 15 items

test/test_game_logic.py::TestCheckGuessDirection::test_too_high_tells_player_to_go_lower PASSED [  6%]
test/test_game_logic.py::TestCheckGuessDirection::test_too_low_tells_player_to_go_higher PASSED [ 13%]
test/test_game_logic.py::TestCheckGuessDirection::test_correct_guess_wins PASSED [ 20%]
test/test_game_logic.py::TestCheckGuessDirection::test_direction_correct_even_when_secret_is_a_string PASSED [ 26%]
test/test_game_logic.py::TestUpdateScore::test_first_attempt_win_scores_full_100 PASSED [ 33%]
test/test_game_logic.py::TestUpdateScore::test_win_points_decrease_with_more_attempts PASSED [ 40%]
test/test_game_logic.py::TestUpdateScore::test_win_points_are_floored_at_10 PASSED [ 46%]
test/test_game_logic.py::TestUpdateScore::test_too_high_always_subtracts_5_even_on_even_attempts PASSED [ 53%]
test/test_game_logic.py::TestUpdateScore::test_too_low_subtracts_5 PASSED [ 60%]
test/test_game_logic.py::TestUpdateScore::test_score_never_goes_below_zero PASSED [ 66%]
test/test_game_logic.py::TestRefactoredHelpers::test_get_range_for_difficulty PASSED [ 73%]
test/test_game_logic.py::TestRefactoredHelpers::test_parse_guess_valid_integer PASSED [ 80%]
test/test_game_logic.py::TestRefactoredHelpers::test_parse_guess_truncates_decimal PASSED [ 86%]
test/test_game_logic.py::TestRefactoredHelpers::test_parse_guess_rejects_empty_and_none PASSED [ 93%]
test/test_game_logic.py::TestRefactoredHelpers::test_parse_guess_rejects_non_number PASSED [100%]

============================= 15 passed in 0.09s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
