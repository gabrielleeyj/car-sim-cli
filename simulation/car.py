class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVE_OFFSETS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }

    def __init__(self, name, position, direction, commands):
        """
        Initializes the car with a name, position as a tuple (x, y),
        direction (N, E, S, W), and a list of commands.
        """
        self.name = name
        self.position = position  # Position is now a tuple (x, y)
        self.direction = direction
        self.commands = commands
        self.collided = False

    def rotate_left(self):
        """
        Rotates the car 90 degrees to the left (counter-clockwise).
        """
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx - 1) % 4]

    def rotate_right(self):
        """
        Rotates the car 90 degrees to the right (clockwise).
        """
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self, width, height):
        """
        Moves the car forward by 1 unit in the direction it's facing.
        Ensures that the car doesn't move outside the field boundaries.
        """
        if self.collided:
            return  # Do not move if the car has collided

        x_offset, y_offset = Car.MOVE_OFFSETS[self.direction]
        new_x = self.position[0] + x_offset
        new_y = self.position[1] + y_offset

        # Ensure the car stays within the field boundaries
        if 0 <= new_x < width and 0 <= new_y < height:
            self.position = (new_x, new_y)  # Update the position as a tuple

    def validate_command(self, command):
        """
        Validates a single command to ensure it's one of 'L', 'R', or 'F'.
        """
        if command not in ['L', 'R', 'F']:
            raise ValueError(f"Invalid command '{command}' for car {self.name}")
