import pandas as pd

# 1) Load your survey data
df = pd.read_csv("EDM_Survey.csv")

# 2) Define the exact column names for each question
pitch_with = "Did you expect something to happen after the build-up for file 1?"
pitch_without = "Did you expect something to happen after the build-up for file 2?"

snare_with = "Did you expect something to happen after the build-up for file 1?.1"
snare_without = "Did you expect something to happen after the build-up for file 2?.1"

noise_with = "Did you expect something to happen after the build-up for file 1?.2"
noise_without = "Did you expect something to happen after the build-up for file 2?.2"

# 3) Build the summary rows
rows = []
for name, col_w, col_wo in [
    ("Pitch riser", pitch_with, pitch_without),
    ("Percussion subdivisions", snare_with, snare_without),
    ("Noise riser", noise_with, noise_without),
]:
    yes_w = df[col_w].eq("Yes").sum()
    no_w = df[col_w].eq("No").sum()
    yes_wo = df[col_wo].eq("Yes").sum()
    no_wo = df[col_wo].eq("No").sum()

    rows.append(
        {
            "Condition": name,
            "With… Yes": yes_w,
            "With… No": no_w,
            "Without… Yes": yes_wo,
            "Without… No": no_wo,
        }
    )

# 4) Convert to DataFrame and print
summary = pd.DataFrame(rows)
print(summary.to_string(index=False))
