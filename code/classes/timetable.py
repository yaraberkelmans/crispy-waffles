from loading_data import Load_init_lists

class Timetable():
    def __init__(self, days, times):
        """
        Inputs days and times are lists and for every combination, 
        a timeslot instance is created to be used as the key for the dictionary, 
        the value is an empty diictionary.
        """
        self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        self.times = ['9-11', '11-13', '13-15', '15-17']

    def create_timetable(self)
        for day in self.days:
            for time in self.times:
                self.timetable[Timeslot(day, time)] = {}
        
                