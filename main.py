from code.classes.timetable import Timetable
from code.classes.Timeslot import Timeslot
from code.algorithms.randomize import random_course_assignment
from code.algorithms.randomize import random_student_course_assignment
from code.algorithms.randomize import random_student_class_assignment
from code.algorithms.randomize import randomize


if __name__ == "__main__":
    # initialize timetable
    timetable = Timetable()
    timetable.load_courses('data/vakken.csv')
    timetable.load_students('data/studenten_en_vakken.csv')
    timetable.load_locations('data/zalen.csv')
    timetable.get_classes_count()
    timetable.name_classes()
    timetable.create_timetable()
    timetable.initialize_locations()

    # random assignment
    randomized_timetable = random_course_assignment(timetable)
    #print(randomized_timetable)

    randomized_student_test = random_student_course_assignment(timetable)
    #print(len(randomized_student_test.classes_list))
    for course in randomized_student_test.courses:
        student_count = 0
        #print(course.course_name)
        for student in course.student_list:
            student_count += 1
            #print(student.student_id)
        #print(student_count)

    randomized_classes_test = random_student_class_assignment(timetable)
    #for course in randomized_classes_test.courses:
       # for activity in course.classes:
            #print(f'The class {cls.name} has the following students:')
            #for student in cls.student_list:
                #print(student.name)

    full_randomized_timetable = randomize(timetable)
    data = {}
    print(full_randomized_timetable.timetable)
    for timeslot in full_randomized_timetable.timetable.keys():
        # print('t:',full_randomized_timetable.timetable[timeslot])
        # print('loop:',full_randomized_timetable.timetable[timeslot].keys())
        # for location, activity in full_randomized_timetable.timetable[timeslot].items():
        #     if activity:
        #         print()
        #         print("---------- ACTIVITY INFORMATION------------")
        #         print()
        #         print(f'Course: {activity.course_name} Activity: {activity.name} Location: {location} Day: {timeslot.day} Time: {timeslot.time}')
        #         print()
        #         print("----------- STUDENTS ----------")
        #         print()
        #         for student in activity.student_list:
        #             print(student.name)

        # for csv output format
        for location, activity in full_randomized_timetable.timetable[timeslot].items():
            if activity:
                data[(timeslot.name, location.name)] = f'Course: {activity.course_name} Activity: {activity.name} Location: {location}
                # print()
                # print("---------- ACTIVITY INFORMATION------------")
                # print()
                # print(f'Course: {activity.course_name} Activity: {activity.name} Location: {location} Day: {timeslot.day} Time: {timeslot.time}')
                # print()
                # print("----------- STUDENTS ----------")
                # print()
                # for student in activity.student_list:
                #     print(student.name)
    
                for student in activity.student_list:
                    print()
                    print("---------- STUDENT ------------")
                    print()
                    print(f'Student: {student}; Course: {activity.course_name}; Activity: {activity.name}; Location: {location}; Day: {timeslot.day}; Time: {timeslot.time}')
                    print()
                    
        #
    print(data)