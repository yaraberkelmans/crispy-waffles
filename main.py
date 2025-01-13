from code.classes.timetable import Timetable
from code.classes.Timeslot import Timeslot
from code.algorithms.randomize import random_course_assignment
from code.algorithms.randomize import random_student_assignment

if __name__ == "__main__":
    # initialize timetable
    timetable = Timetable()
    timetable.load_courses('data/vakken.csv')
    timetable.load_students('data/studenten_en_vakken.csv')
    timetable.get_classes_count()
    timetable.name_classes()
    timetable.create_timetable()
    timetable.initialize_locations()

    # random assignment
    randomized_timetable = random_course_assignment(timetable)
    print(randomized_timetable)

    randomized_student_test = random_student_assignment(timetable)

    for course in randomized_student_test.courses:
        student_count = 0
        #print(course.course_name)
        for student in course.student_list:
            student_count += 1
            #print(student.student_id)
        #print(student_count)