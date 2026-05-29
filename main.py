from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
from umath import floor

async def rightside_0():
    RMODULAR.run_angle(640,-320)

    # gear launcher
    await DRIVEBASE.straight(495)
    for _ in range(4):
        await RMODULAR.run_angle(1200,-360)
        await wait(60+(20*_))
    ###

    await DRIVEBASE.straight(-5)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(100)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(150)
    await DRIVEBASE.straight(30)

    # balls and ring
    DRIVEBASE.settings(turn_rate=DEFAULT_TURN_SPEED/2, turn_acceleration=NORMAL_TURN_ACCELERATION/2)
    await DRIVEBASE.turn(85)
    DRIVEBASE.settings(turn_rate=DEFAULT_TURN_SPEED, turn_acceleration=NORMAL_TURN_ACCELERATION)
    set_motor_settings_to_ULTRA()
    LMODULAR.run_angle(360,360)
    await DRIVEBASE.straight(150)
    await DRIVEBASE.turn(5)
    await DRIVEBASE.straight(150)
    await LMODULAR.run_angle(540,-360)
    ###

    await DRIVEBASE.straight(-150)
    await DRIVEBASE.arc(-220,-60)

    # table push
    await DRIVEBASE.straight(-40)
    set_motor_settings_to_ULTRA()
    await DRIVEBASE.arc(150,-35)
    await DRIVEBASE.straight(-40)
    await DRIVEBASE.turn(35)
    ###
    
    # leave
    LMODULAR.track_target(0)
    await DRIVEBASE.arc(100,20)
    await DRIVEBASE.straight(200,then=Stop.NONE)
    await DRIVEBASE.turn(180)
    await DRIVEBASE.straight(-500,then=Stop.NONE)
    ###


async def rightside_1():
    set_motor_settings_to_ULTRA()

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
    await DRIVEBASE.straight(200)
    LMODULAR.run_angle(300,40)
    await RMODULAR.run_angle(1000,400)
    await RMODULAR.run_angle(1000,-400)
    await DRIVEBASE.straight(-40,then=Stop.NONE)
    await DRIVEBASE.turn(-160)
    await DRIVEBASE.straight(160,then=Stop.NONE)
    LMODULAR.run_angle(1000,-180)
    await DRIVEBASE.straight(100)
    ###

async def transport():
    set_motor_settings_to_ULTRA()
    LMODULAR.track_target(0)
    RMODULAR.track_target(0)
    await DRIVEBASE.straight(1500,then=Stop.NONE)
    await DRIVEBASE.arc(-300,45, then=Stop.NONE)
    await DRIVEBASE.straight(100)

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
    await DRIVEBASE.straight(-30)
    await DRIVEBASE.turn(55)
    await DRIVEBASE.straight(30)
    set_motor_settings_to_ULTRA()
    await LMODULAR.run_angle(200,150)
    await DRIVEBASE.turn(-35)
    DRIVEBASE.use_gyro(False)
    await DRIVEBASE.straight(100)
    await DRIVEBASE.straight(-20)
    DRIVEBASE.use_gyro(True)
    await LMODULAR.run_angle(1000,-220)
    await wait(200)
    await LMODULAR.run_angle(200,200)
    await DRIVEBASE.straight(-80)
    await DRIVEBASE.turn(-80)
    set_motor_settings_to_ULTRA()
    await DRIVEBASE.straight(500)

async def ship():
    # main
    DRIVEBASE.settings(straight_speed=DEFAULT_SPEED, straight_acceleration=1000,
     turn_rate=200, turn_acceleration=100)
    await DRIVEBASE.straight(120)
    await DRIVEBASE.turn(90)
    await wait(1000)
    await DRIVEBASE.straight(350)
    await DRIVEBASE.turn(2)
    await DRIVEBASE.straight(150)
    await LMODULAR.run_angle(270,540)
    await DRIVEBASE.straight(-60)
    await DRIVEBASE.straight(50)
    await RMODULAR.run_angle(720,-360*5)
    ###

    # leave
    set_motor_settings_to_ULTRA()
    DRIVEBASE.use_gyro(False)
    await DRIVEBASE.straight(-50)
    await LMODULAR.run_angle(540,-540)
    await DRIVEBASE.straight(-150)
    await DRIVEBASE.turn(-5)
    await DRIVEBASE.straight(-500)
    DRIVEBASE.use_gyro(True)
    ###

