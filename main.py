from code.classes.timetable import Timetable
from code.classes.Timeslot import Timeslot
from code.algorithms.randomize import random_course_assignment
from code.algorithms.randomize import random_student_course_assignment
from code.algorithms.randomize import random_student_activity_assignment
from code.algorithms.randomize import randomize
from code.algorithms.randomize import apply_random_swap
from code.algorithms.malus import calculate_malus
from code.algorithms.hill_climber import HillClimber
# from code.algorithms.visuealize_timetable import visualize_timetable
# from code.algorithms.visuealize_timetable import save_timetable_to_html
from code.algorithms.greedy import Greedy
import csv
import sys
import copy
import pickle
if __name__ == "__main__":
    # initialize timetable
    timetable = Timetable()
    # timetable.load_courses('data/vakken.csv') # adds course obj to timetable
    # timetable.load_students('data/studenten_en_vakken.csv')
    # timetable.load_locations('data/zalen.csv')
    # timetable.add_actual_students_to_courses()
    # timetable.get_activities_count() # creates expected numbers, does not add activity
    # timetable.name_activities() # adds activity to course.activity
    # timetable.create_timetable() # makes empty .timetable attr
    # timetable.initialize_locations() # turns empty into None
    timetable.generate_initial_timetable()

    # N=100
    # malus_points_list = []
    # for exp in range(N):

    #     full_randomized_timetable = randomize(timetable)
    #     malus_points = calculate_malus(full_randomized_timetable)
    #     malus_points_list.append(malus_points)
    # print(len(malus_points_list))
    # print(malus_points_list)

    
    

        

    # average_malus = total_malus_points/N 
    # print(average_malus)
    
    # for timeslot, rooms in full_randomized_timetable.timetable.items():
    #     for room, activity in rooms.items():
    #         if activity:
    #             print(f"Course: {activity.course} Activity {activity.name} in {room} during {timeslot}: {len(activity.student_list)} students.")
    #             print(f"Students: {[student.name for student in activity.student_list]}")
                
    
    # data = []
    #full_randomized_timetable = randomize(timetable)
    # for timeslot in full_randomized_timetable.timetable.keys():
    #     for location, activity in full_randomized_timetable.timetable[timeslot].items():
            
    #         if activity:
    # #             print(activity.student_list)
    # #             # print()
    # #             # print("---------- ACTIVITY INFORMATION------------")
    # #             # print()
    # #             # print(f'Course: {activity.course_name} Activity: {activity.name} Location: {location} Day: {timeslot.day} Time: {timeslot.time}')
    # #             # print()
    # #             # print("----------- STUDENTS ----------")
    # #             # print()
    #         #      data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id, 'Vak': activity.course, 'Activiteit': activity.name})
                
    #         # else:
    #         #      data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id})

    #             for student in activity.student_list:
    #                     #print(student.name)
    #                 data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id, 'Vak': activity.course, 'Activiteit': activity.name, 'Student': student.name}) 
    #     # # for csv output format
    # # #     # for location, activity in full_randomized_timetable.timetable[timeslot].items():
    # # #     #     if activity:
    # # #     #         for student in activity.student_list:
    # # #     #             print()
    # # #     #             print("---------- STUDENT ------------")
    # # #     #             print()
    # # #     #             print(f'Student: {student}; Course: {activity.course_name}; Activity: {activity.name}; Location: {location}; Day: {timeslot.day}; Time: {timeslot.time}')
    # # #     #             print()
                    
    # # #     #
    # # # for data_row in data:
    # # #     print(data_row)
    # print(full_randomized_timetable.activities_per_course)
    # column_names = ['Tijdslot', 'Zaal', 'Vak', 'Activiteit', 'Student']
    # with open('Timetable_test.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=column_names)
    #     writer.writeheader()
    #     writer.writerows(data) 

    #random_swapped_timetable = apply_random_swap(full_randomized_timetable)

    # data_2 = []
    
    # for timeslot in random_swapped_timetable.timetable.keys():
    #     for location, activity in random_swapped_timetable.timetable[timeslot].items():
            
    #         if activity:
    #             for student in activity.student_list:
    #                     #print(student.name)
    #                 data_2.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id, 'Vak': activity.course, 'Activiteit': activity.name, 'Student': student.name}) 

    # with open('Timetable_vergelijking_swap.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=column_names)
    #     writer.writeheader()
    #     writer.writerows(data_2) 
    #print(full_randomized_timetable.full_student_list[0].pers_timetable)
    #print(full_randomized_timetable.full_student_list[0].pers_activities)
    #print(full_randomized_timetable.full_student_list[0].name)
    # # print(full_randomized_timetable.full_student_list[0].courses)

    
    # malus_points = calculate_malus(full_randomized_timetable)
    # print(f'malus points is {malus_points}')

    sys.setrecursionlimit(10**6)
    # hill_climber_hi_scores = []
    # hill_climber_scores_iterations = []

    # for i in range(5):
    #     hill_climber_individual_score_iterations = []
    #     full_randomized_timetable = randomize(timetable)
    #     hill_climber = HillClimber(full_randomized_timetable)
    #     hill_climber_score = hill_climber.run_1(5000, 10)
        
    #     # append to list to make list in list for results and iterations exports
    #     hill_climber_individual_score_iterations.append(hill_climber_score)
    #     hill_climber_individual_score_iterations.append(hill_climber.iterations)

    #     hill_climber_hi_scores.append(hill_climber_score)
    #     hill_climber_scores_iterations.append(hill_climber_individual_score_iterations)
        
    #     print(f'The score for iteration {i} is {hill_climber_score}')
    #     if hill_climber_score <= min(hill_climber_hi_scores):
    #         best_timetable = copy.deepcopy(hill_climber.timetable)
    #         with open("data/best_timetable_7.pkl", "wb") as f:
    #             pickle.dump(best_timetable, f)
    #             print(f"New best Timetable saved. at score {hill_climber_score}")
        
    # print(min(hill_climber_hi_scores))
    
    # header = ['results', 'iterations']
    # with open ('Results_and_iterations.csv', "w", newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(header)
    #         writer.writerow(hill_climber_scores_iterations)

    # with open ('Results.csv', "w", newline='') as f:
    #         writer = csv.writer(f)
    #         for result in hill_climber_hi_scores:
    #             writer.writerow([result])
    with open("data/KLOPT_NIET.pkl", "rb") as f:
        stored_timetable = pickle.load(f)

    print(calculate_malus(stored_timetable, verbose=True))
    for course in stored_timetable.courses:
        print(f'---------------------Check for course {course}----------------------')
        print(len(course.student_list))
        for activity_type in course.activities.keys():
            for activity in course.activities[activity_type]:
                print(f'----Capactity check for {activity}----')
                print(activity.location)
                print(activity.timeslot)
                print(len(activity.student_list))
                print(f'----Student list of {activity}----')
                for student in activity.student_list:
                    print(student)
        

    # data = []
    # for timeslot in stored_timetable.timetable.keys():
    #         for location, activity in stored_timetable.timetable[timeslot].items():
    #             if activity:
    #                 for student in activity.student_list:
    #                     data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id, 'Vak': activity.course, 'Activiteit': activity.name, 'Student': student.name}) 
    #             else:
    #                 data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id,'Vak': 'Empty'})

    # column_names = ['Tijdslot', 'Zaal', 'Vak', 'Activiteit', 'Student']
    # with open('Timetable_pres.csv', 'w') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=column_names)
    #     writer.writeheader()
    #     writer.writerows(data) 

    # # timetable_file = 'Timetable_pres.csv'
    # # pivot_table = visualize_timetable(timetable_file)

    # # save the timetable to an HTML file
    # output_html_path = 'Timetable_pres.html'
    # save_timetable_to_html(pivot_table, output_html_path)

    # # print(f"Timetable saved as HTML: {output_html_path}")
    
    # greedy = Greedy(full_randomized_timetable)
    # greedy.sort_activities_by_capacity()
    # for activity in full_randomized_timetable.activity_list:
    #     print(activity, activity.capacity)