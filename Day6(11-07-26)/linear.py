import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("co2_emissions_kt_by_country.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

le = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = le.fit_transform(df[col])

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.show()

target = "value"

X = df.drop(columns=["value"])
y = df["value"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Insights
# Imported and cleaned dataset.
# Encoded categorical columns.
# Scaled numerical columns.
# Split data into training and testing data.
# Applied Linear Regression because target is continuous.
# MAE and MSE show prediction error.
# R2 score shows how well the model explains the data.