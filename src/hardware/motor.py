class Motor:
    """Represents a virtual motor."""

    def __init__(self):
        self._running = False

    def turn_on(self):
        self._running = True

    def turn_off(self):
        self._running = False

    def is_running(self):
        return self._running