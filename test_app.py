from app import random_fruit


def test_random_fruit():
    assert "apple" or "mangoe" or "banana" in random_fruit()
