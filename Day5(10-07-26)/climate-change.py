import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Import Dataset
df = pd.read_csv("climate_change_indicators.csv")

# Display basic information
print("First 5 Rows")
print(df.head())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
print(df.info())

print("\nDescription")
print(df.describe())

# Check null values
print("\nNull Values")
print(df.isnull().sum())

# Fill numerical null values with mean
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

# Fill categorical null values with mode
for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nNull Values After Cleaning")
print(df.isnull().sum())

# Feature Engineering
if "Year" in df.columns:
    df["Decade"] = (df["Year"] // 10) * 10

# Label Encoding
le = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = le.fit_transform(df[col])

# Scaling numerical columns
num_cols = df.select_dtypes(include="number").columns
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\nData After Scaling")
print(df.head())

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Histograms
df[num_cols].hist(figsize=(12, 10))
plt.show()

# Boxplots
for col in num_cols[:3]:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

# Pairplot
sns.pairplot(df[num_cols[:4]])
plt.show()

# Insights and Why I Did It

# Imported the dataset to analyze sustainability data.
# Handled null values to clean the dataset.
# Created a new feature (Decade) from Year.
# Applied encoding because machine learning cannot understand text data.
# Applied scaling because numerical columns have different ranges.
# Used Seaborn plots to understand patterns and relationships.
# Dataset is now ready for analysis and machine learning.