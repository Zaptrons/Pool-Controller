from src.hardware.motor import Motor


class MotorController:
    """Controls the motor and exposes its current state."""

    def __init__(self, motor: Motor):
        self._motor = motor

    def start(self):
        self._motor.turn_on()

    def stop(self):
        self._motor.turn_off()

    def status(self):
        return {
            "running": self._motor.is_running()
        }