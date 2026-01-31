# 🎮 User Guide

This guide explains how to use the menu system to run your robot's missions.

## The Menu System
When you start the program, you will see a character on the Hub's display and the Hub status light will change color. This indicates which program is currently selected.

### Controls
| Button | Action |
| :--- | :--- |
| **LEFT Button** (`<`) | **Previous Program**: Scroll to the previous mission in the list. |
| **RIGHT Button** (`>`) | **Next Program**: Scroll to the next mission in the list. |
| **CENTER Button** (`O`) | **Run Program**: Start the selected mission. |
| **BLUETOOTH Button** | **Stop/Exit**: Press this during a mission to emergency stop and return to the menu. |

## Available Programs
The programs are configured in `main.py`. Here is the default list:

| Display Char | Light Color | Program Name | Description |
| :---: | :---: | :--- | :--- |
| **#** | **WHITE** | **Motor Control** | Manual control mode for testing motors. |
| **1** | **BLACK** (Off) | **Right Side** | Mission sequence for the right side of the field. |
| **2** | **BLUE** | **Ship** | Mission sequence for the "Ship" task. |
| **3** | **BROWN** (Orange) | **Left Side** | Mission sequence for the left side of the field. |

## Running a Mission
1. Use the **Left** or **Right** buttons to find the program you want (look at the display character).
2. Press the **Center** button to start.
   - The robot will execute the steps defined in the code.
   - You can stop it manually by pressing the **Bluetooth** button.
3. When the mission finishes, the robot will return to the menu automatically.

## Motor Control Mode (`#`)
If you select the program with the **#** symbol, you enter **Motor Control Mode**. This is useful for resetting attachments without running a full mission.

- **Left/Right Buttons**: Spin the selected motor.
- **Center Button**: Switch between the Left Attachment (`LMODULAR`) and Right Attachment (`RMODULAR`) motor.
- **Force Sensor**: Pressing the force sensor will reset the selected motor to angle 0 (useful for calibration).
