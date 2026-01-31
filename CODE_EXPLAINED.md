# 🧑‍💻 Code Explained

This guide is for those who want to understand *how* the code works. It covers the structure, key concepts, and how to add your own programs.

## Key Concepts

### 1. Asynchronous Programming (`async`/`await`)
This project uses Python's `asyncio` features (via Pybricks). This allows the robot to do multiple things at once (like flashing lights while waiting for a button press).

- **`async def function()`**: Defines a function that can be paused and resumed.
- **`await something()`**: Pauses the current function until `something` is finished.

### 2. Classes and Objects
We use Object-Oriented Programming (OOP) to organize the code.
- **`UI` (in `guis.py`)**: A "blueprint" for any User Interface. It handles checking buttons in a loop.
- **`ProgramManager` (in `guis.py`)**: A specific type of UI that manages a list of missions.
- **`MotorControlManager`**: Another UI that lets you manually move motors.

## File Breakdown

### `hardware_config.py`
This file is the "Central Nervous System". It sets up all the connections.
- It initializes the `Hub`, `Motor`s, and `DriveBase`.
- It defines constants like `DEFAULT_SPEED` so you can change the speed of the whole robot in one place.

### `guis.py`
This file handles the logic for the menus.
- **`ProgramManager`**:
  - `add_program()`: Adds a new mission to the list.
  - `run()`: The main loop that waits for button presses.
  - `exec_current_program()`: Runs the selected mission and handles errors (flashing red light if something crashes).

### `main.py`
This is where the magic happens.
1. It imports everything.
2. It defines the mission functions (`ship()`, `rightside()`, etc.).
   - These functions just list the commands: "Drive straight", "Turn", "Move Arm".
3. It creates a `ProgramManager` (`PM`).
4. It registers the missions using `PM.add_program(...)`.
5. It starts the menu loop with `run_task(main())`.

## How to Add a New Mission
To add your own mission, follow these steps in `main.py`:

1. **Define the function**:
   ```python
   async def my_new_mission():
       await DRIVEBASE.straight(500)
       await DRIVEBASE.turn(90)
       print("Mission Complete!")
   ```

2. **Add it to the menu**:
   Scroll down to the `main()` function and add:
   ```python
   PM.add_program(lambda: await my_new_mission(), "4", Color.GREEN)
   ```
   - `"4"` is the character that will show on the display.
   - `Color.GREEN` is the color the button will glow.

3. **Run it!**: Download the code and select your new program.
