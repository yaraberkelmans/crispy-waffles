import copy
class Greedy():
    def __init__(self, timetable):
        self.timetable = copy.copy(timetable)

    def sort_activities_by_capacity(self):
        self.timetable.activity_list.sort(key=lambda activity: activity.capacity, reverse=True)

    def sort_locations_by_capacity(self):
        self.timetable.locations.sort(key=lambda location: location.capacity, reverse=True)

    def assign_activities_to_locations(self):
        pass


