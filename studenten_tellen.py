import pandas as pd
import argparse

def load_data(filename):
    """
    Loads data from the CSV file into a pandas df.
    """
    df = pd.read_csv(filename)

    return df

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="counting students per course")

    # add argument for the input CSV file
    parser.add_argument('input_file', type=str, help="info per student")

    # parse the arguments
    args = parser.parse_args()

    # load and clean data from the CSV file
    df = load_data(args.input_file)

    print(df)

    vak1= df['Vak1'].value_counts()
    print(vak1)

    vak2= df['Vak2'].value_counts()
    print(vak2)

    vak3= df['Vak3'].value_counts()
    print(vak3)

    vak4= df['Vak4'].value_counts()
    print(vak4)

    vak5= df['Vak5'].value_counts()
    print(vak5)

    total_vak = vak1.add(vak2, fill_value=0)
    total_vak = total_vak.add(vak3, fill_value=0)
    total_vak = total_vak.add(vak4, fill_value=0)
    total_vak = total_vak.add(vak5, fill_value=0)

    print(total_vak)
