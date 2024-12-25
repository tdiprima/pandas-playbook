#!/usr/bin/env python

"""
File is headerless, unsorted, and
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
