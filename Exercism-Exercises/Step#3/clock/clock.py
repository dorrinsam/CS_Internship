from datetime import time


class Clock:

    def __init__(self, hour, minute):
        self.time = time(hour=(hour + minute // 60) % 24, minute=minute % 60)

    def __repr__(self):
        return f'Clock({self.time.hour}, {self.time.minute})'

    def __str__(self):
        return f'{self.time:%H:%M}'

    def __eq__(self, other):
        return self.time == other

    def __add__(self, minutes):
        return Clock(self.time.hour, self.time.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.time.hour, self.time.minute - minutes)
