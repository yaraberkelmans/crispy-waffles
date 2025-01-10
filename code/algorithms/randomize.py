import random
import copy

def random_assignment(timetable):
    new_classes_list = copy.deepcopy(timetable.classes_list)
    new_timetable = copy.deepcopy(timetable.timetable)
    classes_added = 0
    
    while classes_added < len(new_classes_list):
        random_timeslot = random.choice(list(new_timetable.keys()))
        random_classroom = random.choice(list(new_timetable[random_timeslot]))
        random_class = random.choice(new_classes_list)

        if new_timetable[random_timeslot][random_classroom] == None:
            new_timetable[random_timeslot][random_classroom] = random_class
            classes_added += 1
    
    return new_timetable
        