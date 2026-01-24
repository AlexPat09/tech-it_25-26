from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
import fun


async def ship():
    # main
    await DRIVEBASE.straight(650)
    await wait(100)
    await LMODULAR.run_angle(1000,-360)
    await DRIVEBASE.turn(5)
    await wait(500)
    ###

    # leave
    DRIVEBASE.settings(straight_acceleration=1000,turn_acceleration=1000)
    await DRIVEBASE.straight(-650)
    await LMODULAR.run_angle(1000,360)
    ###


async def rightside():
    # gear launcher
    await DRIVEBASE.straight(500)
    for _ in range(3):
        await RMODULAR.run_angle(800,180)
        await wait(200)
        await RMODULAR.run_angle(200,-70)
        await wait(100)
        await RMODULAR.run_angle(200,-100)
        await wait(100)
    ###

    await DRIVEBASE.straight(270)

    # balls
    await DRIVEBASE.turn(35)
    await DRIVEBASE.turn(-35)
    await DRIVEBASE.straight(-40)
    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(250)
    ###

    await DRIVEBASE.straight(-400)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(-100)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(-350)
    
    # pull down the bucket
    await RMODULAR.run_angle(1000,120)
    await wait(200)
    await RMODULAR.run_angle(200,-50)
    await wait(100)
    await RMODULAR.run_angle(200,-50)
    await wait(100)
    ###

    await DRIVEBASE.straight(-90)
    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(-300)

    # gear thingy
    await DRIVEBASE.straight(820)
    await wait(200)
    await DRIVEBASE.turn(-5)
    await LMODULAR.run_angle(1000, -8*360)
    ###
    
    # leave
    DRIVEBASE.settings(straight_acceleration=1000,turn_acceleration=1000)
    await DRIVEBASE.arc(-100,-110)
    await DRIVEBASE.straight(-650)
    ###


async def leftside():
    # WORK IN PROGRESS
    await DRIVEBASE.straight(500)
    await DRIVEBASE.turn(25)
    await DRIVEBASE.straight(170)
    await DRIVEBASE.turn(-75)
    await DRIVEBASE.straight(100)
    await RMODULAR.run_angle(700,-360)
    await DRIVEBASE.straight(200)
    LMODULAR.run_angle(900,2500)
    await RMODULAR.run_angle(500,360)
    await DRIVEBASE.straight(-270)
    DRIVEBASE.settings(turn_rate=500,turn_acceleration=250)
    await DRIVEBASE.turn(-60)
    await DRIVEBASE.turn(140)
    await DRIVEBASE.straight(-800)


async def main():
    #startup sound
    #await HUB.speaker.play_notes(fun.old_spice_jingle(),140)

    PM.add_program(lambda: await MCM.run(),"#",Color.WHITE)
    PM.add_program(lambda: await rightside(),"1",Color.BLACK)
    PM.add_program(lambda: await ship(),"2",Color.BLUE)
    PM.add_program(lambda: await leftside(),"3",Color.BROWN)
    await PM.run()

PM = ProgramManager()
MCM = MotorControlManager(speed=1000)
run_task(main())