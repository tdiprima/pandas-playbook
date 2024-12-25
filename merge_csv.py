# This script does three main tasks in relation to CSV files: First, it retrieves metadata from the CSV file. Second, 
# it prepares the data by reading data from the CSV file while skipping the metadata row, reordering and renaming specific columns.
# Third, it saves data to the file with metadata being the first row. In the main function, it extracts metadata and data from two CSV files, 
# performs a left join operation based on two columns (i, j) from two data sets, fills missing values in the merged data with zero, and
# finally saves the merged data to a new CSV file named 'merged.csv'. 
# This script is helpful in handling and combining CSV data files especially dealing with metadata and specific columns.
import csv
import os
import sys

import pandas as pd


def get_metadata(filename):
    meta_row = ''
    try:
        # Get first line (metadata)
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # Each row is a list
            for row in csv_reader:
                # Get the metadata
                if line_count == 0:
                    line_count += 1
                    if len(row) > 1:
                        # Concatenate list
                        meta_row = ','.join(row)
                    else:
                        meta_row = row[0]
                else:
                    break
        csv_file.close()
    except FileNotFoundError as e:
        print(filename, ":", e.strerror)
        exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    # print(my_obj["metadata"])
    return meta_row


def get_data(filename):
    df = pd.read_csv(filename, skiprows=[0])  # Skipping metadata row
    df = df[['i', 'j', 'Cancer', 'TIL', 'Tissue']]  # Swap columns b/c they screwed up.
    df.columns = ['i', 'j', 'TIL', 'Cancer', 'Tissue']  # Rename.
    # print(df)
    return df


def save_file(filename, data1, data2):
    # Write first row JSON
    with open(filename, 'w') as f:
        f.write(data1 + '\n')

    with open(filename, 'a') as f:
        data2.to_csv(f, mode='a', header=True, index=False)


if __name__ == '__main__':
    # c1 = str(sys.argv[1])
    # c2 = str(sys.argv[2])
    c1 = '14907-T-1_ImageCollection_0000035354_til.csv'
    c2 = '14907-T-1_ImageCollection_0000035354_tumor.csv'

    # df1 = pd.read_csv(c1, delimiter=',')
    meta1 = get_metadata(c1)
    print('meta1', meta1)
    df1 = pd.read_csv(c1, skiprows=[0])  # Skipping metadata row

    meta2 = get_metadata(c2)
    print('meta2', meta2)
    # df2 = pd.read_csv(c2, delimiter=',')
    df2 = pd.read_csv(c2, skiprows=[0])  # Skipping metadata row

    merged_df = df1.merge(df2, how='left', on=['i', 'j'])
    header = list(merged_df.columns)
    merged_df.fillna(0, inplace=True)
    merged_df.to_csv('merged.csv', columns=header, index=False)


# def original():
#     df1 = pd.read_csv('one.csv', delimiter=',')
#     df2 = pd.read_csv('two.csv', delimiter=',')
#     merged_df = df1.merge(df2, how='left', on=['i', 'j'])
#     # print(merged_df)
#     merged_df.fillna(0, inplace=True)
#     header = ["i", "j", "TIL_y", "Cancer", "Tissue"]
#     # merged_df.to_csv('merged.csv', columns=header)
#     merged_df.to_csv('merged.csv', columns=header, index=False)
