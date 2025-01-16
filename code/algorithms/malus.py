
def check_capacity(timetable, malus=1):
    """
    This function checks if any class exceeds the room's capacity and adds malus points for each extra student that exceeds the room's limit.
    It returns the total number of malus points. 
    """
    total_points = 0 
    for rooms in timetable.timetable.values():
        # print(rooms)
        for room, activity in rooms.items():
            # print(room.capacity)
            
            if activity:
                # print('found an activity!')
                # print('students:', activity.student_list)
                if len(activity.student_list) > int(room.capacity):
                    exceeding_students = len(activity.student_list) - int(room.capacity)
                    total_points += exceeding_students * malus
    
    # print(f'total points for capacity is {total_points}')

    return total_points


def check_evening_slot(timetable, malus=5):
    """
    This function adds 5 malus points for any class that is scheduled in the evening slot (17:00-19:00).  
    It returns the total number of malus points. 
    """
    total_points = 0
    for timeslot in timetable.timetable.keys():
        if timeslot.time == '17-19':
            for activity in timetable.timetable[timeslot].values():
                if activity:
                    total_points += malus

    # print(f'total points for evening slot is {total_points}')
    return total_points


def check_individual_conflicts(timetable, malus=1):
    """
    This function adds malus points for students who have overlapping activities in their timetable. 
    If there is an overlap, malus points will be added. It returns the total number of malus points.
    """
    total_points = 0
    for student in timetable.full_student_list:
        
        # count the number of times a student has activities in overlapping timeslots 
        timeslot_counts = {}
        for course in student.pers_activities.keys():
            for activity in student.pers_activities[course]:
                timeslot = activity.timeslot
                if timeslot not in timeslot_counts:
                    timeslot_counts[timeslot] = 0
                else: 
                    timeslot_counts[timeslot] += 1

        for count in timeslot_counts.values():
            if count > 1:
                total_points += malus * (count - 1)
    
    # print(f'total points for individual conflicts is {total_points}')

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
    #  total_points = 0
    # for student in timetable.full_student_list:
    #     gap_hours = {}
    #     double_gap_hours {}
    #     for course in student.pers_activities.keys():
    #         for activity in student.pers_activities[course]:



    #     last_timeslot  = None  

    #      for day in student_timeslot:
    #         if last_timeslot is not None:
    #             gap = timeslot - last_timeslot
    #             if gap == 1:
                    

    # return total_points
    

    total_points = 0
    return total_points

    # malus_points = {}
    # for days, timeslots in student.pers_activities.items():
    #     times = list(timeslots.keys())

        







def calculate_malus(timetable):
    """
    This function calculates summes en returns the total malus points from all scheduling issues for the entire timetable.
    """
    total_malus = (check_capacity(timetable) +
                   check_evening_slot(timetable) +
                   check_individual_conflicts(timetable) +
                   check_gap_hours(timetable))
    
    return total_malus
