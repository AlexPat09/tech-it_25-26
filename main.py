from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
import fun

async def run0():
    accel_on()
    mod_angle = 150
    await RMODULAR.run_angle(800,mod_angle)
    await DRIVEBASE.straight(distance=615)
    await DRIVEBASE.turn(-115)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.turn(-20)
    await DRIVEBASE.straight(distance=-70)
    await RMODULAR.run_angle(800,-mod_angle)
    await DRIVEBASE.straight(distance=70)
    await DRIVEBASE.turn(5)
    await DRIVEBASE.turn(-5)
    await wait(70)
    await RMODULAR.run_angle(800,mod_angle)
    await DRIVEBASE.turn(-55)
    await DRIVEBASE.straight(distance=150)
    await RMODULAR.run_angle(800,-mod_angle)
    await RMODULAR.run_angle(800,mod_angle)
    await DRIVEBASE.straight(distance=-270)
    await DRIVEBASE.turn(100)
    await DRIVEBASE.straight(distance=140)
    await RMODULAR.run_angle(800,-mod_angle)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(distance=-70)
    await DRIVEBASE.turn(-45)
    accel_off()
    await DRIVEBASE.straight(distance=200)
    await DRIVEBASE.straight(distance=-200)
    SPEED = 1000
    await DRIVEBASE.straight(distance=250)
    await DRIVEBASE.straight(distance=-220)
    await DRIVEBASE.straight(distance=250)
    SPEED = 800
    await DRIVEBASE.arc(-300,angle=-45)
    await DRIVEBASE.straight(distance=-600)
    await RMODULAR.run_angle(800,mod_angle)
    DRIVEBASE.stop()

async def run1():
    mod_angle = 360
    accel_on()
    await DRIVEBASE.straight(distance=825)
    await DRIVEBASE.arc(100,angle=90)

    await DRIVEBASE.straight(distance=-100)
    await LMODULAR.run_angle(150,-mod_angle)

    await DRIVEBASE.straight(distance=115)
    await LMODULAR.run_angle(100,mod_angle-270)
    await DRIVEBASE.straight(-100)

    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(800)
    DRIVEBASE.stop()

async def run2():
    pass

async def main():
    PM.add_program(lambda: await motor_control_interface(speed=200),"#",Color.WHITE)
    PM.add_program(lambda: await run0(),"1",Color.RED)
    PM.add_program(lambda: await run1(),"2",Color.ORANGE)
    PM.add_program(lambda: await run2(),"3",Color.YELLOW)
    
    await PM.run()

PM = ProgramManager()

run_task(main())
#run_task(run0())