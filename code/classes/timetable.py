from loading_data import Load_init_lists

class Timetable():
    def __init__(self, days, times):
        for day in days:
            for time in times:
                self.timetable[Timeslot(day, time)] = {}