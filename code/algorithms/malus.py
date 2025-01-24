
def check_capacity(timetable, malus=1, return_details = False):
    """
    This function checks if any class exceeds the room's capacity and adds malus points for each extra student that 
    exceeds the room's limit. It returns the total number of malus points. 
    """
    total_points = 0 
    details = []
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
                    if exceeding_students > 0:
                        activity.over_capacity = exceeding_students
                    # if return_details:
                    #     details.append(activity)
                    # print(activity)
                    # print(activity.location)
                    # print(len(activity.student_list))
    #print(f'total points for capacity is {total_points}')

    #return details if return_details else total_points
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
                    timeslot_counts[timeslot] = 1
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
    an empty time slot between two scheduled activities, for each gap hour 1 malus point is added. Additionally, 
    if a student has two consecutive gap hours, 3 malus points will be applied for the double gap. It returns 
    the total number of malus points.
    """
    total_points = 0
    convert_dict= {'9-11': 1, '11-13': 2, '13-15':3, '15-17':4, '17-19':5}
    # iterate through each student in the timetable
    for student in timetable.full_student_list:

        # iterate over each day and its timeslots in the timetable
        for day, timeslots in student.pers_timetable.items():
            difference_list= []

            # convert the timeslots to values we can work with
            for timeslot in timeslots:
                print
                timeslot_value = convert_dict.get(timeslot)
                difference_list.append(timeslot_value)

            # we only calculate gap hours if a student had more than 1 activity that day, and we sort it chronological
            if len(difference_list) > 1:
                difference_list.sort()

            # iterate through the active timeslots to calculate malus points for gaps
                for i in range(len(difference_list) - 1):

                    # calculate the gap between timeslots with activities
                    gap = difference_list[i + 1] - difference_list[i]
                    
                    if gap == 4:
                        #print('3 gap hours! im quiting uni! Bye:', student)
                        total_points += 1000
                    if gap == 3: 
                        total_points += double_gap_malus
                    if gap == 2: 
                        total_points += gap_malus
    
    # print(f'total points for gap hours is {total_points}')

    return total_points 
        

def calculate_malus(timetable, verbose=False):
    """
    This function calculates summes en returns the total malus points from all scheduling issues for the entire timetable.
    """

    total_malus = (check_capacity(timetable) +
                   check_evening_slot(timetable) +
                   check_individual_conflicts(timetable) +
                   check_gap_hours(timetable))
    if verbose:
        print(f'total points for gap hours is {check_gap_hours(timetable)}')
        print(f'total points for capacity is {check_capacity(timetable)}')
        print(f'total points for evening slots is {check_evening_slot(timetable)}')
        print(f'total points for individual conflicts is {check_individual_conflicts(timetable)}')
        print(f'total malus points is {total_malus}')
    
    return total_malus



