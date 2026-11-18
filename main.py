import click
from HabitManager import CreateHabit, ManageHabit, CompleteHabit, DeleteHabit
from HabitAnalytics import AnalyseHabit

@click.command()
def habit_menu():
    while True:
        click.echo("\n----------------------------------")
        click.echo("Welcome to your Habit Tracking App")
        click.echo("------------------------------------")
        click.echo("1 - Manage Habit")
        click.echo("2 - Complete Habit")
        click.echo("3 - Analyse Habit")
        click.echo("0 - Exit")
    
        choice = click.prompt(
            "Please choose an option",
            type=click.Choice(["1", "2", "3", "0"])
        )

        if choice == "1":
            while True:
                """Creating the Sub Menu of Managing Habits"""
                click.echo("\n----- HABIT MANAGEMENT -----")
                click.echo("1 - I want to create a new Habit.")
                click.echo("2 - I want to manage an existing Habit.")
                click.echo("3 - I want to delete a Habit.")
                click.echo("0 - Exit")

                submenu_manage_habit = click.prompt(
                    "Select one of the given options",
                    type=click.Choice(["1", "2", "3", "0"])
                )

                if submenu_manage_habit == "1":
                    CreateHabit()
                elif submenu_manage_habit == "2":
                    ManageHabit()
                elif submenu_manage_habit == "3":
                    DeleteHabit()
                elif submenu_manage_habit == "0":
                    click.echo("See you next time.")
                    break
        elif choice == "2":
            CompleteHabit()
        elif choice == "3":
            AnalyseHabit()
        elif choice == "0":
            click.echo("Goodbye. See you next time.")
            break

if __name__ == "__main__":
    habit_menu()

