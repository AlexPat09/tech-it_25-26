from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch, run_task, multitask
from hardware_config import *
from fun import rainbow

class UI:
    """Abstract parent class for specialized UI classes such as ProgramManager and MotorControlManager."""
    async def left_action(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    async def right_action(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    async def center_action(self):
        raise NotImplementedError("Subclasses must implement this method.")

    async def extra_action(self):
        raise NotImplementedError("Subclasses must implement this method.")

    async def idle_action(self):
        raise NotImplementedError("Subclasses must implement this method.")

    async def run(self):
        while True:
            if HUB.imu.ready():
                if Button.LEFT in HUB.buttons.pressed():
                    await self.left_action()
                elif Button.RIGHT in HUB.buttons.pressed():
                    await self.right_action()
                elif Button.CENTER in HUB.buttons.pressed():
                    await self.center_action()
                elif await FSENSOR.pressed(2):
                    await self.extra_action()
                else:
                    await self.idle_action()
            else:
                HUB.light.on(Color.RED)
                HUB.display.char('E')
                await wait(50)
                HUB.light.off()
                await wait(50)

class Program:
    """Class that stores a singular program upon initializattion that can be displayed by a UI class (ProgramManager)."""
    def __init__(self, func:callable, character:chr, light_color:Color):
        self.label:chr = character
        self.color:Color = light_color
        self.function:callable = func

class ProgramManager(UI):
    """UI class """
    def __init__(self):
        self.ACTIVE_PROGRAM = 0
        self.PROGRAM_LIST = []
    
    def __verify_list_not_empty(self):
        if self.PROGRAM_LIST == []:
            raise Exception("No programs available to run.")

    def next_program(self):
        self.__verify_list_not_empty()
        self.ACTIVE_PROGRAM = (self.ACTIVE_PROGRAM + 1) % len(self.PROGRAM_LIST)

    def prior_program(self):
        self.__verify_list_not_empty()
        self.ACTIVE_PROGRAM = (self.ACTIVE_PROGRAM - 1) % len(self.PROGRAM_LIST)
    
    def go_to_program(self,program_num:int):
        self.__verify_list_not_empty()
        self.ACTIVE_PROGRAM = program_num % len(self.PROGRAM_LIST)

    def add_program(self, func:callable, char:chr = "E", color:Color = Color.BLUE):
        self.PROGRAM_LIST.append(Program(func, char, color))

    def update_display(self):
        self.__verify_list_not_empty()
        self.current_program = self.PROGRAM_LIST[self.ACTIVE_PROGRAM]
        HUB.display.char(self.current_program.label)
        HUB.light.on(self.current_program.color)
    
    async def check_if_quit_button_pressed(self):
        while True:
            if Button.BLUETOOTH in HUB.buttons.pressed():
                return
            await wait(0)
    
    async def exec_current_program(self):
        self.__verify_list_not_empty()
        try:
            HUB.display.off()
            HUB.light.off()
            HUB.system.set_stop_button(None)
            reset_imu()
            await multitask(self.current_program.function(),rainbow(99999),self.check_if_quit_button_pressed(), race=True)
            stop_all_motors()
            set_motor_settings_to_normal()
            await wait(400)
            HUB.system.set_stop_button(Button.BLUETOOTH)
        except Exception as e:
            print(f"Error executing program: {e}")
            HUB.display.char('E')
            for i in range(5):
                HUB.light.on(Color.RED)
                await wait(100)
                HUB.light.off()
                await wait(100)

    async def left_action(self):
        self.prior_program()
        self.update_display()
        await wait(200)
        await HUB.speaker.beep(523.25, 200)
    async def right_action(self):
        self.next_program()
        self.update_display()
        await wait(200)
        await HUB.speaker.beep(523.25, 200)
    async def center_action(self):
        #await HUB.speaker.beep(1046.5, 200)
        await self.exec_current_program()
    async def extra_action(self):
        pass
    async def idle_action(self):
        self.update_display()
        stop_all_motors()


class MotorControlManager(UI):
    """UI class"""
    def __init__(self, motors:list = [LMODULAR, RMODULAR], reset_angle_to:int=0, speed=400):
        self.motors = motors
        self.selected_motor = motors[0]
        self.reset_angle_to = reset_angle_to
        self.speed = speed

    async def left_action(self):
        self.selected_motor.run(-self.speed)
        await wait(0)
    async def right_action(self):
        self.selected_motor.run(self.speed)
        await wait(0)
    async def center_action(self):
        self.selected_motor.hold()
        self.selected_motor = self.motors[(self.motors.index(self.selected_motor) + 1) % len(self.motors)]

        await wait(200)
    async def extra_action(self):
        self.selected_motor.hold()
        await self.selected_motor.run_target(self.speed,self.reset_angle_to)
        await wait(200)
    async def idle_action(self):
        self.selected_motor.hold()
        if self.selected_motor == LMODULAR:
            HUB.display.char("L")
        elif self.selected_motor == RMODULAR:
            HUB.display.char("R")
        await wait(0)


async def motor_control_interface(motors:list = [LMODULAR, RMODULAR], reset_angle_to:int=0, speed=400):
    """Deprecated. See MotorControlManager."""
    selected_motor = motors[0]
    while True:
        if Button.LEFT in HUB.buttons.pressed():
            selected_motor.run(-speed)
        elif Button.RIGHT in HUB.buttons.pressed():
            selected_motor.run(speed)
        elif Button.CENTER in HUB.buttons.pressed():
            selected_motor.hold()
            selected_motor = motors[(motors.index(selected_motor) + 1) % len(motors)]
            await wait(200)
        elif await FSENSOR.pressed(2):
            selected_motor.hold()
            await selected_motor.run_target(speed,reset_angle_to)
            await wait(200)
        elif Button.BLUETOOTH in HUB.buttons.pressed():
            stop_all_motors()
            return
        else:
            selected_motor.hold()
            await wait(0)