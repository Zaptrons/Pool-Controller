from src.controller.motor_controller import MotorController
from src.hardware.motor import Motor


def test_controller_start():
    motor = Motor()
    controller = MotorController(motor)

    controller.start()

    assert controller.status() == {
        "running": True
    }


def test_controller_stop():
    motor = Motor()
    controller = MotorController(motor)

    controller.start()
    controller.stop()

    assert controller.status() == {
        "running": False
    }


def test_controller_initial_status():
    motor = Motor()
    controller = MotorController(motor)

    assert controller.status() == {
        "running": False
    }