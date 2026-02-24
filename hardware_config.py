from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

### VARIABLES ###
DEFAULT_SPEED = 864 #will throw an error if higher
DEFAULT_TURN_SPEED = 990 #will throw an error if higher

NORMAL_ACCELERATION = 500
NORMAL_TURN_ACCELERATION = 400

HIGH_ACCELERATION = 700
HIGH_TURN_ACCELERATION = 600

### HARDWARE SETUP ###
HUB = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
HUB.system.set_stop_button(Button.BLUETOOTH)
HUB.speaker.volume(0)

FSENSOR = ForceSensor(Port.C)

LDRIVE = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, profile=5)
RDRIVE = Motor(Port.F, positive_direction=Direction.CLOCKWISE, profile=5)

DRIVEBASE = DriveBase(LDRIVE,RDRIVE,49.5,100)
DRIVEBASE.use_gyro(True)
DRIVEBASE.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=NORMAL_ACCELERATION,
    turn_rate=DEFAULT_TURN_SPEED, turn_acceleration=NORMAL_TURN_ACCELERATION)

LMODULAR = Motor(Port.A, positive_direction=Direction.CLOCKWISE, profile=5)
RMODULAR = Motor(Port.E, positive_direction=Direction.CLOCKWISE, profile=5)

print(HUB.battery.voltage())

async def reset_imu():
    HUB.imu.reset_heading(0)
    DRIVEBASE.reset(0,0)
    await wait(400)

def stop_all_motors():
    DRIVEBASE.stop()
    LDRIVE.stop()
    RDRIVE.stop()
    LMODULAR.stop()
    RMODULAR.stop()

def set_motor_settings_to_normal():    
    DRIVEBASE.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=NORMAL_ACCELERATION,
    turn_rate=DEFAULT_TURN_SPEED, turn_acceleration=NORMAL_TURN_ACCELERATION)

def set_motor_settings_to_high():
    #DRIVEBASE.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=1000, turn_rate=DEFAULT_TURN_SPEED, turn_acceleration=1000)
    DRIVEBASE.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=HIGH_ACCELERATION,
    turn_rate=DEFAULT_TURN_SPEED, turn_acceleration=HIGH_TURN_ACCELERATION)

async def wait_until_force_pressed():
    while not await FSENSOR.pressed(force=2):
        await wait(0)