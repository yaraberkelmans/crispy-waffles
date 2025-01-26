import pandas as pd 
import matplotlib.pyplot as plt
from .malus import check_capacity
from .malus import check_evening_slot
from .malus import check_gap_hours
from .malus import check_individual_conflicts
from .malus import calculate_malus

# import matplotlib as plt
def visualize_timetable(timetable_file):
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

def save_timetable_to_html(pivot_table, output_file):
    # convert the pivot table to an HTML file
    html_content = pivot_table.to_html()

    # write the HTML content to a file
    with open(output_file, 'w') as f:
        f.write(html_content)

def plot_malus_iter(iter_list, malus_points_list, title='Malus points per iteration'):
    """
    This function plots the progress of the malus points per iteration in one algorithm run. It takes the iterations and malus_points as arguments, 
    which are both lists.
    """
    average_malus = average_malus = sum(malus_points_list)/ len(malus_points_list)
    min_malus = min(malus_points_list)
    min_malus_idx= malus_points_list.index(min_malus)

    # plot functions
    plt.plot(iter_list, malus_points_list, label= 'Malus points')
    plt.plot(min_malus_idx, min_malus, color = 'g', marker='o', label= f'Minimum = {round(min_malus)}')
    plt.title(title)
    plt.axhline(average_malus,xmin=0, xmax=len(malus_points_list), color = 'r', ls= '--', label= f'Average = {round(average_malus)}')
    plt.xlabel('iterations')
    plt.ylabel('malus points')
    plt.legend()
    plt.show()

def plot_malus_histogram(malus_points_list, bins=20, title='Histogram of Malus Points'):
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

# timetable_file = 'Timetable_pres.csv'
# pivot_table = visualize_timetable(timetable_file)

# # save the timetable to an HTML file
# output_html_path = 'Timetable_pres.html'
# save_timetable_to_html(pivot_table, output_html_path)

# print(f"Timetable saved as HTML: {output_html_path}")

def barplot_malus(timetable):
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

# # Plots all the different values of swaps/neighbours as lines
# def plot_hillclimber_performance(hillclimber, parameter_values, parameter_name, iterations, fixed_swaps=None, fixed_neighbours=None):
#     """
#     This function plots the malus points per iteration for different numbers of swaps and neighbors.
#     """

#     if parameter_name not in ["swaps", "neighbours"]:
#         raise ValueError('parameter_name must be swaps or neighbours')

#     results = {}

#     # store results for each parameter value
#     for parameter_value in parameter_values:
#         hillclimber.value = calculate_malus(hillclimber.timetable) 
#         hillclimber.iteration_values = {}  

#         if parameter_name == "swaps":
#             hillclimber.run(fixed_neighbours, parameter_value, iterations)
#         elif parameter_name == "neighbours":
#             hillclimber.run(parameter_value, fixed_swaps, iterations)

#         results[parameter_value] = list(hillclimber.iteration_values.values())

#     # plot the results
#     plt.figure(figsize=(12, 6))
#     for parameter_value, malus_values in results.items():
#         plt.plot(range(len(malus_values)), malus_values, label=f"{parameter_value} {parameter_name}")
#     plt.title(f"Malus vs. Iterations for Different Numbers of {parameter_name}")
#     plt.xlabel("Iterations")
#     plt.ylabel("Malus Points")
#     plt.legend()
#     plt.show()


def barplot_hillclimber_performance(hillclimber, iterations, parameter_values, parameter_name, fixed_swaps=None, fixed_neighbours=None):
    """
    This function creates a barplot of the average total malus points for different numbers of swaps or neighbors.
    """

    if parameter_name not in ["swaps", "neighbours"]:
        raise ValueError('parameter_name must be "swaps" or "neighbours"')

    average_results = {}

    # collect results for each parameter value
    for parameter_value in parameter_values:
        total_malus = []

        for i in range(iterations):
            hillclimber.value = calculate_malus(hillclimber.timetable)
            hillclimber.iteration_values = {} 

            if parameter_name == "swaps":
                hillclimber.run(fixed_neighbours, parameter_value, iterations)
            elif parameter_name == "neighbours":
                hillclimber.run(parameter_value, fixed_swaps, iterations)

            # store the final malus value after all iterations
            total_malus.append(hillclimber.value)

        # calculate and store the average malus for this parameter value
        average_results[parameter_value] = sum(total_malus) / len(total_malus)

    
    labels = []
    for parameter_value in parameter_values:
        labels.append(str(parameter_value))
    values = list(average_results.values())
    colors = ['red', 'orange', 'yellow', 'green']

    # plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(
        labels,
        values,
        color= colors,
        alpha=0.8
    )
    plt.title(f"Average Total Malus Points for Different Numbers of {parameter_name}")
    plt.xlabel(f"Number of {parameter_name}")
    plt.ylabel("Average Total Malus Points")
    plt.show()

def malus_per_experiment_step(malus_points, title='Malus points distribution'):
    """
    This function plots the distribution of malus points of the resulting timetables of the iterations of the experiment.
    """
    plt.hist(malus_points)
    plt.xlabel('Malus Points')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()

