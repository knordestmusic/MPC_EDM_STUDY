import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load data
df = pd.read_csv('EDM_Survey.csv')

# 2. Explicitly name each tension column (check spelling/punctuation)
pitch_with    = "How tense did the build up in audio file 1 feel? "
pitch_without = "How tense did the build up in audio file 2 feel? "
snare_with    = "How tense did the build up in audio file 1 feel? .1"
snare_without = "How tense did the build up in audio file 2 feel? .1"
noise_with    = "How tense did the build up in audio file 1 feel? .2"
noise_without = "How tense did the build up in the audio file 2 feel? "

# 3. Convert to numeric
for col in [pitch_with, pitch_without,
            snare_with, snare_without,
            noise_with, noise_without]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 4. Plotting function with points and mean marker
def plot_with_points_and_mean(col_with, col_without, title, labels):
    a = df[col_with].dropna().values
    b = df[col_without].dropna().values
    data = [a, b]
    positions = [1, 2]

    fig, ax = plt.subplots()
    # Boxplot
    ax.boxplot(data, positions=positions)

    # Scatter individual points + mean
    for pos, arr in zip(positions, data):
        # horizontal jitter
        x_jitter = np.random.normal(loc=pos, scale=0.04, size=len(arr))
        ax.scatter(x_jitter, arr)
        # mean marker
        mean_val = arr.mean()
        ax.scatter(pos, mean_val, marker='D', s=60)

    # Labels
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.set_ylabel('Tension rating (1–5)')
    ax.set_title(title)
    plt.show()

# 5. Generate enhanced plots
plot_with_points_and_mean(
    pitch_with, pitch_without,
    "Pitch Riser vs No Riser",
    ["With pitch riser", "Without pitch riser"]
)

plot_with_points_and_mean(
    snare_with, snare_without,
    "Faster Percussion Subdivisions vs None",
    ["With faster percussion", "Without faster percussion"]
)

plot_with_points_and_mean(
    noise_with, noise_without,
    "Noise Riser vs No Riser",
    ["With noise riser", "Without noise riser"]
)
