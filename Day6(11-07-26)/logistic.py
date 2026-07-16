import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("global-data-on-sustainable-energy (1).csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

df["High_Renewable"] = (
    df["Renewable energy share in the total final energy consumption (%)"]
    >
    df["Renewable energy share in the total final energy consumption (%)"].median()
).astype(int)

le = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = le.fit_transform(df[col])

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.show()

X = df.drop(columns=["High_Renewable"])
y = df["High_Renewable"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Insights
# Imported and cleaned dataset.
# Created a new target column for classification.
# Encoded categorical columns.
# Scaled numerical columns.
# Split data into training and testing data.
# Applied Logistic Regression because target has two classes.
# Accuracy shows overall performance.
# Confusion matrix shows correct and incorrect predictions.
# Precision and Recall show class-wise performance.