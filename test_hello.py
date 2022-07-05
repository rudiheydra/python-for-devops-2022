from lib.randomfruit import pick_fruit


def test_pick_fruit():
    fruit_choice = pick_fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]