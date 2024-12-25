"""
This python script processes all the .csv files in a given input directory by sorting them and normalizing their values,
eventually outputting the processed files to the specified output directory. The main function takes the input and output
directories as parameters. It assumes that each .csv file consists of five columns and then renames these columns as
'i', 'j', 'TIL', 'Cancer', 'Tissue'. Each row in the file is then sorted based on numerical dimensions from the columns
'i' and 'j'. Thereafter, the 'i' and 'j' values are normalized with respect to a predefined block width and height (patch_wh).
These normalized column values are then rounded up to the nearest integer. The final cleaned, sorted, and normalized
dataframe is then saved as a .csv file in the output directory. In case it encounters any issue while processing a file
(e.g., if a file isn't in the expected format), it skips that file and continues with the next.
"""
import os
import sys

import cv2
import numpy as np
import openslide
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
