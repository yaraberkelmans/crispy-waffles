import pandas as pd 

def visualize_timetable(timetable_file):
    # load the data 
    df_timetable = pd.read_csv(timetable_file)

    # combine the course name and and activity as one name 
    df_timetable['Activity'] =df_timetable['Vak'] + "-" df_timetable['Activiteit']
    
    # split up Timeslot in Day and Time to acces them individually
    df_timetable[['Day', 'Time']] = df_timetable['Tijdslot'].str.split(' ', expand=True)