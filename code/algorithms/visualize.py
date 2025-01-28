import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import pickle
import csv

from .malus import *


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


def plot_malus_iter(scores_per_iter_alg, title='Malus points per iteration', output_file_name):
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

    average_malus = average_malus = sum(malus_points_list)/ len(malus_points_list)
    min_malus = min(malus_points_list)
    
    # plot functions
    plt.plot(iter_list, malus_points_list, label= 'Malus points')
    # plt.plot(min_malus_idx, min_malus, color = 'g', marker='o', label= f'Minimum = {round(min_malus)}')
    plt.title(title)
    plt.axhline(average_malus,xmin=0, xmax=len(malus_points_list), color = 'r', ls= '--', label= f'Average = {round(average_malus)}')
    plt.xlabel('iterations')
    plt.ylabel('malus points')
    plt.legend()
    plt.show()
    plt.savefig(output_file_name)
    


def plot_malus_histogram(malus_points_list, bins=20, title='Histogram of Malus Points',  output_file_name):
    """
    This function creates a histogram of malus points to visualize their distribution.
    """

    average_malus = sum(malus_points_list) / len(malus_points_list)
    min_malus = min(malus_points_list)

    # plot histogram
    plt.hist(malus_points_list, bins=bins, color='blue', edgecolor='black')
    plt.axvline(average_malus, color='red', linestyle='--', label=f'Average = {round(average_malus)}')
    plt.axvline(min_malus, color='green', linestyle='-', label=f'Minimum = {round(min_malus)}')
    plt.title(title)
    plt.xlabel('Malus Points')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    plt.savefig(output_file_name)
    


def barplot_malus(timetable, output_file_name):
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
    plt.title('Distribution of Malus Points')
    plt.show()
    plt.savefig(output_file_name)
    

def malus_per_experiment_step(malus_points, title='Malus points distribution', output_file_name):
    """
    This function plots the distribution of malus points of the resulting timetables of the iterations of the experiment.
    """
    plt.hist(malus_points)
    plt.xlabel('Malus Points')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()
    plt.savefig(output_file_name)
    

def load_pickle_data(filepath):
    """
    This function loads a pickle file into a variable so we can use it for further examination.
    Only workt for lists, dictionaries or single objects. Not for multiple object in 1 file. 
    """
    with open(filepath, 'rb') as f:
        variable = pickle.load(f)
    return variable


def plot_malus_iter_test(score_dict_list, title='Malus per iteration', output_file_name):
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

    plt.title(title)
    #plt.axhline(average_malus,xmin=0, xmax=len(malus_points_list), color = 'r', ls= '--', label= f'Average = {round(average_malus)}')
    plt.xlabel('iterations')
    plt.ylabel('malus points')
    plt.legend()
    plt.show()
    plt.savefig(output_file_name)
    

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

def plot_experiment_results(malus_df, output_file_name): 
    """
    This function plots the combinations of number of neigbours vs. the number of swaps and their distribution of maluspoints. 
    """
    sns.set_theme(style= "darkgrid")
    plot = sns.displot(malus_df, x = "total_malus", col = "swaps_per_neighbour", row="neighbours",  binwidth=100, height=3, facet_kws=dict(margin_titles=True),
    )
    plot.set_axis_labels("Total Malus Points", "Frequenty")
    plot.set_titles(row_template="Neighbours = {row_name}", col_template="Swaps = {col_name}")
    plt.show()
    plt.savefig(output_file_name)




