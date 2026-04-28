## Macro Tracker CLI

Macro Tracker CLI is a simple command-line application for tracking daily calories and macronutrients. Users can add meals with calories, protein, carbohydrates, and fat, then view a daily summary of their totals. It also shows how many macros they have remaining for the day. Users can set daily calorie and macro goals, allowing the program to track progress and help them stay on track.

This tool solves the problem of needing a quick and lightweight way to track nutrition without using a full mobile app. It stores meal and goal data locally in a JSON file, so users can keep track of their daily intake directly from the terminal.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/engelb-er/macro-tracker-cli.git
```

2. Navigate into the project folder:

```bash
cd macro-tracker-cli
```

3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install pytest
```

---

## Usage

### 1. Add a meal

```bash
python macro_tracker.py add "Chicken rice bowl" --calories 520 --protein 42 --carbs 55 --fat 14
```

**Expected output:**
```
Added meal: Chicken rice bowl
```

---

### 2. Set daily goals

```bash
python macro_tracker.py goals --calories 2000 --protein 130 --carbs 220 --fat 60
```

**Expected output:**
```
Daily goals saved.
Calories: 2000
Protein: 130g
Carbs: 220g
Fat: 60g
```

---

### 3. View daily summary

```bash
python macro_tracker.py summary
```

**Expected output:**
```
Daily Macro Summary
-------------------
Calories: 520
Protein:  42g
Carbs:    55g
Fat:      14g
```

---

## Examples

### Example 1: Log breakfast

```bash
python macro_tracker.py add "Greek yogurt and berries" --calories 250 --protein 20 --carbs 30 --fat 4
```

### Example 2: Log lunch

```bash
python macro_tracker.py add "Turkey sandwich" --calories 450 --protein 35 --carbs 45 --fat 12
```

### Example 3: Check totals for the day

```bash
python macro_tracker.py summary
```

---

## Running Tests

To run the test suite:

```bash
pytest
```

All tests should pass and verify that the program works correctly.

---

## Known Limitations and Future Ideas

- The app does not currently support tracking meals by date  
- Meals cannot be edited or deleted once added if you only eat a portion of the meal.
