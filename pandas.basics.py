import pandas as pd

# Create a simple DataFrame
data = {
    "Name": ["Hiruy", "Abiy", "Ameha"],
    "Age": [20, 22, 21],
    "Score": [88, 76, 95]
}

df = pd.DataFrame(data)

# Basic operations
print("DataFrame:\n", df)
print("\nSummary:\n", df.describe())

# Filtering
print("\nFiltered (Score > 80):\n", df[df["Score"] > 80])

# Sorting
print("\nSorted by Score:\n", df.sort_values(by="Score", ascending=False))

# Adding a new column
df["Passed"] = df["Score"] >= 80
print("\nWith Passed Column:\n", df)

# Saving to CSV
df.to_csv("students.csv", index=False)
print("\nData saved to students.csv")
