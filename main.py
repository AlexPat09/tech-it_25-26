from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
import fun

async def ship():
    smooth_accel_off()
    SPEED = 1200
    await DRIVEBASE.straight(650)
    await wait(100)
    await RMODULAR.run_angle(1000,180)
    await wait(100)
    await DRIVEBASE.straight(-650)
    SPEED = 800
    smooth_accel_on()
    DRIVEBASE.stop()

async def rightside():
    smooth_accel_off()
    SPEED = 1000

    # gear launcher
    await DRIVEBASE.straight(500)
    SPEED = 800
    for _ in range(3):
        smooth_accel_off()
        await RMODULAR.run_angle(800,180)
        smooth_accel_on()
        await wait(500)
        await RMODULAR.run_angle(200,-170)
    smooth_accel_off()
    SPEED = 1000

    # balls
    await DRIVEBASE.straight(270)
    await DRIVEBASE.turn(35)
    await DRIVEBASE.turn(-35)
    await DRIVEBASE.straight(-40)
    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(250)
    await DRIVEBASE.straight(-400)

    # push table
    await DRIVEBASE.turn(30)
    await DRIVEBASE.straight(-340)
    await DRIVEBASE.turn(18)
    await DRIVEBASE.straight(300)
    await DRIVEBASE.turn(-3)
    await DRIVEBASE.arc(220,-45)
    await DRIVEBASE.straight(-150)
    
    # pull down the bucket
    smooth_accel_off()
    SPEED = 800
    await RMODULAR.run_angle(1000,120)
    await wait(500)
    await RMODULAR.run_angle(1000,-120)
    SPEED = 1000
    ###smooth_accel_on()
    await DRIVEBASE.arc(90,-90)
    await DRIVEBASE.turn(-185)
    
    # gear thingy
    await DRIVEBASE.straight(530)
    await DRIVEBASE.turn(-10)
    await LMODULAR.run_angle(1000, -8*360)

    SPEED = 800
    DRIVEBASE.stop()

async def mineshaft():
    smooth_accel_on()
    await DRIVEBASE.straight(950)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(-50)
    await DRIVEBASE.turn(45)
    
    DRIVEBASE.stop()


async def main():
    await HUB.speaker.play_notes(fun.old_spice_jingle(),140)
    #await HUB.speaker.play_notes(windows_xp_startup(),120)

    PM.add_program(lambda: await motor_control_interface(speed=1000),"#",Color.WHITE)
    PM.add_program(lambda: await rightside(),"1",Color.RED)
    PM.add_program(lambda: await ship(),"2",Color.ORANGE)
    PM.add_program(lambda: await mineshaft(),"3",Color.YELLOW) 
    
    await PM.run()

PM = ProgramManager()

run_task(main())
#run_task(run0())