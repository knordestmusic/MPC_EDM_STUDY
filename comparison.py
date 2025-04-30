import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1) Load data and mark groups
df = pd.read_csv('EDM_Survey.csv')
df['ParticipantID'] = df.index + 1
target_names = ['dev', 'kyle', 'anukriti', 'noel', 'orlando']
df['Group'] = df['Name'].str.lower().isin(target_names).map({True: 'Target', False: 'Other'})

# 2) Explicitly name the six tension columns
tcols = [
    'How tense did the build up in audio file 1 feel? ',
    'How tense did the build up in audio file 2 feel? ',
    'How tense did the build up in audio file 1 feel? .1',
    'How tense did the build up in audio file 2 feel? .1',
    'How tense did the build up in audio file 1 feel? .2',
    'How tense did the build up in the audio file 2 feel? '
]
# Map to our conditions
conditions = {
    'Pitch Riser':     (tcols[0], tcols[1]),
    'Snare Subdiv':    (tcols[2], tcols[3]),
    'Noise Riser':     (tcols[4], tcols[5])
}

# 3) Convert to numeric
df[tcols] = df[tcols].apply(pd.to_numeric, errors='coerce')

# 4) Plot for each condition
for title, (col1, col2) in conditions.items():
    # data arrays
    a_tgt = df.loc[df.Group=='Target', col1].dropna().values
    b_tgt = df.loc[df.Group=='Target', col2].dropna().values
    a_oth = df.loc[df.Group=='Other',  col1].dropna().values
    b_oth = df.loc[df.Group=='Other',  col2].dropna().values
    
    data = [a_tgt, b_tgt, a_oth, b_oth]
    labels = ['Tgt File1','Tgt File2','Oth File1','Oth File2']
    pos = [1,2,4,5]
    
    fig, ax = plt.subplots(figsize=(6,4))
    ax.boxplot(data, positions=pos, widths=0.6)
    # scatter and mean
    for p, arr in zip(pos, data):
        xj = np.random.normal(p, 0.05, size=len(arr))
        ax.scatter(xj, arr, alpha=0.7)
        ax.scatter(p, np.mean(arr), marker='D', s=60, color='red')
    ax.set_xticks(pos)
    ax.set_xticklabels(labels)
    ax.set_ylabel('Tension (1–5)')
    ax.set_title(f'{title}: Tgt vs Other (File1 vs File2)')
    ax.axvline(2.5, color='gray', linestyle='--')
    plt.tight_layout()
    plt.show()
