import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import pickle
import csv
import ast 
import csv

from ..algorithms.malus import *


def visualize_timetable(timetable_file):
    """
    This function loads a csv file and turns it into a pivot table.
    """
    # load the data
    df_timetable = pd.read_csv(timetable_file)

    # combine the course name and activity into one column
    df_timetable['Activity'] = df_timetable['Vak'] + "-" + df_timetable['Activiteit']

    # split up Timeslot into Day and Time
    df_timetable[['Day', 'Time']] = df_timetable['Tijdslot'].str.split(' ', expand=True)

    # order days manually
    day_order = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    df_timetable['Day'] = pd.Categorical(df_timetable['Day'], categories=day_order, ordered=True)

    # order times manually
    time_order = ['9-11', '11-13', '13-15', '15-17', '17-19']
    df_timetable['Time'] = pd.Categorical(df_timetable['Time'], categories=time_order, ordered=True)

    # sort the DataFrame by Day and Time
    df_timetable = df_timetable.sort_values(by=['Day', 'Time'])

    pivot = pd.pivot_table(df_timetable, values='Activity', index=['Day', 'Time'], columns='Zaal', aggfunc='first')

    return pivot


def save_timetable_to_html(pivot_table, output_file_name):
    """
    This function converts a pivot table to an html file.
    """
    # convert the pivot table to an HTML file
    html_content = pivot_table.to_html()

    # write the HTML content to a file
    with open(output_file_name, 'w') as f:
        f.write(html_content)


def plot_malus_iter_connected(scores_per_iter_alg, output_file_name=None, info=None, export =False, suptitle='Malus points per iteration'):
    """
    This function plots the progress of the malus points per iteration in one algorithm run. It takes the iterations and malus_points as arguments, 
    which are both lists.
    """
    total_iters = 0
    malus_points_list = []

    for alg_dict in scores_per_iter_alg:
        malus_points_list.extend(alg_dict.values())
        total_iters += len(alg_dict.keys())

    iter_list = list(range(total_iters))

    average_malus = sum(malus_points_list)/ len(malus_points_list)
    min_malus = min(malus_points_list)
    
    plt.plot(iter_list, malus_points_list, label= 'Malus points')
    plt.title(info, loc='left', fontsize=10)
    plt.suptitle(suptitle)
    plt.axhline(average_malus,xmin=0, xmax=len(malus_points_list), color = 'r', ls= '--', label= f'Average = {round(average_malus)}')
    plt.xlabel('iterations')
    plt.ylabel('malus points')
    plt.legend()
    if export:
        plt.savefig(output_file_name)
    plt.show()
    

def plot_malus_histogram(malus_points_list, output_file_name=None, bins='auto', info=None, export=False, suptitle='Histogram of Malus Points', binwidth=None):
    """
    This function creates a histogram of malus points to visualize their distribution.
    """
    average_malus = sum(malus_points_list) / len(malus_points_list)
    min_malus = min(malus_points_list)

    sns.histplot(malus_points_list, bins=bins, binwidth=binwidth, kde= True, edgecolor='black')
    plt.axvline(average_malus, color='red', linestyle='--', label=f'Average = {round(average_malus)}')
    plt.axvline(min_malus, color='green', linestyle='-', label=f'Minimum = {round(min_malus)}')
    plt.title(info, loc='left', fontsize=8)
    plt.xlabel('Malus Points')
    plt.ylabel('Frequency')
    plt.suptitle(suptitle)
    plt.legend()
    if export:
        plt.savefig(output_file_name)
    plt.show()
   
    
def barplot_malus_per_category(timetable, output_file_name=None, info=None, export=False, suptitle= 'Distribution of Malus Points'):
    """
    This function creates a barplot showing showing the distribution of malus points across different categories.  
    """
    capacity_malus = check_capacity(timetable)
    evening_malus = check_evening_slot(timetable)
    conflict_malus = check_individual_conflicts(timetable)
    gap_malus = check_gap_hours(timetable)

    malus_values = [capacity_malus, evening_malus, conflict_malus, gap_malus]
    malus_types = ['Capacity', 'Evening slots', 'Individual conflicts' , 'Gap hours']

    plt.figure(figsize=(10,6))
    plt.bar(malus_types, malus_values, color=['red','blue', 'green', 'purple'])
    plt.xlabel('Malus Type')
    plt.ylabel('Malus Points')
    plt.title(info, loc='left', fontsize=10)
    plt.suptitle(suptitle)
    if export:
        plt.savefig(output_file_name)
    plt.show()
    

