class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVE_OFFSETS = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }

    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.position = (x, y)
        self.direction = direction
        self.commands = commands
        self.collided = False

    def rotate_left(self):
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx - 1) % 4]

    def rotate_right(self):
        current_idx = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_idx + 1) % 4]

    def move_forward(self, width, height):
        if self.collided:
            return
        x_offset, y_offset = Car.MOVE_OFFSETS[self.direction]
        new_x = self.position[0] + x_offset
        new_y = self.position[1] + y_offset

        if 0 <= new_x < width and 0 <= new_y < height:
            self.position = (new_x, new_y)

    def validate_command(self, command):
        if command not in ['L', 'R', 'F']:
            raise ValueError(f"Invalid command '{command}' for car {self.name}")
