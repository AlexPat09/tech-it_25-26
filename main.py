from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
import fun
import urandom

async def rightside_0():
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
    await wait_until_force_pressed()
    await RMODULAR.run_angle(500,135)
    ###

async def rightside_1():
    # table
    await DRIVEBASE.straight(340)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(240)
    await LMODULAR.run_angle(300,140)
    #await DRIVEBASE.turn(-5)
    await wait(300)
    await DRIVEBASE.straight(-140)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(-100)
    await LMODULAR.run_angle(720,-20)
    await wait(500)
    await DRIVEBASE.turn(-63)
    await LMODULAR.run_angle(720,40)
    await DRIVEBASE.straight(210)
    await LMODULAR.run_angle(300,40)
    await DRIVEBASE.straight(-40)
    await DRIVEBASE.turn(-120)
    await LMODULAR.run_angle(700,-160)
    await DRIVEBASE.turn(-149)
    await DRIVEBASE.straight(300)
    await DRIVEBASE.turn(-10)
    await DRIVEBASE.straight(120)
    await RMODULAR.run_angle(640,320)
    await wait(500)
    await DRIVEBASE.turn(35)
    RMODULAR.run_angle(640,-320)
    await DRIVEBASE.turn(-5)
    #await DRIVEBASE.straight(-20)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(-150)
    await LMODULAR.run_angle(300,120)
    await DRIVEBASE.straight(80)
    await DRIVEBASE.turn(-28)
    await DRIVEBASE.turn(15)
    LMODULAR.run_angle(300,-150)
    await DRIVEBASE.straight(-550)
    await DRIVEBASE.turn(-90)
    await wait_until_force_pressed()
    await DRIVEBASE.straight(1500)
    ###

async def leftside():
    # WORK IN PROGRESS
    await DRIVEBASE.straight(500)
    await DRIVEBASE.turn(25)
    await DRIVEBASE.straight(200)
    await DRIVEBASE.turn(-75)
    await DRIVEBASE.straight(100)
    await RMODULAR.run_angle(700,-360)
    await DRIVEBASE.straight(200)
    await RMODULAR.run_angle(500,360)
    await DRIVEBASE.straight(-160)
    await LMODULAR.run_angle(200,-130)
    await DRIVEBASE.turn(-65)
    await DRIVEBASE.turn(35)
    await LMODULAR.run_angle(200,130)
    await DRIVEBASE.turn(-15)
    await DRIVEBASE.straight(30)
    await LMODULAR.run_angle(1000,-200)
    await DRIVEBASE.turn(-5)
    await wait(200)
    await LMODULAR.run_angle(200,200)
    await DRIVEBASE.straight(-100)
    await DRIVEBASE.turn(-60)
    await DRIVEBASE.straight(500)

async def ship():
    # main
    DRIVEBASE.settings(straight_acceleration=500,turn_acceleration=200)
    await DRIVEBASE.straight(650)
    await wait(100)
    await LMODULAR.run_angle(1000,-720)
    await DRIVEBASE.turn(5)
    await wait(500)
    ###

    # leave
    DRIVEBASE.settings(straight_acceleration=1000)
    await DRIVEBASE.straight(-650)
    await LMODULAR.run_angle(1000,360)
    ###

async def main():
    #startup sound
    #await HUB.speaker.play_notes(fun.old_spice_jingle(),70*urandom.uniform(1,3))

    print(HUB.battery.voltage())
    PM.add_program(lambda: await MCM.run(),"#",Color.WHITE)
    PM.add_program(lambda: await rightside_0(),"0",Color.RED)
    PM.add_program(lambda: await rightside_1(),"1",Color.ORANGE)
    PM.add_program(lambda: await transfer_via_sealion(),"2",Color.YELLOW)
    PM.add_program(lambda: await ship(),"3",Color.GREEN)
    PM.add_program(lambda: await leftside(),"4",Color.BLUE)
    await PM.run()

PM = ProgramManager()
MCM = MotorControlManager(speed=1000)
run_task(main())