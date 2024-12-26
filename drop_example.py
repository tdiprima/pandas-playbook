import pandas as pd

# Create a dummy DataFrame
data = {
    'country': ['USA', 'India', 'China', 'Germany', 'Brazil'],
    'pop': [331, 1380, 1441, 83, 213],
    'gdpPercap': [65279, 1900, 10500, 46740, 6790],
    'continent': ['North America', 'Asia', 'Asia', 'Europe', 'South America'],
    'lifeExp': [78.9, 69.7, 77.1, 81.2, 75.5]
}

df = pd.DataFrame(data)

# Display the dummy DataFrame
print("Original DataFrame:")
print(df)

# Drop the specified columns
df = df.drop(['pop', 'gdpPercap', 'continent'], axis=1)

# Display the modified DataFrame
print("\nModified DataFrame:")
print(df)
