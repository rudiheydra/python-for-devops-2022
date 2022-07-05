from random import choices


def pick_fruit():
    fruits = ["apple", "cherry", "strawberry"]
    return choices(fruits)[0]
