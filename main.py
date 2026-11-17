import click

@click.command()
def habit_menu():
    while True:
        @click.echo("\n----------------------------------")
        @click.echo("Welcome to your Habit Tracking App")
        @click.echo("------------------------------------")
        @click.echo("1 - Manage Habit")
        @click.echo("2 - Check Habit")
        @click.echo("3 - Analyse Habit")
        @click.echo("0 - Exit")
    
        choice = click.prompt(
            "Please choose an option",
            type=click.Choice(["1", "2", "3"])
        )

        if choice == "1":
            ManageHabit()
        elif choice == "2":
            CompleteHabit()
        elif choice == "3":
            AnalyseHabit()
        elif choice == "0":
            click.echo("Goodbye. See you next time.")
            break

if __name__ == "__main__":
    habit_menu()

