from pathlib import Path
import json
import datetime
import click
from collections import Counter

def LoadHabit():
    try:
        with open("habits.json", "r") as datei:
            habits = json.load(datei)
    except (FileNotFoundError, UnicodeDecodeError):
        habits = []
    except json.JSONDecodeError:
        exit()

def SafeHabit(habit):
    with open("habits.json", "w", encoding="utf-8") as datei:
        json.dump(habit, datei, indent=4, ensure_ascii=False)


def CreateHabit(name, periodicity, daily_target=None, weekly_target=None, monthly_target=None):
    """Creating a new Habit. The user can enter the habit name and periodicity.
    The habit will be stored in a json file. Additionally the creation date will be stored as well.
    The streak counter will be set to zero."""
    habits = LoadHabit()

    for habit in habits:
        if habit["name"].lower() == name.lower():
            raise ValueError("This habit already exists.")

    new_habit = {
        "name": name,
        "periodicity": periodicity,
        "daily_target": daily_target,
        "weekly_target": weekly_target,
        "monthly_target": monthly_target,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "current_streak": 0,
        "longest_streak": 0
    }

    habits.append(new_habit)
    SafeHabit(habits)

def ManageHabit():
    print("Manage Habits")

def CompleteHabit():
    print("Check-off a Habit")

def DeleteHabit():
    print("Delete Habit")

