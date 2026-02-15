# TECH-IT Pybricks Robot Control

Welcome to the Tech-IT 25-26 repository! This project uses [Pybricks](https://pybricks.com/) to control a LEGO SPIKE Prime robot in order to achieve maximum accuracy and efficiency in the FLL robotics competition.

## Project Overview
This repository contains the Python code needed to run the TECH-IT robot. It features:
- A Customizable **Menu System** (`ProgramManager`) to select and run different missions.
- **Asyncio** support for multitasking (running motors, lights, and buttons simultaneously).
- **Modular Design** separating hardware configuration, GUI logic, and mission code, allowing for easy modification.
- Miscellaneous **Secondary Features** (`fun.py`) for quality of life.

## Getting Started

### Prerequisites
1. **LEGO SPIKE Prime Hub**: You need the physical robot.
2. **Pybricks Firmware**: Your SPIKE Prime Hub must be flashed with Pybricks.
   - Go to [code.pybricks.com](https://code.pybricks.com/).
   - Follow the instructions to install Pybricks on your Hub.

### Installation
1. Download this repository to your computer.
2. Open [code.pybricks.com](https://code.pybricks.com/) in your browser (Chrome/Edge).
3. Connect your Hub via Bluetooth or USB.
4. Import the files from this repository into the Pybricks code editor.

### API Reference
This project uses the `pybricks` library. You can find the official documentation here: [docs.pybricks.com](https://docs.pybricks.com/).

## File Structure
- **`main.py`**: The entry point of the program. It defines the missions and starts the menu.
- **`hardware_config.py`**: Defines motors, sensors, and constants (ports, speeds).
- **`guis.py`**: Contains the code for the menu system and motor control interface.
- **`fun.py`**: Contains music and fun extras like light patterns.

## Documentation
For more detailed information, check out these guides:
- [**Hardware Setup**](./HARDWARE.md) - How to wire your robot.
- [**User Guide**](./USER_GUIDE.md) - How to operate the robot and use the menu.
- [**Code Explained**](./CODE_EXPLAINED.md) - A beginner's guide to understanding the code.

