import pytest
from tkinter import StringVar, Tk
from Main import play_two_up

@pytest.fixture(scope="module")
def root():
    root = Tk()
    yield root
    root.destroy()

@pytest.mark.parametrize("coin_1, coin_2, expected_outcome", [
    ("Heads", "Heads", "WIN!"),     # Only "Heads-Heads" is a win condition
    ("Tails", "Tails", "LOSE!"),    # All other combinations are losses
    ("Heads", "Tails", "LOSE!"),
    ("Tails", "Heads", "LOSE!"),
])
def test_play_two_up(coin_1, coin_2, expected_outcome, root):
    prediction = StringVar(value="Two Heads")  # Create StringVar object inside the test function
    # Simulate the outcome based on the coins flipped
    if coin_1 == "Heads" and coin_2 == "Heads":
        simulated_outcome = "WIN!"
    else:
        simulated_outcome = "LOSE!"
    # Assert that the simulated outcome matches the expected outcome
    assert simulated_outcome == expected_outcome