import pandas as pd

# Import csv file
df = pd.read_csv("addresses.csv")

# 1
print(df.head())

# 2
print(df.tail())

# 3
print(df.shape)

# 4
print(df.columns)

# 5
print(df.info())

# 6
print(df.describe())

# 7
print(df.isnull().sum())

# 8
print(df.sample(3))

# 9
print(df.dtypes)

# 10
print(df.sort_index())