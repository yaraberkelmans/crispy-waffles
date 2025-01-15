class Timeslot():
    def __init__(self, day, time):
        self.name = f'{day} {time}'
        self.day = day
        self.time = time

    def __repr__(self) -> str:
        return f"{self.name}"

