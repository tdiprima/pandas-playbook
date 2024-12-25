"""
This script receives four command-line arguments: a filename, the width and height of an image, and an output file name. 
The code reads a .csv file using pandas, converting specific columns in the file to numeric format. These columns contain details about the image like its width, height, patch_x and patch_y values, and a nuclei ratio. These values are then used to calculate new values of 'i' and 'j' which correspond to adjusted x,y coordinates in an image of specified dimensions.
The nuclei ratio is scaled by multiplying it with 255. A dummy variable initialized to 255 is also created. A new dataframe is constructed with these computed and dummy variables and it is written out to a CSV file.
The script ends with a printed message, enclosed with a border, notifying about the completion of the output file.
"""
import sys

import numpy as np
import pandas as pd

filename = sys.argv[1]
png_w = int(sys.argv[2])
png_h = int(sys.argv[3])
output = sys.argv[4]


def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' * row] + ['+'])
    result = h + '\n'"|" + msg + "|"'\n' + h
    print(result)


def panda():
    fields = ['image_width', 'image_height', 'patch_x', 'patch_y', 'nuclei_ratio']
    df = pd.read_csv(filename, usecols=fields)

    df['patch_x'] = pd.to_numeric(df['patch_x'])
    df['patch_y'] = pd.to_numeric(df['patch_y'])
    df['image_width'] = pd.to_numeric(df['image_width'])
    df['image_height'] = pd.to_numeric(df['image_height'])
    df['nuclei_ratio'] = pd.to_numeric(df['nuclei_ratio'])

    patch_x = df['patch_x']
    patch_y = df['patch_y']
    image_width = df['image_width']
    image_height = df['image_height']
    nuclear_ratio = df['nuclei_ratio']

    df['i'] = patch_x * png_w / image_width
    df['j'] = patch_y * png_h / image_height
    df['i'] = np.ceil(df['i']).astype(int)
    df['j'] = np.ceil(df['j']).astype(int)
    df['nuclei_ratio'] = nuclear_ratio * 255
    df['Dummy'] = 255
    # df.sort_values(['i', 'j'], ascending=[True, True])  # SORT doesn't work!

    df1 = pd.DataFrame(df, columns=['i', 'j', 'nuclei_ratio', 'Dummy', 'Dummy'])

    df1.to_csv(output, index=False)

    border_msg('open ' + output)


panda()
