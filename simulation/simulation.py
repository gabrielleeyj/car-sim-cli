from simulation.field import Field

def run_simulation(field):
    max_commands = max(len(car.commands) for car in field.cars)
    positions = {car.position: car for car in field.cars}

    for step in range(max_commands):
        new_positions = {}
        for car in field.cars:
            if car.collided or step >= len(car.commands):
                continue

            command = car.commands[step]
            if command == 'L':
                car.rotate_left()
            elif command == 'R':
                car.rotate_right()
            elif command == 'F':
                car.move_forward(field.width, field.height)

            if car.position in positions:
                other_car = positions[car.position]
                if other_car != car:
                    car.collided = True
                    other_car.collided = True
            new_positions[car.position] = car

        positions = new_positions

    return field.cars