def load_pickle_data(filepath):
    """
    This function loads a pickle file into a variable so we can use it for further examination.
    Only workt for lists, dictionaries or single objects. Not for multiple object in 1 file. 
    """
    with open(filepath, 'rb') as f:
        variable = pickle.load(f)
    return variable


def plot_malus_iter_disconnected(score_dict_list, output_file_name=None, info=None, export=False, suptitle='Malus per iteration'):
    """
    This function plots the malus points per iteration from a list of dictionaries containing maluspoints. 
    """
    total_iterations = 0
    for dict in score_dict_list:
        x_values = []
        y_values = []
        for malus in dict.values():
           
            if len(x_values) < 500:
                total_iterations += 1
                y_values.append(malus)
                x_values.append(total_iterations)
            
        plt.plot(x_values, y_values, color='b' )#lw=0.5)

    plt.title(info, loc='left', fontsize=10)
    plt.suptitle(suptitle)

    plt.axhline(average_malus,xmin=0, xmax=len(malus_points_list), color = 'r', ls= '--', label= f'Average = {round(average_malus)}')
    plt.xlabel('iterations')
    plt.ylabel('malus points')
    if export:
        plt.savefig(output_file_name)
    plt.show()
    

def timetable_to_csv(timetable, output_filepath):
    """
    This function takes a timetable and converts it into an csv file. 
    """
    data = []
    for timeslot in timetable.timetable.keys():
            for location, activity in timetable.timetable[timeslot].items():
                if activity:
                    for student in activity.student_list:
                        data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id, 'Vak': activity.course, 'Activiteit': activity.name, 'Student': student.name}) 
                else:
                    data.append({'Tijdslot':timeslot.name, 'Zaal': location.room_id,'Vak': 'Empty'})

    column_names = ['Tijdslot', 'Zaal', 'Vak', 'Activiteit', 'Student']
    
    with open(f'{output_filepath}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data)


def load_experiment_data(file_paths): 
    """
    This function takes a list of (pickle) filepaths and turns it in a combined dataframe. 
    """
    combined_data = []
    for file_path in file_paths:
        experiment = load_pickle_data(file_path)

        for iteration in experiment.malus_per_cat_list:
            total_malus = sum(iteration.values())
            combined_data.append({
                "total_malus": total_malus,
                "swaps_per_neighbour": experiment.alg_params["swaps_per_neighbour"],
                "neighbours": experiment.alg_params["neighbours"]
                })

    return pd.DataFrame(combined_data)


def plot_experiment_results(malus_df, output_file_name=None, export=False): 
    """
    This function plots the combinations of number of neigbours vs. the number of swaps and their distribution of maluspoints. 
    """
    sns.set_theme(style= "darkgrid")
    plot = sns.displot(malus_df, x = "total_malus", col = "swaps_per_neighbour", row="neighbours", binrange=(0,100), binwidth=5, height=3, facet_kws=dict(margin_titles=True),
    )
   

    plot.set_axis_labels("Total Malus Points", "Frequenty")
    plot.set_titles(row_template="Neighbours = {row_name}", col_template="Swaps = {col_name}")
    if export: 
        plt.savefig(output_file_name)
    plt.show()
    

def plot_temperature(file_paths, output_file_name= None, export= False):
    """
    This function plots the average malus points from each run in the experiment for each temperature.
    Parameters: 
    - file_paths: a list of file_paths
    - output_file_name: a name if we want to export as a picture, defaults to None
    - export: boolean, only exports as a file if set to True
    """
    for file_path in file_paths:
        experiment = load_pickle_data(file_path)
        scores = experiment.summary.get("all_scores")
        
        average_scores=[]
        number = 0
        total_points = 0

        # exclude scores above 1000 (invalid timetables) and 
        for score in scores:
            if score < 1000:
                number += 1
                total_points += score
        average = total_points/number 
        average_scores.append(average)
        
        # get the name out of the file_path
        temp = file_path.split("Temp=")[-1].split("_")[0]

        # plot a bar for each temperature
        plt.bar(temp, average_scores)
    
    plt.xlabel("Temperature")
    plt.ylabel("Average Malus Points")
    plt.title("Average Malus Points per Temperature")

    if export: 
        plt.savefig(output_file_name)
    plt.show()


def get_scores(file_name):
    scores = []  

    with open(file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file) 

        for row in reader:
            for item in row:  
                data_dict = ast.literal_eval(item)  
                scores.append(data_dict['score'])  

    return scores

