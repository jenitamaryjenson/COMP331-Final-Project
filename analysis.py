import pandas as pd

# Load dataset
df = pd.read_csv("student-mat.csv", sep=";")

# Preview dataset structure
print("Dataset Info:")
print(df.info())

# Summary statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check unique values in selected variables
print("\nUnique Values:")
print("G3:", df["G3"].unique())
print("Absences:", df["absences"].unique()[:20])  # first 20 unique values
print("G1:", df["G1"].unique()[:20])
