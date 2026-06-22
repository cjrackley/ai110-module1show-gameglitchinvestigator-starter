"""
Regression tests for the bugs fixed in the Game Glitch Investigator.

Each test class maps to one bug that was fixed:
  1. check_guess gave the reversed direction hint (told you to go HIGHER
     when the guess was too high, and vice versa).
  2. update_score gave wrong/inconsistent points: a first-attempt win
     scored only 80 instead of 100, and a "Too High" guess on an even
     attempt *added* points instead of subtracting them.

The new-game / difficulty-switch reset bug lives in app.py's Streamlit
session_state handling, which is UI state rather than pure logic, so it is
exercised in the app rather than unit-tested here.
"""

import os
import sys

# logic_utils.py lives in the project root, one level up from this test dir.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic_utils import (  # noqa: E402
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


class TestCheckGuessDirection:
    """Bug 1: the higher/lower hint was reversed."""

    def test_too_high_tells_player_to_go_lower(self):
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_too_low_tells_player_to_go_higher(self):
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_correct_guess_wins(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"

    def test_direction_correct_even_when_secret_is_a_string(self):
        # app.py sometimes compares the guess against a str(secret), which
        # triggers the TypeError fallback. The direction must still be right.
        outcome_high, message_high = check_guess(60, "50")
        assert outcome_high == "Too High"
        assert "LOWER" in message_high

        outcome_low, message_low = check_guess(40, "50")
        assert outcome_low == "Too Low"
        assert "HIGHER" in message_low


class TestUpdateScore:
    """Bug 2: win points and wrong-guess penalties were miscalculated."""

    def test_first_attempt_win_scores_full_100(self):
        # Regression: the old formula used (attempt_number + 1) and gave 80.
        assert update_score(0, "Win", attempt_number=1) == 100

    def test_win_points_decrease_with_more_attempts(self):
        assert update_score(0, "Win", attempt_number=2) == 90
        assert update_score(0, "Win", attempt_number=3) == 80

    def test_win_points_are_floored_at_10(self):
        # A win after many attempts still awards the 10-point minimum.
        assert update_score(0, "Win", attempt_number=20) == 10

    def test_too_high_always_subtracts_5_even_on_even_attempts(self):
        # Regression: the old code added +5 on even-numbered attempts.
        assert update_score(50, "Too High", attempt_number=2) == 45
        assert update_score(50, "Too High", attempt_number=3) == 45

    def test_too_low_subtracts_5(self):
        assert update_score(50, "Too Low", attempt_number=1) == 45

    def test_score_never_goes_below_zero(self):
        assert update_score(3, "Too High", attempt_number=1) == 0
        assert update_score(0, "Too Low", attempt_number=1) == 0


class TestRefactoredHelpers:
    """The functions now live in logic_utils.py and are importable there."""

    def test_get_range_for_difficulty(self):
        assert get_range_for_difficulty("Easy") == (1, 20)
        assert get_range_for_difficulty("Normal") == (1, 50)
        assert get_range_for_difficulty("Hard") == (1, 100)
        assert get_range_for_difficulty("Unknown") == (1, 100)

    def test_parse_guess_valid_integer(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_parse_guess_truncates_decimal(self):
        ok, value, err = parse_guess("3.9")
        assert ok is True
        assert value == 3

    def test_parse_guess_rejects_empty_and_none(self):
        assert parse_guess("")[0] is False
        assert parse_guess(None)[0] is False

    def test_parse_guess_rejects_non_number(self):
        ok, value, err = parse_guess("abc")
        assert ok is False
        assert err == "That is not a number."
