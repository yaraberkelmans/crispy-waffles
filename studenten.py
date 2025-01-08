class Student():
    def __init__(self, student_id, courses):
        self.student_id = student_id
        self.courses = courses


class Course():
    def __init__(self, course_name, lectures_n, tutorial_n, tutorial_cap, labs_n, labs_cap, e_students):
        self.course_name = course_name
        self.lectures_n = lectures_n
        self.tutorial_n = tutorial_n
        self.tutorial_cap = tutorial_cap
        self.labs_n = labs_n
        self.labs_cap = labs_cap
        self.e_students = e_students

class Location():
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity= capacity
        self.available = True


student_list = []
course_list= []
location_list = []

with open("vakken.csv") as c:
    for line in c:
        split_data = line.split(',')
        course_name = split_data[0]
        lectures_n = split_data[1]
        tutorial_n = split_data[2]
        tutorial_cap = split_data[3]
        labs_n = split_data[4]
        labs_cap = split_data[5]
        e_students = split_data[6]

        course = Course(course_name, lectures_n, tutorial_n, tutorial_cap, labs_n, labs_cap, e_students)
        course_list.append(course)

print(course_list[1].course_name)
