import pytest
from iterators import Houses

def test_create_a_house():
    assert Houses

def test_print_house():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    actual = str(houses)
    expected = "House: Hogwarts; Residents: Harry, Ryan, Dumbledore, \nHouse: Hell Kichen; Residents: Gordan, \nHouse: HuntedHouse; Residents: Morticia, Wednesday, Gomez, \n"
    assert expected == actual

def test_add_new_house():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    houses.add_house("12345house", ["Joy", "Henry", "Tim"])
    actual = len(houses)
    expected = len(houses)
    assert actual == expected

def test_iterate_house():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    result = ""
    for h in houses:
        result += h + ","
    assert result == "Hogwarts,Hell Kichen,HuntedHouse,"

def test_equal_function():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    new_data = {"Hogwarts": [""], "Hell Kichen": [""],
                "HuntedHouse": [""]}
    another_house = Houses(new_data)
    assert houses == another_house

def test_equal_function_2():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    new_data = {"Hogwarts": [""], "Hell Kichen": [""]}
    another_house = Houses(new_data)
    assert houses != another_house

def test_list_comprehension():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    actual = [h for h in houses]
    expect = ["Hogwarts","Hell Kichen","HuntedHouse"]
    assert actual == expect

def test_getitem():
    data = {"Hogwarts": ["Harry", "Ryan", "Dumbledore"], "Hell Kichen": ["Gordan"],
            "HuntedHouse": ["Morticia", "Wednesday", "Gomez"]}
    houses = Houses(data)
    actual = houses[("Hogwarts")]
    expected = ["Harry", "Ryan", "Dumbledore"]
    assert actual == expected