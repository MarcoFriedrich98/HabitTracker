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
                    click.echo("\n----CREATING A NEW HABIT-----")

                    # Ask for habit name
                    name = click.prompt(
                        "Enter the name of your habit: ",
                        type=str
                    ).strip()

                    if not name:
                        click.echo("Error: Please enter a habit name")
                        return

                    # Ask for periodicity
                    click.echo("\nChoose the periodicity")
                    click.echo("1 - daily")
                    click.echo("2 - multiple times a day")
                    click.echo("3 - weekly")
                    click.echo("4 - multiple times a wwek")
                    click.echo("5 - monthly")
                    click.echo("6 - multiple times a month")
                    click.echo("0 - Exit")

                    periodicity = click.prompt(
                        "Enter a number between 1 and 6: ",
                        type=click.Choice(["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["0"])
                    )

                    periodicities = {
                        "1": "daily",
                        "2": "multiple times a day",
                        "3": "weekly",
                        "4": "multiple times a week",
                        "5": "monthly",
                        "6": "multiple times a month"
                    }

                    periodicity = periodicities[choice]

                    daily_target = None
                    weekly_target = None
                    monthly_target = None
                    if periodicity == "multiple times a day":
                        daily_target = click.prompt(
                            "How many times a day do you want to complete this habit?",
                            type=click.IntRange(2, 24)
                        )
                    elif periodicity == "multiple times a week":
                        weekly_target = click.prompt(
                            "How many times a week to you want to complete this habit?",
                            type=click.IntRange(2, 7)
                        )
                    elif periodicity == "multiple times a month":
                        monthly_target = click.prompt(
                            "How many times a month do you want to complete this habit?",
                            type=click.IntRange(2 , 30)
                        )
                    elif periodicity == "0":
                        click.echo("Back to main menu")
                        break

                    try:
                        habit = CreateHabit(name, periodicity, daily_target, weekly_target, monthly_target)
                        click.echo("\nHabit successfully created.")
                        click.echo(f"Name: {name}")
                        click.echo(f"Periodicity: {periodicity}")

                        if daily_target:
                            click.echo(f"Daily target: {daily_target} times")
                        elif weekly_target:
                            click.echo(f"Weekly target: {weekly_target} days")
                        elif monthly_target:
                            click.echo(f"Monthly target: {monthly_target} days")

                        click.echo("Current streak: 0")

                    except ValueError as error:
                        click.echo(f"Error: {error}")

                    
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

