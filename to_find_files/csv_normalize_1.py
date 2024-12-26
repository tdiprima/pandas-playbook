# Reads CSV files from a given directory, normalizes and rounds up 'i' and 'j' column data with relation to image dimensions,
# sorts the DataFrame by 'i' and 'j', and writes the processed data back into the output directory as a CSV file.
# TODO: Input CSV file
import os
import sys

import numpy as np
import pandas as pd


def main(input, output):
    patch_wh = 200
    # Do for all files in directory:
    for filename in os.listdir(input):
        if filename.endswith(".csv"):
            fin = os.path.join(input, filename)
            try:
                df = pd.read_csv(fin)
            except Exception as ex:
                continue
            df.columns = ['i', 'j', 'TIL', 'Cancer', 'Tissue']
            df = df.sort_values(['i', 'j'], ascending=[1, 1])
            # Normalize to PNG dimensions
            df['i'] = df['i'] / patch_wh
            df['j'] = df['j'] / patch_wh

            # Round up
            df.i = np.ceil(df.i).astype(int)
            df.j = np.ceil(df.j).astype(int)

            df.to_csv(os.path.join(output, filename), index=False)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
