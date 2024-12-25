#!/usr/bin/env python

"""
A simple python script template.
https://stackoverflow.com/questions/53645882/pandas-merging-101
https://stackoverflow.com/questions/27313647/merging-two-pandas-dataframes-results-in-duplicate-columns
"""

import sys
import numpy as np
import pandas as pd


def main():
    np.random.seed(0)
    left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})
    right = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})
    # FULL OUTER JOIN
    left.merge(right, on='key', how='outer').fillna(0)
    left.to_csv('merged.csv', index=False)


if __name__ == '__main__':
    sys.exit(main())
