from .Course import Course, Tutorial, Lab, Lecture

class Student():
    def __init__(self, last_name, first_name, student_id, courses=[]):
        self.student_id = student_id
        self.courses = set(courses)
        self.activities = []
        self.is_valid = True
        self.placed = False    
        self.first_name = first_name
        self.last_name = last_name
        self.name = f'{first_name} {last_name}'

        # key is course, value is a list of activities
        self.pers_timetable = {}
    
    def __repr__(self) -> str:
        return f"{self.first_name} {self.last_name}, {self.student_id}"
    
    def check_validity(self, activity):  
        for value in self.pers_timetable[activity.course]:
            if type(activity) == Tutorial or type(activity) == Lab:
                if isinstance(activity, type(value)):
                    return False
        return True

# test because pushing is not working