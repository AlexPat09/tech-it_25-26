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

    set_motor_settings_to_high()
    await wait(100)
    await DRIVEBASE.straight(-400)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(-100)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(-350)

    # pull down the bucket
    await RMODULAR.run_angle(1000,120)
    await wait(200)
    RMODULAR.run_angle(50,-145)
    ###

    await DRIVEBASE.straight(-90)
    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(-300)

    # gear thingy
    await DRIVEBASE.straight(800)
    await DRIVEBASE.turn(-10)
    await DRIVEBASE.straight(10)
    await LMODULAR.run_angle(1000, -5*360)
    ###

    # leave
    DRIVEBASE.settings(straight_acceleration=1000,turn_acceleration=1000)
    await DRIVEBASE.arc(-100,-120)
    await DRIVEBASE.straight(-650)
    ###

async def rightside_1():
    set_motor_settings_to_high()
    # lift big table
    await DRIVEBASE.straight(340)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(240)
    await LMODULAR.run_angle(300,140)
    await wait(300)
    await DRIVEBASE.straight(-140)
    ###

    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(-100)

    # lift the small table
    await LMODULAR.run_angle(720,-20)
    await wait(500)
    await DRIVEBASE.turn(-63)
    ###

    # pull and deliver tray
    await LMODULAR.run_angle(720,40)
    await DRIVEBASE.straight(210)
    await LMODULAR.run_angle(300,40)
    await DRIVEBASE.straight(-40)
    await DRIVEBASE.turn(-120)
    await LMODULAR.run_angle(700,-160)
    ###

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
    await DRIVEBASE.turn(-42)
    await DRIVEBASE.straight(-150)
    await LMODULAR.run_angle(300,90)
    await DRIVEBASE.straight(90)
    await DRIVEBASE.turn(-28)
    await DRIVEBASE.turn(15)
    LMODULAR.run_angle(300,-120)
    await DRIVEBASE.straight(-450)
    await DRIVEBASE.turn(-85)
    await DRIVEBASE.straight(-100)
    stop_all_motors()
    await wait_until_force_pressed()
    reset_imu()
    await DRIVEBASE.straight(1800)
    ###

async def leftside():
    set_motor_settings_to_high()
    await DRIVEBASE.straight(500)
    await DRIVEBASE.turn(25)
    await DRIVEBASE.straight(200)
    await DRIVEBASE.turn(-70)
    await RMODULAR.run_angle(1000,-360)
    await DRIVEBASE.straight(80)
    await DRIVEBASE.turn(-10)
    DRIVEBASE.use_gyro(False)
    await DRIVEBASE.straight(170)
    await RMODULAR.run_angle(500,360)
    DRIVEBASE.use_gyro(True)
    await DRIVEBASE.straight(-200)
    await LMODULAR.run_angle(200,-130)
    set_motor_settings_to_normal()
    await DRIVEBASE.turn(-65)
    await DRIVEBASE.straight(-10)
    await DRIVEBASE.turn(55)
    set_motor_settings_to_high()
    await LMODULAR.run_angle(200,150)
    await DRIVEBASE.turn(-35)
    await DRIVEBASE.straight(120)
    DRIVEBASE.use_gyro(False)
    await DRIVEBASE.straight(-20)
    DRIVEBASE.use_gyro(True)
    await LMODULAR.run_angle(1000,-220)
    await wait(200)
    await LMODULAR.run_angle(200,200)
    await DRIVEBASE.straight(-100)
    await DRIVEBASE.turn(-75)
    await DRIVEBASE.straight(500)

async def ship():
    # main
    #DRIVEBASE.settings(straight_acceleration=500,turn_acceleration=200)
    set_motor_settings_to_high()
    await DRIVEBASE.straight(650)
    await wait(100)
    await LMODULAR.run_angle(1000,360)
    await wait(400)
    ###

    # leave
    DRIVEBASE.settings(straight_acceleration=1000)
    LMODULAR.run_angle(45,90)
    await DRIVEBASE.straight(-120)
    await DRIVEBASE.turn(15)
    await DRIVEBASE.straight(-430)
    ###

async def dropoff():
    set_motor_settings_to_normal()
    await DRIVEBASE.straight(230)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(250)
    await DRIVEBASE.turn(-10)
    await RMODULAR.run_angle(500,-180)
    await DRIVEBASE.turn(10)
    await DRIVEBASE.straight(-10)
    await RMODULAR.run_angle(135,180)
    await DRIVEBASE.straight(-50)
    await LMODULAR.run_angle(720,-900)
    await DRIVEBASE.straight(-150)
    LMODULAR.run_angle(1000,1000)
    await DRIVEBASE.turn(-5)
    await DRIVEBASE.straight(130)

async def main():
    #startup sound
    #await HUB.speaker.play_notes(fun.windows_xp_startup())
    #await HUB.speaker.play_notes(fun.old_spice_jingle(),70*urandom.uniform(2,3))

    PM.add_program(lambda: await MCM.run(),"#",Color.WHITE)
    PM.add_program(lambda: await rightside_0(),"0",Color.RED)
    PM.add_program(lambda: await rightside_1(),"1",Color.ORANGE)
    PM.add_program(lambda: await leftside(),"L",Color.YELLOW)
    PM.add_program(lambda: await ship(),"S",Color.GREEN)
    PM.add_program(lambda: await dropoff(),"Z",Color.BLUE)
    await PM.run()

PM = ProgramManager()
MCM = MotorControlManager(speed=1000)
run_task(main())