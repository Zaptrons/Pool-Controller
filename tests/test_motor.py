from src.hardware.motor import Motor


def test_motor_starts_off():
    motor = Motor()

    assert motor.is_running() is False


def test_motor_turns_on():
    motor = Motor()

    motor.turn_on()

    assert motor.is_running() is True


def test_motor_turns_off():
    motor = Motor()

    motor.turn_on()
    motor.turn_off()

    assert motor.is_running() is False