# Hardware Configuration

This guide describes how to configure and wire your LEGO SPIKE Prime robot to work with this code.

## Hub Orientation
The code assumes the Hub is mounted in a specific orientation for the Gyro sensor to work correctly (for turning and straight driving).

- **Top Side**: The side with the matrix display is facing **UP** (Axis Z).
- **Front Side**: The side with the USB port is facing **LEFT** (Axis Y).

## Wiring Guide
Connect your motors and sensors to the following ports on the SPIKE Prime Hub.

### Motors
| Motor Name | Port | Description | Direction |
| :--- | :---: | :--- | :--- |
| **Left Drive** (`LDRIVE`) | **B** | Main Left Wheel | Counter-Clockwise (Positive) |
| **Right Drive** (`RDRIVE`) | **F** | Main Right Wheel | Clockwise (Positive) |
| **Left Attachment** (`LMODULAR`) | **A** | Auxiliary Motor (e.g., Arm/Lifter) | Clockwise (Positive) |
| **Right Attachment** (`RMODULAR`) | **E** | Auxiliary Motor (e.g., Claw/Spinner) | Clockwise (Positive) |

### Sensors
| Sensor Name | Port | Description |
| :--- | :---: | :--- |
| **Force Sensor** (`FSENSOR`) | **C** | Used as a touch button for extra actions |

*Note: Port D is currently unused in the config.*

## Robot Constants
These values are defined in `hardware_config.py` and tune the robot's movement.

- **Wheel Diameter**: 49.5 mm
- **Axle Track**: 100 mm (Distance between the two drive wheels)
- **Drive Speed**: 864 deg/s (Max)
- **Turn Speed**: 990 deg/s (Max)

If you change your wheels or the width of your robot, you must update `hardware_config.py`.

```python
# From hardware_config.py
DRIVEBASE = DriveBase(LDRIVE, RDRIVE, wheel_diameter=49.5, axle_track=100)
```

