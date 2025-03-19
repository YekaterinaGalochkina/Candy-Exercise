import pytest
from candy_problem.candy_problem import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict


def test_candy_count_correctness():
    friend_favorites = [
        ["Sally", ["lollipop", "bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    new_candy_data = get_friends_favorite_candy_count(friend_favorites)

    expected_output = {
        "lollipop": 2,
        "bubble gum": 1,
        "laffy taffy": 3,
        "milky way": 2,
        "licorice": 1,
        "chocolate bar": 1,
        "nerds": 1,
        "sour patch kids": 1
    }

    assert new_candy_data == expected_output

    expected_output = {
        "lollipop": 2,
        "bubble gum": 1,
        "laffy taffy": 3,
        "milky way": 2,
        "licorice": 1,
        "chocolate bar": 1,
        "nerds": 1,
        "sour patch kids": 1
    }

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8

    def test_create_new_candy_data_structure():
    # Arrange
        friend_favorites = [
        ["Sally", ["lollipop", "bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    expected_output = {
        "lollipop": ["Sally", "Bob"],
        "bubble gum": ["Sally"],
        "laffy taffy": ["Sally", "Arlene", "Carlie"],
        "milky way": ["Bob", "Arlene"],
        "licorice": ["Bob"],
        "chocolate bar": ["Arlene"],
        "nerds": ["Carlie"],
        "sour patch kids": ["Carlie"]
    }
    
    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert new_candy_data == expected_output

 
