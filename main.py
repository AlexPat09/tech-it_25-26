from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *

PM = ProgramManager()
mod_angle = 150

async def run0():
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
    await DRIVEBASE.straight(distance=200)
    await DRIVEBASE.arc(-500,angle=-45)
    await DRIVEBASE.straight(distance=-600)
    await RMODULAR.run_angle(800,mod_angle)
    await wait_until_force_pressed()

async def run1():
    accel_on()
    await DRIVEBASE.straight(800)
    await DRIVEBASE.arc(300,angle=90)


async def run2():
    pass


async def main():
    PM.add_program(lambda: await motor_control_interface(speed=200),"#",Color.WHITE)
    PM.add_program(lambda: await run0(),"0",Color.RED)
    PM.add_program(lambda: await run1(),"1",Color.ORANGE)
    PM.add_program(lambda: await run2(),"2",Color.YELLOW)

    await PM.run()

run_task(main())
#run_task(run0())