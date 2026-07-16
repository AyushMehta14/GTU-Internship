import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Import dataset
df = pd.read_csv("global-data-on-sustainable-energy (1).csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Handle null values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nNull values after cleaning")
print(df.isnull().sum())

# Encode categorical columns
le = LabelEncoder()

for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = le.fit_transform(df[col])

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Histogram
df.hist(figsize=(12, 10))
plt.show()

# Select numerical columns
X = df.select_dtypes(include="number")

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)

clusters = kmeans.fit_predict(X_scaled)

df["Cluster"] = clusters

print(df["Cluster"].value_counts())

# Evaluation
score = silhouette_score(X_scaled, clusters)

print("Silhouette Score:", score)

# Visualize clusters
sns.scatterplot(
    x=df["gdp_per_capita"],
    y=df["Access to electricity (% of population)"],
    hue=df["Cluster"]
)

plt.title("K Means Clustering")
plt.show()

# Insights and Why I Did It

# Handled null values to clean the dataset.
# Encoded categorical columns because algorithms cannot understand text.
# Applied scaling because numerical columns have different ranges.
# Used the Elbow Method to find a suitable number of clusters.
# Applied K Means to group similar countries.
# Used Silhouette Score to evaluate clustering quality.

# Dataset Understanding
# One cluster may represent highly developed countries.
# One cluster may represent developing countries.
# One cluster may represent low energy access countries.
# Countries with high GDP generally have better electricity access.
# Renewable energy indicators help separate sustainable and less sustainable countries.