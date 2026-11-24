from pathlib import Path
from dataclasses import dataclass, field
import json
import datetime

@dataclass
class Habit:
    name: str
    periodicity: str
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )
    target_count: int = 1
    completed_at: list = field(default_factory=list)
    current_streak: int = 0
    longest_streak: int = 0

    def habit_to_dict(self):
        """Convert a Habit into a dictionary."""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "target_count": self.target_count,
            "completed_at": self.completed_at,
            "current_streak": self.current_streak,
            "longest_streak": self.longest_streak
        }

    @classmethod
    def habit_to_dict(cls, data):
        return cls {
            name=data["name"],
            periodicty=data["periodicity"],
            created_at=data["created_at"],
            target_count=data["target_count"],
            completed_at=data["completed_at"],
            current_streak=data["current_streak"],
            longest_streak=data["longest_streak"]
        }

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

