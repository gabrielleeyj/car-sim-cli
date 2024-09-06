import click
import json
import os
import matplotlib.pyplot as plt

FIELD_SIZE_FILE = "field_size.json"

class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cars = []

    def add_car(self, car):
        # Check for multiple cars at the same position
        for existing_car in self.cars:
            if existing_car.position == car.position:
                click.echo(f"Car {car.name} has the same position as {existing_car.name}.")
                new_x = click.prompt(f"Car {car.name} input new x position", type=int)
                new_y = click.prompt(f"Car {car.name} input new y position", type=int)
                car.position = (new_x, new_y)  # Create a new tuple with updated values

        self.cars.append(car)

    def check_collisions(self):
        positions = {}
        for car in self.cars:
            if car.position in positions:
                raise ValueError(
                    f"Collision detected at position {car.position} between {car.name} and {positions[car.position].name}.")
            positions[car.position] = car

    @staticmethod
    def load_field_size():
        if os.path.exists(FIELD_SIZE_FILE):
            with open(FIELD_SIZE_FILE, 'r') as file:
                data = json.load(file)
                return data.get('width'), data.get('height')
        return None, None

    @staticmethod
    def save_field_size(width, height):
        with open(FIELD_SIZE_FILE, 'w') as file:
            json.dump({'width': width, 'height': height}, file)

    @staticmethod
    def plot_car_positions(field, cars):
        fig, ax = plt.subplots()

        # Plot field boundary
        ax.set_xlim(0, field.width)
        ax.set_ylim(0, field.height)
        ax.set_xticks(range(field.width + 1))
        ax.set_yticks(range(field.height + 1))
        ax.grid(True)

        # Plot each car
        for car in cars:
            x, y = car.position
            ax.text(x, y, car.name, fontsize=12, ha='center', va='center',
                    bbox=dict(facecolor='red' if car.collided else 'green', alpha=0.5, edgecolor='black'))

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Final Positions of Cars on the Field')
        plt.show()

