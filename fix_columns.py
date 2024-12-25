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
    input = './input'
    output = './output'
    for file in os.listdir(input):
        if file.endswith(".csv"):
            f = os.path.join(input, file)
            # print(f)
            meta = get_metadata(f)
            data = get_data(f)
            f = f.replace(input, output)
            p = f.index('2018')
            f = f[:p] + 'tumor.csv'
            print(f)
            save_file(f, meta, data)
    print('Done.')
