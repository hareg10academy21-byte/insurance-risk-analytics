import pandas as pd

df = pd.read_csv(
    "data/MachineLearningRating_v3.txt",
    sep="|",
    low_memory=False
)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Gender values
df["Gender"] = df["Gender"].fillna("Unknown")

# Save cleaned dataset
df.to_csv(
    "data/cleaned_insurance_data.csv",
    index=False
)

print("Cleaned dataset created successfully.")