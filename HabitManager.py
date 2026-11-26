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
    def habit_from_dict(cls, data):
        return cls (
            name=data["name"],
            periodicty=data["periodicity"],
            created_at=data["created_at"],
            target_count=data.get["target_count", 1],
            completed_at=data.get["completed_at", []],
            current_streak=data.get["current_streak", 0],
            longest_streak=data.get["longest_streak", 0]
        )

class HabitManager:
    periodicities = {
        "daily",
        "multiple_per_day",
        "weekly",
        "multiple_per_week",
        "monthly",
        "multiple_per_month"
    }

    def __init__(self, file_path="habits.json"):
        self.file_path = Path.file_path
        self.habits = []
        self.LoadHabit()

    def LoadHabit(self):
        """Load the Habit from the json file"""
        if not self.file_path.exists():
            self.habits = []
            return
        
        try:
            with open(self.file_path, "r", encoding="utf-8") as datei:
                self.habits = json.load(datei)
        except (FileNotFoundError, UnicodeDecodeError):
            self.habits = []
        except json.JSONDecodeError:
            exit()
        return self.habits

    def SafeHabit(self, habit):
        """Saves the Habit in the json file."""
        with open(self, "habits.json", "w", encoding="utf-8") as datei:
            json.dump(self, habit, datei, indent=4, ensure_ascii=False)

    def CreateHabit(self, name, periodicity, target_count=1):
        """Creating a new Habit. The user can enter the habit name and periodicity.
        The habit will be stored in a json file. Additionally the creation date will be stored as well.
        The streak counter will be set to zero."""
        habits = self.LoadHabit()

        name = name.strip()

        if not name:
            raise ValueError("Habit name cannont be empty.")

        if periodicity not in self.periodicities:
            raise ValueError("Invalid Periodicity")

        if periodicity in {"daily", "weeikly", "monthly"}:
            target_count = 1
        elif not isinstance(target_count, int) or target_count < 2:
            raise ValueError("Target count must be at least two.")

        for habit in habits:
            if habit["name"].lower() == name.lower():
                raise ValueError("This habit already exists.")

        new_habit = Habit(
            name=name,
            periodicity=periodicity,
            target_count=target_count
            created_at=datetime.now().isoformat(timespec="seconds"),
            current_streak=0,
            longest_streak=0
        )

        habits.append(new_habit)
        self.SafeHabit(habit)

def get_all_habits(self):
    """Return all currently tracked habits."""
    return self.habits

def ManageHabit():
    print("Manage Habits")

def CompleteHabit():
    print("Check-off a Habit")

def DeleteHabit():
    print("Delete Habit")

