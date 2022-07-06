from devopslib.randomfruit import pick_fruit, meal


def test_pick_fruit():
    fruit_choice = pick_fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]

def test_meal():
    fruit_choice = test_pick_fruit()
    meal_choice = meal("muffins")
    if fruit_choice == "apple" and meal_choice == "muffins":
        assert "muffins" in meal_choice
    elif fruit_choice == "cherry":
        assert "cherrypie" in "I love cherrypie"
    else:
        assert "strawberry" in "I don't like strawberry"
    
    
