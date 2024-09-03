# car-sim-cli

This documents the steps and thought process in which the CLI application is built.

## Step 1: Define the Simulation Field
Field Dimensions: The field is a rectangular grid defined by its width and height, both of which are specified by the user.
Boundary Conditions: The cars are not allowed to move outside the field boundaries. If a command would cause a car to cross the boundary, that command is ignored.

## Step 2: Define the Car Class
**Attributes:**
Name: A unique identifier for the car.  
Position: A tuple (x, y) representing the current position of the car on the field.  
Direction: The current direction the car is facing ('N', 'S', 'E', 'W').  
Commands: A string containing the sequence of commands ('L', 'R', 'F').  

**Methods:**  
`rotate_left()`: Rotates the car 90 degrees to the left.  
`rotate_right()`: Rotates the car 90 degrees to the right.  
`move_forward()`: Moves the car one unit forward in the current direction, unless it would go out of bounds.  

## Step 3: User Interaction Flow
**Initialize Simulation:**

Prompt user to input the field dimensions.  
Store the dimensions and initialize an empty list to hold the cars.  

### Adding Cars:

Prompt the user to input the car’s name, initial position, and direction.  
Prompt the user to input the commands for the car.  
Add the car to the list.  

**Running the Simulation:**

Iterate over the commands for each car, one step at a time.  
Update the car’s position and direction accordingly.  
Check for collisions after each step. If a collision is detected, mark the cars as collided and stop further processing for those cars.  
If no collision, continue until all commands are processed.  

**Displaying Results:**

After the simulation, display the final position and direction of each car, or indicate if any cars collided.

**Restart or Exit:**

Provide the user with an option to start over or exit.



### To run the application

Simply start the command:  

```
python main.py
```

Alternatively:  
