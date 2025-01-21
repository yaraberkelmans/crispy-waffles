import pandas as pd 
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

timetable_file = 'Timetable_pres.csv'
pivot_table = visualize_timetable(timetable_file)

# save the timetable to an HTML file
output_html_path = 'Timetable_pres.html'
save_timetable_to_html(pivot_table, output_html_path)

print(f"Timetable saved as HTML: {output_html_path}")




























class Visualize():
    def __init__(self):
        pass

    def plot_results(self, scores):
        iterations = len(scores)
        plt.plot(scores, iterations)
