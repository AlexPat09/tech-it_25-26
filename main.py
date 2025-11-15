from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from guis import *
import fun

async def run0():
    accel_on()
    mod_angle = 150
    await RMODULAR.run_angle(800,mod_angle)
    await DRIVEBASE.straight(distance=620)
    
    accel_off()
    SPEED = 800
    await DRIVEBASE.turn(-115)
    await wait(1000)
    await DRIVEBASE.turn(45)
    await DRIVEBASE.turn(-20)
    accel_on()

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
    LMODULAR.run_angle(250,-370)
    await DRIVEBASE.turn(100)
    await DRIVEBASE.straight(distance=140)
    await RMODULAR.run_angle(800,-mod_angle)

    await DRIVEBASE.turn(15)
    await DRIVEBASE.straight(distance=-40)
    LMODULAR.run_angle(250,-15)
    await DRIVEBASE.turn(10)
    await DRIVEBASE.straight(distance=75)
    await DRIVEBASE.straight(distance=-75)


    await DRIVEBASE.arc(-400,distance=-150)
    await DRIVEBASE.straight(distance=-800)

    #await DRIVEBASE.turn(-45)
    #accel_off()
    #SPEED = 1000
    #await DRIVEBASE.straight(distance=200)
    #await DRIVEBASE.straight(distance=-200)
    #await DRIVEBASE.straight(distance=250)
    #await DRIVEBASE.arc(-300,angle=-45)
    #await DRIVEBASE.straight(distance=-700)
    #SPEED = 800
    DRIVEBASE.stop()

async def run1():
    ##   360 MODULAR MOTOR DEGREES  =  90 ARM DEGREES
    accel_on()
    await DRIVEBASE.straight(distance=825)
    await DRIVEBASE.arc(100,angle=90)

    # Prep for entry
    await DRIVEBASE.straight(distance=-100)
    await LMODULAR.run_angle(150,-350)

    # Go halfway in and lower 
    await DRIVEBASE.straight(distance=100)

    # In n' out with the loot
    await DRIVEBASE.straight(distance=20)
    await LMODULAR.run_angle(100,50)
    await DRIVEBASE.straight(-100)
    await LMODULAR.run_angle(100,100)

    # Drop off the loot
    await DRIVEBASE.turn(55)
    await DRIVEBASE.straight(200)
    await LMODULAR.run_angle(100,-200)
    await DRIVEBASE.straight(-50)
    await DRIVEBASE.turn(-70)
    await DRIVEBASE.straight(50)
    
    DRIVEBASE.stop()

async def run2():
    pass

async def main():
    await HUB.speaker.play_notes(old_spice_jingle(),140)
    PM.add_program(lambda: await motor_control_interface(speed=1000),"#",Color.WHITE)
    PM.add_program(lambda: await run0(),"1",Color.RED)
    PM.add_program(lambda: await run1(),"2",Color.ORANGE)
    PM.add_program(lambda: await run2(),"3",Color.YELLOW)
    
    await PM.run()

PM = ProgramManager()

run_task(main())
#run_task(run0())