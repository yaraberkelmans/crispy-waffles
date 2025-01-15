
def check_capacity(timetable, malus=1):
    """
    This function checks if any class exceeds the room's capacity and adds malus points for each extra student that exceeds the room's limit.
    It returns the total number of malus points. 
    """
    total_points = 0 
    for timeslot, rooms in timetable.timetable.items():
        for room, activity in rooms.items():
            if activity and len(activity.student_list) > room.capacity:
                exceeding_students = len(activity.student_list) - room.capacity
                total_points += exceeding_students * malus
    return total_points


def check_evening_slot(timetable, malus=5):
    """
    This function adds 5 malus points for any class that is scheduled in the evening slot (17:00-19:00).  
    It returns the total number of malus points. 
    """
    total_points = 0
    evening_slots = ['17-19']
    for timeslot in timetable.timetable.keys():
        if timeslot.time in evening_slots:
            for room, activity in timetable.timetable[timeslot].items():
                if activity:
                    total_points += malus
    return total_points


def check_individual_conflicts(timetable, student,  malus=1):
    """
    This function adds malus points for students who have overlapping activities in their timetable. 
    If there is an overlap, malus points will be added. It returns the total number of malus points.
    """
    total_points = 0
        for student in timetable.full_student_list:
            # Count the number of times a student has activities in overlapping timeslots 
            timeslot_counts = {}
            for activity in student.activities:
                timeslot = timetable
                if timeslot not in timeslot_counts:
                    timeslot_counts[timeslot] = 0
                else: 
                    timeslot_counts[timeslot] += 1

            for count in timeslot_counts.values():
                if count > 1:
                    total_points += malus * (count - 1)

        return total_points


def check_gap_hours(timetable, gap_malus=1, double_gap_malus=3):
    """
    This function adds malus points for students who have gap hours in their schedule. A gap hour is defined as 
    an empty time slot between two scheduled activities, for each gap hour 1 malus point is added. Additionally, if a student has two consecutive gap hours, 3 malus 
    points will be applied for the double gap. 
    It returns the total number of malus points.

    TODO:
        - Loop through all students in the timetable and check their schedule for gaps between activities.
        - Calculate the number of gap hours for each student by looking for empty slots or double empty slots between activities.
        - mutiply gap hours by 1 malus point and double gap hours by 3 malus points 
    """

    for student in timetable.full_student_list:


    total_points = 0
    return total_points


def calculate_malus(timetable):
    """
    This function calculates summes en returns the total malus points from all scheduling issues for the entire timetable.
    """
    total_malus = (capacity_points(timetable) +
                   evening_points(timetable) +
                   conflict_points(timetable) +
                   gap_hour_points(timetable))
    
    return total_malus
