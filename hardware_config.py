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
HUB.speaker.volume(100)
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


def set_arm_mode(arm_mode:bool, l:Motor=LMODULAR, r:Motor=RMODULAR):
    l.close()
    r.close()
    if arm_mode:
        l = Motor(Port.A,gears=[[12,20],[12,20]])
        r = Motor(Port.E,gears=[[20,12],[40,56]])
    else:
        l = Motor(Port.A)
        r = Motor(Port.E)

def accel_on():
    DRIVEBASE.settings(SPEED, ACCELERATION, TURN_SPEED, TURN_ACCELERATION)

def accel_off():
    DRIVEBASE.settings(SPEED, SPEED/2, TURN_SPEED, TURN_SPEED/2)

async def wait_until_force_pressed():
    while not await FSENSOR.pressed(force=2):
        await wait(0)