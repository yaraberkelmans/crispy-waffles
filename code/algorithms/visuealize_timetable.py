import pandas as pd 
import matplotlib as plt
def visualize_timetable(timetable_file):
    # load the data 
    df_timetable = pd.read_csv(timetable_file)

    # combine the course name and and activity as one name 
    df_timetable['Activity'] =df_timetable['Vak'] + "-" df_timetable['Activiteit']
    
    # split up Timeslot in Day and Time to acces them individually
    df_timetable[['Day', 'Time']] = df_timetable['Tijdslot'].str.split(' ', expand=True)

<<<<<<< HEAD
    pivot = pd.pivot_table(df_timetable, values = 'Activity', index = ['Day, Time'], columns = 'Zaal' )
    print(pivot)

    return pivot 
=======
class Visualize():
    def __init__(self):
        pass

    def plot_results(self):
        pass
>>>>>>> 6c3ba42ba03c80c2b7ee39d46bf661b7a83f8c96
