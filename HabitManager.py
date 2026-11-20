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


def CreateHabit(name, periodicity, daily_target=None, weekly_target=None):
    """Creating a new Habit. The user can enter the habit name and periodicity.
    The habit will be stored in a json file. Additionally the creation date will be stored as well.
    The streak counter will be set to zero."""
    habits = LoadHabit()
    HabitName = input("Enter Habit Name: ")
    @click.echo("How often to you want to complete this Haibt?")
    @click.echo("1 - daily")
    @click.echo("2 - weekly")
    @click.echo("3 - monthly")

    choice = click.prompt(
        "Please select one of the options",
        type=click.Choice(["1", "2", "3"])
    )

def ManageHabit():
    print("Manage Habits")

def CompleteHabit():
    print("Check-off a Habit")

def DeleteHabit():
    print("Delete Habit")

