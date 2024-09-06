import click
from simulation import Car, Field, run_simulation

@click.command()
@click.option('--update-field', is_flag=True, help='Update the field size.')
def main(update_field):
    """
    Simulates autonomous driving cars in a field of specified width and height.
    """

    # Load the field size from the file
    width, height = Field.load_field_size()

    if update_field or width is None or height is None:
        # Prompt for field size if updating or if no size is saved
        width = click.prompt('Field width', type=int)
        height = click.prompt('Field height', type=int)
        Field.save_field_size(width, height)
        click.echo(
            f"You have created/updated a field of {width} x {height}.\n")
    else:
        click.echo(f"Loaded saved field size: {width} x {height}.\n")

    field = Field(width, height)

    validate_car = []

    while True:
        click.echo("Please choose from the following options:")
        click.echo("[1] Add a car to field")
        click.echo("[2] Run simulation")
        click.echo("[3] Update field size")
        choice = click.prompt("", type=int)

        if choice == 1:
            name = click.prompt("Please enter the name of the car")
            validate_car.append(name)
            if len(validate_car) > 1:
                if name in validate_car:
                    name = click.prompt(
                            "Please re-enter name of the car")

            x = click.prompt(
                f"Please enter initial X position of car {name}", type=int)
            while x < 0:
                x = click.prompt(
                        f"Please re-enter initial X position of car {name}", type=int)
            y = click.prompt(
                f"Please enter initial Y position of car {name}", type=int)
            while y < 0:
                y = click.prompt(
                        f"Please re-enter initial Y position of car {name}", type=int)
            direction = click.prompt(
                f"Please enter initial direction (N, S, E, W) for car {name}", type=click.Choice(['N', 'S', 'E', 'W']))
            commands = click.prompt(
                f"Please enter the commands for car {name}")


# Same car name should not be there, car should not be on the same position as before

            # Validate the commands and check for position conflicts
            car = Car(name, x, y, direction, commands)


            for command in commands:
                try:
                    car.validate_command(command)
                except ValueError as e:
                    click.echo(e)
                    return

            try:
                field.add_car(car)
            except ValueError as e:
                click.echo(e)
                return

            click.echo(f"\nYour current list of cars are:")
            for car in field.cars:
                click.echo(
                    f"- {car.name}, {car.position} {car.direction}, {car.commands}")

        elif choice == 2:
            try:
                cars = run_simulation(field)
                click.echo("\nFinal Positions:")
                for car in cars:
                    if car.collided:
                        click.echo(f"- {car.name}, collided")
                    else:
                        click.echo(
                            f"- {car.name}, {car.position} {car.direction}")

                # Plot the final positions of the cars
                Field.plot_car_positions(field, cars)

            except ValueError as e:
                click.echo(e)
            break

        elif choice == 3:
            # Allow user to update the field size
            width = click.prompt('New field width', type=int)
            height = click.prompt('New field height', type=int)
            Field.save_field_size(width, height)
            click.echo(f"Field size updated to {width} x {height}.\n")
            field = Field(width, height)  # Reset the field with the new size

    click.echo("\nThank you for running the simulation. Goodbye!")


if __name__ == "__main__":
    main()
