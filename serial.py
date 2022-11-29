class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create serial starting point"""
        self.start = self.current_value = start

    def __repr__(self):
        return f"<SerialGenerator start={self.current_value}"

    def generate(self):
        """Adds 1 to the serial value and returns that value"""
        self.current_value += 1
        return self.current_value - 1

    def reset(self):
        """Resets counter to start value"""
        self.current_value = self.start