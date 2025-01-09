from loading_data import Load_init_lists

class Timetable():
    def __init__(self, days, times):
        """Inputs days and times are lists and for every combination, a timeslot instance is created to be used as the key for the dictionary, the value is an empty diictionary."""
        for day in days:
            for time in times:
                self.timetable[Timeslot(day, time)] = {}