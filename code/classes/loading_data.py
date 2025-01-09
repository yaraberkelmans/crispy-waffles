class Load_init_lists:
    def __init__(self):
        self.course_list = self.load_courses
        self.student_list = self.load_students
        self.location_list = self.load_locations
    
    def load_courses(self):
        course_list = []
        with open("vakken.csv") as c:
            next(c)
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

        return course_list
 
    def load_students(self):
        student_list = []
        with open("studenten_en_vakken.csv") as sv:
            for line in sv:
                split_data = line.split(',')
                student_id = split_data[2]
                courses = [split_data[3],split_data[4],split_data[5],split_data[6],split_data[7]]

                student = Student(student_id, courses)
                student_list.append(student)

        return student_list

    def load_locations(self):
        location_list = []
        with open("zalen.csv") as z:
            for line in z:
                split_data = line.split(',')
                room_id = split_data[0]
                capacity = split_data[1]

                location = Location(room_id, capacity)

                location_list.append(location)
                
        return location_list