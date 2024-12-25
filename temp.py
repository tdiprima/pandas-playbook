# This code is intended to drop specific columns from a dataframe using the pandas library in Python. The columns to be
# dropped are 'pop', 'gdpPercap', and 'continent'.

# pandas drop columns using list of column names
df.drop(['pop', 'gdpPercap', 'continent'], axis=1)