async def dropoff():
    DRIVEBASE.settings(straight_acceleration=HIGH_ACCELERATION,turn_acceleration=200)

    await DRIVEBASE.straight(230)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(250)
    await DRIVEBASE.turn(-20)
    await DRIVEBASE.straight(-10)
    await RMODULAR.run_angle(500,-200)
    DRIVEBASE.use_gyro(False)
    await DRIVEBASE.turn(35)
    await RMODULAR.run_angle(1000,200)
    await DRIVEBASE.straight(-20)
    DRIVEBASE.use_gyro(True)
    await LMODULAR.run_angle(720,-750)
    set_motor_settings_to_ULTRA()
    LMODULAR.run_angle(1000,750)
    await DRIVEBASE.straight(-230)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(230)
    await DRIVEBASE.arc(200,40)
    await DRIVEBASE.straight(100)
    await RMODULAR.run_angle(500,-200)
    await DRIVEBASE.turn(-12)
    await DRIVEBASE.straight(50)
    await RMODULAR.run_angle(100,200)
    await wait(1000)
    await DRIVEBASE.straight(-70)
    await DRIVEBASE.turn(17)

async def mineshaftcart():
    await DRIVEBASE.straight(550)
    RMODULAR.run_angle(180,-45)
    LMODULAR.run_angle(180,-270)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(250)
    await DRIVEBASE.turn(12)
    LMODULAR.run_angle(810,270)
    DRIVEBASE.settings(straight_speed=100,straight_acceleration=100)
    await DRIVEBASE.arc(radius=-270,distance=100)
    await DRIVEBASE.turn(-5)
    await DRIVEBASE.straight(30)
    await RMODULAR.run_angle(1000,405)
    await RMODULAR.run_angle(405,-405)

async def main():
    # startup sound
    #await HUB.speaker.play_notes(fun.songs["windows_xp_startup"])
    #await HUB.speaker.play_notes(fun.songs["old_spice_jingle"],70*urandom.uniform(1,3))
    PM.add_program(lambda: await MCM.run(),"#",Color.WHITE)

    #PM.add_program(lambda: await multitask(rightside_0(), show_time(), race=True),"0",Color.RED)
    #PM.add_program(lambda: await multitask(rightside_1(), show_time(), race=True),"1",Color.ORANGE)
    #PM.add_program(lambda: await multitask(transport(), show_time(), race=True),"-",Color.YELLOW)
    #PM.add_program(lambda: await multitask(leftside(), show_time(), race=True),"L",Color.GREEN)
    #PM.add_program(lambda: await multitask(ship(), show_time(), race=True),"S",Color.BLUE)
    #PM.add_program(lambda: await multitask(dropoff(), show_time(), race=True),"z",Color.MAGENTA)

    PM.add_program(lambda: await rightside_0(),"0",Color.RED)
    PM.add_program(lambda: await rightside_1(),"1",Color.ORANGE)
    PM.add_program(lambda: await transport(),"-",Color.YELLOW)
    PM.add_program(lambda: await leftside(),"L",Color.GREEN)
    PM.add_program(lambda: await ship(),"S",Color.BLUE)
    PM.add_program(lambda: await dropoff(),"z",Color.MAGENTA)
    await PM.run()


PM = ProgramManager()
MCM = MotorControlManager(speed=1000)
#timer = StopWatch()
#timer.pause()
#timer.reset()
run_task(main())