from code.classes.timetable import Timetable
from code.classes.Timeslot import Timeslot
from code.algorithms.randomize import random_course_assignment

if __name__ == "__main__":
    # initialize timetable
    timetable = Timetable()
    timetable.load_courses('data/vakken.csv')
    timetable.get_classes_count()
    timetable.name_classes()
    timetable.create_timetable()
    timetable.initialize_locations()

    # random assignment
    randomized_timetable = random_course_assignment(timetable)
    print(randomized_timetable)