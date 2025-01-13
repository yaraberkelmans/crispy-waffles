class Student():
    def __init__(self, last_name, first_name, student_id, courses=[]):
        self.student_id = student_id
        self.courses = set(courses)
        self.is_valid = True
        self.placed = False    
        self.first_name = first_name
        self.last_name = last_name
        self.name = f'{first_name} {last_name}'
        self.timetable = {}