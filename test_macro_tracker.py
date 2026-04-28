import pytest

from macro_tracker import (
    add_meal,
    calculate_totals,
    compare_to_goals,
    create_meal,
    load_data,
    set_goals,
    validate_macro_value,
)


def test_create_meal_returns_correct_dictionary():
    meal = create_meal("Chicken bowl", 520, 42, 55, 14)

    assert meal["name"] == "Chicken bowl"
    assert meal["calories"] == 520
    assert meal["protein"] == 42
    assert meal["carbs"] == 55
    assert meal["fat"] == 14


def test_calculate_totals_adds_multiple_meals():
    meals = [
        create_meal("Breakfast", 300, 20, 30, 10),
        create_meal("Lunch", 500, 40, 50, 15),
    ]

    totals = calculate_totals(meals)

    assert totals["calories"] == 800
    assert totals["protein"] == 60
    assert totals["carbs"] == 80
    assert totals["fat"] == 25


def test_negative_macro_value_raises_error():
    with pytest.raises(ValueError):
        validate_macro_value(-1)


def test_add_meal_saves_to_file(tmp_path):
    test_file = tmp_path / "test_macro_data.json"

    add_meal("Protein smoothie", 350, 30, 35, 8, test_file)
    data = load_data(test_file)

    assert len(data["meals"]) == 1
    assert data["meals"][0]["name"] == "Protein smoothie"
    assert data["meals"][0]["calories"] == 350


def test_set_goals_saves_goals_to_file(tmp_path):
    test_file = tmp_path / "test_macro_data.json"

    set_goals(2000, 130, 220, 60, test_file)
    data = load_data(test_file)

    assert data["goals"]["calories"] == 2000
    assert data["goals"]["protein"] == 130
    assert data["goals"]["carbs"] == 220
    assert data["goals"]["fat"] == 60


def test_compare_to_goals_calculates_remaining_macros():
    totals = {
        "calories": 800,
        "protein": 60,
        "carbs": 90,
        "fat": 25,
    }

    goals = {
        "name": "Daily Goals",
        "calories": 2000,
        "protein": 130,
        "carbs": 220,
        "fat": 60,
    }

    remaining = compare_to_goals(totals, goals)

    assert remaining["calories"] == 1200
    assert remaining["protein"] == 70
    assert remaining["carbs"] == 130
    assert remaining["fat"] == 35