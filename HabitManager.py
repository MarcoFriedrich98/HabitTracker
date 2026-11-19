from pathlib import Path
import json
import datetime
import click
from collections import Counter

filePath = ""

def LoadHabit():


def CreateHabit():
    """Creating a new Habit. The user can enter the habit name and periodicity.
    The habit will be stored in a json file. Additionally the creation date will be stored as well.
    The streak counter will be set to zero."""
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

