import argparse
import json
from pathlib import Path

DATA_FILE = Path("macro_data.json")


def validate_macro_value(value):
    if value < 0:
        raise ValueError("Macro values cannot be negative.")
    return value


def load_data(file_path=DATA_FILE):
    if not file_path.exists():
        return {"meals": [], "goals": None}

    with open(file_path, "r") as file:
        return json.load(file)


def save_data(data, file_path=DATA_FILE):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def create_meal(name, calories, protein, carbs, fat):
    return {
        "name": name,
        "calories": validate_macro_value(calories),
        "protein": validate_macro_value(protein),
        "carbs": validate_macro_value(carbs),
        "fat": validate_macro_value(fat),
    }


def add_meal(name, calories, protein, carbs, fat, file_path=DATA_FILE):
    data = load_data(file_path)
    meal = create_meal(name, calories, protein, carbs, fat)
    data["meals"].append(meal)
    save_data(data, file_path)
    return meal


def calculate_totals(meals):
    return {
        "calories": sum(meal["calories"] for meal in meals),
        "protein": sum(meal["protein"] for meal in meals),
        "carbs": sum(meal["carbs"] for meal in meals),
        "fat": sum(meal["fat"] for meal in meals),
    }


def set_goals(calories, protein, carbs, fat, file_path=DATA_FILE):
    data = load_data(file_path)
    data["goals"] = create_meal("Daily Goals", calories, protein, carbs, fat)
    save_data(data, file_path)
    return data["goals"]


def compare_to_goals(totals, goals):
    if goals is None:
        return None

    return {
        "calories": goals["calories"] - totals["calories"],
        "protein": goals["protein"] - totals["protein"],
        "carbs": goals["carbs"] - totals["carbs"],
        "fat": goals["fat"] - totals["fat"],
    }


def show_summary(file_path=DATA_FILE):
    data = load_data(file_path)
    totals = calculate_totals(data["meals"])

    print("\nDaily Macro Summary")
    print("-------------------")
    print(f"Calories: {totals['calories']}")
    print(f"Protein:  {totals['protein']}g")
    print(f"Carbs:    {totals['carbs']}g")
    print(f"Fat:      {totals['fat']}g")

    if data["goals"]:
        remaining = compare_to_goals(totals, data["goals"])
        print("\nRemaining Until Goal")
        print("--------------------")
        print(f"Calories: {remaining['calories']}")
        print(f"Protein:  {remaining['protein']}g")
        print(f"Carbs:    {remaining['carbs']}g")
        print(f"Fat:      {remaining['fat']}g")


def main():
    parser = argparse.ArgumentParser(description="Track daily calories and macros.")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a meal")
    add_parser.add_argument("name")
    add_parser.add_argument("--calories", type=int, required=True)
    add_parser.add_argument("--protein", type=int, required=True)
    add_parser.add_argument("--carbs", type=int, required=True)
    add_parser.add_argument("--fat", type=int, required=True)

    goals_parser = subparsers.add_parser("goals", help="Set daily macro goals")
    goals_parser.add_argument("--calories", type=int, required=True)
    goals_parser.add_argument("--protein", type=int, required=True)
    goals_parser.add_argument("--carbs", type=int, required=True)
    goals_parser.add_argument("--fat", type=int, required=True)

    subparsers.add_parser("summary", help="Show daily macro summary")

    args = parser.parse_args()

    try:
        if args.command == "add":
            meal = add_meal(
                args.name,
                args.calories,
                args.protein,
                args.carbs,
                args.fat,
            )
            print(f"Added meal: {meal['name']}")

        elif args.command == "goals":
            goals = set_goals(
                args.calories,
                args.protein,
                args.carbs,
                args.fat,
            )
            print("Daily goals saved.")
            print(f"Calories: {goals['calories']}")
            print(f"Protein: {goals['protein']}g")
            print(f"Carbs: {goals['carbs']}g")
            print(f"Fat: {goals['fat']}g")

        elif args.command == "summary":
            show_summary()

        else:
            parser.print_help()

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()