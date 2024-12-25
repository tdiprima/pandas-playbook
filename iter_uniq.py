# This script imports data from different file formats, specifically Excel and CSV, 
# then sorts and prints the data. 
# In the read_excel and read_csv functions, it reads an Excel or CSV file named 
# 'updated_total_covid_list', sorts the data based on index, then prints unique values and 
# column names. 
# The read_csv1 function read another CSV file named 'mapping_subset' and sorts the data 
# based on the 'Sandeep fields'. It then prints the 'Sandeep fields' and 'REDCap Data Elements' 
# columns row by row.
# The get_data function prints all unique values in each column,
# while the get_columns function prints the name of each column. 
# It starts by executing the read_csv function and then exits.
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
