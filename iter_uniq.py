# Reads and displays unique data values and columns of a specified Excel and CSV file; it also sorts data and iterates over a particular CSV file's rows based on a specified field.
import pandas as pd


def read_excel():
    filename = 'updated_total_covid_list.xlsx'
    data = pd.read_excel(filename)
    data.sort_index(inplace=True, axis=1)
    get_data(data)
    print('\n')
    get_columns(data)


def read_csv():
    filename = 'updated_total_covid_list.csv'
    data = pd.read_csv(filename)
    data.sort_index(inplace=True, axis=1)
    get_data(data)
    print('\n')
    get_columns(data)


def read_csv1():
    filename = 'mapping_subset.csv'
    data = pd.read_csv(filename)
    data.sort_values("Sandeep fields")
    # data.sort_values("REDCap Data Elements")
    for index, row in data.iterrows():
        print(row["Sandeep fields"], row["REDCap Data Elements"])


def get_data(df):
    # print unique data values
    for col in df:
        print(col)
        print(df[col].unique())


def get_columns(df):
    # iterating the columns
    for col in df.columns:
        print(col)


# read_excel()
read_csv()

exit(0)
