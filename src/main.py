from src.hardware.motor import Motor
from src.controller.motor_controller import MotorController


def main():
    motor = Motor()
    controller = MotorController(motor)

    print("Initial status:", controller.status())

    controller.start()
    print("After start:", controller.status())

    controller.stop()
    print("After stop:", controller.status())


if __name__ == "__main__":
    main()