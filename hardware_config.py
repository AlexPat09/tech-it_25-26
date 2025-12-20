from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

### VARIABLES ###
SPEED = 800
ACCELERATION = 200
TURN_SPEED = 800
TURN_ACCELERATION = 200

### HARDWARE SETUP ###
HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
HUB.system.set_stop_button(Button.BLUETOOTH)
HUB.speaker.volume(50)
TIMER = StopWatch()
TIMER.pause()

FSENSOR = ForceSensor(Port.C)

LDRIVE = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, profile=5)
RDRIVE = Motor(Port.F, positive_direction=Direction.CLOCKWISE, profile=5)

DRIVEBASE = DriveBase(LDRIVE,RDRIVE,49.5,100)
DRIVEBASE.use_gyro(True)
DRIVEBASE.settings(SPEED, ACCELERATION, TURN_SPEED, TURN_ACCELERATION)

LMODULAR = Motor(Port.A, positive_direction=Direction.CLOCKWISE, profile=5)
RMODULAR = Motor(Port.E, positive_direction=Direction.CLOCKWISE, profile=5)

def stop_all_motors():
    DRIVEBASE.stop()
    LDRIVE.stop()
    RDRIVE.stop()
    LMODULAR.stop()
    RMODULAR.stop()

def smooth_accel_on():
    DRIVEBASE.settings(SPEED, ACCELERATION, TURN_SPEED, TURN_ACCELERATION)

def smooth_accel_off():
    DRIVEBASE.settings(SPEED, SPEED/2, TURN_SPEED, TURN_SPEED/2)

async def wait_until_force_pressed():
    while not await FSENSOR.pressed(force=2):
        await wait(0)