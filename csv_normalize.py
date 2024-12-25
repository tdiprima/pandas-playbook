"""
This script reads a CSV file named 'TCGA-3C-AALI-01Z-00-DX1.csv' into a pandas DataFrame.
The DataFrame has no header in the CSV file, and its columns are named 'i', 'j', 'TIL', 'Cancer', 'Tissue'.
The data is sorted in ascending order by the 'i' and 'j' columns.
The values of 'i' and 'j' columns are then normalized by dividing them with a constant patch_wh which is set to 200.
Finally, it prints the DataFrame. This is used for some image analysis; patches of an image.
"""
import pandas as pd

patch_wh = 200
df = pd.read_csv('TCGA-3C-AALI-01Z-00-DX1.csv')
df.columns = ['i', 'j', 'TIL', 'Cancer', 'Tissue']
df = df.sort_values(['i', 'j'], ascending=[1, 1])
# Normalize to PNG dimensions
df['i'] = df['i'] / patch_wh
df['j'] = df['j'] / patch_wh
print(df)
