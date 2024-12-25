"""
This script creates two pandas dataframes 'left' and 'right' each with a string column 'key' and a numerically random 'value'
column. It then merges the two dataframes on the 'key' column using an outer join and replaces all null or NaN values with 0.
The resulting 'left' dataframe is then written to a csv file 'merged.csv' without the index. The script uses the 'numpy'
library for generating random numbers and 'pandas' library for handling the dataframes.

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
