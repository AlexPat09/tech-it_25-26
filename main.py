from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
import fun

async def original_rightside():
    smooth_accel_on()
    await DRIVEBASE.straight(700)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.straight(40)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(200)
    await DRIVEBASE.straight(-350)
    await DRIVEBASE.turn(30)
    await DRIVEBASE.straight(-300)
    await DRIVEBASE.turn(15)
    await DRIVEBASE.straight(200)
    await DRIVEBASE.arc(220,-135)
    await DRIVEBASE.turn(-182)
    await DRIVEBASE.straight(360)
    await DRIVEBASE.turn(-5)

    await LMODULAR.run_angle(1000, -7*360)
    DRIVEBASE.stop()

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
    smooth_accel_on()

    # gear launcher
    await DRIVEBASE.straight(500)
    for _ in range(3):
        smooth_accel_off()
        await RMODULAR.run_angle(800,180)
        smooth_accel_on()
        await wait(500)
        await RMODULAR.run_angle(200,-170)

    # balls
    await DRIVEBASE.straight(290)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.turn(-45)
    await DRIVEBASE.straight(-50)
    await DRIVEBASE.turn(90)
    await DRIVEBASE.straight(250)
    await DRIVEBASE.straight(-400)

    # push table
    await DRIVEBASE.turn(30)
    await DRIVEBASE.straight(-300)
    await DRIVEBASE.turn(15)
    await DRIVEBASE.straight(270)
    await DRIVEBASE.arc(220,-45)
    await DRIVEBASE.straight(-150)
    
    # pull down the bucket
    smooth_accel_off()
    await RMODULAR.run_angle(1000,120)
    await wait(500)
    await RMODULAR.run_angle(1000,-120)
    smooth_accel_on()
    await DRIVEBASE.arc(90,-90)

    # gear thingy
    await DRIVEBASE.turn(-182)
    await DRIVEBASE.straight(480)
    await DRIVEBASE.turn(-5 )

    await LMODULAR.run_angle(1000, -8*360)

    DRIVEBASE.stop()



async def main():
    await HUB.speaker.play_notes(old_spice_jingle(),140)
    PM.add_program(lambda: await motor_control_interface(speed=1000),"#",Color.WHITE)
    #PM.add_program(lambda: await run0(),"1",Color.RED)
    #PM.add_program(lambda: await run1(),"2",Color.ORANGE)
    PM.add_program(lambda: await rightside(),"3",Color.YELLOW)
    PM.add_program(lambda: await ship(),"4",Color.GREEN)
    
    await PM.run()

PM = ProgramManager()

run_task(main())
#run_task(run0())